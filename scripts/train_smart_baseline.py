import init
from dataset_utils.smart import preprocess_smart
from dataset_utils.utils import load_smart
from utils import eval_smart
from pathlib import Path
from lifelines import CoxPHFitter
import pandas as pd
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def save_correlation_plots(out: dict, plot_dir: Path, use_full_feature_set: bool):
    plot_dir.mkdir(parents=True, exist_ok=True)

    def _scatter(x, y, xlabel, ylabel, r, p, filename):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(x, y, alpha=0.4, s=10)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(f"Pearson r = {r:.3f}  (p = {p:.2e})")
        fig.tight_layout()
        fig.savefig(plot_dir / filename, dpi=150)
        plt.close(fig)

    _scatter(
        out["smart_risk"], out["pred_ours"],
        "SmrtRisk", "Our model  (1 − S(3650))",
        out["pearson_r_ours_gt"], out["pearson_p_ours_gt"],
        "corr_ours_vs_smartrisk.png",
    )
    if not use_full_feature_set:
        _scatter(
            out["smart_risk"], out["pred_smart"],
            "SmrtRisk", "Original SMART",
            out["pearson_r_smart_gt"], out["pearson_p_smart_gt"],
            "corr_smart_vs_smartrisk.png",
        )
        _scatter(
            out["pred_smart"], out["pred_ours"],
            "Original SMART", "Our model",
            out["pearson_r_ours_smart"], out["pearson_p_ours_smart"],
            "corr_ours_vs_smart.png",
        )


def analyze_smart_discordance(
    out: dict,
    test: pd.DataFrame,
    test_smart_risk_score: pd.Series,
    plot_dir: Path,
    outlier_pct: float = 0.10,
):
    """Identify and characterise patients where SMART predictions diverge from SmrtRisk.

    Produces:
    - discordance_scatter.png  : scatter with over/under-estimators highlighted
    - discordance_residuals.png: histogram of (SMART − SmrtRisk) residuals
    - discordance_cohens_d.png : top features distinguishing each outlier group vs inliers
    - outliers_over.csv / outliers_under.csv: raw rows for manual inspection
    """
    plot_dir.mkdir(parents=True, exist_ok=True)
    nna_mask = ~test_smart_risk_score.isna()
    test_nna = test[nna_mask].reset_index(drop=True)

    pred_smart = out["pred_smart"]
    smart_risk = out["smart_risk"]
    residuals = pred_smart - smart_risk   # positive → SMART over-estimates vs SmrtRisk

    k = max(1, int(len(residuals) * outlier_pct))
    over_idx  = np.argsort(residuals)[-k:]  # SMART predicts much higher than SmrtRisk
    under_idx = np.argsort(residuals)[:k]   # SMART predicts much lower than SmrtRisk
    outlier_mask = np.zeros(len(residuals), dtype=bool)
    outlier_mask[np.concatenate([over_idx, under_idx])] = True
    inlier_mask = ~outlier_mask

    # --- 1. Scatter with highlighted groups ---
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(smart_risk[inlier_mask],  pred_smart[inlier_mask],
               alpha=0.3, s=10, color="steelblue", label="inliers")
    ax.scatter(smart_risk[over_idx],  pred_smart[over_idx],
               alpha=0.8, s=20, color="crimson",
               label=f"SMART over-estimates (top {int(outlier_pct*100)}%)")
    ax.scatter(smart_risk[under_idx], pred_smart[under_idx],
               alpha=0.8, s=20, color="darkorange",
               label=f"SMART under-estimates (top {int(outlier_pct*100)}%)")
    ax.set_xlabel("SmrtRisk")
    ax.set_ylabel("Original SMART")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(plot_dir / "discordance_scatter.png", dpi=150)
    plt.close(fig)

    # --- 2. Residual distribution ---
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(residuals, bins=50, color="steelblue", edgecolor="white")
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_xlabel("SMART − SmrtRisk")
    ax.set_ylabel("Count")
    ax.set_title("Residual distribution")
    fig.tight_layout()
    fig.savefig(plot_dir / "discordance_residuals.png", dpi=150)
    plt.close(fig)

    # --- 3. Cohen's d: outlier groups vs inliers (top 20 features) ---
    feature_cols = [c for c in test_nna.columns if c not in ["cd_time", "cd_event"]]

    def cohens_d(a, b):
        a, b = a.dropna(), b.dropna()
        if len(a) < 2 or len(b) < 2:
            return 0.0
        pooled = np.sqrt(((len(a)-1)*a.std()**2 + (len(b)-1)*b.std()**2) / (len(a)+len(b)-2))
        return float((a.mean() - b.mean()) / (pooled + 1e-10))

    inlier_df = test_nna.iloc[inlier_mask]
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    for ax, group_idx, label, color in [
        (axes[0], over_idx,  f"over-estimates (top {int(outlier_pct*100)}%)",  "crimson"),
        (axes[1], under_idx, f"under-estimates (top {int(outlier_pct*100)}%)", "darkorange"),
    ]:
        group_df = test_nna.iloc[group_idx]
        ds = {col: cohens_d(group_df[col], inlier_df[col]) for col in feature_cols}
        top = sorted(ds.items(), key=lambda x: abs(x[1]), reverse=True)[:20]
        cols, vals = zip(*top)
        bar_colors = [color if v > 0 else "steelblue" for v in vals]
        ax.barh(cols, vals, color=bar_colors)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_xlabel("Cohen's d  (outlier − inlier)")
        ax.set_title(f"SMART {label}\nvs inliers")
    fig.tight_layout()
    fig.savefig(plot_dir / "discordance_cohens_d.png", dpi=150)
    plt.close(fig)

    # --- 4. Save CSV for manual inspection ---
    def _save_group(idx, fname):
        df = test_nna.iloc[idx].copy()
        df["residual"]   = residuals[idx]
        df["pred_smart"] = pred_smart[idx]
        df["smart_risk"] = smart_risk[idx]
        df.to_csv(plot_dir / fname, index=False)

    _save_group(over_idx,  "outliers_over.csv")
    _save_group(under_idx, "outliers_under.csv")
    print(f"  Discordance: {k} over-estimators, {k} under-estimators  (threshold = {outlier_pct*100:.0f}th pct)")


def train_and_evaluate_smart(
    root_path: Path,
    smart_csv: Path,
    use_full_feature_set: bool,
    same_size_as_original: bool,
    plot_dir: Path | None = None,
    outlier_pct: float = 0.10,
):
    train, val, test = load_smart(root_path)

    # Load SmrtRisk from the original CSV and link by m3life_no
    original = pd.read_csv(smart_csv, low_memory=False)
    original = original.rename(columns={"M3LIFE_no": "m3life_no"})
    original = original[["m3life_no", "SmrtRisk"]]
    test = test.merge(original, on="m3life_no", how="left")

    if same_size_as_original:
        train = train.sample(3489, random_state=42)
        test = test.sample(2299, random_state=42)
    test_smart_risk_score = test["SmrtRisk"]
    train = train.drop(columns=["m3life_no", "SmrtRisk"], errors="ignore")
    test = test.drop(columns=["m3life_no", "SmrtRisk"], errors="ignore")
    formula = None
    l1_ratio = 1.0
    penalizer = 0.1
    if not use_full_feature_set:
        train, test = preprocess_smart(train), preprocess_smart(test)
        penalizer = 0.0
        formula = "age + age2 + gender + smoker + systolic_blood_pressure + diabetes + cad + cvd + aaa + pad + time_since_first_cd + hdl_cholesterol + total_cholesterol + egfr + egfr2 + log_high_sens_crp"

    cpf = CoxPHFitter(l1_ratio=l1_ratio, penalizer=penalizer)
    cpf.fit(train, duration_col="cd_time", event_col="cd_event", formula=formula)
    out = eval_smart(cpf, test, test_smart_risk_score, use_full_feature_set)

    print("ROC AUC:", out["roc"][3650])
    print("CI:", out["ci"])
    print(f"Pearson r (ours vs SmrtRisk): {out['pearson_r_ours_gt']:.4f}  (p = {out['pearson_p_ours_gt']:.2e})")

    if not use_full_feature_set:
        print("ROC AUC SMART:", out["roc_smart"][3650])
        print("CI SMART:", out["ci_smart"])
        print(f"Pearson r (ours vs SMART):    {out['pearson_r_ours_smart']:.4f}  (p = {out['pearson_p_ours_smart']:.2e})")
        print(f"Pearson r (SMART vs SmrtRisk):{out['pearson_r_smart_gt']:.4f}  (p = {out['pearson_p_smart_gt']:.2e})")

    if plot_dir is not None:
        save_correlation_plots(out, plot_dir, use_full_feature_set)
        print(f"Correlation plots saved → {plot_dir}")
        if not use_full_feature_set:
            analyze_smart_discordance(out, test, test_smart_risk_score, plot_dir, outlier_pct=outlier_pct)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and evaluate SMART model.")
    parser.add_argument("--root-path", type=Path, help="Root path to the SMART JSONL splits.", required=True)
    parser.add_argument("--smart-csv", type=Path, help="Path to the original CSV with SmrtRisk column.", required=True)
    parser.add_argument(
        "--use-full-feature-set", action="store_true", help="Use the full feature set for training.", default=False
    )
    parser.add_argument(
        "--same-size-as-original",
        action="store_true",
        help="Use the same number of samples used in original SMART paper.",
        default=False,
    )
    parser.add_argument(
        "--plot-dir", type=Path, default=None,
        help="Directory to save correlation scatter plots. Skipped if not set.",
    )
    parser.add_argument(
        "--outlier-pct", type=float, default=0.10,
        help="Fraction of patients in each tail used as outliers for discordance analysis (default: 0.10).",
    )
    args = parser.parse_args()
    train_and_evaluate_smart(
        args.root_path, args.smart_csv, args.use_full_feature_set, args.same_size_as_original,
        plot_dir=args.plot_dir,
        outlier_pct=args.outlier_pct,
    )
