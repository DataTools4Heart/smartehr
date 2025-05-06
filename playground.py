from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel, AutoConfig
from datasets import load_dataset
from models import llm
from torch.utils.data import DataLoader
import torch
from lightning_training.collator import collate_fn_llm
from functools import partial
import gc
#open dataset at data/mimic_los/longitudinal_mimic_los_llm and perform one forward pass of the model
from dataset_utils.utils import load_for_lightning
dataset = load_dataset("data/mimic_los/longitudinal_mimic_los_llm_separate_features")



def collate_fn_llm(batch, pad_value: int = 0, max_length: int = 512):
    inputs = [b["input_ids"] for b in batch]
    inputs = [torch.tensor(ids) for ids in inputs]
    attention_mask = [torch.ones_like(ids) for ids in inputs]
    time_deltas = [b["time_deltas_list"] for b in batch]
    inputs = torch.nn.utils.rnn.pad_sequence(inputs, batch_first=True, padding_value=pad_value)
    attention_mask = torch.nn.utils.rnn.pad_sequence(attention_mask, batch_first=True, padding_value=0)
    outcomes = torch.tensor([b["labels"] for b in batch])
    return {"inputs": {"llm_batches": inputs, "llm_masks": attention_mask, "time_deltas": time_deltas}, "multiclass_cls_labels": outcomes}

#load tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B", max_length=1000)
tokenizer.pad_token = tokenizer.eos_token
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize model with memory optimization settings
config_overrides = {
    #"gradient_checkpointing": True,  # Enable gradient checkpointing
    #"use_cache": False               # Disable KV cache to save memory
}

# Create the model in half precision
model = llm.LLM(
    llm_name="meta-llama/Llama-3.2-1B", 
    llm_config_overrides=config_overrides, 
    num_outputs=4
)

# Convert model to half precision (float16)
model = model.half().to(device)

# Clear memory
torch.cuda.empty_cache()
gc.collect()

# Use a smaller batch size and set max_length
max_seq_length = 512  # Limit sequence length
model_collate_fn = partial(collate_fn_llm, pad_value=tokenizer.pad_token_id, max_length=max_seq_length)

# Use smaller batch size
test_dataloader = DataLoader(dataset["test"], batch_size=1, collate_fn=model_collate_fn)
#test_dataloader_shuffled = DataLoader(dataset["test"], batch_size=1, shuffle=True, collate_fn=model_collate_fn)

# Set model to evaluation mode to save memory
model.eval()

with torch.no_grad():  # Disable gradient calculation to save memory
    # Let's manually handle only a few samples to avoid memory issues
    for i, batch in enumerate(test_dataloader):
        # Skip empty batches
        if batch["inputs"]["llm_batches"].size(0) == 0:
            print("Skipping empty batch")
            continue
            

        #check input shape
        print(f"Input shape: {batch['inputs']['llm_batches'].shape}")
        #check number of time_deltas
        print(f"Number of time_deltas: {len(batch['inputs']['time_deltas'][0])}")
        # Process batch
        outputs = model(
            batch["inputs"]["llm_batches"].to(device, dtype=torch.long), 
            batch["inputs"]["llm_masks"].to(device, dtype=torch.long)
        )
        
        # Print some information and results
        print(f"Processed batch {i+1}, input shape: {batch['inputs']['llm_batches'].shape}")
        print(f"Output logits shape: {outputs.shape}")
        print(f"Prediction: {torch.argmax(outputs, dim=1)}")
        
        # Clear cache after processing each batch
        torch.cuda.empty_cache()
        
        # Process only a few samples to avoid OOM
        #if i >= 2:  # Process 3 samples then stop
        #    break
        
print("Done processing samples!")