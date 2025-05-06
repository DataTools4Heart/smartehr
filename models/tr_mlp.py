import torch
import torch.nn as nn


class TemporalRecurrentMLP(nn.Module):
    def __init__(self, input_size, output_size, num_nodes=list[int], dropout: float = 0.0):
        super().__init__()
        self.hidden_size = num_nodes[-1]
        self.layers = [nn.Linear(input_size, num_nodes[0])] + [
            x
            for i in range(len(num_nodes))
            for x in (nn.ReLU(), nn.Linear(num_nodes[i - 1], num_nodes[i]), nn.Dropout(p=dropout))
        ]
        self.mlp = nn.Sequential(*self.layers)
        self.lstm_hidden_size = self.hidden_size
        self.rnn = nn.LSTM(self.hidden_size, self.lstm_hidden_size, batch_first=True)
        self.time_delta_encoder = nn.Linear(1, self.lstm_hidden_size)
        self.cls = nn.Linear(self.lstm_hidden_size, output_size)

    def forward(self, input_sequence: torch.Tensor, time_deltas_list: list[torch.Tensor]):
        sequence_lengths = [delta.size(0) for delta in time_deltas_list]
        max_seq_len = max(sequence_lengths)
        time_deltas = [torch.nn.functional.pad(t, (0, max_seq_len - len(t)), value=0) for t in time_deltas_list]
        time_deltas = torch.stack(time_deltas).unsqueeze(-1)
        time_deltas = self.time_delta_encoder(time_deltas)

        hidden_states = self.mlp(input_sequence)
        lstm_outputs, _ = self.rnn(hidden_states + time_deltas)
        lstm_outputs = lstm_outputs[
            torch.arange(lstm_outputs.size(0), device=lstm_outputs.device), [i - 1 for i in sequence_lengths]
        ]
        return self.cls(lstm_outputs)
