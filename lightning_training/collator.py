import torch
from functools import partial
import torch.nn.functional as F
from pathlib import Path
import pickle as pkl
from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import PreTrainedTokenizer
import random
from tokenizer_utils.word_tokenizer import WordTokenizer
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


def collate_fn_weighted_lstm(batch):
    features = [b["features"] for b in batch]
    time_deltas_list = [b["time_deltas"] for b in batch]
    outcomes = torch.cat([b["outcomes"] for b in batch])
    inputs = {"input_ids_list": features, "time_deltas_list": time_deltas_list}
    return {"inputs": inputs, "multiclass_cls_labels": outcomes}


def collate_fn_tann(batch, data_types: str):
    input_ids_list = [b["features"] for b in batch]
    time_deltas_list = [b["time_deltas"] for b in batch]
    outcomes = torch.cat([b["outcomes"] for b in batch])
    sequences = []
    time_deltas = []
    for batch_item, time_delta in zip(input_ids_list, time_deltas_list):
        sequence = []
        deltas = []
        for i, feature_dict in enumerate(batch_item):
            for feature_name, input_ids in feature_dict.items():
                if data_types == "structured":
                    if feature_name == "clinical_note":
                        continue
                elif data_types == "unstructured":
                    if feature_name != "clinical_note":
                        continue
                delta = torch.broadcast_to(time_delta[i], (input_ids.shape[0],))
                sequence.append(input_ids)
                deltas.append(delta)
        sequence = torch.cat(sequence, dim=0)
        sequences.append(sequence)
        deltas = torch.cat(deltas, dim=0)
        time_deltas.append(deltas)
    sequences_end = torch.tensor(
        [seq.shape[0] for seq in sequences], dtype=torch.int64, device=sequences[0].device, requires_grad=False
    )
    sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True, padding_value=0)
    time_deltas = torch.nn.utils.rnn.pad_sequence(time_deltas, batch_first=True, padding_value=0)
    return {
        "inputs": {"sequences": sequences, "time_deltas": time_deltas, "sequences_end": sequences_end},
        "multiclass_cls_labels": outcomes,
    }


def collate_fn_clinical_longformer(batch, pad_value: int = 0):
    inputs = [b["input_ids"] for b in batch]
    inputs = [torch.tensor(ids)[:4096] for ids in inputs]
    attention_mask = [torch.ones_like(ids) for ids in inputs]
    inputs = torch.nn.utils.rnn.pad_sequence(inputs, batch_first=True, padding_value=pad_value)
    attention_mask = torch.nn.utils.rnn.pad_sequence(attention_mask, batch_first=True, padding_value=0)
    outcomes = torch.tensor([b["labels"] for b in batch])
    return {"inputs": {"input_ids": inputs, "attention_mask": attention_mask}, "multiclass_cls_labels": outcomes}


def collate_fn_llm(batch, pad_value: int = 0, max_tokens: int | None = None):
    inputs = [b["input_ids"] for b in batch]
    if max_tokens is not None:
        inputs = [ids[-max_tokens:] for ids in inputs]
    inputs = [torch.tensor(ids) for ids in inputs]

    attention_mask = [torch.ones_like(ids) for ids in inputs]
    inputs = torch.nn.utils.rnn.pad_sequence(inputs, batch_first=True, padding_value=pad_value)
    attention_mask = torch.nn.utils.rnn.pad_sequence(attention_mask, batch_first=True, padding_value=0)
    outcomes = torch.tensor([b["labels"] for b in batch])
    return {"inputs": {"input_ids": inputs, "attention_mask": attention_mask}, "multiclass_cls_labels": outcomes}


def collate_fn_mlp(batch):
    inputs = [b["inputs"] for b in batch]
    outcomes = [b["labels"] for b in batch]
    inputs = torch.tensor(inputs)
    outcomes = torch.tensor(outcomes)
    return {
        "inputs": {"inputs": inputs},
        "multiclass_cls_labels": outcomes,
    }


def collate_fn_tr_mlp(batch):
    inputs = [b["inputs"] for b in batch]
    outcomes = [b["labels"] for b in batch]
    time_deltas_list = [b["time_deltas_list"] for b in batch]
    inputs = [torch.tensor(sequence) for sequence in inputs]
    inputs = torch.nn.utils.rnn.pad_sequence(inputs, batch_first=True, padding_value=0)
    time_deltas_list = [torch.tensor(deltas) for deltas in time_deltas_list]
    outcomes = torch.tensor(outcomes)
    return {"inputs": {"input_sequence": inputs, "time_deltas_list": time_deltas_list}, "multiclass_cls_labels": outcomes}


def collate_fn_tr_lm(
    batch, lm_batch_size: int, lm_pad_value: int = 0, max_tokens: int | None = None, max_seq_length: int | None = None
):

    input_ids_list = [b["input_ids_list"] for b in batch]
    time_deltas_list = [b["time_deltas_list"] for b in batch]
    if max_seq_length is not None:
        input_ids_list = [sequence[-max_seq_length:] for sequence in input_ids_list]
        time_deltas_list = [deltas[-max_seq_length:] for deltas in time_deltas_list]

    input_ids_list = [[torch.tensor(ids) for ids in sequence] for sequence in input_ids_list]
    time_deltas_list = [torch.tensor(deltas) for deltas in time_deltas_list]
    outcomes = torch.tensor([b["labels"] for b in batch])

    # Flatten and track original structure
    flat_tensors = []
    attention_masks = []
    for sequence in input_ids_list:
        for tensor in sequence:
            if max_tokens is not None:
                tensor = tensor[:max_tokens]
            flat_tensors.append(tensor)
            attention_masks.append(torch.ones_like(tensor, device=flat_tensors[0].device))

    # Process in batches
    lm_batches = []
    lm_masks = []

    for i in range(0, len(flat_tensors), lm_batch_size):
        batch_tensors = flat_tensors[i : i + lm_batch_size]
        batch_masks = attention_masks[i : i + lm_batch_size]

        # Pad batch to max length
        max_len = max(len(t) for t in batch_tensors)
        padded_tensors = torch.stack(
            [torch.nn.functional.pad(t, (0, max_len - len(t)), value=lm_pad_value) for t in batch_tensors]
        )
        padded_masks = torch.stack([torch.nn.functional.pad(m, (0, max_len - len(m)), value=0) for m in batch_masks])
        lm_batches.append(padded_tensors)
        lm_masks.append(padded_masks)

    return {
        "inputs": {"lm_batches": lm_batches, "lm_masks": lm_masks, "time_deltas_list": time_deltas_list},
        "multiclass_cls_labels": outcomes,
    }


def collate_fn_tr_embedding(batch):
    embeddings = [b["embeddings"] for b in batch]
    embeddings = [torch.tensor(sequence) for sequence in embeddings]
    time_deltas_list = [b["time_deltas_list"] for b in batch]
    time_deltas_list = [torch.tensor(deltas) for deltas in time_deltas_list]
    outcomes = torch.tensor([b["labels"] for b in batch])
    embeddings = torch.nn.utils.rnn.pad_sequence(embeddings, batch_first=True, padding_value=0)
    return {"inputs": {"embeddings": embeddings, "time_deltas_list": time_deltas_list}, "multiclass_cls_labels": outcomes}


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
    dataset_name: str, model_params, tokenizer: PreTrainedTokenizer | ByteLevelBPETokenizer | WordTokenizer | None = None
):
    model_name = model_params.name
    if dataset_name == "longitudinal_mimic_readmission":
        dataset_collate_fn = collate_fn_longitudinal_mimic_readmission
    elif dataset_name == "smart_poc":
        dataset_collate_fn = collate_fn_smart_poc
    elif dataset_name == "longitudinal_mimic_los":
        dataset_collate_fn = lambda x: x
    elif dataset_name == "longitudinal_dummy_smart":
        dataset_collate_fn = lambda x: x
    else:
        raise NotImplementedError(f"Unknown dataset: {dataset_name}")

    if model_name == "weighted_lstm":
        model_collate_fn = collate_fn_weighted_lstm
    elif model_name == "tann":
        model_collate_fn = partial(collate_fn_tann, data_types=model_params.data_types)
    elif model_name == "mlp":
        model_collate_fn = collate_fn_mlp
    elif model_name == "clinical_longformer":
        model_collate_fn = partial(collate_fn_clinical_longformer, pad_value=tokenizer.pad_token_id)
    elif model_name == "llm":
        _llm_fn = partial(collate_fn_llm, pad_value=tokenizer.pad_token_id, max_tokens=model_params.max_tokens)
        # collate_fn_llm always emits multiclass_cls_labels; remap for binary tasks
        def model_collate_fn(batch):
            out = _llm_fn(batch)
            if "multiclass_cls_labels" in out and "binary_cls_labels" not in out:
                out["binary_cls_labels"] = out.pop("multiclass_cls_labels").float()
            return out
    elif model_name == "temporal_recurrent_lm":
        model_collate_fn = partial(
            collate_fn_tr_lm,
            lm_batch_size=model_params.lm_batch_size,
            lm_pad_value=tokenizer.pad_token_id,
            max_tokens=model_params.max_tokens,
            max_seq_length=model_params.max_seq_length,
        )
    elif model_name == "temporal_recurrent_embeddings":
        model_collate_fn = collate_fn_tr_embedding
    elif model_name == "temporal_recurrent_mlp":
        model_collate_fn = collate_fn_tr_mlp
    else:
        raise NotImplementedError(f"Unknown model: {model_name}")

    return lambda batch: model_collate_fn(dataset_collate_fn(batch))
