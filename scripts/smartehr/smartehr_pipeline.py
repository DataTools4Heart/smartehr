import json
import math
from pathlib import Path
import pandas as pd
import argparse
import os
from sklearn.model_selection import train_test_split


# SMART-specific outcome column names (original, unrenamed)
_SMART_OUTCOME_COLS = [
    "edood_f", "edood_n", "edoodvas",
    "ebero_f", "ebero_n", "ebero_s",
    "emi_f",   "emi_n",  "emi_s",
]


def drop_rows_with_missing_smart_outcomes(df):
    """Drop rows where any SMART outcome column is NaN (legacy preprocessing)."""
    for col in [c for c in _SMART_OUTCOME_COLS if c in df.columns]:
        df = df[~df[col].isna()]
    return df


def compute_legacy_targets(df, censoring_time=None):
    """Compute first_event and cd_event using SMART-specific Dutch column names.

    Indicator values per endpoint:
      1 = event occurred  → cd_event=1, time from e*_f column
      0 = censored        → cd_event=0, time from e*_f column
      2 = lost to FU      → cd_event=0, time = censoring_time

    Priority across the three endpoints when computing first_event: 1 > 0 > 2.
    That is: if any endpoint has status 1, use the earliest of those times;
    otherwise if any has status 0, use the earliest of those times;
    otherwise all are lost-to-FU and censoring_time is used.

    - death:  edoodvas == 1 (vascular death); edoodvas == 2 → lost to FU
    - stroke: ebero_n == 1 AND ebero_s in [11, 102]; ebero_n == 2 → lost to FU
    - myo:    emi_n == 1   AND emi_s   in [41, 101]; emi_n == 2 → lost to FU
    """
    target_stroke_types = [11, 102]
    target_myo_types = [41, 101]

    df = df.copy()
    df["_death"]  = df.apply(lambda x: x.get("edoodvas", 0) == 1, axis=1)
    df["_stroke"] = df.apply(
        lambda x: x.get("ebero_n", 0) == 1 and x.get("ebero_s") in target_stroke_types, axis=1
    )
    df["_myo"] = df.apply(
        lambda x: x.get("emi_n", 0) == 1 and x.get("emi_s") in target_myo_types, axis=1
    )
    df["_death_ltfu"]  = df.apply(lambda x: x.get("edoodvas", 0) == 2, axis=1)
    df["_stroke_ltfu"] = df.apply(lambda x: x.get("ebero_n", 0) == 2, axis=1)
    df["_myo_ltfu"]    = df.apply(lambda x: x.get("emi_n", 0) == 2, axis=1)

    _ENDPOINTS = [
        ("edood_f", "_death",  "_death_ltfu"),
        ("ebero_f", "_stroke", "_stroke_ltfu"),
        ("emi_f",   "_myo",    "_myo_ltfu"),
    ]

    def _compute_time_and_event(s):
        # Build (time, priority) pairs: priority 1=event, 0=censored, 2=lost-to-FU
        entries = []
        for time_col, evt_flag, ltfu_flag in _ENDPOINTS:
            if time_col not in s.index:
                continue
            if s[evt_flag]:
                entries.append((s[time_col], 1))
            elif s[ltfu_flag]:
                t = censoring_time if censoring_time is not None else s[time_col]
                entries.append((t, 2))
            else:
                entries.append((s[time_col], 0))

        for priority in [1, 0, 2]:
            candidates = [t for t, p in entries if p == priority]
            if candidates:
                return min(candidates), int(priority == 1)

        return None, 0

    results = df.apply(_compute_time_and_event, axis=1, result_type="expand")
    df["first_event"] = results[0]
    df["cd_event"]    = results[1]

    _tmp_cols = ["_death", "_stroke", "_myo", "_death_ltfu", "_stroke_ltfu", "_myo_ltfu"]
    df = df.drop(columns=_tmp_cols + [c for c in _SMART_OUTCOME_COLS if c in df.columns])
    return df


def compute_first_event(row):
    """Compute first_event as the minimum non-negative value across all e*_f (endpoint time) columns."""
    min_value = float("inf")
    for column in row.index:
        if column.startswith("e") and column.endswith("_f"):
            if row[column] is not None and row[column] >= 0:
                min_value = min(min_value, row[column])
    return min_value


def compute_cd_event(row):
    """Compute cd_event: 1 if ANY endpoint indicator (e*_n) is positive at the first_event time.

    Logic: for each endpoint time column (e*_f), check if it equals first_event AND
    the corresponding indicator column (e*_n) is positive. If so, a true event occurred.
    If first_event corresponds only to censoring times, cd_event = 0.
    """
    first_event = row.get("first_event")
    if first_event is None or pd.isna(first_event):
        return 0

    for column in row.index:
        if column.startswith("e") and column.endswith("_f"):
            if row[column] == first_event:
                # Check corresponding _n indicator column
                indicator_col = column[:-2] + "_n"
                if indicator_col in row.index and pd.notna(row[indicator_col]) and row[indicator_col] > 0:
                    return 1
    return 0


def drop_outcomes(df):
    """Drop all outcome-related columns (e*_f and their sibling columns e*_n, e*_s, etc.) and SmrtRisk."""
    outcome_prefixes = ["_".join(c.split("_")[:-1]) for c in df.columns if c.startswith("e") and c.endswith("_f")]
    cols_to_drop = [c for c in df.columns if "_".join(c.split("_")[:-1]) in outcome_prefixes]
    cols_to_drop += [c for c in df.columns if c.startswith("SmrtRisk")]
    return df.drop(columns=cols_to_drop)


def preprocess_smart_ehr(
    smart_csv,
    event_csvs,
    baseline_time,
    output_path,
    split_json,
    fix_test_split=False,
    exclusion_window=0,
    val_size=0.16,
    seed=42,
    legacy=False,
    censoring_time=None,
):
    """
    Preprocess SmartEHR data to create a longitudinal dataset with train/val/test splits.

    Parameters:
    - smart_csv: Path to the smart.csv file (raw, with outcome columns e*_f, e*_n, etc.).
    - event_csvs: Dictionary of event source names and their file paths.
    - baseline_time: Reference point; events with datediff < this are kept.
    - output_path: Path whose parent directory will contain the split JSONL files.
    - split_json: Path to a JSON file mapping split names (train/val/test) to lists of m3life_no.
    - fix_test_split: If False (default), use all three splits exactly as given in split_json.
        If True, use only the test split from split_json and randomly resample train/validation
        from the remaining patients (stratified by cd_event).
    - exclusion_window: Apply a washout window of this many days.
        Patients whose first_event < exclusion_window are dropped entirely.
        For the remaining patients, longitudinal events within this many days of
        first_event are also dropped (i.e. events where first_event - datediff < exclusion_window).
        0 means no exclusion.
    - val_size: Fraction of non-test patients assigned to validation when fix_test_split=True.
    - seed: Random seed for splitting (used only when fix_test_split=True).
    - legacy: If True, use SMART-specific outcome columns (edood_f, ebero_f, emi_f …)
        with the logic from compute_first_cd_event and drop rows with missing outcomes
        before computing targets.
    - censoring_time: Used only when legacy=True. Time assigned to patients/endpoints
        whose indicator is 2 (lost to follow-up). Required when any patient has a
        lost-to-FU indicator.

    Returns:
    - dataset: List of all patient records.
    - splits: Dict mapping split name → list of indices.
    """
    # Load smart.csv
    smart_df = pd.read_csv(smart_csv)
    n_raw = len(smart_df)

    # Check if data has raw outcome columns (e*_f) or pre-computed first_event
    if legacy:
        # Legacy mode: use SMART-specific column names, drop rows with missing outcomes
        smart_df = drop_rows_with_missing_smart_outcomes(smart_df)
        if censoring_time is None:
            ltfu_cols = [c for c in ["edoodvas", "ebero_n", "emi_n"] if c in smart_df.columns]
            n_ltfu = smart_df[ltfu_cols].isin([2]).any(axis=1).sum()
            if n_ltfu > 0:
                print(
                    f"  Note: {n_ltfu:,} patients have lost-to-FU indicator (value 2); "
                    f"using their recorded e*_f time as censoring time (--censoring_time not set)."
                )
        smart_df = compute_legacy_targets(smart_df, censoring_time=censoring_time)
    else:
        has_endpoint_cols = any(c.startswith("e") and c.endswith("_f") for c in smart_df.columns)

        if has_endpoint_cols:
            # Compute survival targets from outcome columns
            smart_df["first_event"] = smart_df.apply(compute_first_event, axis=1)
            smart_df["cd_event"] = smart_df.apply(compute_cd_event, axis=1)
            # Drop outcome columns from features (they must not leak into inputs)
            smart_df = drop_outcomes(smart_df)
        else:
            # Data already has first_event; ensure cd_event exists
            if "cd_event" not in smart_df.columns:
                # Without explicit censoring info, assume all patients had an event
                smart_df["cd_event"] = 1

    # Drop patients with no follow-up data or invalid IDs
    smart_df = smart_df[~smart_df["first_event"].isna()]
    smart_df = smart_df[smart_df["m3life_no"] >= 0]

    # Deduplicate: keep the row with the minimum first_event per patient
    smart_df = smart_df.loc[smart_df.groupby("m3life_no")["first_event"].idxmin()]

    # Apply exclusion window at the patient level: drop patients whose outcome
    # is within the window (i.e. first_event < exclusion_window days from baseline)
    if exclusion_window > 0:
        n_before = len(smart_df)
        smart_df = smart_df[smart_df["first_event"] >= exclusion_window]
        n_excluded = n_before - len(smart_df)
        if n_excluded:
            print(f"  Excluded {n_excluded:,} patients with first_event < {exclusion_window} days")

    n_total = len(smart_df)
    smart_df = smart_df.reset_index(drop=True)
    print(f"Patients: {n_raw:,} raw rows → {n_total:,} unique patients")

    # Drop SmrtRisk and every column that follows it in the original CSV order.
    # first_event and cd_event are computed targets appended after the raw columns,
    # so they must be explicitly preserved even though they sit beyond SmrtRisk.
    if "SmrtRisk" in smart_df.columns:
        always_keep = {"first_event", "cd_event", "m3life_no"}
        smrtrisk_idx = smart_df.columns.get_loc("SmrtRisk")
        cols_before = list(smart_df.columns[:smrtrisk_idx])
        cols_keep_after = [c for c in smart_df.columns[smrtrisk_idx:] if c in always_keep]
        n_dropped = len(smart_df.columns) - len(cols_before) - len(cols_keep_after)
        print(f"  Dropped {n_dropped} columns from SmrtRisk onwards (outcome-adjacent)")
        smart_df = smart_df[cols_before + cols_keep_after]

    # Columns that belong to smart (everything except m3life_no)
    smart_feature_cols = [c for c in smart_df.columns if c != "m3life_no"]

    # Load event CSVs, apply event-level filter
    event_frames = []
    for source, path in event_csvs.items():
        df = pd.read_csv(path)
        df = df[df["datediff"] < baseline_time].copy()
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
        first_event = row.get("first_event")
        patient_events = events_by_patient.get(pid, [])

        # Apply exclusion window: drop events too close to the outcome
        if exclusion_window > 0 and first_event is not None:
            patient_events = [
                e for e in patient_events
                if (first_event - e["datediff"]) >= exclusion_window
            ]

        record = {
            "m3life_no": pid,
            "smart": {
                k: (int(v) if isinstance(v, (int,)) else float(v) if isinstance(v, float) else v)
                for k, v in row.items() if k in smart_feature_cols
            },
            "events": patient_events,
        }
        dataset.append(record)

    # Load split assignments from JSON file
    with open(split_json) as f:
        split_pids = json.load(f)
    # Normalize "val" key to "validation"
    if "val" in split_pids and "validation" not in split_pids:
        split_pids["validation"] = split_pids.pop("val")

    pid_to_idx = {r["m3life_no"]: i for i, r in enumerate(dataset)}

    if not fix_test_split:
        # Use all splits exactly as provided in the JSON
        splits = {}
        for split_name, pids in split_pids.items():
            idxs = [pid_to_idx[pid] for pid in pids if pid in pid_to_idx]
            n_missing = len(pids) - len(idxs)
            if n_missing:
                print(f"  Warning: {n_missing} patients from '{split_name}' split not found in dataset (filtered out)")
            splits[split_name] = idxs
    else:
        # Fix test set from JSON; randomly split remaining patients into train/validation
        test_pids = set(int(p) for p in split_pids.get("test", []))
        test_idxs = [pid_to_idx[pid] for pid in test_pids if pid in pid_to_idx]
        n_missing = len(test_pids) - len(test_idxs)
        if n_missing:
            print(f"  Warning: {n_missing} test patients not found in dataset (filtered out)")

        rest_idxs = [i for i in range(len(dataset)) if dataset[i]["m3life_no"] not in test_pids]
        rest_events = [dataset[i]["smart"]["cd_event"] for i in rest_idxs]
        idx_train, idx_val = train_test_split(
            rest_idxs, test_size=val_size, random_state=seed, stratify=rest_events
        )
        splits = {"train": idx_train, "validation": idx_val, "test": test_idxs}

    # Save as split JSONL files
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    for split_name, idxs in splits.items():
        split_path = output_dir / f"{split_name}.jsonl"
        with open(split_path, "w") as f:
            for i in idxs:
                f.write(json.dumps(dataset[i]) + "\n")

    n_events = sum(1 for r in dataset if r["smart"]["cd_event"] == 1)
    print(f"Saved {len(dataset):,} patient records → {output_dir}/")
    print(f"  Events: {n_events:,} ({100*n_events/len(dataset):.1f}%) | Censored: {len(dataset)-n_events:,}")
    total_events = sum(len(p["events"]) for p in dataset)
    print(f"  Total longitudinal events across all patients: {total_events:,}")
    for split_name, idxs in splits.items():
        split_events = sum(1 for i in idxs if dataset[i]["smart"]["cd_event"] == 1)
        print(f"  {split_name:12s}: {len(idxs):5,} | events={split_events} ({100*split_events/len(idxs):.1f}%)")

    return dataset, splits

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
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the split JSONL files (train/val/test).")
    parser.add_argument("--split_json", type=str, required=True,
                        help="Path to a JSON file mapping split names (train/val/test) to lists of m3life_no.")
    parser.add_argument("--fix_test_split", action="store_true", default=False,
                        help="If set, use only the test split from --split_json and randomly resample "
                             "train/validation from the remaining patients.")
    parser.add_argument("--window_size", type=int, default=10, help="Size of each time bucket (same unit as datediff).")
    parser.add_argument("--windowed_output_dir", type=str, required=True, help="Directory to save the windowed split JSONL files.")
    parser.add_argument("--exclusion_window", type=int, default=0,
                        help="Exclude events within this many days of first_event. "
                             "E.g. 180 drops events whose temporal distance to outcome is < 180 days. Default: 0.")
    parser.add_argument("--val_size", type=float, default=0.15,
                        help="Fraction of non-test patients assigned to validation (used only with --fix_test_split).")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for splitting (used only with --fix_test_split).")
    parser.add_argument(
        "--legacy",
        action="store_true",
        default=False,
        help="Use SMART-specific outcome columns (edood_f, ebero_f, emi_f …) with the "
             "compute_first_cd_event logic. Rows with any missing outcome column are "
             "dropped before target computation.",
    )
    parser.add_argument(
        "--censoring_time",
        type=int,
        default=None,
        help="Time (in days) assigned to patients lost to follow-up (indicator == 2). "
             "Required when --legacy is set and any patient has a lost-to-FU indicator.",
    )

    args = parser.parse_args()

    # Generate event_csvs from the folder
    event_csvs = get_event_csvs(args.event_csv_folder)

    # Preprocess the dataset
    dataset, splits = preprocess_smart_ehr(
        args.smart_csv,
        event_csvs,
        args.baseline_time,
        args.output_dir,
        split_json=args.split_json,
        fix_test_split=args.fix_test_split,
        exclusion_window=args.exclusion_window,
        val_size=args.val_size,
        seed=args.seed,
        legacy=args.legacy,
        censoring_time=args.censoring_time,
    )

    # Apply time windows (per split)
    windowed_output_dir = Path(args.windowed_output_dir)
    windowed_output_dir.mkdir(parents=True, exist_ok=True)
    for split_name, idxs in splits.items():
        split_dataset = [dataset[i] for i in idxs]
        windowed_split = apply_time_windows(
            split_dataset,
            args.window_size,
            args.baseline_time,
            windowed_output_path=str(windowed_output_dir / f"{split_name}.jsonl"),
        )