import torch
import math
from torch import Tensor
from typing import Optional
from transformers import AutoModel, MistralConfig, MistralModel, PreTrainedTokenizer
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


class MistralForRegression(nn.Module):
    def __init__(self, time_intervals: int, tokenizer: PreTrainedTokenizer):
        super().__init__()
        self.time_intervals = time_intervals
        self.tokenizer = tokenizer
        vocab_size = len(tokenizer.get_vocab())
        config = MistralConfig(
            **{
                "architectures": ["MistralForCausalLM"],
                "attention_dropout": 0.0,
                "bos_token_id": 1,
                "eos_token_id": 2,
                "head_dim": 128,
                "hidden_act": "silu",
                "hidden_size": 1024,
                "initializer_range": 0.02,
                "intermediate_size": 14336,
                "max_position_embeddings": vocab_size,
                "model_type": "mistral",
                "num_attention_heads": 8,
                "num_hidden_layers": 8,
                "num_key_value_heads": 4,
                "rms_norm_eps": 1e-05,
                "rope_theta": 1000000.0,
                "sliding_window": 4096,
                "tie_word_embeddings": False,
                "torch_dtype": "bfloat16",
                "transformers_version": "4.45.1",
                "use_cache": True,
                "vocab_size": vocab_size,
            }
        )

        self.model = MistralModel(config=config)
        self.cls = nn.Linear(self.model.config.hidden_size, time_intervals)

    def forward(self, input_ids: Tensor, attention_mask: Optional[Tensor] = None):
        x = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[
            :, -1
        ]  # TODO: -1 is incorrect, slice according to attentoin_mask
        x = self.cls(x)
        return x


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


from transformers import MistralModel, MistralConfig, AutoTokenizer, PreTrainedTokenizer
import torch.nn as nn
import torch


class TemporalRecurrentMistral(nn.Module):
    def __init__(self, num_outputs: int, tokenizer: PreTrainedTokenizer):
        super().__init__()
        self.num_outputs = num_outputs
        self.time_intervals = num_outputs
        self.tokenizer = tokenizer
        vocab_size = len(tokenizer.get_vocab())
        config = MistralConfig(
            **{
                "architectures": ["MistralForCausalLM"],
                "attention_dropout": 0.0,
                "bos_token_id": 1,
                "eos_token_id": 2,
                "head_dim": 16,
                "hidden_act": "silu",
                "hidden_size": 256,
                "initializer_range": 0.02,
                "intermediate_size": 1791,
                "max_position_embeddings": vocab_size,
                "model_type": "mistral",
                "num_attention_heads": 4,
                "num_hidden_layers": 4,
                "num_key_value_heads": 4,
                "rms_norm_eps": 1e-05,
                "rope_theta": 1000000.0,
                "sliding_window": 512,
                "tie_word_embeddings": False,
                "torch_dtype": "bfloat16",
                "transformers_version": "4.45.1",
                "use_cache": True,
                "vocab_size": vocab_size,
            }
        )
        lstm_input_size = config.hidden_size
        bidirectional = False
        self.model = MistralModel(config=config)
        self.rnn = nn.LSTM(lstm_input_size, config.hidden_size, bidirectional=bidirectional, batch_first=True)
        self.cls = nn.Linear(self.model.config.hidden_size, num_outputs)

    def forward(self, input_ids, attention_mask):
        last_sequence_embeddings = []
        for ids, mask in zip(input_ids, attention_mask):
            outputs = self.model(input_ids=ids, attention_mask=mask)
            hidden_states = outputs.last_hidden_state
            last_indices = (mask.sum(dim=1) - 1).long()
            hidden_states = hidden_states[torch.arange(hidden_states.size(0), device=hidden_states.device), last_indices]
            last_sequence_embeddings.append(hidden_states)
        last_sequence_embeddings = torch.stack(last_sequence_embeddings, dim=1)

        lstm_outputs, _ = self.rnn(last_sequence_embeddings)
        cls_outputs = self.cls(lstm_outputs)
        return cls_outputs.view(-1, self.num_outputs)
