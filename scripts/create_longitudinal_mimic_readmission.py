import init
import datetime
import duckdb
import argparse
import pandas as pd
import numpy as np
from dataset_utils.mimic import itemids_lab, itemids_chart
import os
from pathlib import Path


def load_readmission_data(mimic_db_path: str, notes_db_path: str, itemids_lab: list, itemids_chart: list):
    with duckdb.connect(mimic_db_path) as con, duckdb.connect(notes_db_path) as con2:
        lab = con.sql("""SELECT * FROM mimiciv_hosp.labevents""").df()
        lab_id = con.sql("""SELECT * FROM mimiciv_hosp.d_labitems""").df()
        adm = con.sql(f"""SELECT * FROM mimiciv_hosp.admissions""").df()
        patients = con.sql("""SELECT * FROM mimiciv_hosp.patients""").df()
        icustays = con.sql("""SELECT * FROM mimiciv_icu.icustays""").df()
        chartevents = con.sql("""SELECT * FROM mimiciv_icu.chartevents""").df()
        d_items = con.sql("""SELECT * FROM mimiciv_icu.d_items""").df()
        sofa = con.sql("""SELECT * FROM mimiciv_derived.sofa""").df()
        sapsii = con.sql("""SELECT * FROM mimiciv_derived.sapsii""").df()
        notes = con2.sql("""SELECT * FROM mimiciv_note.discharge""").df()

    icustays = icustays.merge(
        sofa.loc[:, ["stay_id", "sofa_24hours"]].groupby("stay_id", as_index=False).mean(), on="stay_id", how="inner"
    )
    icustays = icustays.merge(
        sapsii.loc[:, ["stay_id", "sapsii"]].groupby("stay_id", as_index=False).mean(), on="stay_id", how="inner"
    )
    data = adm.merge(notes, on="hadm_id", how="inner")
    data = data.rename({"subject_id_x": "subject_id"}, axis=1)
    data = data.merge(patients, on="subject_id", how="inner").merge(icustays, on="hadm_id", how="inner")
    data = data.rename({"subject_id_x": "subject_id"}, axis=1)
    data = data[data["admission_type"] != "ELECTIVE"]
    data = data.sort_values(["subject_id", "admittime"])
    data["next_admittime"] = data.groupby("subject_id").admittime.shift(-1)
    data["next_admission_type"] = data.groupby("subject_id").admission_type.shift(-1)
    data[["next_admittime", "next_admission_type"]] = data.groupby(["subject_id"])[
        ["next_admittime", "next_admission_type"]
    ].bfill()
    data["event"] = ~data["next_admittime"].isna()

    data.loc[data["next_admittime"].isna(), "next_admittime"] = data.loc[
        data["next_admittime"].isna(), "dischtime"
    ] + datetime.timedelta(days=365)
    data["days_next_admit"] = (data.next_admittime - data.dischtime).dt.total_seconds() / (24 * 60 * 60)
    data = data[data["days_next_admit"] <= 365]
    data = data[data["days_next_admit"] >= 0]

    data = data.loc[
        :,
        [
            "subject_id",
            "hadm_id",
            "text",
            "event",
            "days_next_admit",
            "admittime",
            "gender",
            "anchor_age",
            "marital_status",
            "insurance",
            "first_careunit",
            "last_careunit",
            "sapsii",
            "sofa_24hours",
        ],
    ]

    chartevents = chartevents[chartevents["itemid"].apply(lambda x: x in itemids_chart)]
    chartevents = chartevents.merge(d_items[["itemid", "label"]], on="itemid", how="left")
    chartevents["valuenum"] = chartevents["valuenum"].fillna(chartevents["value"])
    chartevents = chartevents.pivot_table(index="hadm_id", columns="itemid", values="value", aggfunc="first")
    chartevents.columns = [d_items.loc[d_items["itemid"] == col, "label"].values[0] for col in chartevents.columns]
    chartevents.reset_index(inplace=True)

    lab = lab[lab["itemid"].apply(lambda x: x in itemids_lab)]
    lab = lab.merge(lab_id[["itemid", "label"]], on="itemid", how="left")
    lab["value"] = lab["valuenum"].fillna(lab["value"])
    lab = lab.pivot_table(index="hadm_id", columns="itemid", values="value", aggfunc="first")
    lab.columns = [lab_id.loc[lab_id["itemid"] == col, "label"].values[0] for col in lab.columns]
    lab.reset_index(inplace=True)
    data = lab.merge(chartevents, on="hadm_id", how="inner").merge(data, on="hadm_id", how="inner")

    data["Temperature Fahrenheit"] = (data["Temperature Fahrenheit"].astype(float) - 32) * 5 / 9
    data["Temperature Celsius"] = data["Temperature Celsius"].fillna(data["Temperature Fahrenheit"])
    data["Temperature Celsius"] = data["Temperature Celsius"].astype(float).round(1)
    data = data.drop("Temperature Fahrenheit", axis=1)

    more_than_one_entry_subjects = data.groupby("subject_id").size()
    more_than_one_entry_subjects = more_than_one_entry_subjects[more_than_one_entry_subjects > 1].index
    data = data[(data["subject_id"].isin(more_than_one_entry_subjects))]
    data = data.sort_values(["subject_id", "admittime"])

    cols = data.columns.tolist()
    cols.remove("subject_id")
    cols = ["subject_id"] + cols
    data = data[cols]
    return data


def save_readmission_data(readmission_path: str, readmission_data: pd.DataFrame):
    unique_subjects = readmission_data["subject_id"].unique()
    n = len(unique_subjects)
    test_size = int(n * 0.2)
    train_size = int((n - test_size) * 0.8)
    splits = np.array(["test"] * test_size + ["train"] * train_size + ["val"] * (n - test_size - train_size))
    np.random.seed(42)
    np.random.shuffle(splits)

    # Create mapping of subject_id to split
    subject_to_split = dict(zip(unique_subjects, splits))

    # Add split column by mapping from subject_id
    readmission_data.loc[:, "split"] = readmission_data["subject_id"].map(subject_to_split)
    readmission_path = Path(readmission_path)
    os.makedirs(readmission_path, exist_ok=True)
    readmission_data.to_csv(readmission_path / "longitudinal_mimic_readmission.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load readmission data from MIMIC database.")
    parser.add_argument("--mimic-db-path", type=str, required=True, help="Path to the MIMIC-IV duckdb database.")
    parser.add_argument("--notes-db-path", type=str, required=True, help="Path to the MIMIC-IV Notes duckdb database.")
    parser.add_argument("--out-path", type=str, required=True, help="Path to save the readmission data.")
    args = parser.parse_args()

    readmission_data = load_readmission_data(args.mimic_db_path, args.notes_db_path, itemids_lab, itemids_chart)
    save_readmission_data(args.out_path, readmission_data)
