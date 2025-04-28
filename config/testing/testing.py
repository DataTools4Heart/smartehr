from dataclasses import dataclass, field
from hydra.core.config_store import ConfigStore
from typing import List, Optional, Union

@dataclass
class TestingParams:
    pass

@dataclass
class LightningTestingParams(TestingParams):
    checkpoint_path: str
    test_batch_size: int = 4
    time_intervals: int = 365
    devices: List[int] = field(default_factory=lambda: [0])
    num_workers: int = 1
    lr: float = 2e-4
    model_type: str = "llm"  # can be "llm" or "standard"

    def __post_init__(self):
        if isinstance(self.devices, str):
            self.devices = [int(d) for d in self.devices.split(',')]
        elif isinstance(self.devices, int):
            self.devices = [self.devices]

def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="testing",
        name="base_lightning",
        node=LightningTestingParams,
    )
