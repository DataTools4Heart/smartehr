import init
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
import os
import torch
from lightning_utils.utils import SurvivalAnalysisModule
import lightning.pytorch as L
from torch.utils.data import DataLoader
import argparse
from omegaconf import OmegaConf
from lightning_utils.utils import prepare_data_for_training
from lightning_utils.utils import load_lightning_model, MimicReadmissionParams


def train_lightning_model(params: MimicReadmissionParams):
    time_intervals = 365
    model_params = params.model_params
    train_params = params.train_params
    dataset_params = params.dataset_params
    model, lab_trans, collate_fn = load_lightning_model(model_params, time_intervals=time_intervals)
    train, val, test = prepare_data_for_training(dataset_params, lab_trans)

    model = SurvivalAnalysisModule(model, lr=train_params.lr)

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Lightning model for MIMIC readmission prediction.")
    parser.add_argument("--cfg-path", type=str, required=True, help="Path to the configuration file.")
    args = parser.parse_args()

    # Load configuration from the provided path
    with open(args.cfg_path, "r") as f:
        yaml_conf = OmegaConf.to_container(OmegaConf.load(f), resolve=True)
    params = MimicReadmissionParams(**yaml_conf)

    # Train the model
    train_lightning_model(params)
