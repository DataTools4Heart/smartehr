import math

import torch
import torch.nn as nn
from torch import Tensor


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
