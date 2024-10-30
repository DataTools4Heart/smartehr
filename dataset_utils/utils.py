from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from functools import partial
from collections import defaultdict
from pycox.preprocessing import label_transforms
from pathlib import Path
from dataset_utils.smart import SMARTPoC


@dataclass
class MimicReadmissionParams:
    root_path: str


@dataclass
class SMARTParams:
    root_path: str
    use_full_feature_set: bool


@dataclass
class SMARTPoCParams:
    root_path: str
    value_dict_path: str
    data_dict_path: str


@dataclass
class DatasetParams:
    dataset_name: str
    params: SMARTPoCParams | MimicReadmissionParams | SMARTParams

    def __post_init__(self):
        if self.dataset_name == "smart_poc":
            self.params = SMARTPoCParams(**self.params)
        elif self.dataset_name == "mimic_readmission":
            self.params = MimicReadmissionParams(**self.params)
        elif self.dataset_name == "smart":
            self.params = SMARTParams(**self.params)
        else:
            raise NotImplementedError(f"Unknown dataset: {self.dataset_name}")


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
