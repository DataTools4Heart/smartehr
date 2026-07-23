"""Bootstrap significance test for the concordance-index difference between two runs.

Given two prediction files from scripts/predict_survival.py (same test patients, same
order), computes the per-evaluation-time concordance for each run and a bootstrap 95% CI
on the difference (B - A). If the CI excludes 0, the difference is significant.

Concordance matches the repo (lifelines.concordance_index on the survival probability
surv[:, t]; higher survival = lower risk), so the point estimates equal the ci_{t} values
logged during training.

    python scripts/smartehr/bootstrap_ci_compare.py \
        --pred-a <baseline>_test_predictions.parquet \
        --pred-b <baseline+events>_test_predictions.parquet \
        --times 12,24,36,48,57 --n-boot 2000
"""

import argparse

import numpy as np
import pyarrow.parquet as pq
from lifelines.utils import concordance_index


def _load(path):
    t = pq.read_table(path).to_pydict()
    surv = np.asarray(t["surv"], dtype=np.float64)          # [N, num_bins]
    dur = np.asarray(t["duration"], dtype=np.float64)       # [N] (discretized bins)
    evt = np.asarray(t["event"], dtype=np.float64)          # [N]
    return surv, dur, evt


def _cindex(dur, surv_t, evt):
    # predicted_scores = survival prob (higher = longer survival), matching SurvMetrics
    return concordance_index(event_times=dur, predicted_scores=surv_t, event_observed=evt)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pred-a", required=True, help="Baseline / reference predictions parquet.")
    p.add_argument("--pred-b", required=True, help="Candidate predictions parquet (compared as B - A).")
    p.add_argument("--times", default="12,24,36,48,57", help="Comma list of evaluation bin indices.")
    p.add_argument("--n-boot", type=int, default=2000)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    surv_a, dur_a, evt_a = _load(args.pred_a)
    surv_b, dur_b, evt_b = _load(args.pred_b)
    assert len(dur_a) == len(dur_b), f"different N: {len(dur_a)} vs {len(dur_b)}"
    if not (np.allclose(dur_a, dur_b) and np.allclose(evt_a, evt_b)):
        print("WARNING: labels differ between files — are these the SAME test split / order?")

    n = len(dur_a)
    n_bins = surv_a.shape[1]
    times = [int(t) for t in args.times.split(",") if t.strip()]
    times = [t for t in times if t < n_bins] or [n_bins - 3]
    rng = np.random.default_rng(args.seed)
    boot_idx = [rng.integers(0, n, n) for _ in range(args.n_boot)]

    print(f"N={n}  bins={n_bins}  n_boot={args.n_boot}")
    print(f"{'time':>5} | {'CI_A':>7} {'CI_B':>7} {'dCI':>7} | {'95% CI of dCI':>20} | P(B>A) sig")
    print("-" * 74)
    for t in times:
        sa, sb = surv_a[:, t], surv_b[:, t]
        ci_a, ci_b = _cindex(dur_a, sa, evt_a), _cindex(dur_b, sb, evt_b)
        diffs = np.empty(args.n_boot)
        for i, idx in enumerate(boot_idx):
            diffs[i] = _cindex(dur_a[idx], sb[idx], evt_a[idx]) - _cindex(dur_a[idx], sa[idx], evt_a[idx])
        lo, hi = np.percentile(diffs, [2.5, 97.5])
        p_better = float((diffs > 0).mean())
        sig = "yes" if (lo > 0 or hi < 0) else "no"
        print(f"{t:>5} | {ci_a:7.4f} {ci_b:7.4f} {ci_b-ci_a:+7.4f} | [{lo:+.4f}, {hi:+.4f}] | {p_better:5.2f}  {sig}")

    print("\nΔCI = CI_B - CI_A (positive => B better). 'sig' = 95% bootstrap CI excludes 0.")


if __name__ == "__main__":
    main()
