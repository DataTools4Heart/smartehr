from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from config.training.task import task


# Training params
@dataclass
class TrainingParams:
    pass


@dataclass
class LightningTrainingParams(TrainingParams):
    lr: float
    epochs: int
    batch_size: int
    num_workers: int
    accumulation_steps: int
    devices: list[int]
    patience: int
    resume_ckpt_path: None | str
    task: task.TaskParams
    # Precision string passed to Lightning Trainer (e.g. "bf16-true", "bf16-mixed", "16-mixed").
    # Use "16-mixed" on Tesla T4 (no native bf16); use "bf16-true" on A100/H100.
    precision: str = "bf16-true"
    # AdamW weight decay. 0.0 = no decay (previous behavior). Raise (e.g. 1e-2) to
    # regularize small-data survival runs that overfit.
    weight_decay: float = 0.0

    def __post_init__(self):
        self.devices = [int(device) for device in self.devices]


@dataclass
class PycoxTrainingParams(TrainingParams):
    batch_size: int
    device: str
    epochs: int
    patience: int
    lr: None | float


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="training",
        name="base_pycox",
        node=PycoxTrainingParams,
    )
    cs.store(
        group="training",
        name="base_lightning",
        node=LightningTrainingParams,
    )
    task.register_configs()
