import json
import math
from pathlib import Path
import pandas as pd
import argparse
import os

def preprocess_smart_ehr(
    smart_csv,
    event_csvs,
    baseline_time,
    end_of_study,
    output_path,
):
    """
    Preprocess SmartEHR data to create a longitudinal dataset.

    Parameters:
    - smart_csv: Path to the smart.csv file. Must contain 'first_event' (time)
      and 'cd_event' (0/1 indicator) columns for survival analysis.
    - event_csvs: Dictionary of event source names and their file paths.
    - baseline_time: Reference point; events with datediff < this are kept.
    - end_of_study: Maximum follow-up time. Patients with first_event > this
      are administratively censored at end_of_study.
    - output_path: Path to save the longitudinal dataset as JSONL.
    """
    # Load smart.csv
    smart_df = pd.read_csv(smart_csv)
    n_total = len(smart_df)

    # Ensure cd_event column exists; if missing, assume all are events (legacy behavior)
    if "cd_event" not in smart_df.columns:
        print("WARNING: 'cd_event' column not found. Assuming all patients had events.")
        smart_df["cd_event"] = 1

    # Apply administrative censoring at end_of_study rather than dropping patients
    beyond_study = smart_df["first_event"] - baseline_time > end_of_study
    smart_df.loc[beyond_study, "first_event"] = end_of_study + baseline_time
    smart_df.loc[beyond_study, "cd_event"] = 0
    print(f"Patients: {n_total:,} total, {beyond_study.sum():,} administratively censored at end_of_study={end_of_study}")

    # Columns that belong to smart (everything except m3life_no)
    smart_feature_cols = [c for c in smart_df.columns if c != "m3life_no"]

    # Load event CSVs, apply event-level filter
    event_frames = []
    for source, path in event_csvs.items():
        df = pd.read_csv(path)
        df = df[df["datediff"] < baseline_time].copy()
        source_cols = [c for c in df.columns if c in ("m3life_no", "datediff") or c.startswith(f"{source}_")]
        df = df[source_cols]
        df["_source"] = source
        event_frames.append(df)

    all_events = pd.concat(event_frames, ignore_index=True, sort=False)

    # Merge events that share the same (m3life_no, datediff)
    def merge_event_rows(rows):
        merged = {"datediff": int(rows["datediff"].iloc[0])}
        for _, r in rows.iterrows():
            for col, val in r.items():
                if col in ("m3life_no", "datediff", "_source"):
                    continue
                if pd.notna(val):
                    merged[col] = float(val) if isinstance(val, float) else val
        return merged

    events_by_patient = {}
    for pid, grp in all_events.groupby("m3life_no"):
        events = [merge_event_rows(sub) for _, sub in grp.groupby("datediff", sort=True)]
        events_by_patient[int(pid)] = events

    # Build longitudinal dataset
    dataset = []
    for _, row in smart_df.iterrows():
        pid = int(row["m3life_no"])
        record = {
            "m3life_no": pid,
            "smart": {
                k: (int(v) if isinstance(v, (int,)) else float(v) if isinstance(v, float) else v)
                for k, v in row.items() if k in smart_feature_cols
            },
            "events": events_by_patient.get(pid, []),
        }
        dataset.append(record)

    # Save as JSONL
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        for record in dataset:
            f.write(json.dumps(record) + "\n")

    print(f"Saved {len(dataset):,} patient records → {output_path}")
    total_events = sum(len(p["events"]) for p in dataset)
    print(f"Total events across all patients: {total_events:,}")

    return dataset

def apply_time_windows(
    dataset,
    window_size,
    baseline_time,
    windowed_output_path=None,
):
    """
    Replace each patient's flat `events` list with a `windows` dict.

    Parameters:
    - dataset: List of patient dictionaries from the preprocessing step.
    - window_size: Size of each time bucket (same unit as datediff).
    - baseline_time: Reference point.
    - windowed_output_path: If given, saves the result as JSONL at this path.
    """
    def collapse_window(events):
        sorted_events = sorted(events, key=lambda e: e["datediff"])
        collapsed = {}
        for event in sorted_events:
            for k, v in event.items():
                collapsed[k] = v
        return collapsed

    windowed = []
    for patient in dataset:
        record = {k: v for k, v in patient.items() if k != "events"}
        buckets = {}
        for event in patient["events"]:
            idx = math.floor((event["datediff"] - baseline_time) / window_size)
            buckets.setdefault(idx, []).append(event)
        record["windows"] = {k: collapse_window(buckets[k]) for k in sorted(buckets)}
        windowed.append(record)

    if windowed_output_path:
        Path(windowed_output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(windowed_output_path, "w") as f:
            for record in windowed:
                f.write(json.dumps(record) + "\n")
        print(f"Saved windowed dataset → {windowed_output_path}")

    return windowed

def get_event_csvs(folder_path):
    """Generate a dictionary of event CSVs with file stems as keys."""
    event_csvs = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            stem = Path(file_name).stem
            event_csvs[stem] = os.path.join(folder_path, file_name)
    return event_csvs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SmartEHR Pipeline")

    # Add arguments
    parser.add_argument("--smart_csv", type=str, required=True, help="Path to the smart.csv file.")
    parser.add_argument("--event_csv_folder", type=str, required=True, help="Path to the folder containing event CSV files.")
    parser.add_argument("--baseline_time", type=int, default=0, help="Reference point; events with datediff < this are kept.")
    parser.add_argument("--end_of_study", type=int, default=3650, help="Patients with first_event - baseline_time > this are dropped.")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the longitudinal dataset as JSONL.")
    parser.add_argument("--window_size", type=int, default=10, help="Size of each time bucket (same unit as datediff).")
    parser.add_argument("--windowed_output_path", type=str, required=True, help="Path to save the windowed dataset as JSONL.")

    args = parser.parse_args()

    # Generate event_csvs from the folder
    event_csvs = get_event_csvs(args.event_csv_folder)

    # Preprocess the dataset
    dataset = preprocess_smart_ehr(
        args.smart_csv,
        event_csvs,
        args.baseline_time,
        args.end_of_study,
        args.output_path,
    )

    # Apply time windows
    windowed_dataset = apply_time_windows(
        dataset,
        args.window_size,
        args.baseline_time,
        args.windowed_output_path,
    )