import torch
import torch.nn as nn
import lightning.pytorch as L
from pycox.models.loss import nll_pmf
from lightning_training.metrics import SurvMetrics
from typing import Optional, Callable


class SurvivalAnalysisModule(L.LightningModule):
    def __init__(self, model: nn.Module, lr: float, evaluation_times: list[int]):
        super().__init__()
        self.model = model
        self.lr = lr
        self.surv_metrics = SurvMetrics(evaluation_times=evaluation_times)

    def training_step(self, batch, batch_idx):
        features = batch["inputs"]
        durations = batch["labels"]["duration"]
        events = batch["labels"]["event"]
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("train_loss", loss, on_epoch=True, sync_dist=True, batch_size=durations.shape[0])
        return loss

    def validation_step(self, batch, batch_idx):
        features = batch["inputs"]
        durations = batch["labels"]["duration"]
        events = batch["labels"]["event"]
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("val_loss", loss, on_epoch=True, sync_dist=True, batch_size=durations.shape[0])
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def test_step(self, batch, batch_idx):
        features = batch["inputs"]
        durations = batch["labels"]["duration"]
        events = batch["labels"]["event"]
        logits = self.model(**features)
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def on_validation_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        for t, ci in results["ci"].items():
            self.log(f"ci_{t}", ci, rank_zero_only=True, sync_dist=True)
        for t, roc in results["roc_auc"].items():
            self.log(f"roc_auc_{t}", roc, rank_zero_only=True, sync_dist=True)

    def on_test_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        print(results)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
        return optimizer


from torchmetrics import Accuracy, F1Score, AUROC, Precision, Recall


class BinaryClassificationModule(L.LightningModule):
    def __init__(self, model: nn.Module, lr: float):
        super().__init__()
        self.model = model
        self.lr = lr
        self.metrics = nn.ModuleDict(
            {
                "acc": Accuracy(task="binary"),
                "f1": F1Score(task="binary"),
                "precision": Precision(task="binary"),
                "recall": Recall(task="binary"),
                "auroc": AUROC(task="binary"),
            }
        )
        self.loss_fn = nn.BCEWithLogitsLoss()

    def training_step(self, batch, batch_idx):
        features = batch["inputs"]
        labels = batch["labels"]
        logits = self.model(**features)
        loss = self.loss_fn(logits, labels)
        self.log("train_loss", loss, on_epoch=True, sync_dist=True, batch_size=labels.shape[0])
        return loss

    def validation_step(self, batch, batch_idx):
        features = batch["inputs"]
        labels = batch["labels"]
        logits = self.model(**features)
        loss = self.loss_fn(logits, labels)
        self.log("val_loss", loss, on_epoch=True, sync_dist=True, batch_size=labels.shape[0])
        logits = logits.squeeze(1).sigmoid()
        labels = labels.squeeze(1)
        for metric in self.metrics.values():
            metric.update(logits, labels)
        return loss

    def on_validation_epoch_end(self):
        for metric_name, metric in self.metrics.items():
            self.log(f"val_{metric_name}", metric.compute(), sync_dist=True)
            metric.reset()

    def test_step(self, batch, batch_idx):
        features = batch["inputs"]
        labels = batch["labels"]
        logits = self.model(**features)
        for metric in self.metrics.values():
            metric.update(logits, labels)

    def on_test_epoch_end(self):
        for metric_name, metric in self.metrics.items():
            self.log(f"test_{metric_name}", metric.compute(), sync_dist=True)
            metric.reset()

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
        return optimizer
