import torch
from torch import nn, Tensor
import lightning.pytorch as L
from torchmetrics import Metric
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score
from pycox.models.loss import nll_pmf
from dataset_utils.utils import DatasetParams, load_mimic_readmission
from dataset_utils.mimic import MIMICReadmission
from pycox.preprocessing import label_transforms
from pathlib import Path
import numpy as np
from transformers import AutoTokenizer
from functools import partial
from dataclasses import dataclass
from typing import Union
from models.models import MIMICNotesModel
from dataset_utils.mimic import collate_fn_longformer


@dataclass
class ModelParams:
    model_name: str = "clinical_longformer"
    freeze_last_n_layers: int = 6
    freeze_embeddings: bool = True


@dataclass
class TrainingParams:
    lr: float = 2e-5
    epochs: int = 100
    batch_size: int = 4
    num_workers: int = 0
    devices: Union[list[int], str] = "cpu"
    patience: int = 10


@dataclass
class MimicReadmissionParams:
    dataset_params: DatasetParams
    model_params: ModelParams
    train_params: TrainingParams

    def __post_init__(self):
        self.model_params = ModelParams(**self.model_params)
        self.train_params = TrainingParams(**self.train_params)
        self.dataset_params = DatasetParams(**self.dataset_params)


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


def prepare_data_for_training(dataset_params: DatasetParams, lab_trans: label_transforms.LabTransDiscreteTime):
    if dataset_params.dataset_name == "mimic_readmission":
        train, val, test = load_mimic_readmission(Path(dataset_params.root_path))
        train, val, test = MIMICReadmission(train, lab_trans), MIMICReadmission(val, lab_trans), MIMICReadmission(test, lab_trans)
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_params.dataset_name}")
    return train, val, test


def load_lightning_model(model_params: ModelParams, time_intervals: int):
    assert model_params.model_name in ["clinical_longformer"]
    if model_params.model_name == "clinical_longformer":
        lab_trans = label_transforms.LabTransDiscreteTime(cuts=np.array([i for i in range(time_intervals + 1)], dtype=float))
        model = MIMICNotesModel(
            time_intervals=time_intervals + 1,
            freeze_last_n_layers=model_params.freeze_last_n_layers,
            freeze_embeddings=model_params.freeze_embeddings,
        )
        tokenizer = AutoTokenizer.from_pretrained("yikuan8/Clinical-Longformer")
        collate_fn = partial(collate_fn_longformer, tokenizer=tokenizer)
    return model, lab_trans, collate_fn
