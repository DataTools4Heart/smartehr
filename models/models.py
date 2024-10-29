import torch
from torch import Tensor
from typing import Optional
from transformers import AutoModel
import torch.nn as nn


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
