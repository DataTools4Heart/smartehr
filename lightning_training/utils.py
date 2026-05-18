import torch
from config.model.model import (
    ModelParams,
    ClinicalLongformerModelParams,
    TransformerEncoderModelParams,
    WeightedLSTMModelParams,
    TANNModelParams,
    MLPModelParams,
    TemporalRecurrentLMParams,
    LLMParams,
    TemporalRecurrentEmbeddingsParams,
    TemporalRecurrentMLPModelParams,
)
from config.training.training import LightningTrainingParams
from config.training.task.task import SurvivalAnalysisParams, BinaryClassificationParams, MulticlassClassificationParams
from transformers import AutoTokenizer
from models import (
    TransformerEncoderForClassification,
    WeightedLSTM,
    TANN,
    ClinicalLongformer,
    MLP,
    TemporalRecurrentLM,
    LLM,
    TemporalRecurrentEmbeddings,
    TemporalRecurrentMLP,
)
from functools import partial
import torch.nn.functional as F
from pathlib import Path
import pickle as pkl
from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizer_utils.word_tokenizer import load_tann_tokenizer, load_tokenizers
from lightning_training.modules import SurvivalAnalysisModule, ClassificationModule
from omegaconf import OmegaConf
from peft import get_peft_model, LoraConfig
import yaml
import os


def load_tokenizer(tokenizer_path: str):
    tokenizer_path = Path(tokenizer_path)
    tokenizer = ByteLevelBPETokenizer.from_file(
        str(tokenizer_path / "vocab.json"),
        str(tokenizer_path / "merges.txt"),
    )
    with open(tokenizer_path / "special_tokens.pkl", "rb") as f:
        special_tokens = pkl.load(f)
    tokenizer.add_special_tokens(special_tokens=special_tokens)
    tokenizer._tokenizer.model.continuing_subword_prefix = None
    tokenizer._tokenizer.model.end_of_word_suffix = None
    tokenizer.enable_padding(pad_id=tokenizer.token_to_id("<pad>"), pad_token="<pad>")

    return tokenizer


def load_lightning_model(model_params: ModelParams, train_params: LightningTrainingParams):
    task_name = train_params.task.name
    model_name = model_params.name
    task_params = train_params.task
    if task_name == "survival_analysis":
        task_params = SurvivalAnalysisParams(**task_params)
        num_outputs = task_params.num_time_intervals
        module_cls = partial(SurvivalAnalysisModule, evaluation_times=task_params.evaluation_times)
    elif task_name == "binary_classification":
        task_params = BinaryClassificationParams(**task_params)
        num_outputs = 1
        module_cls = partial(ClassificationModule, task=task_name, num_outputs=num_outputs)
    elif task_name == "multiclass_classification":
        task_params = MulticlassClassificationParams(**task_params)
        num_outputs = task_params.num_outputs
        module_cls = partial(ClassificationModule, task=task_name, num_outputs=num_outputs)
    else:
        raise NotImplementedError(f"Unknown task: {task_name}")

    tokenizer = None
    if model_name == "clinical_longformer":
        model_params = ClinicalLongformerModelParams(**model_params)
        tokenizer = AutoTokenizer.from_pretrained("yikuan8/Clinical-Longformer")
        model = ClinicalLongformer(
            num_outputs=num_outputs,
            freeze_first_n_layers=model_params.freeze_first_n_layers,
            freeze_embeddings=model_params.freeze_embeddings,
        )
    elif model_name == "llm":
        model_params = LLMParams(**model_params)
        model = LLM(
            llm_name=model_params.llm_name,
            llm_config_overrides=model_params.llm_config_overrides,
            num_outputs=num_outputs,
            freeze_backbone=model_params.freeze_backbone,
            gradient_checkpointing=model_params.gradient_checkpointing,
            chunk_size=model_params.chunk_size,
        )
        tokenizer = AutoTokenizer.from_pretrained(model_params.llm_name)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
    elif model_name == "temporal_recurrent_lm":
        model_params = TemporalRecurrentLMParams(**model_params)
        tokenizer = AutoTokenizer.from_pretrained(model_params.lm_name)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        model = TemporalRecurrentLM(
            lm_name=model_params.lm_name,
            lm_config_overrides=model_params.lm_config_overrides,
            num_outputs=num_outputs,
            is_encoder=model_params.is_encoder,
        )
        if model_params.use_lora:

            lora_config = LoraConfig(inference_mode=False, **model_params.lora_config)
            model.model = get_peft_model(model.model, lora_config)
    elif model_name == "temporal_recurrent_embeddings":
        model_params = TemporalRecurrentEmbeddingsParams(**model_params)
        model = TemporalRecurrentEmbeddings(
            embedding_dim=model_params.embedding_dim,
            num_outputs=num_outputs,
            dropout=model_params.dropout,
        )
    elif model_name == "temporal_recurrent_mlp":
        model_params = TemporalRecurrentMLPModelParams(**model_params)
        model = TemporalRecurrentMLP(
            input_size=model_params.input_size,
            output_size=num_outputs,
            num_nodes=model_params.num_nodes,
            dropout=model_params.dropout,
        )
    elif model_name == "transformer_encoder":
        model_params = TransformerEncoderModelParams(**model_params)
        tokenizer = load_tokenizer(model_params.tokenizer_path)
        num_embeddings = tokenizer.get_vocab_size()
        model = TransformerEncoderForClassification(
            num_embeddings=num_embeddings,
            d_model=model_params.d_model,
            nhead=model_params.nhead,
            dim_feedforward=model_params.dim_feedforward,
            num_layers=model_params.num_layers,
            dropout=model_params.dropout,
            activation=F.gelu,
            time_intervals=num_outputs,
        )
    elif model_name == "mlp":
        model_params = MLPModelParams(**model_params)
        model = MLP(
            input_size=model_params.input_size,
            output_size=num_outputs,
            num_nodes=model_params.num_nodes,
            dropout=model_params.dropout,
        )
    elif model_name == "weighted_lstm":
        model_params = WeightedLSTMModelParams(**model_params)
        vocab_path = Path(model_params.vocab_path)
        feature_types = [f.name.split(".")[0] for f in vocab_path.glob("*.json")]
        if model_params.data_types == "unstructured":
            feature_types = ["clinical_note"]
        elif model_params.data_types == "structured":
            feature_types = [k for k in feature_types if k not in ["clinical_note"]]
        tokenizer = load_tokenizers(vocab_path)
        vocabs = {feature_type: tokenizer[feature_type].vocab for feature_type in feature_types}
        model = WeightedLSTM(
            vocabs=vocabs,
            alpha_r=model_params.alpha_r,
            time_embedding_dim=model_params.time_embedding_dim,
            lstm_hidden_size=model_params.lstm_hidden_size,
            lstm_dropout=model_params.lstm_dropout,
            num_outputs=num_outputs,
        )
    elif model_name == "tann":
        model_params = TANNModelParams(**model_params)
        tokenizer = load_tann_tokenizer(Path(model_params.vocab_path))
        if not model_params.uniform_bank:
            assert model_params.probabilities is not None, "probabilities must be provided"
            assert len(model_params.probabilities) == 4, "probabilities must have length 4"
            assert torch.sum(torch.tensor(model_params.probabilities)) == 1, "probabilities must sum to 1"
        model = TANN(
            vocab_size=len(tokenizer.vocab),
            embedding_dim=model_params.embedding_dim,
            num_layers=model_params.num_layers,
            hidden_dim=model_params.hidden_dim,
            k=model_params.k,
            one_day=model_params.one_day,
            uniform_bank=model_params.uniform_bank,
            probabilities=model_params.probabilities,
            out_dim=num_outputs,
        )
    else:
        raise NotImplementedError(f"Unknown model: {model_params.name}")

    model = module_cls(model, lr=train_params.lr)
    return model, tokenizer


def save_config(cfg, logger):
    config_dict = OmegaConf.to_container(cfg, resolve=True)
    config_path = os.path.join(logger.log_dir, "config.yaml")

    with open(config_path, "w") as f:
        yaml.dump(config_dict, f, default_flow_style=False)

    print(f"Config saved to: {config_path}")
