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


def train_and_evaluate_smart(
    root_path: Path,
    smart_csv: Path,
    use_full_feature_set: bool,
    same_size_as_original: bool,
    plot_dir: Path | None = None,
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
    args = parser.parse_args()
    train_and_evaluate_smart(
        args.root_path, args.smart_csv, args.use_full_feature_set, args.same_size_as_original,
        plot_dir=args.plot_dir,
    )
