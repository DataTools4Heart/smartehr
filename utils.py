import numpy as np
from sklearn.metrics import roc_auc_score
import pandas as pd
from lifelines import CoxPHFitter
from lifelines.utils import concordance_index
from models import smart_survival_times, original_smart_risk_score, smart_weights


def time_dependent_roc_auc_score(y_true, y_pred, survival_times, times):
    scores = {}
    y_true_time_dependent = np.zeros((y_pred.shape[0], y_pred.shape[1]))
    for i, time in enumerate(times):
        y_true_time_dependent[:, i] = (y_true == 0) | (survival_times > time)
    for i, time in zip(range(y_pred.shape[1]), times):
        try:
            scores[time] = roc_auc_score(y_true_time_dependent[:, i], y_pred[:, i])
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
