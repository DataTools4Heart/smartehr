import numpy as np
from sklearn.metrics import roc_auc_score


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
