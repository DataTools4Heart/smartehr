import init
import json
import argparse
import os
from pathlib import Path

import numpy as np
from datasets import Dataset, DatasetDict
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer


LABEL_THRESHOLD = 3650  # first_event <= threshold → label 1 (event within 10 years), else 0


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
        if k == "first_event":
            continue  # target variable, must not be in the input
        parts.append(f"{k}: {round(v, 4) if isinstance(v, float) else v}")

    cutoff = -exclusion_window  # keep datediff <= cutoff (strictly more negative)
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


def print_statistics(
    records: list,
    input_ids_list: list,
    labels_list: list,
    idx_train: list,
    idx_val: list,
    idx_test: list,
    exclusion_window: int,
    label_threshold: int,
    max_length: int,
) -> dict:
    n = len(records)
    token_counts = [len(ids) for ids in input_ids_list]
    event_counts = [
        sum(1 for e in rec.get("events", []) if e["datediff"] <= -exclusion_window)
        for rec in records
    ]

    def pct(arr, p):
        return int(np.percentile(arr, p))

    pos = sum(labels_list)
    truncated = sum(1 for t in token_counts if t == max_length) if max_length > 0 else 0
    no_events = sum(1 for c in event_counts if c == 0)

    splits_stats = {}
    for name, idxs in [("train", idx_train), ("validation", idx_val), ("test", idx_test)]:
        split_labels = [labels_list[i] for i in idxs]
        p = sum(split_labels)
        splits_stats[name] = {"n": len(idxs), "positive": p, "negative": len(idxs) - p}

    stats = {
        "patients": n,
        "label_threshold_days": label_threshold,
        "exclusion_window_days": exclusion_window,
        "max_token_length": max_length,
        "labels": {"positive": pos, "negative": n - pos},
        "tokens_per_patient": {
            "mean": round(float(np.mean(token_counts)), 2),
            "median": round(float(np.median(token_counts)), 2),
            "min": int(min(token_counts)),
            "max": int(max(token_counts)),
            "p25": pct(token_counts, 25),
            "p75": pct(token_counts, 75),
            "p95": pct(token_counts, 95),
            "truncated": truncated,
        },
        "events_per_patient": {
            "mean": round(float(np.mean(event_counts)), 2),
            "median": round(float(np.median(event_counts)), 2),
            "min": int(min(event_counts)),
            "max": int(max(event_counts)),
            "p25": pct(event_counts, 25),
            "p75": pct(event_counts, 75),
            "p95": pct(event_counts, 95),
            "no_events": no_events,
        },
        "splits": splits_stats,
    }

    print("\n" + "=" * 60)
    print("DATASET STATISTICS")
    print("=" * 60)
    print(f"  Patients            : {n:,}")
    print(f"  Label threshold     : first_event <= {label_threshold} days")
    print(f"  Exclusion window    : {exclusion_window} days before baseline")
    print(f"  Max token length    : {max_length if max_length > 0 else 'no truncation'}")
    print()
    print("  Labels")
    print(f"    Positive (1)      : {pos:,}  ({100*pos/n:.1f}%)")
    print(f"    Negative (0)      : {n-pos:,}  ({100*(n-pos)/n:.1f}%)")
    print()
    print("  Tokens per patient  (after truncation)")
    print(f"    Mean              : {np.mean(token_counts):.1f}")
    print(f"    Median            : {np.median(token_counts):.1f}")
    print(f"    Min / Max         : {min(token_counts)} / {max(token_counts)}")
    print(f"    p25 / p75 / p95   : {pct(token_counts,25)} / {pct(token_counts,75)} / {pct(token_counts,95)}")
    print(f"    Truncated         : {truncated} ({100*truncated/n:.1f}%)")
    print()
    print("  Events per patient  (after exclusion window)")
    print(f"    Mean              : {np.mean(event_counts):.1f}")
    print(f"    Median            : {np.median(event_counts):.1f}")
    print(f"    Min / Max         : {min(event_counts)} / {max(event_counts)}")
    print(f"    p25 / p75 / p95   : {pct(event_counts,25)} / {pct(event_counts,75)} / {pct(event_counts,95)}")
    print(f"    No events         : {no_events} ({100*no_events/n:.1f}%)")
    print()
    print("  Splits")
    for name, idxs in [("train", idx_train), ("validation", idx_val), ("test", idx_test)]:
        split_labels = [labels_list[i] for i in idxs]
        p = sum(split_labels)
        print(f"    {name:12s}: {len(idxs):5,} rows  |  pos={p} ({100*p/len(idxs):.1f}%)")
    print("=" * 60)

    return stats


def preprocess_dummy_smart(
    jsonl_path: str,
    out_dir: str,
    tokenizer_name: str = "meta-llama/Llama-3.2-1B",
    max_length: int = 512,
    label_threshold: int = LABEL_THRESHOLD,
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

    print(f"Loaded {len(records):,} patients. Tokenising with {tokenizer_name} ...")
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    truncate = max_length > 0
    input_ids_list = []
    labels_list = []
    for rec in records:
        text = serialize_patient(rec, exclusion_window=exclusion_window)
        if truncate:
            enc = tokenizer(text, truncation=True, max_length=max_length, add_special_tokens=True)
        else:
            enc = tokenizer(text, add_special_tokens=True)  # full sequence, no truncation
        input_ids_list.append(enc["input_ids"])
        label = int(rec["smart"]["first_event"] <= label_threshold)
        labels_list.append(label)

    n = len(input_ids_list)
    indices = list(range(n))
    idx_trainval, idx_test = train_test_split(indices, test_size=test_size, random_state=seed, stratify=labels_list)
    labels_trainval = [labels_list[i] for i in idx_trainval]
    adjusted_val = val_size / (1.0 - test_size)
    idx_train, idx_val = train_test_split(
        idx_trainval, test_size=adjusted_val, random_state=seed, stratify=labels_trainval
    )

    def make_split(idxs):
        return Dataset.from_dict(
            {
                "input_ids": [input_ids_list[i] for i in idxs],
                "labels": [labels_list[i] for i in idxs],
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

    stats = print_statistics(records, input_ids_list, labels_list, idx_train, idx_val, idx_test,
                              exclusion_window, label_threshold, max_length)
    stats_path = out_dir / "statistics.json"
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"\nSaved to {out_dir}  (statistics.json included)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--jsonl-path", type=str, default="data/dummy_data/longitudinal_dataset.jsonl")
    parser.add_argument("--out-dir", type=str, default="data/dummy_data/longitudinal_dummy_smart")
    parser.add_argument("--tokenizer-name", type=str, default="meta-llama/Llama-3.2-1B")
    parser.add_argument("--max-length", type=int, default=512,
                        help="Max token length per patient. Set to 0 to disable truncation (store full sequences).")
    parser.add_argument("--label-threshold", type=int, default=LABEL_THRESHOLD,
                        help="first_event <= threshold → label 1 (early event). Default: 3650 (10 years).")
    parser.add_argument("--exclusion-window", type=int, default=0,
                        help="Exclude events within this many days before baseline (datediff > -N). "
                             "E.g. 180 drops the last 6 months of events. Default: 0 (no exclusion).")
    args = parser.parse_args()

    preprocess_dummy_smart(
        jsonl_path=args.jsonl_path,
        out_dir=args.out_dir,
        tokenizer_name=args.tokenizer_name,
        max_length=args.max_length,
        label_threshold=args.label_threshold,
        exclusion_window=args.exclusion_window,
    )
