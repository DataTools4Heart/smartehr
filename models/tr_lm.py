import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig


class TemporalRecurrentLM(nn.Module):
    def __init__(
        self, lm_name: str, lm_config_overrides: dict, num_outputs: int, is_encoder: bool, quantization_config: dict = None
    ):
        super().__init__()
        self.num_outputs = num_outputs
        if quantization_config:
            self.model = AutoModel.from_pretrained(lm_name, quantization_config=quantization_config)
            model_config = self.model.config
        else:
            model_config = AutoConfig.from_pretrained(lm_name)
            for k, v in lm_config_overrides.items():
                if k in model_config.__dict__:
                    setattr(model_config, k, v)
            self.model = AutoModel.from_config(model_config)
        self.rnn = nn.LSTM(model_config.hidden_size, model_config.hidden_size, batch_first=True)
        self.time_delta_encoder = nn.Linear(1, model_config.hidden_size)
        self.cls = nn.Linear(model_config.hidden_size, num_outputs)
        self.is_encoder = is_encoder

    def forward(self, lm_batches, lm_masks, time_deltas_list):
        # Process in batches
        all_embeddings = []

        for lm_batch, lm_mask in zip(lm_batches, lm_masks):
            # Get embeddings from LLM
            outputs = self.model(input_ids=lm_batch, attention_mask=lm_mask)
            hidden_states = outputs.last_hidden_state

            # Get last non-padded embedding for each sequence
            if not self.is_encoder:
                last_indices = (lm_mask.sum(dim=1) - 1).long()
                batch_embeddings = hidden_states[torch.arange(hidden_states.size(0), device=hidden_states.device), last_indices]
            else:
                batch_embeddings = hidden_states[:, 0]
            all_embeddings.append(batch_embeddings)

        # Concatenate all embeddings
        all_embeddings = torch.cat(all_embeddings, dim=0)
        # Reconstruct original sequence structure
        sequence_lengths = [delta.size(0) for delta in time_deltas_list]
        start_idx = 0
        sequence_embeddings = []
        for seq_len in sequence_lengths:
            sequence_embeddings.append(all_embeddings[start_idx : start_idx + seq_len])
            start_idx += seq_len

        # Pad sequences to max length for LSTM
        max_seq_len = max(len(seq) for seq in sequence_embeddings)
        sequence_embeddings = [
            torch.nn.functional.pad(seq, (0, 0, 0, max_seq_len - len(seq)), value=0) for seq in sequence_embeddings
        ]
        sequence_embeddings = torch.stack(sequence_embeddings)
        time_deltas = [torch.nn.functional.pad(t, (0, max_seq_len - len(t)), value=0) for t in time_deltas_list]

        time_deltas = torch.stack(time_deltas).unsqueeze(-1)
        time_deltas = self.time_delta_encoder(time_deltas)
        # Process through LSTM and classifier
        lstm_outputs, _ = self.rnn(sequence_embeddings + time_deltas)
        # print(lstm_outputs.shape, sequence_lengths)
        lstm_outputs = lstm_outputs[
            torch.arange(lstm_outputs.size(0), device=lstm_outputs.device), [i - 1 for i in sequence_lengths]
        ]
        cls_outputs = self.cls(lstm_outputs)
        return cls_outputs
