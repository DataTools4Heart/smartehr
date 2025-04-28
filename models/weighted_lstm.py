import torch
import torch.nn as nn
import torch.nn.functional as F


class WeightedLSTM(nn.Module):
    def __init__(self, vocabs: dict, alpha_r: float, lstm_hidden_size, time_embedding_dim, num_outputs, lstm_dropout):
        super().__init__()
        self.vocabs = vocabs
        self.token_embeddings = {}
        self.embedding_weights = {}
        total_embedding_dim = 0
        for feature_type in vocabs:
            vocab_size = len(vocabs[feature_type])
            embedding_dim = int(6 * alpha_r * (vocab_size**0.25))
            self.token_embeddings[feature_type] = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
            self.embedding_weights[feature_type] = nn.Embedding(num_embeddings=vocab_size, embedding_dim=1)
            total_embedding_dim += embedding_dim
        self.token_embeddings = nn.ModuleDict(self.token_embeddings)
        self.embedding_weights = nn.ModuleDict(self.embedding_weights)
        self.time_proj = nn.Linear(1, time_embedding_dim)
        self.lstm = nn.LSTM(
            input_size=total_embedding_dim + time_embedding_dim,
            hidden_size=lstm_hidden_size,
            batch_first=True,
            dropout=lstm_dropout,
        )
        self.cls = nn.Linear(lstm_hidden_size, num_outputs)

    def forward(self, input_ids_list, time_deltas_list):
        sequences = []
        for input_ids_dicts, time_deltas in zip(input_ids_list, time_deltas_list):
            sequence = []
            time_embeddings = self.time_proj(time_deltas.unsqueeze(1))
            for time_step, input_ids_dict in enumerate(input_ids_dicts):
                concat_embedding = []
                for feature_type in self.token_embeddings.keys():
                    feature_ids = input_ids_dict[feature_type]
                    if len(feature_ids) == 0:
                        concat_embedding.append(
                            torch.zeros(
                                self.token_embeddings[feature_type].embedding_dim,
                                device=time_embeddings[time_step].device,
                                requires_grad=False,
                            )
                        )
                    else:
                        feature_ids = torch.cat(feature_ids, dim=0)
                        embedding_weights = self.embedding_weights[feature_type](feature_ids)
                        embedding_weights = F.relu(embedding_weights)
                        feature_embedding = self.token_embeddings[feature_type](feature_ids)
                        feature_embedding = torch.sum(feature_embedding * embedding_weights, dim=0)
                    concat_embedding.append(feature_embedding)
                concat_embedding = torch.cat(concat_embedding, dim=0)
                concat_embedding = torch.cat([concat_embedding, time_embeddings[time_step]])
                sequence.append(concat_embedding)
            sequence = torch.stack(sequence, dim=0)
            sequences.append(sequence)

        sequences_end = torch.tensor([seq.shape[0] - 1 for seq in sequences])
        sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True)

        out = self.lstm(sequences)[0]
        out = out[torch.arange(out.size(0), device=out.device, requires_grad=False), sequences_end]
        out = self.cls(out)
        return out


def tensorize_features(batch):
    for batch_item in batch["features"]:
        for feature_dict in batch_item:
            for feature_type in feature_dict:
                feature_dict[feature_type] = [torch.tensor(t) for t in feature_dict[feature_type]]
    batch["time_deltas"] = [torch.tensor(t) for t in batch["time_deltas"]]
    batch["outcomes"] = [torch.tensor(t["los"]) for t in batch["outcomes"]]
    return batch
