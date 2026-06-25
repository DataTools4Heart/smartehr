import json
import argparse
import os
from pathlib import Path

from datasets import Dataset
from transformers import AutoTokenizer


def serialize_patient(record: dict) -> str:
    """Serialize a patient record to a natural-language text string.

    Args:
        record: Patient record dict with 'smart' and 'events' keys.
    """
    smart = record["smart"]
    parts = ["[PATIENT]"]
    for k, v in smart.items():
        if k in ("first_event", "cd_event"):
            continue  # target variables, must not be in the input
        parts.append(f"{k}: {round(v, 4) if isinstance(v, float) else v}")

    for event in record.get("events", []):
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


def preprocess_smart_survival(
    jsonl_dir: str,
    out_dir: str,
    tokenizer_name: str = "meta-llama/Llama-3.2-1B",
    max_length: int = 512,
    horizon_days: int = 1825,
):
    jsonl_dir = Path(jsonl_dir)
    print(f"Loading split JSONL files from {jsonl_dir} ...")
    print(f"Applying administrative censoring at {horizon_days} days ({horizon_days / 365:.1f} years)")
    print(f"Tokenising with {tokenizer_name} ...")

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    truncate = max_length > 0
    out_dir = Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    split_datasets = {}
    total_n = 0
    total_events = 0

    for split_name in ["train", "validation", "test"]:
        split_file = jsonl_dir / f"{split_name}.jsonl"
        records = []
        with open(split_file) as f:
            for line in f:
                records.append(json.loads(line))

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
            cd_event = int(cd_event_raw) if cd_event_raw is not None else 1

            text = serialize_patient(rec)
            if truncate:
                enc = tokenizer(text, truncation=True, max_length=max_length, add_special_tokens=True)
            else:
                enc = tokenizer(text, add_special_tokens=True)
            input_ids_list.append(enc["input_ids"])

            duration, event = apply_censoring(first_event, cd_event, horizon_days)
            durations_list.append(duration)
            events_list.append(event)

        if n_skipped > 0:
            print(f"  WARNING: Skipped {n_skipped} patients in {split_name} with missing first_event")

        ds = Dataset.from_dict(
            {"input_ids": input_ids_list, "duration": durations_list, "event": events_list}
        )
        ds.to_parquet(out_dir / f"{split_name}.parquet")
        split_datasets[split_name] = ds

        n = len(ds)
        e = sum(events_list)
        total_n += n
        total_events += e
        print(f"  {split_name:12s}: {n:5,} rows  |  events={e} ({100*e/n:.1f}%)  censored={n-e}")

    # Print summary
    print(f"\n{'='*60}")
    print("SURVIVAL DATASET STATISTICS")
    print(f"{'='*60}")
    print(f"  Total patients      : {total_n:,}")
    print(f"  Horizon             : {horizon_days} days ({horizon_days/365:.1f} years)")
    print(f"  Events (Y=1)        : {total_events:,} ({100*total_events/total_n:.1f}%)")
    print(f"  Censored (Y=0)      : {total_n-total_events:,} ({100*(total_n-total_events)/total_n:.1f}%)")

    # Save metadata
    metadata = {
        "horizon_days": horizon_days,
        "tokenizer_name": tokenizer_name,
        "max_length": max_length,
        "n_patients": total_n,
        "n_events": total_events,
        "n_censored": total_n - total_events,
        "event_rate": round(total_events / total_n, 4),
        "splits": {name: len(ds) for name, ds in split_datasets.items()},
    }
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n  Saved to {out_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare SMART longitudinal data for survival analysis with administrative censoring."
    )
    parser.add_argument("--jsonl-dir", type=str, required=True,
                        help="Directory containing train.jsonl, validation.jsonl, test.jsonl (output of smartehr_pipeline.py).")
    parser.add_argument("--out-dir", type=str, default="data/dummy_data/longitudinal_dummy_smart_survival")
    parser.add_argument("--tokenizer-name", type=str, default="meta-llama/Llama-3.2-1B")
    parser.add_argument("--max-length", type=int, default=512,
                        help="Max token length per patient. Set to 0 to disable truncation.")
    parser.add_argument("--horizon-days", type=int, default=1825,
                        help="Administrative censoring horizon in days. Default: 1825 (5 years). "
                             "Patients with first_event > horizon are censored at horizon (Y=0, T=horizon).")
    args = parser.parse_args()

    preprocess_smart_survival(
        jsonl_dir=args.jsonl_dir,
        out_dir=args.out_dir,
        tokenizer_name=args.tokenizer_name,
        max_length=args.max_length,
        horizon_days=args.horizon_days,
    )
