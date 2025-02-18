from pycox.models.base import SurvBase
from pycox.models import BCESurv, CoxPH, DeepHitSingle, CoxCC, CoxTime, PCHazard, PMF, MTLR

import pandas as pd
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score
from config.dataset.dataset import DatasetParams, SmartParams, MimicReadmissionParams

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


def discrete_label_transform(y_train, y_val, labtrans_cls, num_intervals):
    labtrans = labtrans_cls(num_intervals)
    y_train = labtrans.fit_transform(*y_train)
    y_val = labtrans.transform(*y_val)
    return y_train, y_val, labtrans


def eval_pycox(model, x_test: pd.DataFrame, y_test: tuple, is_discrete: bool, evaluation_times: list[int]):
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
