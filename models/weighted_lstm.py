import torch
import torch.nn as nn
import torch.nn.functional as F


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
