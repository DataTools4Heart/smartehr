"""Extract NUMERIC longitudinal features directly from the events (no serialization,
no LLM) and write the flat `inputs`/duration/event parquet for `model=mlp`.

Motivation: frozen text embeddings blur numeric magnitude/trend, which is where the
longitudinal signal lives. This aggregates each numeric event field over a patient's
history into fixed features so an MLP can use the actual values.

Per patient, for every numeric field seen across the events, compute aggregates over
the (time-ordered) history: last (most recent), mean, min, max, count. Optionally
concatenate the baseline SMART numeric fields (--include-baseline), and optionally
pivot coded sources so each test/measurement becomes its own feature (--pivot-codes:
lab_result by lab_testcode, data1 by label/meting, Value_ECHO by MeasName_ECHO).

Caveats: consumes the JSONL from smartehr_pipeline.py, whose merge_event_rows is
last-write-wins per (m3life_no, datediff) — so multiple same-source records on one day
were already collapsed. Without --pivot-codes, a generic field like `lab_result` is
aggregated across all test types (only meaningful with the pivot). Standardization is
fit on train only; absent features are filled with the (standardized) mean = 0.

Output schema matches the MLP path:
    inputs [n_features], duration, event   ->  dataset=smartehr_embeddings model=mlp
    model.input_size = n_features (printed at the end and stored in metadata.json)
"""

import argparse
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import Dataset

# code_field -> value_field, for --pivot-codes (each code value becomes its own feature)
_PIVOT = {"lab_testcode": "lab_result", "label": "data1", "MeasName_ECHO": "Value_ECHO"}
_AGGS = ["last", "mean", "min", "max", "count"]


def apply_censoring(first_event: float, cd_event: int, horizon: int) -> tuple[float, int]:
    """Administrative censoring at `horizon` days (same rule as the other prep scripts)."""
    if cd_event == 0:
        return (float(min(first_event, horizon)), 0)
    if first_event <= horizon:
        return (float(first_event), 1)
    return (float(horizon), 0)


def _is_num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and not (isinstance(v, float) and v != v)


def _patient_series(rec: dict, pivot: bool) -> dict[str, list[float]]:
    """Collect {feature_name: [values ordered oldest->most recent]} from a patient's events."""
    events = sorted(rec.get("events", []), key=lambda e: e["datediff"])
    series: dict[str, list[float]] = {}
    for ev in events:
        consumed = set()
        if pivot:
            for code_field, value_field in _PIVOT.items():
                if code_field in ev and value_field in ev and _is_num(ev[value_field]):
                    series.setdefault(f"{value_field}[{ev[code_field]}]", []).append(float(ev[value_field]))
                    consumed.update((code_field, value_field))
        for k, v in ev.items():
            if k == "datediff" or k in consumed:
                continue
            if _is_num(v):
                series.setdefault(k, []).append(float(v))
    return series


def _aggregate(series: dict[str, list[float]], aggs: list[str]) -> dict[str, float]:
    """Reduce each feature's value list to the requested aggregates (last = most recent)."""
    out = {}
    for feat, vals in series.items():
        arr = np.asarray(vals, dtype=np.float64)
        for a in aggs:
            if a == "last":
                out[f"{feat}__last"] = arr[-1]
            elif a == "mean":
                out[f"{feat}__mean"] = arr.mean()
            elif a == "min":
                out[f"{feat}__min"] = arr.min()
            elif a == "max":
                out[f"{feat}__max"] = arr.max()
            elif a == "count":
                out[f"{feat}__count"] = float(arr.size)
    return out


def _baseline_features(rec: dict) -> dict[str, float]:
    """Numeric SMART baseline fields (leakage guard: drop SmrtRisk-onward + targets)."""
    out = {}
    past = False
    for k, v in rec["smart"].items():
        if k == "SmrtRisk":
            past = True
        if past or k in ("first_event", "cd_event"):
            continue
        if _is_num(v):
            out[f"baseline__{k}"] = float(v)
    return out


def _rows_for_split(jsonl_path: Path, pivot: bool, aggs: list[str], include_baseline: bool, horizon: int):
    rows, durations, events = [], [], []
    with open(jsonl_path) as f:
        for line in f:
            rec = json.loads(line)
            first_event = rec["smart"].get("first_event")
            if first_event is None:
                continue
            cd = rec["smart"].get("cd_event")
            cd = int(cd) if cd is not None else 1
            feats = _aggregate(_patient_series(rec, pivot), aggs)
            if include_baseline:
                feats.update(_baseline_features(rec))
            rows.append(feats)
            d, e = apply_censoring(first_event, cd, horizon)
            durations.append(d)
            events.append(e)
    return rows, durations, events


def main(jsonl_dir, out_dir, pivot, aggs, include_baseline, horizon):
    jsonl_dir, out_dir = Path(jsonl_dir), Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    split_rows, split_dur, split_evt = {}, {}, {}
    for split in ["train", "validation", "test"]:
        r, d, e = _rows_for_split(jsonl_dir / f"{split}.jsonl", pivot, aggs, include_baseline, horizon)
        split_rows[split], split_dur[split], split_evt[split] = r, d, e

    # Feature vocabulary fixed from TRAIN; count columns fill 0 (absent), others NaN -> mean.
    feature_names = sorted({k for row in split_rows["train"] for k in row})
    count_cols = {f for f in feature_names if f.endswith("__count")}
    print(f"Feature vocabulary: {len(feature_names)} columns "
          f"(pivot={pivot}, aggs={aggs}, include_baseline={include_baseline})")

    def to_frame(rows):
        df = pd.DataFrame(rows, columns=feature_names)
        df[list(count_cols)] = df[list(count_cols)].fillna(0.0)
        return df

    train_df = to_frame(split_rows["train"])
    means = train_df.mean(numeric_only=True)       # nan-aware (present values only)
    stds = train_df.std(numeric_only=True).replace(0.0, 1.0)

    n_features = len(feature_names)
    for split in ["train", "validation", "test"]:
        df = to_frame(split_rows[split])
        std_df = ((df - means) / stds).fillna(0.0)  # absent -> standardized mean (0)
        ds = Dataset.from_dict({
            "inputs": std_df.to_numpy(dtype=np.float32).tolist(),
            "duration": [float(x) for x in split_dur[split]],
            "event": [float(x) for x in split_evt[split]],
        })
        ds.to_parquet(out_dir / f"{split}.parquet")
        n, ev = len(ds), int(sum(split_evt[split]))
        print(f"  {split:12s}: {n:5,} patients | events={ev} ({100*ev/max(n,1):.1f}%) | features={n_features}")

    with open(out_dir / "metadata.json", "w") as f:
        json.dump({
            "representation": "event_numeric_features",
            "pivot_codes": pivot, "aggregators": aggs, "include_baseline": include_baseline,
            "horizon_days": horizon, "n_features": n_features,
            "feature_names": feature_names,
            "feature_means": means.reindex(feature_names).fillna(0.0).tolist(),
            "feature_stds": stds.reindex(feature_names).fillna(1.0).tolist(),
        }, f, indent=2)

    print(f"\nSaved to {out_dir}")
    print(f"Train with:  dataset=smartehr_embeddings dataset.root_path={out_dir} "
          f"model=mlp model.input_size={n_features}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--jsonl-dir", required=True, help="Dir with train/validation/test.jsonl (smartehr_pipeline.py output).")
    p.add_argument("--out-dir", required=True)
    p.add_argument("--aggregators", default=",".join(_AGGS),
                   help=f"Comma list from {_AGGS}. Default: all.")
    p.add_argument("--pivot-codes", action="store_true",
                   help="Pivot coded sources so each lab test / measurement / echo becomes its own feature "
                        "(recommended for real data; otherwise lab_result etc. is conflated across test types).")
    p.add_argument("--include-baseline", action="store_true",
                   help="Also concatenate the numeric SMART baseline fields (test baseline+events additivity).")
    p.add_argument("--horizon-days", type=int, default=1825)
    args = p.parse_args()

    aggs = [a.strip() for a in args.aggregators.split(",") if a.strip()]
    assert all(a in _AGGS for a in aggs), f"aggregators must be a subset of {_AGGS}"
    main(args.jsonl_dir, args.out_dir, args.pivot_codes, aggs, args.include_baseline, args.horizon_days)
