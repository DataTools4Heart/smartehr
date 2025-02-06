import torch
import math
from torch import Tensor
from typing import Optional
import torch.utils
from transformers import AutoModel, PreTrainedTokenizer
import pandas as pd
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

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
        x = self.model(input_ids=input_ids, attention_mask=attention_mask)
        x = x.last_hidden_state  # B, S, E
        last_indices = (attention_mask.sum(dim=1) - 1).long()
        x = x[torch.arange(x.size(0), device=x.device), last_indices]  # B, E
        x = self.cls(x)  # B, T
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


from transformers import MistralModel, MistralConfig, PreTrainedTokenizer
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


class WeightedLSTM(nn.Module):
    def __init__(self, vocab_size, word_embedding_dim, lstm_hidden_size, time_embedding_dim, num_outputs, lstm_dropout):
        super().__init__()
        self.word_embeddings = nn.Embedding(num_embeddings=vocab_size, embedding_dim=word_embedding_dim)
        self.embedding_weights = nn.Embedding(num_embeddings=vocab_size, embedding_dim=1)
        self.time_proj = nn.Linear(1, time_embedding_dim)
        self.lstm = nn.LSTM(
            input_size=word_embedding_dim + time_embedding_dim,
            hidden_size=lstm_hidden_size,
            batch_first=True,
            dropout=lstm_dropout,
        )
        self.cls = nn.Linear(lstm_hidden_size, num_outputs)

    def forward(self, input_ids_list, time_deltas_list):
        sequences = []
        for input_ids, time_deltas in zip(input_ids_list, time_deltas_list):
            sequence = []
            time_embeddings = self.time_proj(time_deltas.unsqueeze(1))
            for i, ids in enumerate(input_ids):
                embedding_weights = self.embedding_weights(ids)
                embedding_weights = F.relu(embedding_weights)
                word_embeddings = self.word_embeddings(ids)
                word_embedding = torch.sum(word_embeddings * embedding_weights, dim=0)

                embedding = torch.cat([word_embedding, time_embeddings[i]])
                sequence.append(embedding)
            sequence = torch.stack(sequence, dim=0)
            sequences.append(sequence)

        sequences_end = torch.tensor([seq.shape[0] - 1 for seq in sequences])
        sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True)

        out = self.lstm(sequences)[0]
        out = out[torch.arange(out.size(0), device=out.device), sequences_end]
        out = self.cls(out)
        return out


class MLP(nn.Module):
    def __init__(self, input_size, output_size, num_nodes=list[int], dropout: float = 0.0):
        super().__init__()
        self.layers = (
            [nn.Linear(input_size, num_nodes[0])]
            + [
                x
                for i in range(len(num_nodes))
                for x in (nn.ReLU(), nn.Linear(num_nodes[i - 1], num_nodes[i]), nn.Dropout(p=dropout))
            ]
            + [nn.Linear(num_nodes[-1], output_size)]
        )
        self.mlp = nn.Sequential(*self.layers)

    def forward(self, inputs: torch.Tensor):
        return self.mlp(inputs)


class PiecewiseFunction(nn.Module):
    def __init__(self):
        super().__init__()
        self.piecewise_y = nn.Parameter(torch.randn(365))

    def forward(self, delta: torch.Tensor):
        bucket = torch.max(torch.zeros(delta.shape, device=delta.device), torch.ceil(torch.log2(delta + 1e-10))).int()
        y1 = self.piecewise_y[bucket]
        y2 = self.piecewise_y[bucket + 1]
        x1 = 2**bucket
        x2 = 2 ** (bucket + 1)
        return y1 + (y2 - y1) * (delta - x1) / (x2 - x1)


class Lambda(nn.Module):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def forward(self, x):
        return self.fn(x)


class TANN(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embedding_dim: int,
        num_layers: int,
        hidden_dim: int,
        out_dim: int,
        k: int,
        one_day: float,
        uniform_bank: bool = True,
        probabilities: torch.Tensor | None = None,
    ):
        super().__init__()

        self.one_day = one_day
        self.k = k
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.proj = nn.Linear(embedding_dim, k)

        if uniform_bank:
            assert k % 4 == 0, "k must be divisible by 4"
            self.piecewise_y = nn.ParameterList(
                [nn.Parameter(torch.randn(365)) for _ in range(k // 4)]
            )  # TODO: change 365 to max days
            self.fn_bank = nn.ModuleList([x for _ in range(k // 4) for x in self.get_fn_bank()])
        else:
            assert probabilities is not None, "probabilities must be provided"
            assert len(probabilities) == 4, "probabilities must have length 4"
            indices = torch.multinomial(probabilities, num_samples=k, replacement=True)
            self.fn_bank = nn.ModuleList([self.get_fn_bank()[idx] for idx in indices])

        self.mlp = nn.Sequential(
            *(
                [nn.Linear(embedding_dim + 2, hidden_dim), nn.ReLU()]
                + [
                    x
                    for _ in range(num_layers - 1)
                    for x in [
                        nn.Linear(hidden_dim, hidden_dim),
                        nn.ReLU(),
                    ]
                ]
                + [nn.Linear(hidden_dim, out_dim)]
            )
        )

    def get_fn_bank(self):
        return [
            Lambda(lambda delta: torch.log(delta + self.one_day)),
            Lambda(lambda delta: torch.ones(delta.shape, device=delta.device)),
            Lambda(lambda delta: delta),
            PiecewiseFunction(),
        ]

    def compute_attribution_logits(self, embeddings: torch.Tensor, time_deltas: torch.Tensor):
        p = self.proj(embeddings)
        A = torch.stack([self.fn_bank[i](time_deltas) for i in range(self.k)], dim=-1)
        return torch.sum(p * A, dim=-1)

    def forward(self, input_ids_list: list[list[torch.Tensor]], time_deltas_list: list[torch.Tensor]):
        sequences = []
        time_deltas = []
        for input_ids, time_delta in zip(input_ids_list, time_deltas_list):
            sequence = []
            deltas = []
            for i, ids in enumerate(input_ids):
                embeddings = self.embedding(ids)
                delta = torch.broadcast_to(time_delta[i], (embeddings.shape[0],))
                sequence.append(embeddings)
                deltas.append(delta)
            sequence = torch.cat(sequence, dim=0)
            sequences.append(sequence)
            deltas = torch.cat(deltas, dim=0)
            time_deltas.append(deltas)
        sequences_end = torch.tensor([seq.shape[0] for seq in sequences], dtype=torch.int64, device=sequences[0].device)
        sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True, padding_value=0)
        time_deltas = torch.nn.utils.rnn.pad_sequence(time_deltas, batch_first=True, padding_value=0)
        a = self.compute_attribution_logits(sequences, time_deltas)

        E = []
        for b_i, e_i, end in zip(a, sequences, sequences_end):
            e_i, b_i = e_i[None, :end], b_i[None, :end]
            b_i = torch.softmax(b_i, dim=-1)
            E_i = torch.sum(b_i[..., None].broadcast_to(e_i.shape) * e_i, dim=1)
            s1 = torch.log(torch.ones(e_i.shape[0], device=e_i.device) + end)
            s2 = torch.log(torch.sum(b_i**2, dim=-1))
            E.append(torch.cat([E_i, s1[..., None], s2[..., None]], dim=-1))
        E = torch.cat(E, dim=0)
        return self.mlp(E)
