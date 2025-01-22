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
from lightning.pytorch.loggers import WandbLogger
from datetime import datetime

@hydra.main(version_base=None, config_path="../config", config_name="config")
def train_lightning_model(cfg: Config):
    model_params = cfg.model
    train_params = cfg.training
    dataset_params = cfg.dataset
    train_params = LightningTrainingParams(**train_params)

    model, collate_fn = load_lightning_model(model_params, train_params.time_intervals, train_params)
    train, val, test = load_for_lightning(dataset_params, train_params.time_intervals)

    #model = SurvivalAnalysisModule(model, lr=train_params.lr)

    train_dl = DataLoader(
        train, batch_size=train_params.batch_size, shuffle=True, collate_fn=collate_fn, num_workers=train_params.num_workers
    )
    val_dl = DataLoader(
        val, batch_size=train_params.batch_size, shuffle=False, collate_fn=collate_fn, num_workers=train_params.num_workers
    )
    test_dl = DataLoader(test, batch_size=1, shuffle=False, collate_fn=collate_fn, num_workers=1)

    if torch.cuda.is_available():
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        torch.set_float32_matmul_precision("medium")
    devices = train_params.devices
    print(devices, type(devices))
    experiment_name = f"{model_params.model_name}-{train_params.lr}-{train_params.batch_size}-{train_params.patience}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

    callbacks = [
        EarlyStopping(monitor="val_loss", mode="min", patience=train_params.patience),
        ModelCheckpoint(monitor="val_loss", mode="min",
                        dirpath=f"checkpoints/{experiment_name}"),
    ]
    strategy = "ddp_find_unused_parameters_true" if len(devices) > 1 else "auto"
    #create a unique name for the experiment with the current date and time
    trainer = L.Trainer(
        callbacks=callbacks,
        devices=devices,
        #max_epochs=train_params.epochs,
        logger=WandbLogger(project="survival-analysis", name=experiment_name),
        max_steps=train_params.max_steps, #these are backprop steps!!!!
        val_check_interval=5,
        strategy=strategy,
        precision="16-mixed" if isinstance(devices, list) or devices == "cuda" else "auto",
        accumulate_grad_batches=4,
        limit_val_batches=1000,
        limit_train_batches=10000,
        #limit_test_batches=100000,
        
    )
    trainer.fit(model, train_dataloaders=train_dl, val_dataloaders=val_dl)
    trainer.test(model, dataloaders=test_dl)

@hydra.main(version_base=None, config_path="../config", config_name="config")
def train_lightning_model_peft(cfg: Config):
    model_params = cfg.model
    train_params = cfg.training
    dataset_params = cfg.dataset
    train_params = LightningTrainingParams(**train_params)

if __name__ == "__main__":
    train_lightning_model()
