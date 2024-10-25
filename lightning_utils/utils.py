import torch
from torch import nn, Tensor
import lightning.pytorch as L
from torchmetrics import Metric
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score
from pycox.models.loss import nll_pmf


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
            preds, events, durations = torch.cat(self.preds), torch.cat(self.events), torch.cat(self.durations)
        preds = torch.cat([preds, torch.zeros((preds.shape[0], 1), device=preds.device)], dim=1)
        preds = torch.softmax(preds, dim=1)[:, :-1]
        surv = 1 - preds.cumsum(dim=1)
        surv = surv.cpu().numpy()
        durations = durations.cpu().numpy()
        events = events.cpu().numpy()
        roc_auc = time_dependent_roc_auc_score(
            y_true=events, y_pred=surv[:, self.evaluation_times], survival_times=durations, times=self.evaluation_times
        )
        ci = concordance_index(event_times=durations, predicted_scores=surv[:, 30], event_observed=events)
        return {"roc_auc": roc_auc[30], "ci": ci}


class SurvivalAnalysisModule(L.LightningModule):
    def __init__(self, model: nn.Module, lr: float):
        super().__init__()
        self.model = model
        self.lr = lr
        self.surv_metrics = SurvMetrics(evaluation_times=[i for i in range(1, self.model.time_intervals)])

    def training_step(self, batch, batch_idx):
        features, durations, events = batch
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("train_loss", loss, on_epoch=True, sync_dist=True)
        return loss

    def validation_step(self, batch, batch_idx):
        features, durations, events = batch
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("val_loss", loss, on_epoch=True, sync_dist=True)
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def test_step(self, batch, batch_idx):
        features, durations, events = batch
        logits = self.model(**features)
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def on_validation_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        self.log("roc_auc", results["roc_auc"], rank_zero_only=True, sync_dist=True)
        self.log("ci", results["ci"], rank_zero_only=True, sync_dist=True)

    def on_test_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        print(results)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        return optimizer
