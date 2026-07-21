"""Re-aggregate EXISTING per-time-point embedding sequences into flat per-patient
vectors — no re-encoding, no GPU. Use this to run the baseline-vs-events diagnostic
on embeddings you already extracted (the `embeddings` [L, E] + duration + event
parquet produced by extract_qwen_embeddings_longitudinal.py in sequence mode).

Modes:
  - flat : inputs = baseline embedding (time point 0)                 [dim E]
  - pool : inputs = concat(baseline, mean(event embeddings))          [dim 2E]
           (event-mean is zeros when a patient has no events)
  - mean : inputs = mean over ALL time points (baseline + events)     [dim E]

Then train the same MLP on the output and compare CI/AUC:
    python scripts/train_lightning_model.py \
        dataset=smartehr_embeddings dataset.root_path=<OUT> \
        model=mlp model.input_size=<E or 2E> ... training.weight_decay=1e-2
If `pool` does not beat `flat`, the events add nothing beyond baseline.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from datasets import load_dataset


def pool_split(in_path: Path, out_path: Path, mode: str) -> tuple[int, int]:
    ds = load_dataset("parquet", data_files=str(in_path), split="train")
    inputs, durations, events = [], [], []
    for rec in ds:
        emb = np.asarray(rec["embeddings"], dtype=np.float32)  # [L, E]
        base = emb[0]
        if mode == "flat":
            vec = base
        elif mode == "pool":
            ev_mean = emb[1:].mean(axis=0) if emb.shape[0] > 1 else np.zeros_like(base)
            vec = np.concatenate([base, ev_mean])
        elif mode == "mean":
            vec = emb.mean(axis=0)
        else:
            raise ValueError(f"unknown mode: {mode}")
        inputs.append(vec.tolist())
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
    parser.add_argument("--mode", choices=["flat", "pool", "mean"], default="pool")
    args = parser.parse_args()
    main(seq_dir=args.seq_dir, out_dir=args.out_dir, mode=args.mode)
