import torch
from functools import partial
import torch.nn.functional as F
from pathlib import Path
import pickle as pkl
from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import PreTrainedTokenizer
import random
from dataset_utils.mimic import WordTokenizer
import numpy as np
from dataclasses import dataclass


@dataclass
class DatasetBatch:
    inputs: torch.Tensor | None = None
    texts: list[str] | list[list[str]] | None = None
    binary_cls_labels: torch.Tensor | None = None
    survival_labels: dict[str, torch.Tensor] | None = None
    multiclass_cls_labels: torch.Tensor | None = None
    time_deltas_list: list[torch.Tensor] | None = None

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        setattr(self, item, value)


def collate_fn_longitudinal_mimic_readmission(batch):
    inputs = torch.tensor([b[0]["features"].values for b in batch])
    texts = [b[0]["text"] for b in batch]
    time_deltas = [torch.tensor(b[1]["time_deltas"]) for b in batch]
    durations = torch.tensor([b[1]["duration"] for b in batch])
    events = torch.tensor([b[1]["event"] for b in batch])
    binary_cls_labels = ((durations <= 30) & (events == 1)).float()
    survival_labels = {"duration": durations[durations > 30], "event": events[durations > 30]}
    return DatasetBatch(
        inputs=inputs,
        texts=texts,
        binary_cls_labels=binary_cls_labels,
        survival_labels=survival_labels,
        time_deltas_list=time_deltas,
    )


def collate_fn_longitudinal_mimic_los(batch):
    inputs = [
        torch.tensor(b["features"][[col for col in b["features"].columns if col != "text"]].values, dtype=torch.float32)
        for b in batch
    ]
    texts = [b["features"]["text"].values for b in batch]
    time_deltas = [torch.tensor(b["time_deltas"], dtype=torch.float32) for b in batch]
    multiclass_labels = torch.tensor(np.array([b["outcomes"]["los"] for b in batch]), dtype=torch.long).squeeze(1)
    return DatasetBatch(
        inputs=inputs,
        texts=texts,
        multiclass_cls_labels=multiclass_labels,
        time_deltas_list=time_deltas,
    )


def collate_fn_weighted_lstm(batch: DatasetBatch, tokenizer: WordTokenizer):
    inputs_ids_list = [[torch.tensor(tokenizer.encode(t), dtype=torch.long) for t in texts] for texts in batch.texts]
    batch.inputs = {"input_ids_list": inputs_ids_list, "time_deltas_list": batch.time_deltas_list}
    return batch


def collate_fn_tann(batch: DatasetBatch, tokenizer: WordTokenizer):
    return collate_fn_weighted_lstm(batch, tokenizer)


def collate_fn_longformer(batch: DatasetBatch, tokenizer: PreTrainedTokenizer):
    encodings = tokenizer.batch_encode_plus(batch.texts, padding=True, max_length=4096, truncation=True, return_tensors="pt")
    batch.inputs = {"input_ids": encodings["input_ids"], "attention_mask": encodings["attention_mask"]}
    return batch


def collate_fn_mlp(batch: DatasetBatch):
    return batch


def collate_fn_smart_poc(batch: DatasetBatch, tokenizer: ByteLevelBPETokenizer):
    for i in range(len(batch.inputs)):
        random.shuffle(batch.inputs[i])
        batch.inputs[i] = "<sep>".join(batch.inputs[i])

    encodings = tokenizer.encode_batch(batch.inputs)
    ids = torch.stack([torch.tensor(e.ids) for e in encodings])
    masks = ~torch.stack([torch.tensor(e.attention_mask, dtype=torch.bool) for e in encodings])
    batch.inputs = {"input_ids": ids, "padding_mask": masks}
    return batch


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


def build_collate_fn(
    dataset_name: str, model_name: str, tokenizer: PreTrainedTokenizer | ByteLevelBPETokenizer | WordTokenizer | None = None
):
    if dataset_name == "longitudinal_mimic_readmission":
        dataset_collate_fn = collate_fn_longitudinal_mimic_readmission
    elif dataset_name == "longitudinal_mimic_los":
        dataset_collate_fn = collate_fn_longitudinal_mimic_los
    elif dataset_name == "smart_poc":
        dataset_collate_fn = collate_fn_smart_poc
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_name}")

    if model_name == "weighted_lstm":
        model_collate_fn = partial(collate_fn_weighted_lstm, tokenizer=tokenizer)
    elif model_name == "tann":
        model_collate_fn = partial(collate_fn_tann, tokenizer=tokenizer)
    elif model_name == "mlp":
        model_collate_fn = collate_fn_mlp
    elif model_name == "clinical_longformer":
        model_collate_fn = partial(collate_fn_longformer, tokenizer=tokenizer)
    else:
        raise NotImplementedError(f"Unknown model: {model_name}")

    return lambda batch: model_collate_fn(dataset_collate_fn(batch))
