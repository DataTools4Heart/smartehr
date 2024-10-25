from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass
class DatasetParams:
    dataset_name: str
    root_path: str


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
