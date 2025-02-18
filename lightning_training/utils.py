import torch
from config.model.model import (
    ModelParams,
    ClinicalLongformerModelParams,
    TransformerEncoderModelParams,
    WeightedLSTMModelParams,
    TANNModelParams,
    MLPModelParams,
)
from config.training.training import LightningTrainingParams
from config.training.task.task import SurvivalAnalysisParams, BinaryClassificationParams, MulticlassClassificationParams
from transformers import AutoTokenizer
from models.models import TransformerEncoderForClassification, MIMICNotesModel, WeightedLSTM, MLP
from functools import partial
import torch.nn.functional as F
from pathlib import Path
import pickle as pkl
from tokenizers.implementations import ByteLevelBPETokenizer
from dataset_utils.mimic import WordTokenizer
from lightning_training.modules import SurvivalAnalysisModule, ClassificationModule
import numpy as np
from models.models import TANN


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
        task_params = BinaryClassificationParams(**task_params, num_outputs=1)
        num_outputs = 1
        module_cls = partial(ClassificationModule, task=task_name)
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
        model = MIMICNotesModel(  # TODO: change the name of the model
            time_intervals=num_outputs,
            freeze_last_n_layers=model_params.freeze_last_n_layers,
            freeze_embeddings=model_params.freeze_embeddings,
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
            output_size=task_params.num_time_intervals,
            num_nodes=model_params.num_nodes,
            dropout=model_params.dropout,
        )
    elif model_name == "weighted_lstm":
        model_params = WeightedLSTMModelParams(**model_params)
        tokenizer = WordTokenizer(vocab_path=model_params.vocab_path, lang=model_params.lang)
        model = WeightedLSTM(
            vocab_size=len(tokenizer.vocab),
            word_embedding_dim=model_params.word_embedding_dim,
            time_embedding_dim=model_params.time_embedding_dim,
            lstm_hidden_size=model_params.lstm_hidden_size,
            lstm_dropout=model_params.lstm_dropout,
            num_outputs=num_outputs,
        )
    elif model_name == "tann":
        model_params = TANNModelParams(**model_params)
        tokenizer = WordTokenizer(vocab_path=model_params.vocab_path, lang=model_params.lang)
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
