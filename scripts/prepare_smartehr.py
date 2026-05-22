import json
import math
from pathlib import Path

import pandas as pd

# ── Paths (adjust here if files move) ─────────────────────────────────────
SMART_CSV  = "data/smart/smart_utf8.csv"
EVENT_CSVS_PATH = "data/smartehr-utf8/"
EVENT_CSVS = {}
for csv in Path(EVENT_CSVS_PATH).glob("*.csv"):
    EVENT_CSVS[csv.stem] = csv
# ── Filtering parameters ───────────────────────────────────────────────────
BASELINE_TIME = 0       # reference point; events with datediff < this are kept
END_OF_STUDY  = 3650    # patients with first_event - baseline_time > this are dropped

# ── Output ─────────────────────────────────────────────────────────────────
OUTPUT_PATH = "data/test/longitudinal_dataset.jsonl"

def first_event(row):
    min_value = float("inf")
    for column in row.index:
        if column.startswith("e") and column.endswith("_f"):
            if row[column] is not None and row[column] >= 0:
                min_value = min(min_value, row[column])

    if min_value == float("inf"):
        return None
    return min_value

def drop_outcomes(df):
    to_drop = [c for c in df if c.startswith("e") and c.endswith("_f")]
    to_drop = ["_".join(c.split("_")[:-1]) for c in to_drop]
    for c in df.columns:
        if "_".join(c.split("_")[:-1]) in to_drop:
            df = df.drop(c, axis=1)
    return df

# ── Load smart.csv and apply patient-level filter ─────────────────────────
smart_df = pd.read_csv(SMART_CSV)
smart_df["first_event"] = smart_df.apply(first_event, axis=1)
smart_df = drop_outcomes(smart_df)
smart_df = smart_df[~smart_df["first_event"].isna()]
smart_df = smart_df.loc[smart_df.groupby("m3life_no")["first_event"].idxmin()]
n_total = len(smart_df)
smart_df = smart_df[smart_df["first_event"] - BASELINE_TIME <= END_OF_STUDY].reset_index(drop=True)
print(f"Patients after filter: {len(smart_df):,} / {n_total:,}")

# Columns that belong to smart (everything except m3life_no)
SMART_FEATURE_COLS = [c for c in smart_df.columns if c != "m3life_no"]

# ── Load event CSVs, apply event-level filter ─────────────────────────────
# Keep only source-specific feature columns (no NaN-producing columns from other sources)
event_frames = []
for source, path in EVENT_CSVS.items():
    df = pd.read_csv(path)
    df = df[df["datediff"] < BASELINE_TIME].copy()
    source_cols = [c for c in df.columns]
    df = df[source_cols]
    df["_source"] = source
    event_frames.append(df)

all_events = pd.concat(event_frames, ignore_index=True, sort=False)

# ── Merge events that share the same (m3life_no, datediff) ────────────────
def merge_event_rows(rows: pd.DataFrame) -> dict:
    """Collapse multiple rows at the same datediff into one merged dict (source-only keys)."""
    merged = {"datediff": int(rows["datediff"].iloc[0])}
    for _, r in rows.iterrows():
        for col, val in r.items():
            if col in ("m3life_no", "datediff", "_source"):
                continue
            if pd.notna(val):
                merged[col] = float(val) if isinstance(val, float) else val
    return merged

# Group by patient, then by datediff to merge same-day collisions
events_by_patient: dict[int, list[dict]] = {}
for pid, grp in all_events.groupby("m3life_no"):
    events = [merge_event_rows(sub) for _, sub in grp.groupby("datediff", sort=True)]
    events_by_patient[int(pid)] = events

# ── Build longitudinal dataset ─────────────────────────────────────────────
dataset = []
for _, row in smart_df.iterrows():
    pid = int(row["m3life_no"])
    record = {
        "m3life_no": pid,
        "smart": {
            k: (int(v) if isinstance(v, (int,)) else float(v) if isinstance(v, float) else v)
            for k, v in row.items() if k in SMART_FEATURE_COLS
        },
        "events": events_by_patient.get(pid, []),
    }
    dataset.append(record)

# ── Save as JSONL (one patient per line) ──────────────────────────────────
Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_PATH, "w") as f:
    for record in dataset:
        f.write(json.dumps(record) + "\n")

print(f"Saved {len(dataset):,} patient records → {OUTPUT_PATH}")
total_events = sum(len(p["events"]) for p in dataset)
print(f"Total events across all patients: {total_events:,}")

# Spot-check
sample = dataset[0]
print(f"\nSample record (first patient):")
print(f"  m3life_no : {sample['m3life_no']}")
print(f"  smart     : {sample['smart']}")
print(f"  events[0] : {sample['events'][0] if sample['events'] else 'none'}")