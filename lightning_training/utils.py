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
import math


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


def build_pmf_time_grid(
    horizon_days: float,
    interval_width_days: float | None = None,
    num_time_intervals: int | None = None,
) -> tuple[int, list[float]]:
    """Build a discrete-time grid for pycox's PMF loss.

    `nll_pmf` pads the open-ended tail internally, so `num_time_intervals`
    equals the number of finite cut points / model outputs. The final cut is the
    prediction horizon itself.
    """
    if (interval_width_days is None) == (num_time_intervals is None):
        raise ValueError("Provide exactly one of interval_width_days or num_time_intervals.")
    if horizon_days <= 0:
        raise ValueError("horizon_days must be positive.")

    if interval_width_days is not None:
        if interval_width_days <= 0:
            raise ValueError("interval_width_days must be positive.")
        raw_intervals = horizon_days / interval_width_days
        rounded_intervals = round(raw_intervals)
        if not math.isclose(raw_intervals, rounded_intervals, rel_tol=1e-9, abs_tol=1e-9):
            raise ValueError(
                "interval_width_days must divide horizon_days exactly to place the horizon on a cut point."
            )
        num_time_intervals = int(rounded_intervals)

    assert num_time_intervals is not None
    if num_time_intervals <= 0:
        raise ValueError("num_time_intervals must be positive.")

    step = horizon_days / num_time_intervals
    cuts = [step * (idx + 1) for idx in range(num_time_intervals)]
    return num_time_intervals, cuts


def evaluation_time_index_for_day(target_day: float, cuts: list[float]) -> int:
    """Return the PMF evaluation index whose cut point matches `target_day`."""
    for idx, cut in enumerate(cuts):
        if math.isclose(cut, target_day, rel_tol=1e-9, abs_tol=1e-6):
            return idx
    raise ValueError(f"target_day={target_day} does not fall exactly on any cut point.")


def load_lightning_model(model_params: ModelParams, train_params: LightningTrainingParams):
    task_name = train_params.task.name
    model_name = model_params.name
    task_params = train_params.task
    if task_name == "survival_analysis":
        task_params = SurvivalAnalysisParams(**task_params)
        num_outputs = task_params.num_time_intervals
        # dataset_utils.utils.load_for_lightning clips durations to cuts[-1] before
        # np.searchsorted, so bin index num_outputs-1 never receives any sample
        # (event or censored) — it's structurally empty regardless of the data.
        # bin num_outputs-2 IS reachable (it absorbs everything clipped to cuts[-1],
        # often a large administrative-censoring pileup at the horizon), but it is
        # also the maximum value any sample can take. time_dependent_roc_auc_score
        # (utils.py) defines controls as durations > time, so evaluating exactly at
        # the max value always yields zero controls — degenerate regardless of data.
        # The first evaluation index that can have nonzero controls is num_outputs-3.
        max_eval_time = num_outputs - 3
        raw_times = task_params.evaluation_times
        clamped = [min(t, max_eval_time) for t in raw_times]
        if clamped != raw_times:
            adjusted = {r: c for r, c in zip(raw_times, clamped) if r != c}
            print(f"  evaluation_times: clamped {adjusted} to last valid bin (max={max_eval_time})")
        evaluation_times = sorted(set(clamped))
        module_cls = partial(SurvivalAnalysisModule, evaluation_times=evaluation_times)
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
            hidden_dim=model_params.hidden_dim,
            time_delta_dim=model_params.time_delta_dim,
            input_dropout=model_params.input_dropout,
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

    model = module_cls(model, lr=train_params.lr, weight_decay=train_params.weight_decay)
    return model, tokenizer


def save_config(cfg, logger):
    config_dict = OmegaConf.to_container(cfg, resolve=True)
    config_path = os.path.join(logger.log_dir, "config.yaml")

    with open(config_path, "w") as f:
        yaml.dump(config_dict, f, default_flow_style=False)

    print(f"Config saved to: {config_path}")
