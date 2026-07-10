import argparse
import json
import sys
from pathlib import Path

sys.path.append(".")  # run from repo root so `dataset_utils` is importable, matching scripts/init.py

import numpy as np
from datasets import Dataset

from dataset_utils.utils import load_smart


def apply_censoring(first_event: float, cd_event: int, horizon: int) -> tuple[float, int]:
    """Apply administrative censoring at the given time horizon.

    Same semantics as scripts/smartehr/preprocess_smartehr_survival.py's apply_censoring,
    duplicated here (rather than imported) since these are standalone scripts.
    """
    if cd_event == 0:
        return (float(min(first_event, horizon)), 0)
    else:
        if first_event <= horizon:
            return (float(first_event), 1)
        else:
            return (float(horizon), 0)


def main(jsonl_dir: str, out_dir: str, horizon_days: int):
    jsonl_dir = Path(jsonl_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading + imputing SMART features from {jsonl_dir} ...")
    train, val, test = load_smart(jsonl_dir)
    splits = {"train": train, "validation": val, "test": test}

    feature_cols = [c for c in train.columns if c not in ("m3life_no", "cd_time", "cd_event")]
    print(f"Feature columns ({len(feature_cols)}): {feature_cols}")

    # Standardize features, fit on train only
    means = train[feature_cols].mean()
    stds = train[feature_cols].std().replace(0, 1.0)

    metadata = {
        "horizon_days": horizon_days,
        "feature_names": feature_cols,
        "n_features": len(feature_cols),
        "feature_means": means.to_dict(),
        "feature_stds": stds.to_dict(),
    }

    total_n, total_events = 0, 0
    for split_name, df in splits.items():
        df = df.copy()
        durations, events = [], []
        for cd_time, cd_event in zip(df["cd_time"], df["cd_event"]):
            duration, event = apply_censoring(cd_time, int(cd_event), horizon_days)
            durations.append(duration)
            events.append(event)

        standardized = (df[feature_cols] - means) / stds
        inputs = standardized.to_numpy(dtype=np.float32).tolist()

        ds = Dataset.from_dict({"inputs": inputs, "duration": durations, "event": events})
        ds.to_parquet(out_dir / f"{split_name}.parquet")

        n, e = len(ds), sum(events)
        total_n += n
        total_events += e
        print(f"  {split_name:12s}: {n:5,} rows  |  events={e} ({100*e/n:.1f}%)  censored={n-e}")

    metadata["n_patients"] = total_n
    metadata["n_events"] = total_events
    metadata["event_rate"] = round(total_events / total_n, 4)
    metadata["splits"] = {name: len(df) for name, df in splits.items()}
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\nSaved to {out_dir}")
    print(f"Set model.input_size={len(feature_cols)} when training the MLP head.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare raw (imputed, standardized) SMART baseline features for a small "
        "MLP survival head, as a controlled comparison against MLP-on-LLM-embeddings and Cox."
    )
    parser.add_argument("--jsonl-dir", type=str, required=True,
                        help="Directory containing train/validation/test.jsonl (output of smartehr_pipeline.py).")
    parser.add_argument("--out-dir", type=str, required=True)
    parser.add_argument("--horizon-days", type=int, default=1825,
                        help="Administrative censoring horizon in days. Use the same value as the "
                             "preprocess_smartehr_survival.py run you're comparing against.")
    args = parser.parse_args()

    main(jsonl_dir=args.jsonl_dir, out_dir=args.out_dir, horizon_days=args.horizon_days)
