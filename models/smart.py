import torch.utils
import pandas as pd
import numpy as np

smart_weights = {
    "age": -0.0850,
    "age2": 0.00105,
    "gender": 0.156,
    "smoker": 0.262,
    "systolic_blood_pressure": 0.00429,
    "diabetes": 0.223,
    "cad": 0.14,
    "cvd": 0.406,
    "aaa": 0.558,
    "pad": 0.283,
    "time_since_first_cd": 0.0229,
    "hdl_cholesterol": -0.426,
    "total_cholesterol": 0.0959,
    "egfr": -0.0532,
    "egfr2": 0.000306,
    "log_high_sens_crp": 0.139,
}


def original_smart_risk_score(weights: dict, data: pd.DataFrame):
    b, c = 0.81066, 2.099
    cov = []
    for k in weights.keys():
        x = data[k]
        cov.append(weights[k] * x)
    A = np.sum(np.array(cov), axis=0)
    return [(1 - b ** (np.exp(a + c))) for a in A]


def smart_survival_times(weights, data: pd.DataFrame):
    b, c = 0.81066, 2.099
    cov = []
    for k in weights.keys():
        x = data[k]
        cov.append(weights[k] * x)
    A = np.sum(np.array(cov), axis=0)
    return pd.Series([b ** np.exp(a + c) for a in A], index=data.index)
