from pycox.models.base import SurvBase
from pycox.models import BCESurv, CoxPH, DeepHitSingle, CoxCC, CoxTime, PCHazard, PMF, MTLR
from dataclasses import dataclass
import pandas as pd
import numpy as np
import math
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score
from dataset_utils.utils import DatasetParams
from sklearn.preprocessing import OrdinalEncoder
from pathlib import Path
from dataset_utils.smart import preprocess_smart
from dataset_utils.utils import load_mimic_readmission, load_smart

supported_models = [
    "deep_surv",
    "cox_cc",
    "cox_time",
    "pc_hazard",
    "deep_hit",
    "pmf",
    "mtlr",
    "bce_surv",
]


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


@dataclass
class PyCoxModelParams:
    model_name: str
    num_nodes: list[int]
    batch_norm: bool
    dropout: float
    output_bias: bool


@dataclass
class PyCoxTrainingParams:
    batch_size: int
    epochs: int
    patience: int
    device: str


@dataclass
class PyCoxBaselineParams:
    model_params: PyCoxModelParams
    train_params: PyCoxTrainingParams
    dataset_params: DatasetParams

    def __post_init__(self):
        self.model_params = PyCoxModelParams(**self.model_params)
        self.train_params = PyCoxTrainingParams(**self.train_params)
        self.dataset_params = DatasetParams(**self.dataset_params)


def load_pycox_model(model_name: str) -> tuple[SurvBase, callable, bool]:
    assert model_name in supported_models, f"Supported models: {supported_models}"
    if model_name == "deep_surv":
        model_cls = CoxPH
        label_transform = None
        is_discrete = False
    elif model_name == "cox_cc":
        model_cls = CoxCC
        label_transform = None
        is_discrete = False
    elif model_name == "cox_time":
        model_cls = CoxTime
        label_transform = CoxTime.label_transform
        is_discrete = False
    elif model_name == "pc_hazard":
        model_cls = PCHazard
        label_transform = PCHazard.label_transform
        is_discrete = False
    elif model_name == "deep_hit":
        model_cls = DeepHitSingle
        label_transform = DeepHitSingle.label_transform
        is_discrete = True
    elif model_name == "pmf":
        model_cls = PMF
        label_transform = PMF.label_transform
        is_discrete = True
    elif model_name == "mtlr":
        model_cls = MTLR
        label_transform = MTLR.label_transform
        is_discrete = True
    elif model_name == "bce_surv":
        model_cls = BCESurv
        label_transform = BCESurv.label_transform
        is_discrete = True
    else:
        raise ValueError(f"Unknown model name: {model_name}")

    return model_cls, label_transform, is_discrete


def encode_categorical_features(train, val, test):
    encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    categorical_cols = train.select_dtypes(include=["object"]).columns
    train[categorical_cols] = encoder.fit_transform(train[categorical_cols])
    val[categorical_cols] = encoder.transform(val[categorical_cols])
    test[categorical_cols] = encoder.transform(test[categorical_cols])
    return train, val, test


def prepare_data_for_training(dataset_params: DatasetParams):
    if dataset_params.dataset_name == "smart":
        train, val, test = load_smart(Path(dataset_params.params.root_path))
        if not dataset_params.params.use_full_feature_set:
            train, val, test = preprocess_smart(train), preprocess_smart(val), preprocess_smart(test)
        num_intervals = 24
        evaluation_times = [i * 365 for i in range(1, 11)]
        y_names = ["cd_time", "cd_event"]
        x_names = [k for k in train.columns if k not in y_names and k != "SmrtRisk"]

    elif dataset_params.dataset_name == "mimic_readmission":
        train, val, test = load_mimic_readmission(Path(dataset_params.params.root_path))
        num_intervals = 366
        evaluation_times = [i * 30 for i in range(1, 11)]
        y_names = ["days_next_admit", "event"]
        x_names = [k for k in train.columns if k not in (y_names + ["split", "hadm_id", "text"])]
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_params.dataset_name}")

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


def discrete_label_transform(y_train, y_val, labtrans_cls, num_intervals):
    labtrans = labtrans_cls(num_intervals)
    y_train = labtrans.fit_transform(*y_train)
    y_val = labtrans.transform(*y_val)
    return y_train, y_val, labtrans


def eval_pycox(model, x_test: pd.DataFrame, y_test: tuple, is_discrete: bool, evaluation_times: list[int]):
    """if is_discrete:
        surv = model.interpolate(365).predict_surv_df(x_test.values).T
    else:"""
    surv = model.predict_surv_df(x_test.values).T
    cols = [i for i in surv.columns]
    series = {}
    for i in evaluation_times:
        if i not in cols:
            series[i] = pd.Series(dtype="float")

    surv = surv.join(pd.DataFrame(series, index=surv.index))
    surv = surv.reindex(sorted(surv.columns), axis=1)
    surv = surv.interpolate(axis=1)
    event_times = y_test[0]
    event_observed = y_test[1]
    roc = time_dependent_roc_auc_score(event_observed, surv.loc[:, evaluation_times].to_numpy(), event_times, evaluation_times)
    ci = {}
    for e in evaluation_times:
        ci[e] = concordance_index(
            event_times=event_times, predicted_scores=surv.loc[:, e].to_numpy(), event_observed=event_observed
        )
    return roc, ci
