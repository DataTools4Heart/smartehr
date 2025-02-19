from transformers import MistralModel, MistralConfig, PreTrainedTokenizer
import torch.nn as nn
import torch


class TemporalRecurrentMistral(nn.Module):
    def __init__(self, num_outputs: int, tokenizer: PreTrainedTokenizer):
        super().__init__()
        self.num_outputs = num_outputs
        self.time_intervals = num_outputs
        self.tokenizer = tokenizer
        vocab_size = len(tokenizer.get_vocab())
        config = MistralConfig(
            **{
                "architectures": ["MistralForCausalLM"],
                "attention_dropout": 0.0,
                "bos_token_id": 1,
                "eos_token_id": 2,
                "head_dim": 16,
                "hidden_act": "silu",
                "hidden_size": 256,
                "initializer_range": 0.02,
                "intermediate_size": 1791,
                "max_position_embeddings": vocab_size,
                "model_type": "mistral",
                "num_attention_heads": 4,
                "num_hidden_layers": 4,
                "num_key_value_heads": 4,
                "rms_norm_eps": 1e-05,
                "rope_theta": 1000000.0,
                "sliding_window": 512,
                "tie_word_embeddings": False,
                "torch_dtype": "bfloat16",
                "transformers_version": "4.45.1",
                "use_cache": True,
                "vocab_size": vocab_size,
            }
        )
        lstm_input_size = config.hidden_size
        bidirectional = False
        self.model = MistralModel(config=config)
        self.rnn = nn.LSTM(lstm_input_size, config.hidden_size, bidirectional=bidirectional, batch_first=True)
        self.cls = nn.Linear(self.model.config.hidden_size, num_outputs)

    def forward(self, input_ids, attention_mask):
        last_sequence_embeddings = []
        for ids, mask in zip(input_ids, attention_mask):
            outputs = self.model(input_ids=ids, attention_mask=mask)
            hidden_states = outputs.last_hidden_state
            last_indices = (mask.sum(dim=1) - 1).long()
            hidden_states = hidden_states[torch.arange(hidden_states.size(0), device=hidden_states.device), last_indices]
            last_sequence_embeddings.append(hidden_states)
        last_sequence_embeddings = torch.stack(last_sequence_embeddings, dim=1)

        lstm_outputs, _ = self.rnn(last_sequence_embeddings)
        cls_outputs = self.cls(lstm_outputs)
        return cls_outputs.view(-1, self.num_outputs)
