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
    task: task.TaskParams

    def __post_init__(self):
        self.devices = [int(device) for device in self.devices]


@dataclass
class PycoxTrainingParams(TrainingParams):
    batch_size: int
    device: str
    epochs: int
    patience: int


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
