import init
import pandas as pd
import json
from pathlib import Path
from dataset_utils.mimic_los import load_mimic_los_dataset, save_datasets


def prepare_longitudinal_mimic_los(
    data_csv: pd.DataFrame,
    out_dir: str,
    feature_types: dict,
    only_last_feature: bool = False,
    impute_and_normalize: bool = False,
):
    datasets = load_mimic_los_dataset(data_csv, feature_types, only_last_feature, impute_and_normalize)
    save_datasets(out_dir, datasets)


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_path", type=str, required=True, help="Path to the root directory of the MIMIC LoS csv file")
    parser.add_argument("--out_dir", type=str, required=True, help="Path to the output directory")
    parser.add_argument("--only_last_feature", action="store_true", default=False, help="Whether to only keep the last feature")
    parser.add_argument(
        "--impute_and_normalize",
        action="store_true",
        default=False,
        help="Whether to impute missing values and normalize the dataset",
    )
    args = parser.parse_args()

    root_path = Path(args.root_path)
    csv_path = root_path / "longitudinal_mimic_los.csv"
    feature_types_path = root_path / "feature_types.json"
    data = pd.read_csv(csv_path, parse_dates=["intime", "outtime"])
    with open(feature_types_path, "r") as f:
        feature_types = json.load(f)
    prepare_longitudinal_mimic_los(data, args.out_dir, feature_types, args.only_last_feature, args.impute_and_normalize)
