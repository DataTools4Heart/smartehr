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
from config.dataset.dataset import DatasetParams
from config.training.task.task import SurvivalAnalysisParams, BinaryClassificationParams
from transformers import AutoTokenizer
from models.models import TransformerEncoderForClassification, MIMICNotesModel, WeightedLSTM, MLP
from functools import partial
import torch.nn.functional as F
from pathlib import Path
import pickle as pkl
from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import PreTrainedTokenizer
import random
from dataset_utils.mimic import MIMICWordTokenizer
from lightning_training.modules import SurvivalAnalysisModule, BinaryClassificationModule
import numpy as np
from pycox.preprocessing.label_transforms import LabTransDiscreteTime
from models.models import TANN
from typing import Callable, Optional


def collate_fn_longformer(batch, tokenizer: PreTrainedTokenizer):
    features, durations, events = (
        [b[0]["text"] for b in batch],
        [b[1]["duration"] for b in batch],
        [b[1]["event"] for b in batch],
    )
    encodings = tokenizer.batch_encode_plus(features, padding=True, max_length=4096, truncation=True, return_tensors="pt")
    return (
        {"input_ids": encodings["input_ids"], "attention_mask": encodings["attention_mask"]},
        torch.tensor(durations),
        torch.tensor(events),
    )


def collate_fn_longformer_longitudinal(batch, task: str, tokenizer: PreTrainedTokenizer, lab_trans: Optional[Callable] = None):
    features = [b[0]["text"].iloc[0] for b in batch]
    durations = np.array([b[1]["duration"] for b in batch])
    events = np.array([b[1]["event"] for b in batch])
    encodings = tokenizer.batch_encode_plus(features, padding=True, max_length=4096, truncation=True, return_tensors="pt")
    if task == "survival_analysis":
        durations, events = lab_trans(durations, events)
        durations = torch.from_numpy(durations).squeeze(1)
        events = torch.from_numpy(events).squeeze(1)
        labels = {"duration": durations, "event": events}
    elif task == "binary_classification":
        labels = torch.from_numpy(durations)
        thirty_day_mask = labels <= 30
        labels[thirty_day_mask] = 1
        labels[~thirty_day_mask] = 0
    else:
        raise NotImplementedError(f"Unknown task: {task}")
    return {
        "inputs": {"input_ids": encodings["input_ids"], "attention_mask": encodings["attention_mask"]},
        "labels": labels,
    }


def collate_fn_smart_poc(batch, tokenizer: ByteLevelBPETokenizer):
    features, durations, events = [b[0] for b in batch], [b[1] for b in batch], [b[2] for b in batch]
    features = [[v for v in f.values()] for f in features]

    for i in range(len(features)):
        random.shuffle(features[i])
        features[i] = "<sep>".join(features[i])

    encodings = tokenizer.encode_batch(features)
    ids = torch.stack([torch.tensor(e.ids) for e in encodings])
    masks = ~torch.stack([torch.tensor(e.attention_mask, dtype=torch.bool) for e in encodings])

    return (
        {"input_ids": ids, "padding_mask": masks},
        torch.tensor(durations),
        torch.tensor(events),
    )


def collate_fn_rnn_longitudinal(
    batch, tokenizer: PreTrainedTokenizer, task: str = "survival", lab_trans: Optional[Callable] = None
):
    inputs = [b[0] for b in batch]
    durations = np.array([b[1]["duration"] for b in batch])
    events = np.array([b[1]["event"] for b in batch])
    time_deltas = [b[1]["time_deltas"] for b in batch]
    inputs = [[torch.tensor(tokenizer.encode(x), dtype=torch.long) for x in item["text"]] for item in inputs]
    if task == "survival_analysis":
        durations, events = lab_trans(durations, events)
        durations = torch.from_numpy(durations).squeeze(1)
        events = torch.from_numpy(events).squeeze(1)
        labels = {"duration": durations, "event": events}
    elif task == "binary_classification":
        labels = torch.from_numpy(durations)
        thirty_day_mask = labels <= 30
        labels[thirty_day_mask] = 1
        labels[~thirty_day_mask] = 0
    else:
        raise NotImplementedError(f"Unknown task: {task}")

    return {
        "inputs": {"input_ids_list": inputs, "time_deltas_list": [torch.tensor(t, dtype=torch.float32) for t in time_deltas]},
        "labels": labels,
    }


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


def collate_fn_mlp(batch):
    features = [b[0].loc[:, b[0].columns != "text"].iloc[-1].values for b in batch]
    features = torch.tensor(features)
    durations = np.array([b[1]["duration"] for b in batch])
    labels = torch.from_numpy(durations)
    thirty_day_mask = labels <= 30
    labels[thirty_day_mask] = 1
    labels[~thirty_day_mask] = 0
    return {
        "inputs": {"inputs": features},
        "labels": labels,
    }


from hydra.core.hydra_config import HydraConfig


def load_lightning_model(model_params: ModelParams, train_params: LightningTrainingParams):
    task_name = HydraConfig.get().runtime.choices["training/task"]
    model_name = HydraConfig.get().runtime.choices["model"]
    task_params = train_params.task
    if task_name == "survival_analysis":
        task_params = SurvivalAnalysisParams(**task_params)
        lab_trans = LabTransDiscreteTime(
            cuts=np.array([i for i in range(task_params.num_time_intervals - 1)], dtype=float)
        ).transform
        num_outputs = task_params.num_time_intervals
        module_cls = partial(SurvivalAnalysisModule, evaluation_times=task_params.evaluation_times)
    elif task_name == "binary_classification":
        task_params = BinaryClassificationParams(**task_params)
        num_outputs = 1
        lab_trans = None
        module_cls = BinaryClassificationModule
    else:
        raise NotImplementedError(f"Unknown task: {task_name}")

    if model_name == "clinical_longformer":
        model_params = ClinicalLongformerModelParams(**model_params)
        tokenizer = AutoTokenizer.from_pretrained("yikuan8/Clinical-Longformer")
        model = MIMICNotesModel(  # TODO: change the name of the model
            time_intervals=num_outputs,
            freeze_last_n_layers=model_params.freeze_last_n_layers,
            freeze_embeddings=model_params.freeze_embeddings,
        )

        # collate_fn = partial(collate_fn_longformer, tokenizer=tokenizer)
        collate_fn = partial(collate_fn_longformer_longitudinal, task=task_name, tokenizer=tokenizer, lab_trans=lab_trans)
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
        collate_fn = partial(collate_fn_smart_poc, tokenizer=tokenizer)
    elif model_name == "mlp":
        model_params = MLPModelParams(**model_params)
        model = MLP(
            input_size=model_params.input_size,
            output_size=task_params.num_time_intervals,
            num_nodes=model_params.num_nodes,
            dropout=model_params.dropout,
        )
        collate_fn = collate_fn_mlp
    elif model_name == "weighted_lstm":
        model_params = WeightedLSTMModelParams(**model_params)
        tokenizer = MIMICWordTokenizer(vocab_path=model_params.vocab_path, lang=model_params.lang)
        model = WeightedLSTM(
            vocab_size=len(tokenizer.vocab),
            word_embedding_dim=model_params.word_embedding_dim,
            time_embedding_dim=model_params.time_embedding_dim,
            lstm_hidden_size=model_params.lstm_hidden_size,
            lstm_dropout=model_params.lstm_dropout,
            num_outputs=num_outputs,
        )
        collate_fn = partial(collate_fn_rnn_longitudinal, tokenizer=tokenizer, task=task_name, lab_trans=lab_trans)
    elif model_name == "tann":
        model_params = TANNModelParams(**model_params)
        tokenizer = MIMICWordTokenizer(vocab_path=model_params.vocab_path, lang=model_params.lang)
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
        collate_fn = partial(collate_fn_rnn_longitudinal, tokenizer=tokenizer, task=task_name, lab_trans=lab_trans)
    else:
        raise NotImplementedError(f"Unknown model: {model_params.name}")

    model = module_cls(model, lr=train_params.lr)
    return model, collate_fn
