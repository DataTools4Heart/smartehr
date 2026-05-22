import init
import json
import argparse
import os
from pathlib import Path

import numpy as np
from datasets import Dataset, DatasetDict
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer


def serialize_patient(record: dict, exclusion_window: int = 0) -> str:
    """Serialize a patient record to a natural-language text string.

    Args:
        record: Patient record dict with 'smart' and 'events' keys.
        exclusion_window: Exclude events with datediff > -exclusion_window (i.e. too close to
            baseline). E.g. exclusion_window=180 drops events in the last 6 months before
            baseline. 0 means no additional exclusion (keep all events with datediff < 0).
    """
    smart = record["smart"]
    parts = ["[PATIENT]"]
    for k, v in smart.items():
        if k in ("first_event", "cd_event"):
            continue  # target variables, must not be in the input
        parts.append(f"{k}: {round(v, 4) if isinstance(v, float) else v}")

    cutoff = -exclusion_window
    for event in record.get("events", []):
        if exclusion_window > 0 and event["datediff"] > cutoff:
            continue
        event_parts = [f"[EVENT datediff={event['datediff']}]"]
        for k, v in event.items():
            if k == "datediff":
                continue
            event_parts.append(f"{k}: {round(v, 4) if isinstance(v, float) else v}")
        parts.append(" ".join(event_parts))

    return " | ".join(parts)


def apply_censoring(first_event: float, cd_event: int, horizon: int) -> tuple[float, int]:
    """Apply administrative censoring at the given time horizon.

    Args:
        first_event: Time to event or censoring (continuous, in days).
        cd_event: Original event indicator (1 = event occurred, 0 = censored).
        horizon: Administrative censoring horizon in days.

    Returns:
        (duration, event): The adjusted (T, Y) pair.
        - If the patient was already censored (cd_event=0) before the horizon:
          T = first_event, Y = 0
        - If the patient had an event within the horizon:
          T = first_event, Y = 1
        - If the patient had an event BEYOND the horizon (landmark rule):
          T = horizon, Y = 0 (event-free at the horizon)
    """
    if cd_event == 0:
        # Already censored — cap at horizon if censoring time exceeds it
        return (float(min(first_event, horizon)), 0)
    else:
        # Had an event
        if first_event <= horizon:
            return (float(first_event), 1)
        else:
            return (float(horizon), 0)


def preprocess_dummy_smart_survival(
    jsonl_path: str,
    out_dir: str,
    tokenizer_name: str = "meta-llama/Llama-3.2-1B",
    max_length: int = 512,
    horizon_days: int = 1825,
    exclusion_window: int = 0,
    val_size: float = 0.15,
    test_size: float = 0.15,
    seed: int = 42,
):
    print(f"Loading {jsonl_path} ...")
    records = []
    with open(jsonl_path) as f:
        for line in f:
            records.append(json.loads(line))

    print(f"Loaded {len(records):,} patients.")
    print(f"Applying administrative censoring at {horizon_days} days ({horizon_days / 365:.1f} years)")
    print(f"Tokenising with {tokenizer_name} ...")

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    truncate = max_length > 0
    input_ids_list = []
    durations_list = []
    events_list = []

    n_skipped = 0
    for rec in records:
        first_event = rec["smart"].get("first_event")
        if first_event is None:
            n_skipped += 1
            continue

        cd_event_raw = rec["smart"].get("cd_event")
        cd_event = int(cd_event_raw) if cd_event_raw is not None else 1  # default 1 for legacy data

        text = serialize_patient(rec, exclusion_window=exclusion_window)
        if truncate:
            enc = tokenizer(text, truncation=True, max_length=max_length, add_special_tokens=True)
        else:
            enc = tokenizer(text, add_special_tokens=True)
        input_ids_list.append(enc["input_ids"])

        duration, event = apply_censoring(first_event, cd_event, horizon_days)
        durations_list.append(duration)
        events_list.append(event)

    if n_skipped > 0:
        print(f"WARNING: Skipped {n_skipped} patients with missing first_event")

    # Print statistics
    n = len(input_ids_list)
    n_events = sum(events_list)
    n_censored = n - n_events
    token_counts = [len(ids) for ids in input_ids_list]
    durations_arr = np.array(durations_list)

    print(f"\n{'='*60}")
    print("SURVIVAL DATASET STATISTICS")
    print(f"{'='*60}")
    print(f"  Patients            : {n:,}")
    print(f"  Horizon             : {horizon_days} days ({horizon_days/365:.1f} years)")
    print(f"  Exclusion window    : {exclusion_window} days")
    print(f"  Events (Y=1)        : {n_events:,} ({100*n_events/n:.1f}%)")
    print(f"  Censored (Y=0)      : {n_censored:,} ({100*n_censored/n:.1f}%)")
    print(f"  Duration (days)")
    print(f"    Mean              : {durations_arr.mean():.1f}")
    print(f"    Median            : {np.median(durations_arr):.1f}")
    print(f"    Min / Max         : {durations_arr.min():.0f} / {durations_arr.max():.0f}")
    print(f"  Tokens per patient")
    print(f"    Mean              : {np.mean(token_counts):.1f}")
    print(f"    Max               : {max(token_counts)}")
    truncated = sum(1 for t in token_counts if t == max_length) if max_length > 0 else 0
    print(f"    Truncated         : {truncated} ({100*truncated/n:.1f}%)")

    # Stratified split (stratify on event indicator for balanced splits)
    indices = list(range(n))
    idx_trainval, idx_test = train_test_split(
        indices, test_size=test_size, random_state=seed, stratify=events_list
    )
    events_trainval = [events_list[i] for i in idx_trainval]
    adjusted_val = val_size / (1.0 - test_size)
    idx_train, idx_val = train_test_split(
        idx_trainval, test_size=adjusted_val, random_state=seed, stratify=events_trainval
    )

    def make_split(idxs):
        return Dataset.from_dict(
            {
                "input_ids": [input_ids_list[i] for i in idxs],
                "duration": [durations_list[i] for i in idxs],
                "event": [events_list[i] for i in idxs],
            }
        )

    datasets = DatasetDict(
        {
            "train": make_split(idx_train),
            "validation": make_split(idx_val),
            "test": make_split(idx_test),
        }
    )

    out_dir = Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    for split, ds in datasets.items():
        ds.to_parquet(out_dir / f"{split}.parquet")

    # Print split stats
    print(f"\n  Splits:")
    for name, idxs in [("train", idx_train), ("validation", idx_val), ("test", idx_test)]:
        split_events = [events_list[i] for i in idxs]
        e = sum(split_events)
        print(f"    {name:12s}: {len(idxs):5,} rows  |  events={e} ({100*e/len(idxs):.1f}%)  censored={len(idxs)-e}")

    # Save metadata
    metadata = {
        "horizon_days": horizon_days,
        "exclusion_window": exclusion_window,
        "tokenizer_name": tokenizer_name,
        "max_length": max_length,
        "n_patients": n,
        "n_events": n_events,
        "n_censored": n_censored,
        "event_rate": round(n_events / n, 4),
        "splits": {
            "train": len(idx_train),
            "validation": len(idx_val),
            "test": len(idx_test),
        },
    }
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n  Saved to {out_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare SMART longitudinal data for survival analysis with administrative censoring."
    )
    parser.add_argument("--jsonl-path", type=str, default="data/dummy_data/longitudinal_dataset.jsonl")
    parser.add_argument("--out-dir", type=str, default="data/dummy_data/longitudinal_dummy_smart_survival")
    parser.add_argument("--tokenizer-name", type=str, default="meta-llama/Llama-3.2-1B")
    parser.add_argument("--max-length", type=int, default=512,
                        help="Max token length per patient. Set to 0 to disable truncation.")
    parser.add_argument("--horizon-days", type=int, default=1825,
                        help="Administrative censoring horizon in days. Default: 1825 (5 years). "
                             "Patients with first_event > horizon are censored at horizon (Y=0, T=horizon).")
    parser.add_argument("--exclusion-window", type=int, default=0,
                        help="Exclude events within this many days before baseline (datediff > -N). "
                             "E.g. 180 drops the last 6 months of events. Default: 0 (no exclusion).")
    args = parser.parse_args()

    preprocess_dummy_smart_survival(
        jsonl_path=args.jsonl_path,
        out_dir=args.out_dir,
        tokenizer_name=args.tokenizer_name,
        max_length=args.max_length,
        horizon_days=args.horizon_days,
        exclusion_window=args.exclusion_window,
    )
