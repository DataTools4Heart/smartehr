import torch
from torch import Tensor
from torchmetrics import Metric
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score


class SurvMetrics(Metric):
    def __init__(self, evaluation_times: Tensor, **kwargs):
        super().__init__(**kwargs)
        self.evaluation_times = evaluation_times
        self.add_state("preds", default=[], dist_reduce_fx="cat")
        self.add_state("events", default=[], dist_reduce_fx="cat")
        self.add_state("durations", default=[], dist_reduce_fx="cat")

    def update(self, preds: Tensor, events: Tensor, durations: Tensor) -> None:
        self.preds.append(preds)
        self.events.append(events)
        self.durations.append(durations)

    def compute(self):
        preds, events, durations = self.preds, self.events, self.durations
        if isinstance(preds, list):
            print(preds[0].shape)
            print(events[0].shape)
            print(durations[0].shape)
            preds, events, durations = torch.cat(self.preds), torch.cat(self.events), torch.cat(self.durations)
        print(preds.shape)
        print(events.shape)
        print(durations.shape)
        #0/0
        preds = torch.cat([preds, torch.zeros((preds.shape[0], 1), device=preds.device)], dim=1)
        preds = torch.softmax(preds, dim=1)[:, :-1]
        surv = 1 - preds.cumsum(dim=1)
        surv = surv.cpu().numpy()
        durations = durations.cpu().numpy()
        events = events.cpu().numpy()
        roc_auc = time_dependent_roc_auc_score(
            y_true=events, y_pred=surv[:, self.evaluation_times], survival_times=durations, times=self.evaluation_times
        )
        ci = {}
        for t in self.evaluation_times:
            try:
                ci[t] = concordance_index(event_times=durations, predicted_scores=surv[:, t], event_observed=events)
            except:
                ci[t] = 0
        return {"roc_auc": roc_auc, "ci": ci}
