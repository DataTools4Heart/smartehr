import json
import argparse
import os
from pathlib import Path

from datasets import Dataset


def apply_censoring(first_event: float, cd_event: int, horizon: int) -> tuple[float, int]:
    """Administrative censoring at ``horizon`` days.

    Identical rule to ``preprocess_smartehr_survival.apply_censoring`` (kept in sync,
    duplicated for the same reason ``prepare_smart_features_for_mlp.py`` does — so this
    script runs standalone via ``python scripts/smartehr/...`` without a two-level import):
      - censored (cd_event=0): (min(first_event, horizon), 0)
      - event within horizon:  (first_event, 1)
      - event beyond horizon:  (horizon, 0)  # landmark rule: event-free at the horizon
    """
    if cd_event == 0:
        return (float(min(first_event, horizon)), 0)
    if first_event <= horizon:
        return (float(first_event), 1)
    return (float(horizon), 0)


def _is_missing(v) -> bool:
    """True for values we omit from the serialization: None, empty string, or NaN.

    NaN matters specifically: pandas missing cells become Python ``float('nan')`` in
    the JSONL (json dumps/loads pass ``NaN`` through), and ``float('nan')`` is neither
    None nor "" — so it must be caught explicitly (``v != v`` is the NaN test), else it
    serializes as the noise token ``"nan"``.
    """
    return v is None or v == "" or (isinstance(v, float) and v != v)


def serialize_time_point(fields: dict, skip_keys: tuple = ()) -> str:
    """Serialize one time point (a dict of field->value) into a text string.

    One ``name: value`` per line (floats rounded); free-text fields render verbatim.
    No imputation, no standardization, no code translation — the text is the
    near-lossless representation of whatever was actually recorded at this point, and
    missing fields are omitted rather than emitted as ``nan``.
    """
    parts = []
    for k, v in fields.items():
        if k in skip_keys:
            continue
        if _is_missing(v):
            continue  # omit missing values rather than imputing or emitting "nan"
        parts.append(f"{k}: {round(v, 4) if isinstance(v, float) else v}")
    return "\n".join(parts)


def serialize_baseline(smart: dict) -> str:
    """Serialize the static SMART baseline block as time point 0.

    Mirrors the leakage guard in preprocess_smartehr_survival.serialize_patient:
    drop ``SmrtRisk`` and every column after it (outcome-adjacent), and never
    include the targets ``first_event`` / ``cd_event``.
    """
    parts = []
    past_smrtrisk = False
    for k, v in smart.items():
        if k == "SmrtRisk":
            past_smrtrisk = True
        if past_smrtrisk:
            continue
        if k in ("first_event", "cd_event"):
            continue
        if _is_missing(v):
            continue
        parts.append(f"{k}: {round(v, 4) if isinstance(v, float) else v}")
    return "\n".join(parts)


def build_patient_sequence(record: dict) -> tuple[list[str], list[float]]:
    """Turn one patient record into a time-ordered sequence of time points.

    Returns (texts, time_deltas) where:
      - texts[0] is the static SMART baseline (time delta 0.0),
      - texts[1:] are the longitudinal events sorted by datediff,
      - time_deltas are ``datediff / 365.0`` (years, sign preserved) — raw day
        magnitudes (~-8000) would destabilize the model's Linear(1, .) time encoder.

    Every sequence has length >= 1 (baseline always present), so a patient with no
    events cleanly degrades to a length-1 sequence (the static baseline alone).
    """
    texts = [serialize_baseline(record["smart"])]
    time_deltas = [0.0]

    events = sorted(record.get("events", []), key=lambda e: e["datediff"])
    for event in events:
        texts.append(serialize_time_point(event, skip_keys=("datediff",)))
        time_deltas.append(event["datediff"] / 365.0)

    return texts, time_deltas


def preprocess_longitudinal_survival(
    jsonl_dir: str,
    out_dir: str,
    horizon_days: int = 1825,
):
    jsonl_dir = Path(jsonl_dir)
    out_dir = Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    print(f"Loading split JSONL files from {jsonl_dir} ...")
    print(f"Applying administrative censoring at {horizon_days} days ({horizon_days / 365:.1f} years)")
    print("Serializing each time point to raw text (instruction + tokenization happen in the extractor).")

    split_datasets = {}
    total_n = 0
    total_events = 0
    total_tps = 0

    for split_name in ["train", "validation", "test"]:
        split_file = jsonl_dir / f"{split_name}.jsonl"
        texts_list = []
        time_deltas_list = []
        durations_list = []
        events_list = []
        n_skipped = 0
        seq_lengths = []

        with open(split_file) as f:
            for line in f:
                rec = json.loads(line)
                first_event = rec["smart"].get("first_event")
                if first_event is None:
                    n_skipped += 1
                    continue

                cd_event_raw = rec["smart"].get("cd_event")
                cd_event = int(cd_event_raw) if cd_event_raw is not None else 1

                texts, time_deltas = build_patient_sequence(rec)
                duration, event = apply_censoring(first_event, cd_event, horizon_days)

                texts_list.append(texts)
                time_deltas_list.append(time_deltas)
                durations_list.append(duration)
                events_list.append(event)
                seq_lengths.append(len(texts))

        if n_skipped > 0:
            print(f"  WARNING: Skipped {n_skipped} patients in {split_name} with missing first_event")

        ds = Dataset.from_dict(
            {
                "texts": texts_list,
                "time_deltas_list": time_deltas_list,
                "duration": durations_list,
                "event": events_list,
            }
        )
        ds.to_parquet(out_dir / f"{split_name}.parquet")
        split_datasets[split_name] = ds

        n = len(ds)
        e = sum(events_list)
        tps = sum(seq_lengths)
        total_n += n
        total_events += e
        total_tps += tps
        print(
            f"  {split_name:12s}: {n:5,} patients  |  events={e} ({100*e/max(n,1):.1f}%)  "
            f"seq len min/mean/max = {min(seq_lengths)}/{tps/max(n,1):.1f}/{max(seq_lengths)}"
        )

    print(f"\n{'='*60}")
    print("LONGITUDINAL SURVIVAL DATASET STATISTICS")
    print(f"{'='*60}")
    print(f"  Total patients      : {total_n:,}")
    print(f"  Total time points   : {total_tps:,} (avg {total_tps/max(total_n,1):.1f}/patient)")
    print(f"  Horizon             : {horizon_days} days ({horizon_days/365:.1f} years)")
    print(f"  Events (Y=1)        : {total_events:,} ({100*total_events/max(total_n,1):.1f}%)")

    metadata = {
        "horizon_days": horizon_days,
        "representation": "per_time_point_text",
        "time_delta_unit": "years",
        "n_patients": total_n,
        "n_time_points": total_tps,
        "n_events": total_events,
        "n_censored": total_n - total_events,
        "event_rate": round(total_events / max(total_n, 1), 4),
        "splits": {name: len(ds) for name, ds in split_datasets.items()},
    }
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n  Saved to {out_dir}")
    print(f"  Next: run scripts/smartehr/extract_qwen_embeddings_longitudinal.py on this directory.")
    print(f"{'='*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare SMART longitudinal data for survival analysis as a sequence of "
        "per-time-point text records (minimal preprocessing). Consumes the JSONL output of "
        "smartehr_pipeline.py and emits parquet with per-patient text sequences + time deltas + "
        "(duration, event) survival targets."
    )
    parser.add_argument("--jsonl-dir", type=str, required=True,
                        help="Directory containing train/validation/test.jsonl (output of smartehr_pipeline.py).")
    parser.add_argument("--out-dir", type=str,
                        default="data/dummy_data/longitudinal_dummy_smart_survival_longitudinal")
    parser.add_argument("--horizon-days", type=int, default=1825,
                        help="Administrative censoring horizon in days. Default: 1825 (5 years).")
    args = parser.parse_args()

    preprocess_longitudinal_survival(
        jsonl_dir=args.jsonl_dir,
        out_dir=args.out_dir,
        horizon_days=args.horizon_days,
    )
