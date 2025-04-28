import init
import hydra
from omegaconf import DictConfig
from config.config import Config
from dataset_utils.utils import load_for_lightning 
from models.models import MistralForRegression
from lightning_training.utils import collate_fn_longformer
from transformers import AutoTokenizer
import lightning.pytorch as L
from torch.utils.data import DataLoader
import torch
from pathlib import Path
import pandas as pd
from datetime import datetime
import os
from lightning.pytorch.loggers import WandbLogger, CSVLogger
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
from config.testing.testing import LightningTestingParams
from functools import partial
from lightning_training.modules import SurvivalAnalysisModuleLLM

@hydra.main(version_base=None, config_path="../config", config_name="config")
def test_model(cfg: DictConfig) -> None:
    model_params = cfg.model
    test_params = cfg.testing
    dataset_params = cfg.dataset
    testing_params = LightningTestingParams(**test_params)
    
    # Create results directory if it doesn't exist
    results_dir = Path("test_results")
    results_dir.mkdir(exist_ok=True)
    
    # Setup CSV logger with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logger = CSVLogger(save_dir=str(results_dir), name=f"test_results_{timestamp}")
    
    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_params.model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    # Load checkpoint
    checkpoint_path = Path(testing_params.checkpoint_path)
    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint not found at {checkpoint_path}")
    print(f"Loading checkpoint from {checkpoint_path}")
    
    # Debug: examine checkpoint contents
    checkpoint = torch.load(checkpoint_path, map_location='cpu')
    #print("\nCheckpoint keys:", checkpoint.keys())
    state_dict = checkpoint['state_dict']
    
    # Create base model
    base_model = MistralForRegression(
        model_name=model_params.model_name,
        time_intervals=testing_params.time_intervals + 1,
        tokenizer=tokenizer
    )
    
    # Create survival model
    model = SurvivalAnalysisModuleLLM(base_model, lr=testing_params.lr)
    model = model.cuda().half()  # Ensure model is in float16
    
    # Debug: examine keys before loading
    #print("\nModel state dict keys:", model.state_dict().keys())
    
    # Add breakpoint to examine output
    #breakpoint()
    
    # Debug: try to load state dict directly
    print("\nTrying to load state dict...")
    
    def adjust_state_dict(state_dict):
        new_state_dict = {}
        old_prefix = "model.base_model.model.model."
        new_prefix = "model.base_model.model."
        for key, value in state_dict.items():
            if key.startswith(old_prefix):
                new_key = key.replace(old_prefix, new_prefix)
            else:
                new_key = key
            new_state_dict[new_key] = value
        return new_state_dict

    fixed_state_dict = adjust_state_dict(state_dict)

    # Optionally, if there are extra quantization/LoRA keys that you need to ignore,
    # you can filter them out:
    filtered_state_dict = {
        key: value
        for key, value in fixed_state_dict.items()
        if not any(sub in key for sub in [".absmax", ".quant_map", ".quant_state"])
    }

    # Finally, load your model state.
    model.load_state_dict(filtered_state_dict, strict=False)
    print("State dict loaded successfully")
    
    # Setup data
    collate_fn = partial(collate_fn_longformer, tokenizer=tokenizer)
    train, val, test = load_for_lightning(dataset_params, testing_params.time_intervals)
    test_dl = DataLoader(test, batch_size=testing_params.test_batch_size, shuffle=False, 
                        collate_fn=collate_fn, num_workers=testing_params.num_workers)

    if torch.cuda.is_available():
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        torch.set_float32_matmul_precision("medium")
    
    devices = testing_params.devices
    strategy = "ddp_find_unused_parameters_true" if len(devices) > 1 else "auto"
    
    trainer = L.Trainer(
        devices=devices,
        strategy=strategy,
        precision="32-true" if not (isinstance(devices, list) or devices == "cuda") else "16-mixed",
        logger=logger
    )
    
    # Run test and get metrics
    results = trainer.test(model, dataloaders=test_dl)
    
    # Ensure results is a list and has content
    if results and isinstance(results, list):
        results = results[0]  # Lightning returns a list of dicts, take the first one
    else:
        results = {}
    
    # Extract test metrics
    metrics = {
        'test_loss': results.get('test_loss', None),
        'test_c_index': results.get('test_c_index', None),
        'test_brier_1': results.get('test_brier_1', None),
        'test_brier_2': results.get('test_brier_2', None),
        'test_brier_3': results.get('test_brier_3', None),
        'test_brier_4': results.get('test_brier_4', None),
        'test_brier_5': results.get('test_brier_5', None),
        'test_brier_score': results.get('test_brier_score', None),
        'test_integrated_brier_score': results.get('test_integrated_brier_score', None),
        'test_auc_1': results.get('test_auc_1', None),
        'test_auc_2': results.get('test_auc_2', None),
        'test_auc_3': results.get('test_auc_3', None),
        'test_auc_4': results.get('test_auc_4', None),
        'test_auc_5': results.get('test_auc_5', None),
        'test_mean_auc': results.get('test_mean_auc', None),
        'test_integrated_auc': results.get('test_integrated_auc', None)
    }
    
    # Add metadata
    metadata = {
        'model_type': testing_params.model_type,
        'checkpoint_path': str(checkpoint_path),
        'test_batch_size': testing_params.test_batch_size,
        'time_intervals': testing_params.time_intervals,
        'timestamp': timestamp
    }
    
    # Combine metrics and metadata
    all_results = {**metadata, **metrics}
    
    # Save results summary
    results_df = pd.DataFrame([all_results])
    results_path = results_dir / f"summary_results_{timestamp}.csv"
    results_df.to_csv(results_path, index=False, float_format='%.4f')  # Format floats to 4 decimal places
    
    # Print results in a readable format
    print("\nTest Results Summary:")
    print("-" * 50)
    print("Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
    print("\nMetrics:")
    for key, value in metrics.items():
        if value is not None:
            print(f"{key}: {value:.4f}")
    print("-" * 50)
    print(f"\nDetailed results saved to: {results_path}")

if __name__ == "__main__":
    test_model()
