import init
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
import os
import torch
from lightning_training.modules import SurvivalAnalysisModule
import lightning.pytorch as L
from torch.utils.data import DataLoader
from lightning_training.utils import load_lightning_model
from dataset_utils.utils import load_for_lightning
import hydra
from config.config import Config
from config.training.training import LightningTrainingParams
from lightning_training.collator import build_collate_fn


@hydra.main(version_base=None, config_path="../config", config_name="config")
def train_lightning_model(cfg: Config):
    if torch.cuda.is_available():
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        torch.set_float32_matmul_precision("medium")

    model_params = cfg.model
    train_params = cfg.training
    dataset_params = cfg.dataset
    train_params = LightningTrainingParams(**train_params)

    model, tokenizer = load_lightning_model(model_params, train_params)
    collate_fn = build_collate_fn(dataset_params.name, model_params.name, tokenizer)
    train, val, test = load_for_lightning(dataset_params, train_params.task)

    train_dl = DataLoader(
        train, batch_size=train_params.batch_size, shuffle=True, collate_fn=collate_fn, num_workers=train_params.num_workers
    )
    val_dl = DataLoader(
        val, batch_size=train_params.batch_size, shuffle=False, collate_fn=collate_fn, num_workers=train_params.num_workers
    )
    test_dl = DataLoader(test, batch_size=1, shuffle=False, collate_fn=collate_fn, num_workers=1)

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
        accumulate_grad_batches=train_params.accumulation_steps,
    )
    trainer.fit(model, train_dataloaders=train_dl, val_dataloaders=val_dl)
    trainer.test(dataloaders=test_dl)


if __name__ == "__main__":
    train_lightning_model()
