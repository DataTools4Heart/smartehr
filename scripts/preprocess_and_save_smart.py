import init
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
import numpy as np
import pandas as pd
from dataset_utils.smart import compute_first_cd_event, smart_outcomes_map, smart_features_map
import argparse
from pathlib import Path
import os


def preprocess_and_save_smart_data(smart: pd.DataFrame, out_path: str):
    smart = smart.drop(["M3LIFE_no"], axis=1)
    to_remove = [
        i
        for i in range(smart.columns.get_loc("SmrtRisk") + 1, len(smart.columns))
        if smart.columns[i] not in smart_outcomes_map.values()
    ]
    smart = smart.iloc[:, [i for i in range(len(smart.columns)) if i not in to_remove]]
    columns_to_keep = [
        col
        for col in smart.columns
        if (smart[col].isna().sum() / len(smart)) <= 0.10 or (col in smart_features_map.values()) or col == "SmrtRisk"
    ]
    smart = smart[columns_to_keep]
    smart.loc[smart["vz_t2d"] == "LIMA LAD-Y graft FRima D1-Mo", "vz_t2d"] = np.nan
    smart["vz_t2d"] = smart["vz_t2d"].astype(float)
    smart = smart.drop("AlbCr", axis=1)
    inverse_smart_outcomes_map = {v: k for k, v in smart_outcomes_map.items()}
    smart = smart.rename(columns=inverse_smart_outcomes_map)
    for col in smart:
        if col in smart_outcomes_map.keys():
            smart = smart[~smart[col].isna()]
    smart = compute_first_cd_event(smart)
    smart = smart.astype(float)
    train, test = train_test_split(smart, train_size=0.8, random_state=42)
    train, val = train_test_split(smart, test_size=0.2, random_state=42)

    imp = KNNImputer(n_neighbors=5, weights="uniform")
    imp.fit(train.drop(["cd_time", "cd_event", "SmrtRisk"], axis=1))
    train.loc[:, [col for col in train.columns if col not in ["cd_time", "cd_event", "SmrtRisk"]]] = imp.transform(
        train.drop(["cd_time", "cd_event", "SmrtRisk"], axis=1)
    )
    val.loc[:, [col for col in val.columns if col not in ["cd_time", "cd_event", "SmrtRisk"]]] = imp.transform(
        val.drop(["cd_time", "cd_event", "SmrtRisk"], axis=1)
    )
    test.loc[:, [col for col in test.columns if col not in ["cd_time", "cd_event", "SmrtRisk"]]] = imp.transform(
        test.drop(["cd_time", "cd_event", "SmrtRisk"], axis=1)
    )

    out_path = Path(out_path)
    os.makedirs(out_path, exist_ok=True)
    train.to_csv(out_path / "smart_full_train.csv", index=False)
    val.to_csv(out_path / "smart_full_val.csv", index=False)
    test.to_csv(out_path / "smart_full_test.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--smart-path", type=str, required=True, help="Path to the smart data CSV file.")
    parser.add_argument("--output-path", type=str, required=True, help="Path to save the processed data.")
    args = parser.parse_args()
    try:
        smart = pd.read_csv(args.smart_path, low_memory=False, encoding="ISO-8859-1", sep=";")
    except pd.errors.ParserError:
        smart = pd.read_csv(args.smart_path, low_memory=False)
    preprocess_and_save_smart_data(smart, args.output_path)
