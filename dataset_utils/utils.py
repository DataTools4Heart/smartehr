from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from functools import partial
from collections import defaultdict
from pycox.preprocessing import label_transforms
from pathlib import Path
from dataset_utils.smart import SMARTPoC

from dataset_utils.mimic import MIMICReadmission
from dataset_utils.smart import SMARTPoC, preprocess_smart
from pycox.preprocessing import label_transforms
import numpy as np

from config.dataset.dataset import DatasetParams, MimicReadmissionParams, SmartPoCParams, SmartParams
from sklearn.preprocessing import OrdinalEncoder


def load_smart(root_path: Path):
    train = pd.read_csv(root_path / "smart_full_train.csv", low_memory=False)
    val = pd.read_csv(root_path / "smart_full_val.csv", low_memory=False)
    test = pd.read_csv(root_path / "smart_full_test.csv", low_memory=False)
    return train, val, test


def load_mimic_readmission(root_path: Path):
    data = pd.read_csv(root_path / "readmission.csv")
    train = data[data["split"] == "train"]
    val = data[data["split"] == "val"]
    test = data[data["split"] == "test"]
    return train, val, test


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

    feature_cols = [c for c in train if c not in ["cd_time", "cd_event"]]
    for dataset in [train, val, test]:
        for col in feature_cols:
            dataset[col] = dataset[col].apply(partial(substitute_value, col=col))
    name_map = {}
    for i, col in enumerate(feature_cols):
        name_map[col] = f"<feature_{i}>"

    return train, val, test, name_map


def load_for_lightning(dataset_params: DatasetParams, time_intervals: int):
    if dataset_params.name == "mimic_readmission":
        dataset_params = MimicReadmissionParams(**dataset_params)
        lab_trans = label_transforms.LabTransDiscreteTime(cuts=np.array([i for i in range(time_intervals + 1)], dtype=float))
        train, val, test = load_mimic_readmission(Path(dataset_params.root_path))
        train, val, test = MIMICReadmission(train, lab_trans), MIMICReadmission(val, lab_trans), MIMICReadmission(test, lab_trans)
    elif dataset_params.name == "smart_poc":
        dataset_params = SmartPoCParams(**dataset_params)
        train, val, test, name_map = load_smart_poc(
            Path(dataset_params.root_path),
            value_dict_path=Path(dataset_params.value_dict_path),
            data_dict_path=Path(dataset_params.data_dict_path),
        )
        lab_trans = label_transforms.LabTransDiscreteTime(time_intervals).fit(train["cd_time"].values, train["cd_event"].values)
        train, val, test = (
            SMARTPoC(train, name_map, lab_trans),
            SMARTPoC(val, name_map, lab_trans),
            SMARTPoC(test, name_map, lab_trans),
        )
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_params.dataset_name}")
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
        x_names = [k for k in train.columns if k not in y_names and k != "SmrtRisk"]

    elif dataset_params.name == "mimic_readmission":
        dataset_params = MimicReadmissionParams(**dataset_params)
        train, val, test = load_mimic_readmission(Path(dataset_params.root_path))
        num_intervals = 366
        evaluation_times = [i * 30 for i in range(1, 11)]
        y_names = ["days_next_admit", "event"]
        x_names = [k for k in train.columns if k not in (y_names + ["split", "hadm_id", "text"])]
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
