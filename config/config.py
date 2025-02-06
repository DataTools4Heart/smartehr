from dataclasses import dataclass

from hydra.core.config_store import ConfigStore
from omegaconf import ListConfig, DictConfig
import config.training.training as training
import config.model.model as model
import config.dataset.dataset as dataset
from typing import Any


def fail_on_missing(cfg: Any) -> None:
    if isinstance(cfg, ListConfig):
        for x in cfg:
            fail_on_missing(x)
    elif isinstance(cfg, DictConfig):
        for _, v in cfg.items():
            fail_on_missing(v)


@dataclass
class Config:
    dataset: dataset.DatasetParams
    model: model.ModelParams
    training: training.TrainingParams


cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)
dataset.register_configs()
model.register_configs()
training.register_configs()
