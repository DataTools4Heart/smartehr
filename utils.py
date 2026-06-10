import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.stats import pearsonr
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
    pred_ours_nna = (1 - surv.loc[nna_mask, 3650]).to_numpy()
    smart_risk_nna = test_smart_risk_score[nna_mask].to_numpy()
    r_ours_gt, p_ours_gt = pearsonr(smart_risk_nna, pred_ours_nna)
    results["pearson_r_ours_gt"] = r_ours_gt
    results["pearson_p_ours_gt"] = p_ours_gt
    results["pred_ours"] = pred_ours_nna
    results["smart_risk"] = smart_risk_nna

    if not use_full_feature_set:
        smart_surv = smart_survival_times(smart_weights, test).to_numpy()[..., None]
        evaluation_times = [3650.0]
        ci_smart = concordance_index(event_times=event_times, predicted_scores=smart_surv, event_observed=event_observed)
        roc_smart = time_dependent_roc_auc_score(event_observed.to_numpy(), smart_surv, event_times, evaluation_times)
        pred_smart_nna = np.asarray(original_smart_risk_score(smart_weights, test[nna_mask]))
        r_ours_smart, p_ours_smart = pearsonr(pred_smart_nna, pred_ours_nna)
        r_smart_gt, p_smart_gt = pearsonr(smart_risk_nna, pred_smart_nna)
        results["ci_smart"] = ci_smart
        results["roc_smart"] = roc_smart
        results["pearson_r_ours_smart"] = r_ours_smart
        results["pearson_p_ours_smart"] = p_ours_smart
        results["pearson_r_smart_gt"] = r_smart_gt
        results["pearson_p_smart_gt"] = p_smart_gt
        results["pred_smart"] = pred_smart_nna

    results["roc"] = roc
    results["ci"] = ci

    return results
