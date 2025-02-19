import torch
import torch.nn as nn


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
