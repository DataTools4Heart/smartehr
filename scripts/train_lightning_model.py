import init
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
import os
import numpy as np
import torch
from transformers import AutoTokenizer
from dataset_utils.mimic import MIMICReadmission, MIMICNotesModel, collate_fn_longformer
from lightning_utils.utils import SurvivalAnalysisModule
from pycox.preprocessing import label_transforms
import lightning.pytorch as L
from torch.utils.data import DataLoader
from functools import partial
from pathlib import Path


from dataclasses import dataclass
from typing import Optional, Union
from pycox_utils.utils import load_pycox_model


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
    num_workers: int = min(batch_size, os.cpu_count())
    devices: Union[list[int], str] = "cpu"
    patience: int = 10


@dataclass
class MimicReadmissionParams:
    model_params: ModelParams
    train_params: TrainingParams


from pycox.preprocessing.discretization import DiscretizeUnknownC, Duration2Idx


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


def train_lightning_model(root_path: Path, params: MimicReadmissionParams):
    time_intervals = 365
    model_params = params.model_params
    train_params = params.train_params
    model, lab_trans, collate_fn = load_lightning_model(model_params, time_intervals=time_intervals)
    train = MIMICReadmission(root_path, lab_trans, split="train")
    val = MIMICReadmission(root_path, lab_trans, split="val")
    test = MIMICReadmission(root_path, lab_trans, split="test")

    model = SurvivalAnalysisModule(model, lr=train_params.lr)

    train_dl = DataLoader(
        train, batch_size=train_params.batch_size, shuffle=True, collate_fn=collate_fn, num_workers=train_params.num_workers
    )
    val_dl = DataLoader(
        val, batch_size=train_params.batch_size, shuffle=False, collate_fn=collate_fn, num_workers=train_params.num_workers
    )
    test_dl = DataLoader(test, batch_size=1, shuffle=False, collate_fn=collate_fn, num_workers=1)

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    torch.set_float32_matmul_precision("medium")
    devices = train_params.devices
    callbacks = [
        EarlyStopping(monitor="val_loss", mode="min", patience=train_params.patience),
        ModelCheckpoint(monitor="val_loss", mode="min"),
    ]
    strategy = "ddp_find_unused_parameters_true" if len(devices) > 1 else "auto"
    trainer = L.Trainer(
        callbacks=callbacks,
        devices=devices,
        max_epochs=train_params.epochs,
        strategy=strategy,
        precision="16-mixed" if isinstance(devices, list) or devices == "cuda" else "auto",
    )
    trainer.fit(model, train_dataloaders=train_dl, val_dataloaders=val_dl)
    trainer.test(dataloaders=test_dl)


def train_readmission_model(root_path: str):
    root_path = Path(root_path) / "readmission.csv"
