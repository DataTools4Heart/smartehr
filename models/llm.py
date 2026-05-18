import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig, BitsAndBytesConfig, AutoModelForCausalLM


class LLM(nn.Module):
    def __init__(
        self,
        llm_name: str,
        num_outputs: int,
        llm_config_overrides: dict = {},
        freeze_backbone: bool = False,
        gradient_checkpointing: bool = False,
        chunk_size: int | None = None,
        quantization_config: BitsAndBytesConfig = None,
    ):
        super().__init__()
        self.num_outputs = num_outputs
        self.freeze_backbone = freeze_backbone
        self.chunk_size = chunk_size

        if quantization_config is None:
            if llm_config_overrides:
                # Architecture is modified → cannot load pretrained weights, initialise randomly.
                model_config = AutoConfig.from_pretrained(llm_name)
                for k, v in llm_config_overrides.items():
                    setattr(model_config, k, v)
                self.model = AutoModel.from_config(model_config)
            else:
                # No overrides → load the original pretrained weights.
                self.model = AutoModel.from_pretrained(llm_name)
                model_config = self.model.config
        else:
            self.model = AutoModelForCausalLM.from_pretrained(llm_name, quantization_config=quantization_config)
            self.model = self.model.model
            model_config = self.model.config

        if freeze_backbone:
            # Freeze all backbone parameters; only the classification head will be trained.
            for param in self.model.parameters():
                param.requires_grad = False
        elif gradient_checkpointing:
            # Recompute activations during backward to trade compute for memory.
            self.model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})

        self.cls = nn.Linear(model_config.hidden_size, num_outputs)

    def _backbone_forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Run backbone; detach output when frozen so gradients stay in cls only."""
        if self.freeze_backbone:
            with torch.no_grad():
                hidden = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
            return hidden.detach()
        return self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state

    def _last_token_embedding(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Extract the last non-padded token's hidden state for each sample. Shape: [B, H]."""
        hidden = self._backbone_forward(input_ids, attention_mask)  # [B, T, H]
        last_idx = (attention_mask.sum(dim=1) - 1).clamp(min=0).long()  # [B]
        return hidden[torch.arange(hidden.size(0), device=hidden.device), last_idx]  # [B, H]

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        B, L = input_ids.shape

        if self.chunk_size is not None and L > self.chunk_size:
            # Process the sequence in non-overlapping chunks and mean-pool the per-chunk
            # last-token embeddings.  Samples whose sequence doesn't reach a given chunk
            # are excluded from that chunk's contribution via the validity mask.
            chunk_embs: list[torch.Tensor] = []
            chunk_weights: list[torch.Tensor] = []

            for start in range(0, L, self.chunk_size):
                end = min(start + self.chunk_size, L)
                chunk_ids = input_ids[:, start:end]
                chunk_mask = attention_mask[:, start:end]
                has_tokens = (chunk_mask.sum(dim=1) > 0).float()  # [B]
                if has_tokens.sum() == 0:
                    continue
                emb = self._last_token_embedding(chunk_ids, chunk_mask)  # [B, H]
                emb = emb * has_tokens.unsqueeze(-1)  # zero out samples with no tokens here
                chunk_embs.append(emb)
                chunk_weights.append(has_tokens)

            embs = torch.stack(chunk_embs, dim=1)        # [B, C, H]
            weights = torch.stack(chunk_weights, dim=1)  # [B, C]
            weights = weights / weights.sum(dim=1, keepdim=True).clamp(min=1)
            hidden_states = (embs * weights.unsqueeze(-1)).sum(dim=1)  # [B, H]
        else:
            hidden_states = self._last_token_embedding(input_ids, attention_mask)  # [B, H]

        return self.cls(hidden_states)
