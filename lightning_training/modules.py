import torch
import torch.nn as nn
import lightning.pytorch as L
from pycox.models.loss import nll_pmf
from lightning_training.metrics import SurvMetrics
from lightning_training.collator import DatasetBatch


class SurvivalAnalysisModule(L.LightningModule):
    def __init__(self, model: nn.Module, lr: float, evaluation_times: list[int], weight_decay: float = 0.0):
        super().__init__()
        self.model = model
        self.lr = lr
        self.weight_decay = weight_decay
        self.surv_metrics = SurvMetrics(evaluation_times=evaluation_times)

    def training_step(self, batch: DatasetBatch, batch_idx):
        features = batch["inputs"]
        durations = batch["survival_labels"]["duration"]
        events = batch["survival_labels"]["event"]
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("train_loss", loss, on_epoch=True, sync_dist=True, batch_size=durations.shape[0])
        return loss

    def validation_step(self, batch: DatasetBatch, batch_idx):
        features = batch["inputs"]
        durations = batch["survival_labels"]["duration"]
        events = batch["survival_labels"]["event"]
        logits = self.model(**features)
        loss = nll_pmf(logits, durations, events)
        self.log("val_loss", loss, on_epoch=True, sync_dist=True, batch_size=durations.shape[0])
        self.surv_metrics.update(preds=logits, events=events, durations=durations)

    def test_step(self, batch: DatasetBatch, batch_idx):
        features = batch["inputs"]
        durations = batch["survival_labels"]["duration"]
        events = batch["survival_labels"]["event"]
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
        trainable = [p for p in self.model.parameters() if p.requires_grad]
        return torch.optim.AdamW(trainable, lr=self.lr, weight_decay=self.weight_decay)


from torchmetrics import Accuracy, F1Score, AUROC, Precision, Recall


class ClassificationModule(L.LightningModule):
    def __init__(self, model: nn.Module, lr: float, task: str, num_outputs: int, weight_decay: float = 0.0):
        super().__init__()
        self.model = model
        self.lr = lr
        self.weight_decay = weight_decay
        self.num_outputs = num_outputs
        self.task = task

        if task == "binary_classification":
            self.loss_fn = nn.BCEWithLogitsLoss()
            metric_task = "binary"
        elif task == "multiclass_classification":
            self.loss_fn = nn.CrossEntropyLoss()
            metric_task = "multiclass"
        else:
            raise ValueError(f"Task {task} not supported")

        self.metrics = nn.ModuleDict(
            {
                "accuracy": Accuracy(task=metric_task, num_classes=self.num_outputs),
                "f1": F1Score(task=metric_task, num_classes=self.num_outputs, average="none"),
                "precision": Precision(task=metric_task, num_classes=self.num_outputs, average="none"),
                "recall": Recall(task=metric_task, num_classes=self.num_outputs, average="none"),
                "auroc": AUROC(task=metric_task, num_classes=self.num_outputs, average="none"),
            }
        )

    def log_metrics(self, split: str):
        for metric_name, metric in self.metrics.items():
            results = metric.compute()
            if metric_name == "accuracy" or results.ndim == 0:
                self.log(f"{split}_{metric_name}", results, sync_dist=True)
            else:
                for i, result in enumerate(results):
                    self.log(f"{split}_{metric_name}_class_{i}", result, sync_dist=True)
                macro_score = sum(results) / len(results)
                self.log(f"{split}_{metric_name}_macro", macro_score, sync_dist=True)
            metric.reset()

    def select_labels(self, batch):
        if self.task == "binary_classification":
            return batch["binary_cls_labels"].float()
        elif self.task == "multiclass_classification":
            return batch["multiclass_cls_labels"].long()
        else:
            raise ValueError(f"Task {self.task} not supported")

    def _prepare_logits(self, logits):
        """Squeeze last dim for binary classification (model outputs [B,1]) and cast to float32."""
        if self.task == "binary_classification" and logits.ndim == 2 and logits.shape[-1] == 1:
            return logits.squeeze(-1).float()
        return logits.float()

    def training_step(self, batch, batch_idx):
        features = batch["inputs"]
        labels = self.select_labels(batch)
        logits = self._prepare_logits(self.model(**features))
        loss = self.loss_fn(logits, labels)
        self.log("train_loss", loss, on_epoch=True, sync_dist=True, batch_size=labels.shape[0])
        return loss

    def validation_step(self, batch, batch_idx):
        features = batch["inputs"]
        labels = self.select_labels(batch)
        logits = self._prepare_logits(self.model(**features))
        loss = self.loss_fn(logits, labels)
        self.log("val_loss", loss, on_epoch=True, sync_dist=True, batch_size=labels.shape[0])
        for metric in self.metrics.values():
            metric.update(logits, labels)
        return loss

    def on_validation_epoch_end(self):
        self.log_metrics("val")

    def test_step(self, batch, batch_idx):
        features = batch["inputs"]
        labels = self.select_labels(batch)
        logits = self._prepare_logits(self.model(**features))
        for metric in self.metrics.values():
            metric.update(logits, labels)

    def on_test_epoch_end(self):
        self.log_metrics("test")

    def configure_optimizers(self):
        trainable = [p for p in self.model.parameters() if p.requires_grad]
        return torch.optim.AdamW(trainable, lr=self.lr, weight_decay=self.weight_decay)
