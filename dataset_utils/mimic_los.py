import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
from datasets import Dataset, DatasetDict
from dataset_utils.utils import prepare_structured_data


def load_mimic_los_dataset(data_csv: pd.DataFrame, feature_types: dict, only_last_feature: bool = False, normalize: bool = False):
    if normalize:
        ignore_cols = ["class", "split", "stay_id", "hadm_id", "text", "subject_id", "intime", "outtime"]
        data_csv = prepare_structured_data(data_csv, ignore_cols)
    datasets = {}
    for col in data_csv.columns:
        if data_csv[col].dtype == "object":
            data_csv[col] = data_csv[col].astype(str)
    for split in data_csv["split"].unique():
        data = data_csv[data_csv["split"] == split]
        data = data.sort_values(["subject_id", "intime"])
        dataset = []
        for subject_id, group in data.groupby("subject_id"):
            outcomes = {
                "los": [group["class"].iloc[-1].item()],
            }

            time_deltas = ((group["intime"].iloc[-1] - group["intime"]).dt.total_seconds() / (24 * 3600)).values.tolist()
            group = group[
                [
                    col
                    for col in group.columns
                    if col not in ["outtime", "class", "split", "subject_id", "hadm_id", "stay_id", "los", "intime"]
                ]
            ]
            if only_last_feature:
                group = group.iloc[-1:]
                time_deltas = time_deltas[-1:]

            features = []
            for _, row in group.iterrows():
                element = {}
                for feature_type in feature_types:
                    element[feature_type] = {}
                    for feature_element in feature_types[feature_type]:
                        value = row[feature_element]
                        element[feature_type][feature_element] = value
                features.append(element)

            dataset.append({"subject_id": subject_id, "features": features, "time_deltas": time_deltas, "outcomes": outcomes})

        datasets[split] = Dataset.from_list(dataset)
    datasets = DatasetDict(datasets)
    return datasets


def convert_numeric_to_str(value):
    if isinstance(value, (int, float)):
        # Convert to string with at most one decimal place
        if value == int(value):
            # If it's a whole number, don't show decimal
            return str(int(value))
        else:
            # Round to one decimal place
            return f"{round(value, 1)}"
    else:
        # Return as is if not numeric
        return str(value)


def save_datasets(out_dir: str, datasets: DatasetDict):
    out_dir = Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    for split in datasets.keys():
        datasets[split].to_parquet(out_dir / f"{split}.parquet")
