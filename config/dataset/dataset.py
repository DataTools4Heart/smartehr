from dataclasses import dataclass
from hydra.core.config_store import ConfigStore


@dataclass
class DatasetParams:
    name: str


@dataclass
class SmartParams(DatasetParams):
    root_path: str
    use_full_feature_set: bool


@dataclass
class MimicReadmissionParams(DatasetParams):
    root_path: str


@dataclass
class LongitudinalMimicReadmissionParams(DatasetParams):
    root_path: str
    only_one_readmission_label: bool
    only_last_feature: bool


@dataclass
class LongitudinalMimicLoSParams(DatasetParams):
    root_path: str
    only_last_feature: bool


@dataclass
class SmartPoCParams(DatasetParams):
    root_path: str
    value_dict_path: str
    data_dict_path: str


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(group="dataset", name="base_smart", node=SmartParams)
    cs.store(group="dataset", name="base_mimic_readmission", node=MimicReadmissionParams)
    cs.store(group="dataset", name="base_smart_poc", node=SmartPoCParams)
    cs.store(group="dataset", name="base_longitudinal_mimic_readmission", node=LongitudinalMimicReadmissionParams)
    cs.store(group="dataset", name="base_longitudinal_mimic_los", node=LongitudinalMimicLoSParams)
