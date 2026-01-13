import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig, BitsAndBytesConfig, AutoModelForCausalLM


class LLM(nn.Module):
    def __init__(
        self, llm_name: str, num_outputs: int, llm_config_overrides: dict = {}, quantization_config: BitsAndBytesConfig = None
    ):
        super().__init__()
        self.num_outputs = num_outputs
        if quantization_config is None:
            model_config = AutoConfig.from_pretrained(llm_name)
            for k, v in llm_config_overrides.items():
                setattr(model_config, k, v)
            self.model = AutoModel.from_config(model_config)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(llm_name, quantization_config=quantization_config)
            self.model = self.model.model
            model_config = self.model.config
        self.cls = nn.Linear(model_config.hidden_size, num_outputs)

    def forward(self, input_ids, attention_mask):
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        hidden_states = outputs.last_hidden_state
        last_indices = (attention_mask.sum(dim=1) - 1).long()
        hidden_states = hidden_states[torch.arange(hidden_states.size(0), device=hidden_states.device), last_indices]
        cls_outputs = self.cls(hidden_states)
        return cls_outputs
