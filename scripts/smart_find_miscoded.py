#!/usr/bin/env python3
"""
Exhaustive search for miscoded SMART features.

For each feature (and every pair of features), tries all candidate
transformations and reports Pearson r vs SmrtRisk, ranked by improvement
over the baseline prediction.

Strategy
--------
- Binary features (0/1 unique values)   → try flip: 1 − x
- 1/2-coded features (1/2 unique values) → try recode to 0/1 and to 1/0
- Continuous features                    → try reflecting around the mean

Usage
-----
  python scripts/smart_find_miscoded.py \\
      --root-path data/smart/ \\
      --smart-csv data/smart/smart.csv
"""

import sys
import argparse
from itertools import combinations, product
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dataset_utils.utils import load_smart
from dataset_utils.smart import preprocess_smart
from models.smart import original_smart_risk_score, smart_weights


# ── candidate transformations ─────────────────────────────────────────────────

def candidate_transforms(col: pd.Series) -> list[tuple[str, pd.Series]]:
    """Return a list of (name, transformed_series) for a given feature column."""
    vals = col.dropna()
    uniq = set(vals.unique())

    if uniq <= {0, 1} or uniq <= {0.0, 1.0}:
        return [("flip_0↔1", 1 - col)]

    if uniq <= {1, 2} or uniq <= {1.0, 2.0}:
        return [
            ("recode_1→0,2→1", col - 1),           # 1/2 → 0/1
            ("recode_1→1,2→0", 2.0 - col),          # 1/2 → 1/0  (flip after recode)
        ]

    # Continuous
    mean = float(vals.mean())
    return [("reflect_mean", 2 * mean - col)]


# ── SMART prediction helpers ──────────────────────────────────────────────────

def _predict(df: pd.DataFrame) -> np.ndarray:
    return np.array(original_smart_risk_score(smart_weights, df), dtype=float)


def pearson_with_mods(df: pd.DataFrame, smart_risk: np.ndarray, mods: dict) -> float:
    """Apply feature modifications, recompute SMART predictions, return Pearson r."""
    df_mod = df.copy()
    for feat, vals in mods.items():
        df_mod[feat] = vals.values if isinstance(vals, pd.Series) else vals
    r, _ = pearsonr(smart_risk, _predict(df_mod))
    return float(r)


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Find miscoded SMART features by maximising Pearson r vs SmrtRisk.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--root-path", type=Path, required=True,
                        help="Root path to SMART JSONL splits (train/validation/test.jsonl).")
    parser.add_argument("--smart-csv", type=Path, required=True,
                        help="Path to original CSV containing the SmrtRisk column.")
    parser.add_argument("--use-full-feature-set", action="store_true", default=False,
                        help="Skip preprocess_smart() (use raw JSONL features).")
    parser.add_argument("--top-n", type=int, default=10,
                        help="Number of top results to print per table.")
    args = parser.parse_args()

    # ── load & align data ────────────────────────────────────────────────────
    _, _, test = load_smart(args.root_path)
    original = pd.read_csv(args.smart_csv, low_memory=False)
    original = original.rename(columns={"M3LIFE_no": "m3life_no"})[["m3life_no", "SmrtRisk"]]
    test = test.merge(original, on="m3life_no", how="left")

    smart_risk_series = test["SmrtRisk"]
    test = test.drop(columns=["m3life_no", "SmrtRisk"], errors="ignore")
    if not args.use_full_feature_set:
        test = preprocess_smart(test)

    nna_mask = ~smart_risk_series.isna()
    test_nna = test[nna_mask].reset_index(drop=True)
    smart_risk = smart_risk_series[nna_mask].to_numpy(dtype=float)

    model_features = list(smart_weights.keys())

    # ── baseline ─────────────────────────────────────────────────────────────
    baseline_r, _ = pearsonr(smart_risk, _predict(test_nna))
    print(f"\nBaseline Pearson r : {baseline_r:.6f}")
    print(f"Model features     : {len(model_features)}")
    print(f"Test patients (n)  : {len(test_nna)}\n")

    SEP = "─" * 74

    # ── single-feature search ─────────────────────────────────────────────────
    single = []
    for feat in model_features:
        for tname, tvals in candidate_transforms(test_nna[feat]):
            r = pearson_with_mods(test_nna, smart_risk, {feat: tvals})
            single.append(dict(feature=feat, transform=tname,
                               r=r, delta_r=r - baseline_r))
    single.sort(key=lambda x: x["r"], reverse=True)

    print(SEP)
    print("  Single-feature candidates  (ranked by Pearson r)")
    print(SEP)
    print(f"  {'Feature':<30} {'Transform':<20} {'r':>9}  {'Δr':>9}")
    print(SEP)
    for row in single[:args.top_n]:
        marker = " ◄" if row["delta_r"] > 0 else ""
        print(f"  {row['feature']:<30} {row['transform']:<20} "
              f"{row['r']:>9.6f}  {row['delta_r']:>+9.6f}{marker}")
    print(f"  {'(baseline)':<30} {'identity':<20} {baseline_r:>9.6f}  {'0.000000':>9}")
    print(SEP)

    # ── pairwise search ───────────────────────────────────────────────────────
    # For each ordered pair of features, try every combination of transforms
    # (including flipping only one at a time)
    pair = []
    all_transforms = {
        feat: candidate_transforms(test_nna[feat]) for feat in model_features
    }

    for f1, f2 in combinations(model_features, 2):
        t1_list = all_transforms[f1]
        t2_list = all_transforms[f2]
        # Also include identity for each feature so we capture single-flip-in-a-pair cases
        t1_with_id = [("identity", test_nna[f1])] + t1_list
        t2_with_id = [("identity", test_nna[f2])] + t2_list

        for (t1n, t1v), (t2n, t2v) in product(t1_with_id, t2_with_id):
            if t1n == "identity" and t2n == "identity":
                continue  # skip pure baseline
            mods = {}
            if t1n != "identity":
                mods[f1] = t1v
            if t2n != "identity":
                mods[f2] = t2v
            r = pearson_with_mods(test_nna, smart_risk, mods)
            pair.append(dict(f1=f1, t1=t1n, f2=f2, t2=t2n,
                             r=r, delta_r=r - baseline_r))

    pair.sort(key=lambda x: x["r"], reverse=True)

    print(f"\n  Pairwise candidates  (ranked by Pearson r)")
    print(SEP)
    print(f"  {'Feature 1':<24} {'T1':<20} {'Feature 2':<24} {'T2':<20} {'r':>9}  {'Δr':>9}")
    print(SEP)
    for row in pair[:args.top_n]:
        marker = " ◄" if row["delta_r"] > 0 else ""
        print(f"  {row['f1']:<24} {row['t1']:<20} {row['f2']:<24} {row['t2']:<20} "
              f"{row['r']:>9.6f}  {row['delta_r']:>+9.6f}{marker}")
    print(SEP)


if __name__ == "__main__":
    main()
