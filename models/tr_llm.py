import torch
import torch.nn as nn
from transformers import AutoModel, AutoConfig


class TemporalRecurrentLLM(nn.Module):
    def __init__(self, llm_name: str, llm_config_overrides: dict, num_outputs: int):
        super().__init__()
        self.num_outputs = num_outputs
        model_config = AutoConfig.from_pretrained(llm_name)
        for k, v in llm_config_overrides.items():
            setattr(model_config, k, v)
        self.model = AutoModel.from_config(model_config)
        self.rnn = nn.LSTM(model_config.hidden_size, model_config.hidden_size, batch_first=True)
        self.time_delta_encoder = nn.Linear(1, model_config.hidden_size)
        self.cls = nn.Linear(model_config.hidden_size, num_outputs)

    def forward(self, llm_batches, llm_masks, time_deltas_list):
        # Process in batches
        all_embeddings = []

        for llm_batch, llm_mask in zip(llm_batches, llm_masks):
            # Get embeddings from LLM
            outputs = self.model(input_ids=llm_batch, attention_mask=llm_mask)
            hidden_states = outputs.last_hidden_state

            # Get last non-padded embedding for each sequence
            last_indices = (llm_mask.sum(dim=1) - 1).long()
            batch_embeddings = hidden_states[torch.arange(hidden_states.size(0), device=hidden_states.device), last_indices]
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
