import torch
from config.model.model import ModelParams, ClinicalLongformerModelParams, TransformerEncoderModelParams
from transformers import AutoTokenizer
from models.models import TransformerEncoderForClassification, MIMICNotesModel
from functools import partial
import torch.nn.functional as F
from pathlib import Path
import pickle as pkl
from tokenizers.implementations import ByteLevelBPETokenizer
from transformers import PreTrainedTokenizer
import random


def collate_fn_longformer(batch, tokenizer: PreTrainedTokenizer):
    features, durations, events = [b[0]["text"] for b in batch], [b[1][0] for b in batch], [b[1][1] for b in batch]
    encodings = tokenizer.batch_encode_plus(features, padding=True, max_length=4096, truncation=True, return_tensors="pt")
    return (
        {"input_ids": encodings["input_ids"], "attention_mask": encodings["attention_mask"]},
        torch.tensor(durations),
        torch.tensor(events),
    )


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


def load_lightning_model(model_params: ModelParams, time_intervals: int):
    if model_params.name == "clinical_longformer":
        model_params = ClinicalLongformerModelParams(**model_params)
        tokenizer = AutoTokenizer.from_pretrained("yikuan8/Clinical-Longformer")
        model = MIMICNotesModel(  # TODO: change the name of the model
            time_intervals=time_intervals + 1,
            freeze_last_n_layers=model_params.freeze_last_n_layers,
            freeze_embeddings=model_params.freeze_embeddings,
        )
        collate_fn = partial(collate_fn_longformer, tokenizer=tokenizer)
    elif model_params.name == "transformer_encoder":
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
            time_intervals=24,
        )
        collate_fn = partial(collate_fn_smart_poc, tokenizer=tokenizer)
    else:
        raise NotImplementedError(f"Unknown model: {model_params.name}")
    return model, collate_fn
