"""Dump per-patient test-set survival curves from a trained checkpoint, for the
bootstrap significance comparison (scripts/smartehr/bootstrap_ci_compare.py).

Runs the same setup as training but only evaluates: rebuilds the model from the Hydra
config, loads the checkpoint weights, runs the test loader, and computes the survival
curve exactly as SurvMetrics does (softmax over bins + zero pad, drop last, 1 - cumsum).
Saves parquet columns: duration (discretized bin), event, surv (list [num_bins]).

Usage (point resume_ckpt_path at the checkpoint of the run you want to score):
    python scripts/predict_survival.py \
        dataset=smartehr_embeddings dataset.root_path=<DIR> \
        model=mlp model.input_size=<N> training=lightning_survival_5yr \
        training.precision=32 training.resume_ckpt_path=<lightning_logs/.../checkpoints/xxx.ckpt>
Output: <ckpt_dir>/<ckpt_stem>_test_predictions.parquet
"""

import init  # noqa: F401  (adds repo root to sys.path)
from pathlib import Path

import torch
import hydra
import pyarrow as pa
import pyarrow.parquet as pq
from torch.utils.data import DataLoader
from transformers import set_seed

from config.config import Config
from config.training.training import LightningTrainingParams
from lightning_training.utils import load_lightning_model
from dataset_utils.utils import load_for_lightning
from lightning_training.collator import build_collate_fn
from lightning_training.transforms import apply_transforms


def _to_device(x, dev):
    if torch.is_tensor(x):
        return x.to(dev)
    if isinstance(x, dict):
        return {k: _to_device(v, dev) for k, v in x.items()}
    if isinstance(x, list):
        return [_to_device(v, dev) for v in x]
    return x


@hydra.main(version_base=None, config_path="../config", config_name="config")
def predict(cfg: Config):
    set_seed(42)
    train_params = LightningTrainingParams(**cfg.training)
    ckpt = train_params.resume_ckpt_path
    assert ckpt, "Set training.resume_ckpt_path=<checkpoint.ckpt>"

    module, tokenizer = load_lightning_model(cfg.model, train_params)
    state = torch.load(ckpt, map_location="cpu")
    state = state.get("state_dict", state)
    missing, unexpected = module.load_state_dict(state, strict=False)
    print(f"Loaded {ckpt}  (missing={len(missing)}, unexpected={len(unexpected)})")

    train, val, test = load_for_lightning(cfg.dataset, train_params.task)
    train, val, test = apply_transforms(train, val, test, cfg.model.name)
    collate_fn = build_collate_fn(cfg.dataset.name, cfg.model, tokenizer)
    test_dl = DataLoader(test, batch_size=train_params.batch_size, shuffle=False, collate_fn=collate_fn)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    module.to(device).eval()

    logits_all, dur_all, evt_all = [], [], []
    with torch.no_grad():
        for batch in test_dl:
            logits = module.model(**_to_device(batch["inputs"], device))
            logits_all.append(logits.float().cpu())
            dur_all.append(batch["survival_labels"]["duration"].cpu())
            evt_all.append(batch["survival_labels"]["event"].cpu())

    logits = torch.cat(logits_all)
    durations = torch.cat(dur_all).numpy()
    events = torch.cat(evt_all).numpy()

    # Survival curve, identical to SurvMetrics.compute
    padded = torch.cat([logits, torch.zeros((logits.shape[0], 1))], dim=1)
    pmf = torch.softmax(padded, dim=1)[:, :-1]
    surv = (1 - pmf.cumsum(dim=1)).numpy()

    out_path = Path(ckpt).with_name(Path(ckpt).stem + "_test_predictions.parquet")
    pq.write_table(
        pa.table({"duration": durations.tolist(), "event": events.tolist(), "surv": surv.tolist()}),
        out_path,
    )
    print(f"Wrote {len(durations):,} patients x {surv.shape[1]} bins -> {out_path}")


if __name__ == "__main__":
    predict()
