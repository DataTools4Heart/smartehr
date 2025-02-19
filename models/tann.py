import torch
import torch.nn as nn


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
