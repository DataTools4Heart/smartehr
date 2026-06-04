from dataclasses import dataclass
from pathlib import Path
import json
import pandas as pd
from functools import partial
from collections import defaultdict
from pycox.preprocessing import label_transforms
from pathlib import Path
from dataset_utils.smart import SMARTPoC
from dataset_utils.mimic import (
    MIMICReadmission,
    LongitudinalMIMICReadmission,
)
from dataset_utils.smart import SMARTPoC, preprocess_smart, smart_features_map
from pycox.preprocessing import label_transforms
import numpy as np
from sklearn.impute import KNNImputer

from config.dataset.dataset import (
    DatasetParams,
    MimicReadmissionParams,
    SmartPoCParams,
    SmartParams,
    LongitudinalMimicReadmissionParams,
    LongitudinalMimicLoSParams,
    LongitudinalDummySmartParams,
    SmartEHRParams,
)
from sklearn.preprocessing import OrdinalEncoder
from datasets import load_dataset


def load_smart(root_path: Path):
    """Load SMART data from JSONL splits (output of smartehr_pipeline.py).

    Reads train.jsonl, validation.jsonl, test.jsonl and extracts the 'smart'
    fields plus 'm3life_no' into DataFrames. Applies runtime preprocessing:
    - Renames first_event → cd_time
    - Computes cd_event: 0 if cd_time > 3650 or cd_time <= 0, else 1
    - Keeps columns with <=10% missing or in smart_features_map
    - Fixes vz_t2d data issue, drops AlbCr
    - Casts to float
    - KNN imputation (fit on train, transform all)
    """
    splits = {}
    for split_name in ["train", "validation", "test"]:
        records = []
        with open(root_path / f"{split_name}.jsonl") as f:
            for line in f:
                rec = json.loads(line)
                row = {"m3life_no": rec["m3life_no"]}
                row.update(rec["smart"])
                records.append(row)
        df = pd.DataFrame(records)
        if "first_event" in df.columns:
            df = df.rename(columns={"first_event": "cd_time"})
        df["cd_event"] = ((df["cd_time"] > 0) & (df["cd_time"] <= 3650)).astype(int)
        splits[split_name] = df

    train, val, test = splits["train"], splits["validation"], splits["test"]

    # Keep columns with <=10% missing or in smart_features_map values
    protected_cols = set(smart_features_map.values()) | {"m3life_no", "cd_time", "cd_event"}
    columns_to_keep = [
        col for col in train.columns
        if (train[col].isna().sum() / len(train)) <= 0.10 or col in protected_cols
    ]
    train, val, test = train[columns_to_keep], val[columns_to_keep], test[columns_to_keep]

    # Fix data issues
    for df in [train, val, test]:
        if "vz_t2d" in df.columns:
            df.loc[df["vz_t2d"] == "LIMA LAD-Y graft FRima D1-Mo", "vz_t2d"] = np.nan
            df["vz_t2d"] = df["vz_t2d"].astype(float)
    if "AlbCr" in train.columns:
        train, val, test = train.drop("AlbCr", axis=1), val.drop("AlbCr", axis=1), test.drop("AlbCr", axis=1)

    # Cast to float
    non_numeric = {"m3life_no"}
    for df in [train, val, test]:
        for col in df.columns:
            if col not in non_numeric:
                df[col] = pd.to_numeric(df[col], errors="coerce")

    # KNN imputation (fit on train, transform all)
    meta_cols = ["m3life_no", "cd_time", "cd_event"]
    feature_cols = [c for c in train.columns if c not in meta_cols]
    imp = KNNImputer(n_neighbors=5, weights="uniform")
    imp.fit(train[feature_cols])
    train.loc[:, feature_cols] = imp.transform(train[feature_cols])
    val.loc[:, feature_cols] = imp.transform(val[feature_cols])
    test.loc[:, feature_cols] = imp.transform(test[feature_cols])

    return train, val, test


def load_mimic_readmission(root_path: Path):
    data = pd.read_csv(root_path / "readmission.csv")
    train = data[data["split"] == "train"]
    val = data[data["split"] == "val"]
    test = data[data["split"] == "test"]
    return train, val, test


def load_longitudinal_mimic_los(root_path: Path):
    data = pd.read_csv(root_path / "longitudinal_mimic_los.csv", parse_dates=["intime", "outtime"])
    return data


def load_longitudinal_mimic_readmission(root_path: Path):
    return pd.read_csv(root_path / "longitudinal_mimic_readmission.csv")


def load_smart_poc(root_path: str, value_dict_path: str, data_dict_path: str):
    root_path = Path(root_path)
    train, val, test = load_smart(root_path)
    data_dict = pd.read_csv(data_dict_path)
    value_dict = pd.ExcelFile(value_dict_path)
    value_dict = value_dict.parse()

    value_map = defaultdict(dict)
    name_map = {}
    for i in range(1, len(data_dict) - 2):
        col = data_dict["name"][i]
        if col in train.columns:
            field_name = data_dict["label"][i]
            name_map[col] = field_name.strip()

    for i in range(1, len(value_dict)):
        col = value_dict["Var Name"][i].strip()
        if col in train.columns:
            value = value_dict["Value"][i].strip()
            new_value = value_dict["Value Label"][i].strip()
        value_map[col][value] = new_value
    value_map = {k: v for k, v in value_map.items() if k in name_map.keys()}

    def substitute_value(x, col):
        if isinstance(x, float) or isinstance(x, int):
            if isinstance(x, float) and x.is_integer():
                x = int(x)
            if isinstance(x, float):
                x = round(x, 1)
        x = str(x)
        if col in value_map and x in value_map[col].keys():
            x = value_map[col][x]
        return x

    feature_cols = [c for c in train if c not in ["cd_time", "cd_event", "m3life_no"]]
    for dataset in [train, val, test]:
        for col in feature_cols:
            dataset[col] = dataset[col].apply(partial(substitute_value, col=col))
    name_map = {}
    for i, col in enumerate(feature_cols):
        name_map[col] = f"<feature_{i}>"

    return train, val, test, name_map


from config.training.task.task import SurvivalAnalysisParams, TaskParams


def load_for_lightning(dataset_params: DatasetParams, task_params: TaskParams):
    task_name = task_params.name
    if task_name == "survival_analysis":
        if not isinstance(task_params, SurvivalAnalysisParams):
            task_params = SurvivalAnalysisParams(**task_params)
        lab_trans = label_transforms.LabTransDiscreteTime(
            cuts=np.array([i for i in range(task_params.num_time_intervals)], dtype=float)
        )
    elif task_name == "binary_classification" or task_name == "multiclass_classification":
        lab_trans = None
    else:
        raise NotImplementedError(f"Unknown task: {task_name}")

    if dataset_params.name == "mimic_readmission":
        dataset_params = MimicReadmissionParams(**dataset_params)
        train, val, test = load_mimic_readmission(Path(dataset_params.root_path))
        train, val, test = MIMICReadmission(train, lab_trans), MIMICReadmission(val, lab_trans), MIMICReadmission(test, lab_trans)
    elif dataset_params.name == "longitudinal_mimic_readmission":
        dataset_params = LongitudinalMimicReadmissionParams(**dataset_params)
        data = load_longitudinal_mimic_readmission(Path(dataset_params.root_path))
        ignore_cols = ["days_next_admit", "event", "split", "hadm_id", "text", "subject_id", "admittime"]
        data = prepare_structured_data(data, ignore_cols)
        train, val, test = (
            LongitudinalMIMICReadmission(
                data,
                split="train",
                only_one_readmission_label=dataset_params.only_one_readmission_label,
                only_last_feature=dataset_params.only_last_feature,
                lab_trans=lab_trans,
            ),
            LongitudinalMIMICReadmission(
                data,
                split="val",
                only_one_readmission_label=dataset_params.only_one_readmission_label,
                only_last_feature=dataset_params.only_last_feature,
                lab_trans=lab_trans,
            ),
            LongitudinalMIMICReadmission(
                data,
                split="test",
                only_one_readmission_label=dataset_params.only_one_readmission_label,
                only_last_feature=dataset_params.only_last_feature,
                lab_trans=lab_trans,
            ),
        )
    elif dataset_params.name == "longitudinal_mimic_los":
        dataset_params = LongitudinalMimicLoSParams(**dataset_params)
        datasets = load_dataset(dataset_params.root_path, keep_in_memory=True)
        train, val, test = datasets["train"], datasets["validation"], datasets["test"]
    elif dataset_params.name == "longitudinal_dummy_smart":
        dataset_params = LongitudinalDummySmartParams(**dataset_params)
        datasets = load_dataset(dataset_params.root_path, keep_in_memory=True)
        train, val, test = datasets["train"], datasets["validation"], datasets["test"]
    elif dataset_params.name == "smartehr":
        if not isinstance(dataset_params, SmartEHRParams):
            dataset_params = SmartEHRParams(**dataset_params)
        datasets = load_dataset(dataset_params.root_path, keep_in_memory=True)
        train, val, test = datasets["train"], datasets["validation"], datasets["test"]
        if lab_trans is not None:
            # Discretize continuous durations using equidistant cuts spanning the horizon
            durations_raw = [d for d in train["duration"] if d is not None]
            max_duration = float(max(durations_raw))
            cuts = np.linspace(0, max_duration, task_params.num_time_intervals + 1)[1:]

            def discretize_split(split):
                # Convert to numpy, replacing None with NaN
                durations = np.array(
                    [d if d is not None else float("nan") for d in split["duration"]], dtype=np.float64
                )
                events = np.array(
                    [e if e is not None else float("nan") for e in split["event"]], dtype=np.float64
                )
                # Filter out rows with NaN/None values
                valid_mask = ~(np.isnan(durations) | np.isnan(events))
                if not valid_mask.all():
                    n_invalid = int((~valid_mask).sum())
                    print(f"WARNING: Dropping {n_invalid} rows with missing duration/event")
                    split = split.select(np.where(valid_mask)[0].tolist())
                    durations = durations[valid_mask]
                    events = events[valid_mask]
                # Discretize durations into bin indices using searchsorted
                disc_durations = np.searchsorted(cuts, durations).astype(np.int64)
                disc_events = events.astype(np.float32)
                return split.remove_columns(["duration", "event"]).add_column(
                    "duration", disc_durations.tolist()
                ).add_column("event", disc_events.tolist())

            train = discretize_split(train)
            val = discretize_split(val)
            test = discretize_split(test)
    elif dataset_params.name == "smart_poc":
        dataset_params = SmartPoCParams(**dataset_params)
        train, val, test, name_map = load_smart_poc(
            Path(dataset_params.root_path),
            value_dict_path=Path(dataset_params.value_dict_path),
            data_dict_path=Path(dataset_params.data_dict_path),
        )
        # lab_trans = label_transforms.LabTransDiscreteTime(time_intervals).fit(train["cd_time"].values, train["cd_event"].values)
        train, val, test = (
            SMARTPoC(train, name_map, lab_trans),
            SMARTPoC(val, name_map, lab_trans),
            SMARTPoC(test, name_map, lab_trans),
        )
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_params.name}")
    return train, val, test


class Normalizer:
    def __init__(self) -> None:
        self.stats = {}

    def fit(self, data: pd.DataFrame):
        for col in data.columns:
            if len(data[col].unique()) > 2:
                self.stats[col] = {"mean": data[col].mean(), "std": data[col].std()}
            else:
                self.stats[col] = None

    def transform(self, data: pd.DataFrame):
        for col in data.columns:
            if self.stats[col] is not None:
                data[col] = (data[col] - self.stats[col]["mean"]) / self.stats[col]["std"]
            data[col] = data[col].astype(np.float32)
        return data


def prepare_structured_data(dataset: pd.DataFrame, ignore_cols: list[str]):
    original_index = dataset.index
    train = dataset[dataset["split"] == "train"]
    val = dataset[dataset["split"] == "val"]
    test = dataset[dataset["split"] == "test"]
    x_names = [k for k in train.columns if k not in ignore_cols]
    x_train = train.loc[:, x_names]
    x_val = val.loc[:, x_names]
    x_test = test.loc[:, x_names]
    x_train, x_val, x_test = encode_categorical_features(x_train, x_val, x_test)
    x_train, x_val, x_test = x_train.fillna(-1), x_val.fillna(-1), x_test.fillna(-1)

    normalizer = Normalizer()
    normalizer.fit(x_train)
    x_train, x_val, x_test = normalizer.transform(x_train), normalizer.transform(x_val), normalizer.transform(x_test)
    train = pd.concat([x_train, train[ignore_cols]], axis=1)
    val = pd.concat([x_val, val[ignore_cols]], axis=1)
    test = pd.concat([x_test, test[ignore_cols]], axis=1)

    dataset = pd.concat([train, val, test])
    dataset = dataset.reindex(original_index)
    return dataset


def encode_categorical_features(train, val, test):
    encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    categorical_cols = train.select_dtypes(include=["object"]).columns
    train[categorical_cols] = encoder.fit_transform(train[categorical_cols])
    val[categorical_cols] = encoder.transform(val[categorical_cols])
    test[categorical_cols] = encoder.transform(test[categorical_cols])
    return train, val, test


def load_for_pycox(dataset_params: DatasetParams):
    if dataset_params.name == "smart":
        dataset_params = SmartParams(**dataset_params)
        train, val, test = load_smart(Path(dataset_params.root_path))
        if not dataset_params.use_full_feature_set:
            train, val, test = preprocess_smart(train), preprocess_smart(val), preprocess_smart(test)
        num_intervals = 24
        evaluation_times = [i * 365 for i in range(1, 11)]
        y_names = ["cd_time", "cd_event"]
        x_names = [k for k in train.columns if k not in y_names and k != "m3life_no"]

    elif dataset_params.name == "mimic_readmission":
        dataset_params = MimicReadmissionParams(**dataset_params)
        train, val, test = load_mimic_readmission(Path(dataset_params.root_path))
        num_intervals = 366
        evaluation_times = [i * 30 for i in range(1, 11)]
        y_names = ["days_next_admit", "event"]
        x_names = [k for k in train.columns if k not in (y_names + ["split", "hadm_id", "text"])]
    elif dataset_params.name == "longitudinal_mimic_readmission":
        dataset_params = LongitudinalMimicReadmissionParams(**dataset_params)
        dataset = load_longitudinal_mimic_readmission(Path(dataset_params.root_path))
        dataset = dataset.sort_values(by=["subject_id", "admittime"])
        new_data = []
        for _, group in dataset.groupby("subject_id"):
            if dataset_params.only_one_readmission_label:
                group = group.iloc[:-1]
            group = group.iloc[-1]
            new_data.append(group)
        dataset = pd.DataFrame(new_data).reset_index(drop=True)
        train = dataset[dataset["split"] == "train"]
        val = dataset[dataset["split"] == "val"]
        test = dataset[dataset["split"] == "test"]
        num_intervals = 366
        evaluation_times = [i * 30 for i in range(1, 11)]
        y_names = ["days_next_admit", "event"]
        x_names = [k for k in train.columns if k not in (y_names + ["split", "hadm_id", "text", "subject_id", "admittime"])]
    elif dataset_params.name == "longitudinal_mimic_los":
        dataset_params = LongitudinalMimicLoSParams(**dataset_params)
        dataset = load_longitudinal_mimic_los(Path(dataset_params.root_path))
        dataset = dataset.sort_values(by=["subject_id", "intime"])
        new_data = []
        for _, group in dataset.groupby("subject_id"):
            group = group.iloc[-1]
            new_data.append(group)
        dataset = pd.DataFrame(new_data).reset_index(drop=True)
        dataset["event"] = pd.Series(np.ones(len(dataset)), index=dataset.index)
        dataset["class"] = dataset["class"] + 1
        # dataset.loc[dataset["class"] == 4, "event"] = 0
        train = dataset[dataset["split"] == "train"]
        val = dataset[dataset["split"] == "val"]
        test = dataset[dataset["split"] == "test"]
        num_intervals = len(dataset["class"].unique()) + 1
        evaluation_times = [1, 2, 3, 4]

        y_names = ["class", "event"]
        x_names = [
            k
            for k in train.columns
            if k not in (y_names + ["split", "hadm_id", "stay_id", "los", "text", "subject_id", "intime", "outtime"])
        ]
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_params.name}")

    x_train, y_train = train.loc[:, x_names], train.loc[:, y_names]
    x_val, y_val = val.loc[:, x_names], val.loc[:, y_names]
    x_test, y_test = test.loc[:, x_names], test.loc[:, y_names]
    x_train, x_val, x_test = encode_categorical_features(x_train, x_val, x_test)
    x_train, x_val, x_test = x_train.fillna(-1), x_val.fillna(-1), x_test.fillna(-1)

    normalizer = Normalizer()
    normalizer.fit(x_train)
    x_train, x_val, x_test = normalizer.transform(x_train), normalizer.transform(x_val), normalizer.transform(x_test)
    y_train, y_val, y_test = (
        [y_train[col].values for col in y_train],
        [y_val[col].values for col in y_val],
        [y_test[col].values for col in y_test],
    )

    return {
        "x_train": x_train,
        "y_train": y_train,
        "x_val": x_val,
        "y_val": y_val,
        "x_test": x_test,
        "y_test": y_test,
        "evaluation_times": evaluation_times,
        "num_intervals": num_intervals,
    }
