from dataclasses import dataclass
from hydra.core.config_store import ConfigStore


# Task params
@dataclass
class TaskParams:
    pass


# Training params
@dataclass
class BinaryClassificationParams(TaskParams):
    pass


@dataclass
class SurvivalAnalysisParams(TaskParams):
    num_time_intervals: int
    evaluation_times: list[int]


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="training/task",
        name="base_binary_classification",
        node=BinaryClassificationParams,
    )
    cs.store(
        group="training/task",
        name="base_survival_analysis",
        node=SurvivalAnalysisParams,
    )
