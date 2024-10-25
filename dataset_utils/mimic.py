import pandas as pd
from typing import Optional, Union
from pycox.preprocessing.label_transforms import LabTransCoxTime, LabTransDiscreteTime, LabTransPCHazard
import re
import os
import torch
import torch.nn as nn
from tokenizers import ByteLevelBPETokenizer
from torch import Tensor
from torch.utils.data import Dataset, DataLoader
from transformers import AutoModel

itemids_lab = [
    51006,
    51265,
    50960,
    50862,
    50893,
]

itemids_chart = [
    807,
    811,
    1529,
    3745,
    3744,
    225664,
    220621,
    226537,
    615,
    618,
    220210,
    224690,
    211,
    220045,
    51,
    442,
    455,
    6701,
    220179,
    220050,
    8368,
    8440,
    8441,
    8555,
    220180,
    220051,
    223761,
    678,
    223762,
    676,
    40055,
    226559,
]


def preprocess_note(note: str):
    """
    Preprocesses a clinical note by performing the following steps:
    1. Removes all de-identification placeholders "___".
    2. Replaces all characters other than alphanumericals and punctuation marks.
    3. Converts all alphabetical characters to lower case.
    4. Strips extra white spaces.

    Args:
        note (str): The clinical note to preprocess.

    Returns:
        str: The preprocessed clinical note.
    """
    preproc_note = re.sub(r"___", "", note)
    preproc_note = re.sub(r"[^a-zA-Z0-9.,;:!?()\-\'\"\s]", " ", preproc_note)
    preproc_note = preproc_note.lower()
    preproc_note = re.sub(r"\s+", " ", preproc_note).strip()
    return preproc_note


class MIMICReadmission(Dataset):
    def __init__(
        self,
        data: pd.DataFrame,
        lab_trans: Optional[Union[LabTransCoxTime, LabTransDiscreteTime, LabTransPCHazard]] = None,
    ):
        self.lab_trans = lab_trans
        self.data = data
        if self.lab_trans:
            self.outcomes = lab_trans.transform(self.data["days_next_admit"].values, self.data["event"].values)
        else:
            self.outcomes = (self.data["days_next_admit"].values, self.data["event"].values)
        self.data = self.data.drop(["days_next_admit", "event", "split", "hadm_id"], axis=1)
        self.data["text"] = self.data["text"].apply(preprocess_note)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        features = self.data.iloc[idx].to_dict()
        outcomes = [o[idx] for o in self.outcomes]
        return features, outcomes


class MIMICNotesModel(nn.Module):
    def __init__(self, time_intervals: int, freeze_last_n_layers: int = 0, freeze_embeddings: bool = False):
        super().__init__()
        assert freeze_last_n_layers >= 0, "freeze_last_n_layers must be greater than or equal to 0"
        self.time_intervals = time_intervals
        self.model = AutoModel.from_pretrained("yikuan8/Clinical-Longformer", add_pooling_layer=False)
        if freeze_last_n_layers > 0:
            for layer in self.model.encoder.layer[-freeze_last_n_layers:]:
                for param in layer.parameters():
                    param.requires_grad = False
        if freeze_embeddings:
            for param in self.model.embeddings.parameters():
                param.requires_grad = False

        self.cls = nn.Linear(self.model.config.hidden_size, time_intervals)

    def forward(self, input_ids: Tensor, attention_mask: Optional[Tensor] = None):
        x = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:, 0]
        x = self.cls(x)
        return x


def load_tokenizer(use_notes: bool = True):

    if use_notes:
        tokenizer = ByteLevelBPETokenizer.from_file(
            "./mimic/smartehr-notes-vocab.json",
            "./mimic/smartehr-notes-merges.txt",
        )
        tokenizer.add_special_tokens(special_tokens=["<pad>", "<unk>", "<mask>"])
        tokenizer.enable_truncation(max_length=4096)
    else:
        tokenizer = ByteLevelBPETokenizer.from_file(
            "./mimic/smartehr-vocab.json",
            "./mimic/smartehr-merges.txt",
        )
        tokenizer.add_special_tokens(special_tokens=["<pad>", "<unk>", "<mask>", "<sep>"])
    tokenizer._tokenizer.model.continuing_subword_prefix = None
    tokenizer._tokenizer.model.end_of_word_suffix = None
    tokenizer.enable_padding(pad_id=tokenizer.token_to_id("<pad>"), pad_token="<pad>")

    return tokenizer


def train_tokenizer(train: pd.DataFrame, use_notes: bool = True):
    os.makedirs("mimic/", exist_ok=True)
    tokenizer = ByteLevelBPETokenizer()
    if use_notes:
        dl = DataLoader(train, batch_size=1, shuffle=False, collate_fn=lambda x: x[0][0]["text"])
        tokenizer.train_from_iterator(dl, vocab_size=52_000, min_frequency=2, special_tokens=["<pad>", "<unk>", "<mask>"])
        tokenizer.save_model(".", "mimic/smartehr-notes")
    else:
        dl = DataLoader(train, batch_size=1, shuffle=False, collate_fn=lambda x: "<sep>".join(x[0][0]))
        tokenizer.train_from_iterator(
            dl, vocab_size=52_000, min_frequency=2, special_tokens=["<pad>", "<unk>", "<mask>", "<sep>"]
        )
        tokenizer.save_model(".", "mimic/smartehr")


def collate_fn_longformer(batch, tokenizer):
    features, durations, events = [b[0]["text"] for b in batch], [b[1][0] for b in batch], [b[1][1] for b in batch]
    encodings = tokenizer.batch_encode_plus(features, padding=True, max_length=4096, truncation=True, return_tensors="pt")
    return (
        {"input_ids": encodings["input_ids"], "attention_mask": encodings["attention_mask"]},
        torch.tensor(durations),
        torch.tensor(events),
    )
