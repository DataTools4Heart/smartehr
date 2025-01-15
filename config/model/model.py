from dataclasses import dataclass
from hydra.core.config_store import ConfigStore


@dataclass
class ModelParams:
    name: str


@dataclass
class PycoxModelParams(ModelParams):
    batch_norm: bool
    dropout: float
    num_nodes: list[int]
    output_bias: bool

    def __post_init__(self):
        self.num_nodes = [int(n) for n in self.num_nodes]


@dataclass
class ClinicalLongformerModelParams(ModelParams):
    freeze_last_n_layers: int
    freeze_embeddings: bool


@dataclass
class TransformerEncoderModelParams(ModelParams):
    tokenizer_path: str
    d_model: int
    nhead: int
    dim_feedforward: int
    num_layers: int
    dropout: float


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(group="model", name="base_pycox", node=PycoxModelParams)
    cs.store(group="model", name="base_clinical_longformer", node=ClinicalLongformerModelParams)
    cs.store(group="model", name="base_transformer_encoder", node=TransformerEncoderModelParams)
