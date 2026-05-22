import numpy as np
from sklearn.metrics import roc_auc_score
import pandas as pd
from lifelines import CoxPHFitter
from lifelines.utils import concordance_index
from models import smart_survival_times, original_smart_risk_score, smart_weights


def time_dependent_roc_auc_score(y_true, y_pred, survival_times, times):
    scores = {}
    for i, time in enumerate(times):
        # Exclude patients censored before time t (status unknown)
        mask = ~((y_true == 0) & (survival_times <= time))
        if mask.sum() < 2:
            scores[time] = 0.0
            continue
        # 1 = alive at time t (control), 0 = had event by time t (case)
        y_binary = (survival_times[mask] > time).astype(int)
        if y_binary.sum() == 0 or y_binary.sum() == len(y_binary):
            scores[time] = 0.0
            continue
        try:
            scores[time] = roc_auc_score(y_binary, y_pred[mask, i])
        except ValueError:
            print(f"WARNING: encountered ValueError while computing ROC AUC score for time {time}")
            scores[time] = 0.0
    return scores


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
