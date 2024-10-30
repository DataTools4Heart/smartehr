import torch
from torch import nn, Tensor
import lightning.pytorch as L
from torchmetrics import Metric
from lifelines.utils import concordance_index
from utils import time_dependent_roc_auc_score
from pycox.models.loss import nll_pmf
from dataset_utils.utils import DatasetParams, load_mimic_readmission, load_smart_poc
from dataset_utils.mimic import MIMICReadmission, collate_fn_longformer
from dataset_utils.smart import SMARTPoC, collate_fn_smart_poc
from pycox.preprocessing import label_transforms
from pathlib import Path
import numpy as np
from transformers import AutoTokenizer
from functools import partial
from dataclasses import dataclass
from typing import Union
from models.models import MIMICNotesModel, TransformerEncoderForClassification
import pickle as pkl
from tokenizers import ByteLevelBPETokenizer
import torch.nn.functional as F


@dataclass
class ClinicalLongformerParams:
    freeze_last_n_layers: int = 6
    freeze_embeddings: bool = True


@dataclass
class TransformerEncoderParams:
    tokenizer_path: str = ""
    d_model: int = 32
    nhead: int = 4
    dim_feedforward: int = 32
    num_layers: int = 1
    dropout: float = 0.2


@dataclass
class ModelParams:
    model_name: str
    h_params: ClinicalLongformerParams | TransformerEncoderParams

    def __post_init__(self):
        if self.model_name == "clinical_longformer":
            self.h_params = ClinicalLongformerParams(**self.h_params)
        elif self.model_name == "transformer_encoder":
            self.h_params = TransformerEncoderParams(**self.h_params)
        else:
            raise NotImplementedError(f"Unknown model: {self.model_name}")


@dataclass
class TrainingParams:
    lr: float = 2e-5
    epochs: int = 100
    batch_size: int = 4
    num_workers: int = 0
    devices: Union[list[int], str] = "cpu"
    patience: int = 10


@dataclass
class LightningParams:
    time_intervals: int
    dataset_params: DatasetParams
    train_params: TrainingParams
    model_params: ModelParams

    def __post_init__(self):
        self.dataset_params = DatasetParams(**self.dataset_params)
        self.train_params = TrainingParams(**self.train_params)
        self.model_params = ModelParams(**self.model_params)


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
        ci = {}
        for t in self.evaluation_times:
            ci[t] = concordance_index(event_times=durations, predicted_scores=surv[:, t], event_observed=events)
        return {"roc_auc": roc_auc, "ci": ci}


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
        for t, ci in results["ci"].items():
            self.log(f"ci_{t}", ci, rank_zero_only=True, sync_dist=True)
        for t, roc in results["roc_auc"].items():
            self.log(f"roc_auc_{t}", roc, rank_zero_only=True, sync_dist=True)

    def on_test_epoch_end(self) -> None:
        results = self.surv_metrics.compute()
        self.surv_metrics.reset()
        print(results)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        return optimizer


def prepare_data_for_training(dataset_params: DatasetParams, time_intervals: int):
    if dataset_params.dataset_name == "mimic_readmission":
        lab_trans = label_transforms.LabTransDiscreteTime(cuts=np.array([i for i in range(time_intervals + 1)], dtype=float))
        train, val, test = load_mimic_readmission(Path(dataset_params.params.root_path))
        train, val, test = MIMICReadmission(train, lab_trans), MIMICReadmission(val, lab_trans), MIMICReadmission(test, lab_trans)
    elif dataset_params.dataset_name == "smart_poc":
        train, val, test, name_map = load_smart_poc(
            Path(dataset_params.params.root_path),
            value_dict_path=Path(dataset_params.params.value_dict_path),
            data_dict_path=Path(dataset_params.params.data_dict_path),
        )
        lab_trans = label_transforms.LabTransDiscreteTime(time_intervals).fit(train["cd_time"].values, train["cd_event"].values)
        train, val, test = (
            SMARTPoC(train, name_map, lab_trans),
            SMARTPoC(val, name_map, lab_trans),
            SMARTPoC(test, name_map, lab_trans),
        )
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_params.dataset_name}")
    return train, val, test


def load_tokenizer(tokenizer_path: str):
    tokenizer_path = Path(tokenizer_path)
    tokenizer = ByteLevelBPETokenizer.from_file(
        str(tokenizer_path / "vocab.json"),
        str(tokenizer_path / "merges.txt"),
    )
    with open(tokenizer_path / "special_tokens.pkl", "rb") as f:
        special_tokens = pkl.load(f)
    tokenizer.add_special_tokens(special_tokens=special_tokens)
    tokenizer._tokenizer.model.continuing_subword_prefix = None
    tokenizer._tokenizer.model.end_of_word_suffix = None
    tokenizer.enable_padding(pad_id=tokenizer.token_to_id("<pad>"), pad_token="<pad>")

    return tokenizer


def load_lightning_model(model_params: ModelParams, time_intervals: int):
    if model_params.model_name == "clinical_longformer":
        tokenizer = AutoTokenizer.from_pretrained("yikuan8/Clinical-Longformer")
        model = MIMICNotesModel(
            time_intervals=time_intervals + 1,
            freeze_last_n_layers=model_params.h_params.freeze_last_n_layers,
            freeze_embeddings=model_params.h_params.freeze_embeddings,
        )
        collate_fn = partial(collate_fn_longformer, tokenizer=tokenizer)
    elif model_params.model_name == "transformer_encoder":
        tokenizer = load_tokenizer(model_params.h_params.tokenizer_path)
        num_embeddings = tokenizer.get_vocab_size()
        model = TransformerEncoderForClassification(
            num_embeddings=num_embeddings,
            d_model=model_params.h_params.d_model,
            nhead=model_params.h_params.nhead,
            dim_feedforward=model_params.h_params.dim_feedforward,
            num_layers=model_params.h_params.num_layers,
            dropout=model_params.h_params.dropout,
            activation=F.gelu,
            time_intervals=24,
        )
        collate_fn = partial(collate_fn_smart_poc, tokenizer=tokenizer)
    else:
        raise NotImplementedError(f"Unknown model: {model_params.model_name}")
    return model, collate_fn
