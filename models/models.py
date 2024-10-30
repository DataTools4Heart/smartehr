import torch
import math
from torch import Tensor
from typing import Optional
from transformers import AutoModel
import pandas as pd
import numpy as np
import torch.nn as nn


smart_weights = {
    "age": -0.0850,
    "age2": 0.00105,
    "gender": 0.156,
    "smoker": 0.262,
    "systolic_blood_pressure": 0.00429,
    "diabetes": 0.223,
    "cad": 0.14,
    "cvd": 0.406,
    "aaa": 0.558,
    "pad": 0.283,
    "time_since_first_cd": 0.0229,
    "hdl_cholesterol": -0.426,
    "total_cholesterol": 0.0959,
    "egfr": -0.0532,
    "egfr2": 0.000306,
    "log_high_sens_crp": 0.139,
}


def original_smart_risk_score(weights: dict, data: pd.DataFrame):
    b, c = 0.81066, 2.099
    cov = []
    for k in weights.keys():
        x = data[k]
        cov.append(weights[k] * x)
    A = np.sum(np.array(cov), axis=0)
    return [(1 - b ** (np.exp(a + c))) for a in A]


def smart_survival_times(weights, data: pd.DataFrame):
    b, c = 0.81066, 2.099
    cov = []
    for k in weights.keys():
        x = data[k]
        cov.append(weights[k] * x)
    A = np.sum(np.array(cov), axis=0)
    return pd.Series([b ** np.exp(a + c) for a in A], index=data.index)


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


class PositionalEncoding(nn.Module):

    def __init__(self, d_model: int, dropout: float = 0.1, max_len: int = 5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(max_len, 1, d_model)
        pe[:, 0, 0::2] = torch.sin(position * div_term)
        pe[:, 0, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe)

    def forward(self, x: Tensor) -> Tensor:
        """
        Arguments:
            x: Tensor, shape ``[seq_len, batch_size, embedding_dim]``
        """
        x = x + self.pe[: x.size(0)]
        return self.dropout(x)


class TransformerEncoderForClassification(nn.Module):
    def __init__(self, num_embeddings, d_model, nhead, dim_feedforward, dropout, activation, num_layers, time_intervals):
        super().__init__()
        self.time_intervals = time_intervals
        self.embeddings = nn.Embedding(num_embeddings=num_embeddings, embedding_dim=d_model)
        self.pos_encoder = PositionalEncoding(d_model=d_model, dropout=dropout)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            activation=activation,
            batch_first=True,
            norm_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer=encoder_layer, num_layers=num_layers, enable_nested_tensor=False)
        self.linear = nn.Linear(d_model, time_intervals, bias=False)

    def forward(self, input_ids, padding_mask=None):
        x = self.embeddings(input_ids)
        x = self.pos_encoder(x)
        x = self.transformer.forward(x, src_key_padding_mask=padding_mask)
        x = x[:, 0, :]
        x = self.linear(x)
        return x
