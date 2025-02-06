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


@dataclass
class WeightedLSTMModelParams(ModelParams):
    vocab_path: str
    lang: str
    word_embedding_dim: int
    time_embedding_dim: int
    lstm_hidden_size: int
    lstm_dropout: float


@dataclass
class TANNModelParams(ModelParams):
    vocab_path: str
    lang: str
    embedding_dim: int
    hidden_dim: int
    num_layers: int
    k: int
    one_day: float
    uniform_bank: bool
    probabilities: list[float] | None


@dataclass
class MLPModelParams(ModelParams):
    input_size: int
    num_nodes: list[int]
    dropout: float


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(group="model", name="base_pycox", node=PycoxModelParams)
    cs.store(group="model", name="base_clinical_longformer", node=ClinicalLongformerModelParams)
    cs.store(group="model", name="base_transformer_encoder", node=TransformerEncoderModelParams)
    cs.store(group="model", name="base_weighted_lstm", node=WeightedLSTMModelParams)
    cs.store(group="model", name="base_tann", node=TANNModelParams)
    cs.store(group="model", name="base_mlp", node=MLPModelParams)
