import torch
import torch.nn as nn


class TemporalRecurrentEmbeddings(nn.Module):
    def __init__(self, embedding_dim: int, num_outputs: int, dropout: float = 0.1):
        super().__init__()
        self.num_outputs = num_outputs
        time_delta_embedding_dim = embedding_dim
        self.time_delta_encoder = nn.Linear(1, time_delta_embedding_dim)
        lstm_input_dim = embedding_dim + time_delta_embedding_dim
        lstm_hidden_dim = embedding_dim
        self.rnn = nn.LSTM(lstm_input_dim, lstm_hidden_dim, batch_first=True)
        self.dropout = nn.Dropout(dropout)
        self.cls = nn.Linear(lstm_hidden_dim, num_outputs)

    def forward(self, embeddings, time_deltas_list):
        sequence_lengths = [delta.size(0) for delta in time_deltas_list]

        # Pad sequences to max length for LSTM
        max_seq_len = max(sequence_lengths)
        time_deltas = [torch.nn.functional.pad(t, (0, max_seq_len - len(t)), value=0) for t in time_deltas_list]
        time_deltas = torch.stack(time_deltas).unsqueeze(-1)
        time_deltas = self.time_delta_encoder(time_deltas)

        lstm_inputs = torch.cat([embeddings, time_deltas], dim=-1)
        # Process through LSTM and classifier
        lstm_outputs, _ = self.rnn(lstm_inputs)
        lstm_outputs = lstm_outputs[
            torch.arange(lstm_outputs.size(0), device=lstm_outputs.device), [i - 1 for i in sequence_lengths]
        ]
        lstm_outputs = self.dropout(lstm_outputs)
        cls_outputs = self.cls(lstm_outputs)
        return cls_outputs
