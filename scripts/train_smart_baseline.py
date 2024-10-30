import init
from dataset_utils.smart import preprocess_smart
from dataset_utils.utils import load_smart
from utils import eval_smart
from pathlib import Path
from lifelines import CoxPHFitter
import argparse
from omegaconf import OmegaConf


def train_and_evaluate_smart(root_path: Path, use_full_feature_set: bool, same_size_as_original: bool):
    train, val, test = load_smart(root_path)
    if same_size_as_original:
        train = train.sample(3489, random_state=42)
        test = test.sample(2299, random_state=42)
    test_smart_risk_score = test["SmrtRisk"]
    train = train.drop("SmrtRisk", axis=1)
    test = test.drop("SmrtRisk", axis=1)
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

    if not use_full_feature_set:
        print("ROC AUC SMART:", out["roc_smart"][3650])
        print("CI SMART:", out["ci_smart"])
        print("MAE (SMART ours - SMART):", out["mae_ours_smart"], "+-", out["mae_std_ours_smart"])
        print("MAE (SMART - GT):", out["mae_smart_gt"], "+-", out["mae_std_smart_gt"])
    print("MAE (SMART ours - GT):", out["mae_ours_gt"], "+-", out["mae_std_ours_gt"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and evaluate SMART model.")
    parser.add_argument("--root-path", type=Path, help="Root path to the SMART dataset.", required=True)
    parser.add_argument(
        "--use-full-feature-set", action="store_true", help="Use the full feature set for training.", default=False
    )
    parser.add_argument(
        "--same-size-as-original",
        action="store_true",
        help="Use the same number of samples used in original SMART paper.",
        default=False,
    )
    args = parser.parse_args()
    train_and_evaluate_smart(args.root_path, args.use_full_feature_set, args.same_size_as_original)
