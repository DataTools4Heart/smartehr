"""Re-aggregate EXISTING per-time-point embedding sequences into flat per-patient
vectors — no re-encoding, no GPU. Use this to run the baseline-vs-events diagnostic
on embeddings you already extracted (the `embeddings` [L, E] + duration + event
parquet produced by extract_qwen_embeddings_longitudinal.py in sequence mode).

The event embeddings (rows 1:) are ordered oldest -> most recent (row -1 = latest
pre-baseline event); row 0 is the baseline. Aggregators:

Baseline / additive:
  - flat      : baseline embedding (time point 0)                     [dim E]
  - pool      : concat(baseline, mean(events))                        [dim 2E]
  - pool_last : concat(baseline, most-recent event)                   [dim 2E]
  - pool_max  : concat(baseline, elementwise max over events)         [dim 2E]
  - mean      : mean over ALL time points (baseline + events)         [dim E]
Events-only (does the event representation carry ANY signal vs baseline/random?):
  - events    : mean over event embeddings                            [dim E]
  - last      : most-recent event embedding                           [dim E]
  - max       : elementwise max over event embeddings                 [dim E]
(event aggregate is zeros when a patient has no events)

Diagnostic reading (train the same MLP on each, compare CI/AUC):
  - pool/pool_last/pool_max don't beat flat  -> events add nothing beyond baseline.
  - BUT if events/last/max alone are ~random -> the frozen event *representation* is
    the weak link (fix: better event encoding / LoRA), not necessarily redundancy.
  - if events-only is well above random but pool* ties flat -> real but redundant.
    python scripts/train_lightning_model.py \
        dataset=smartehr_embeddings dataset.root_path=<OUT> \
        model=mlp model.input_size=<E or 2E> ... training.weight_decay=1e-2
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from datasets import load_dataset


def _event_agg(emb: np.ndarray, how: str) -> np.ndarray:
    """Aggregate the event rows emb[1:] (oldest..most-recent); zeros if no events."""
    ev = emb[1:]
    if ev.shape[0] == 0:
        return np.zeros(emb.shape[1], dtype=np.float32)
    if how == "mean":
        return ev.mean(axis=0)
    if how == "last":
        return ev[-1]
    if how == "max":
        return ev.max(axis=0)
    raise ValueError(f"unknown event aggregator: {how}")


def _make_vec(emb: np.ndarray, mode: str) -> np.ndarray:
    base = emb[0]
    if mode == "flat":
        return base
    if mode == "mean":
        return emb.mean(axis=0)
    if mode in ("events", "last", "max"):
        return _event_agg(emb, {"events": "mean", "last": "last", "max": "max"}[mode])
    if mode in ("pool", "pool_last", "pool_max"):
        how = {"pool": "mean", "pool_last": "last", "pool_max": "max"}[mode]
        return np.concatenate([base, _event_agg(emb, how)])
    raise ValueError(f"unknown mode: {mode}")


def pool_split(in_path: Path, out_path: Path, mode: str) -> tuple[int, int]:
    ds = load_dataset("parquet", data_files=str(in_path), split="train")
    inputs, durations, events = [], [], []
    for rec in ds:
        emb = np.asarray(rec["embeddings"], dtype=np.float32)  # [L, E]
        inputs.append(_make_vec(emb, mode).tolist())
        durations.append(float(rec["duration"]))
        events.append(float(rec["event"]))
    pq.write_table(
        pa.table({"inputs": inputs, "duration": durations, "event": events}), out_path
    )
    return len(inputs), len(inputs[0])


def main(seq_dir: str, out_dir: str, mode: str):
    seq_dir = Path(seq_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    input_dim = None
    for split in ["train", "validation", "test"]:
        in_path = seq_dir / f"{split}.parquet"
        out_path = out_dir / f"{split}.parquet"
        n, dim = pool_split(in_path, out_path, mode)
        input_dim = dim
        print(f"  {split:12s}: {n:,} patients -> {out_path}  (inputs dim {dim})")

    meta_path = seq_dir / "metadata.json"
    metadata = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    metadata.update({"pooled_from": str(seq_dir), "pool_mode": mode, "input_dim": input_dim})
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\nSaved to {out_dir}")
    print(f"Train with:  dataset=smartehr_embeddings dataset.root_path={out_dir} "
          f"model=mlp model.input_size={input_dim}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Re-aggregate existing per-time-point embedding sequences into flat "
        "per-patient vectors (flat / pool / mean) for the baseline-vs-events MLP diagnostic. "
        "No re-encoding — reuses the sequence-mode embeddings you already have."
    )
    parser.add_argument("--seq-dir", type=str, required=True,
                        help="Directory with train/validation/test.parquet that have an `embeddings` "
                             "[L, E] column (sequence-mode output of extract_qwen_embeddings_longitudinal.py).")
    parser.add_argument("--out-dir", type=str, required=True)
    parser.add_argument(
        "--mode",
        choices=["flat", "pool", "pool_last", "pool_max", "mean", "events", "last", "max"],
        default="pool",
    )
    args = parser.parse_args()
    main(seq_dir=args.seq_dir, out_dir=args.out_dir, mode=args.mode)
