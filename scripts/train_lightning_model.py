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
from lightning.pytorch.loggers import TensorBoardLogger
from lightning_training.utils import save_config
from lightning_training.transforms import apply_transforms
from transformers import set_seed


@hydra.main(version_base=None, config_path="../config", config_name="config")
def train_lightning_model(cfg: Config):
    set_seed(42)
    if torch.cuda.is_available():
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        torch.set_float32_matmul_precision("medium")

    model_params = cfg.model
    train_params = cfg.training
    dataset_params = cfg.dataset
    train_params = LightningTrainingParams(**train_params)

    model, tokenizer = load_lightning_model(model_params, train_params)
    train, val, test = load_for_lightning(dataset_params, train_params.task)
    train, val, test = apply_transforms(train, val, test, model_params.name)

    collate_fn = build_collate_fn(dataset_params.name, model_params, tokenizer)

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

    logger = TensorBoardLogger(save_dir=".", name=f"lightning_logs/{model_params.name}")
    trainer = L.Trainer(
        callbacks=callbacks,
        devices=devices,
        max_epochs=train_params.epochs,
        strategy=strategy,
        precision="bf16-true" if isinstance(devices, list) or devices == "cuda" else "auto",
        accumulate_grad_batches=train_params.accumulation_steps,
        logger=logger,
        log_every_n_steps=2,
    )
    trainer.fit(model, train_dataloaders=train_dl, val_dataloaders=val_dl)
    trainer.test(dataloaders=test_dl)
    if trainer.is_global_zero:
        save_config(cfg, logger)


if __name__ == "__main__":
    train_lightning_model()
