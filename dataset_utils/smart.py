import numpy as np
import pandas as pd
from lifelines import CoxPHFitter
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score

smart_features_map = {
    "age": "leeftijd",
    "gender": "geslacht",  # 1 Male and 2 Female? or the opposite?
    "smoker": "roken",  # 0 non smoker, >=1 smoker?
    "systolic_blood_pressure": "bdsys",
    "diabetes": "vz_DM",  # Defined differently, 0 is no and 1 yes?
    "cad": "vz_hart",  # it says general cardiac disease vg_0321
    "cvd": "vz_kop",  # 0 no, 1 yes?
    "aaa": "vz_aaa",  # 0 no, 1 yes?
    "pad": "vz_been",  # It's vascular and not arterial
    "time_since_first_cd": "KliMaDur",  # "KliMaDur", #not sure
    "hdl_cholesterol": "labhdl",
    "total_cholesterol": "labchol",
    "egfr": "labkrea",  # Can this be considered standardized serum creatinine?
    "high_sens_crp": "labcrp",
}

smart_outcomes_map = {
    "death_time": "edood_f",
    "death_yesno": "edood_n",
    "death_vascular": "edoodvas",  # Vascular death is the same as cardio-vascular death?
    "stroke_time": "ebero_f",
    "stroke_yesno": "ebero_n",
    "stroke_type": "ebero_s",  # Codes for ischaemic and hemorrahagic strokes
    "myo_time": "emi_f",
    "myo_yesno": "emi_n",
    "myo_type": "emi_s",  # Which codes are good?
}


numeric_feature_ranges = {
    "age": [30, 100],
    "systolic_blood_pressure": [70, 200],
    "time_since_first_cd": [0, 30],
    "hdl_cholesterol": [0.6, 2.50],
    "total_cholesterol": [2.5, 8.0],
    "egfr": [30.0, 120.0],
    "high_sens_crp": [0.1, 15.0],
}

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


def egfr(scr: float, age: int, male: int):
    if scr == 0.0 or age == 0.0:
        return 0
    gender_f = 1.0 if male == 1 else 0.742
    egfr = 175 * (scr ** (-1.154)) * (age ** (-0.203)) * gender_f
    return egfr


def compute_first_cd_event(smart: pd.DataFrame):
    def compute_time(s: pd.Series):
        t = max([s[f"{event}_time"] for event in ["death", "stroke", "myo"]])  # OR cut-off date (censoring)
        times = [s[f"{event}_time"] for event in ["death", "stroke", "myo"] if s[event]]
        if times:
            t = min(times)
        return t

    target_stroke_types = [11, 102]
    target_myo_types = [41, 101]
    smart["death"] = smart.apply(lambda x: x["death_vascular"] > 0, axis=1)
    smart["stroke"] = smart.apply(lambda x: x["stroke_yesno"] > 0 and x["stroke_type"] in target_stroke_types, axis=1)
    smart["myo"] = smart.apply(lambda x: x["myo_yesno"] > 0 and x["myo_type"] in target_myo_types, axis=1)
    smart["cd_event"] = smart.apply(lambda x: x["death"] or x["stroke"] or x["myo"] in target_myo_types, axis=1)
    smart["cd_time"] = smart.apply(compute_time, axis=1)
    smart = smart.drop([k for k in smart_outcomes_map.keys()] + ["death", "stroke", "myo"], axis=1)
    return smart


def preprocess_smart(smart: pd.DataFrame):
    inverse_smart_features_map = {v: k for k, v in smart_features_map.items()}
    inverse_smart_outcomes_map = {v: k for k, v in smart_outcomes_map.items()}
    rename_dict = inverse_smart_features_map | inverse_smart_outcomes_map
    rename_dict = {k: v for k, v in rename_dict.items() if k in smart.columns}
    keys = [v for v in rename_dict.values()] + ["cd_event", "cd_time"]
    smart = smart.rename(columns=rename_dict).loc[:, keys]
    for feature, (min_val, max_val) in numeric_feature_ranges.items():
        if feature in smart.columns:
            smart[feature] = smart[feature].clip(lower=min_val, upper=max_val)

    smart["egfr"] = smart.apply(lambda x: egfr(x["egfr"] * 0.0113, x["age"], x["gender"]), axis=1)
    smart["smoker"] = smart["smoker"].apply(lambda x: 1 if x > 0 else 0)  # assuming non smoker == 0
    smart["age2"] = smart["age"] ** 2
    smart["egfr2"] = smart["egfr"] ** 2
    smart["log_high_sens_crp"] = np.log(smart["high_sens_crp"])
    return smart


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


def eval_smart(cpf: CoxPHFitter, test: pd.DataFrame, test_smart_risk_score: pd.Series, use_full_feature_set: bool):
    evaluation_times = np.array([i * 365 for i in range(2, 15)])
    event_times = test.cd_time
    event_observed = test.cd_event
    surv = cpf.predict_survival_function(test, times=evaluation_times).T

    ci = concordance_index(event_times=event_times, predicted_scores=surv.loc[:, 3650].to_numpy(), event_observed=event_observed)
    roc = time_dependent_roc_auc_score(event_observed.to_numpy(), surv.to_numpy(), event_times, surv.columns)
    nna_mask = ~test_smart_risk_score.isna()
    results = {}
    abs_err_ours_gt = (test_smart_risk_score[nna_mask] - (1 - surv.loc[nna_mask, 3650])).abs().to_numpy()
    results["mae_ours_gt"] = abs_err_ours_gt.mean()
    results["mae_std_ours_gt"] = abs_err_ours_gt.std()

    if not use_full_feature_set:
        smart_surv = smart_survival_times(smart_weights, test).to_numpy()[..., None]
        evaluation_times = [3650.0]
        ci_smart = concordance_index(event_times=event_times, predicted_scores=smart_surv, event_observed=event_observed)
        roc_smart = time_dependent_roc_auc_score(event_observed.to_numpy(), smart_surv, event_times, evaluation_times)
        abs_err_ours_smart = (
            (original_smart_risk_score(smart_weights, test[nna_mask]) - (1 - surv.loc[nna_mask, 3650])).abs().to_numpy()
        )
        abs_err_smart_gt = (
            (test_smart_risk_score[nna_mask] - original_smart_risk_score(smart_weights, test[nna_mask])).abs().to_numpy()
        )
        results["ci_smart"] = ci_smart
        results["roc_smart"] = roc_smart
        results["mae_ours_smart"] = abs_err_ours_smart.mean()
        results["mae_std_ours_smart"] = abs_err_ours_smart.std()
        results["mae_smart_gt"] = abs_err_smart_gt.mean()
        results["mae_std_smart_gt"] = abs_err_smart_gt.std()

    results["roc"] = roc
    results["ci"] = ci

    return results
