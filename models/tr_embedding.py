import torch
import torch.nn as nn
import torch.nn.functional as F


class TemporalRecurrentEmbeddings(nn.Module):
    """Time-aware LSTM over a sequence of per-time-point embeddings, with a PMF head.

    Capacity is decoupled from the (frozen) input embedding size so the model can be
    shrunk to fit small cohorts:
      - ``hidden_dim``     : LSTM hidden size AND the input projection width. Defaults to
                             ``embedding_dim`` (legacy behavior) — set it small (e.g. 128)
                             to project 1024/2560-dim embeddings down and cut parameters.
      - ``time_delta_dim`` : width of the scalar time-delta encoder. Defaults to
                             ``embedding_dim``; a small value (e.g. 16) is plenty.
      - ``input_dropout``  : dropout on the projected input embeddings.
      - ``dropout``        : dropout on the final LSTM state before the head.
    """

    def __init__(
        self,
        embedding_dim: int,
        num_outputs: int,
        dropout: float = 0.1,
        hidden_dim: int | None = None,
        time_delta_dim: int | None = None,
        input_dropout: float = 0.0,
    ):
        super().__init__()
        self.num_outputs = num_outputs
        hidden_dim = hidden_dim or embedding_dim
        time_delta_dim = time_delta_dim or embedding_dim

        self.input_proj = nn.Linear(embedding_dim, hidden_dim)
        self.input_dropout = nn.Dropout(input_dropout)
        self.time_delta_encoder = nn.Linear(1, time_delta_dim)
        self.rnn = nn.LSTM(hidden_dim + time_delta_dim, hidden_dim, batch_first=True)
        self.dropout = nn.Dropout(dropout)
        self.cls = nn.Linear(hidden_dim, num_outputs)

    def forward(self, embeddings, time_deltas_list):
        sequence_lengths = [delta.size(0) for delta in time_deltas_list]

        # Pad time deltas to max length for LSTM
        max_seq_len = max(sequence_lengths)
        time_deltas = [F.pad(t, (0, max_seq_len - len(t)), value=0) for t in time_deltas_list]
        time_deltas = torch.stack(time_deltas).unsqueeze(-1)
        time_deltas = self.time_delta_encoder(time_deltas)

        # Project (and regularize) the frozen input embeddings before the LSTM
        embeddings = self.input_dropout(self.input_proj(embeddings))

        lstm_inputs = torch.cat([embeddings, time_deltas], dim=-1)
        lstm_outputs, _ = self.rnn(lstm_inputs)
        lstm_outputs = lstm_outputs[
            torch.arange(lstm_outputs.size(0), device=lstm_outputs.device), [i - 1 for i in sequence_lengths]
        ]
        lstm_outputs = self.dropout(lstm_outputs)
        cls_outputs = self.cls(lstm_outputs)
        return cls_outputs
