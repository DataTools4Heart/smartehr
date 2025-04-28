import torch
import torch.nn as nn
from torch import Tensor
from transformers import AutoModel
from typing import Optional


class ClinicalLongformer(nn.Module):
    def __init__(self, num_outputs: int, freeze_first_n_layers: int = 0, freeze_embeddings: bool = False):
        super().__init__()
        assert freeze_first_n_layers >= 0, "freeze_first_n_layers must be greater than or equal to 0"
        self.num_outputs = num_outputs
        self.model = AutoModel.from_pretrained("yikuan8/Clinical-Longformer", add_pooling_layer=False)
        if freeze_first_n_layers > 0:
            for layer in self.model.encoder.layer[:freeze_first_n_layers]:
                for param in layer.parameters():
                    param.requires_grad = False
        if freeze_embeddings:
            for param in self.model.embeddings.parameters():
                param.requires_grad = False

        self.cls = nn.Linear(self.model.config.hidden_size, num_outputs)

    def forward(self, input_ids: Tensor, attention_mask: Optional[Tensor] = None):
        x = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:, 0]
        x = self.cls(x)
        return x
