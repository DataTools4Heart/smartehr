import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


PRIMARY_PATIENT_KEY_CANDIDATES = (
    "m3life_no",
    "m3life_no",
    "m3life_no",
    "m3life_no",
)


@dataclass
class TranslationStats:
    replaced_values: int = 0
    passthrough_values: int = 0
    unmapped_coded_values: int = 0


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if text.lower() in {"na", "nan", "none", ""}:
        return ""
    return text


def canonical_source_name(stem: str) -> str:
    return re.sub(r"_\d{8}$", "", stem.lower())


def load_fixture_columns(columns_dir: Path) -> dict[str, list[str]]:
    file_columns: dict[str, list[str]] = {}
    for path in sorted(columns_dir.glob("*.txt")):
        columns = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        file_columns[path.stem] = columns
    return file_columns


def load_data_dictionary(data_dict_csv: Path) -> pd.DataFrame:
    return pd.read_csv(data_dict_csv, low_memory=False)


def build_column_description_map(data_dict_df: pd.DataFrame) -> dict[tuple[str, str], str]:
    description_map: dict[tuple[str, str], str] = {}
    for _, row in data_dict_df.iterrows():
        filename = normalize_text(row.get("filename"))
        column = normalize_text(row.get("column"))
        if not filename or not column:
            continue
        description = normalize_text(row.get("Additional0_Info"))
        if not description:
            description = normalize_text(row.get("class"))
        if description:
            description_map[(filename.lower(), column.lower())] = description
    return description_map


def load_code_map(path: Path, key_col: str, value_col: str, fallback_col: str | None = None) -> dict[str, str]:
    if not path.exists():
        return {}
    df = pd.read_csv(path, low_memory=False)
    mapping: dict[str, str] = {}
    for _, row in df.iterrows():
        key = normalize_text(row.get(key_col))
        if not key:
            continue
        value = normalize_text(row.get(value_col))
        if not value and fallback_col is not None:
            value = normalize_text(row.get(fallback_col))
        if value:
            mapping[key] = value
    return mapping


def build_code_mappings(data_dicts_dir: Path) -> dict[str, dict[str, str]]:
    return {
        "lab_testcode": load_code_map(data_dicts_dir / "lab.csv", "lab_testcode", "Local Name"),
        "label": load_code_map(data_dicts_dir / "meting.csv", "label", "explanation", fallback_col="Omschrijving"),
        "measname_echo": load_code_map(data_dicts_dir / "echo.csv", "MeasName_ECHO", "Name"),
    }


def get_patient_key_column(df: pd.DataFrame) -> str | None:
    by_lower = {c.lower(): c for c in df.columns}
    for candidate in PRIMARY_PATIENT_KEY_CANDIDATES:
        if candidate in by_lower:
            return by_lower[candidate]
    for col in df.columns:
        if col.lower().replace("_", "") == "m3lifeno":
            return col
    return None


def build_file_description_map(data_dict_df: pd.DataFrame) -> dict[str, str]:
    file_desc_map: dict[str, str] = {}
    for _, row in data_dict_df.iterrows():
        filename = normalize_text(row.get("filename"))
        if not filename:
            continue
        current = file_desc_map.get(filename.lower(), "")
        incoming = normalize_text(row.get("Data table type"))
        if not current and incoming:
            file_desc_map[filename.lower()] = incoming
    return file_desc_map


def infer_link_hints(file_columns: dict[str, list[str]]) -> dict[str, Any]:
    per_file = {}
    for stem, cols in file_columns.items():
        per_file[stem] = {
            "join_key": "m3life_no",
            "has_datediff": "datediff" in {c.lower() for c in cols},
            "extra_keys": [c for c in cols if c.lower() in {"hos_nr", "datediff"}],
        }

    cross_file_links = [
        {
            "files": ["hos_20251209", "hos_mut_20251209"],
            "keys": ["m3life_no", "hos_nr"],
            "reason": "hos_mut extends hospitalization rows from hos with specialty/location details",
        },
        {
            "files": ["ok_20250626", "ok_verslag_20250626"],
            "keys": ["m3life_no", "datediff"],
            "reason": "operation metadata and operation report answers align at patient+time level",
        },
    ]
    return {
        "primary_join_key": "m3life_no",
        "per_file": per_file,
        "cross_file_links": cross_file_links,
    }


def value_mapping_for_column(code_mappings: dict[str, dict[str, str]], column: str) -> dict[str, str] | None:
    return code_mappings.get(column.lower())


def get_column_description(
    column_descriptions: dict[tuple[str, str], str],
    source_filename: str,
    column: str,
) -> str:
    key = (source_filename.lower(), column.lower())
    return column_descriptions.get(key, column)


def translate_value(
    source_filename: str,
    column: str,
    value: Any,
    code_mappings: dict[str, dict[str, str]],
    stats: TranslationStats,
    unmapped_details: set[str],
) -> str:
    text = normalize_text(value)
    if not text:
        return ""

    mapping = value_mapping_for_column(code_mappings, column)
    if mapping is None:
        stats.passthrough_values += 1
        return text

    translated = mapping.get(text)
    if translated:
        stats.replaced_values += 1
        return translated

    stats.unmapped_coded_values += 1
    unmapped_details.add(f"{source_filename}:{column}:{text}")
    return text


def compute_coverage_report(
    file_columns: dict[str, list[str]],
    column_descriptions: dict[tuple[str, str], str],
    code_mappings: dict[str, dict[str, str]],
) -> dict[str, Any]:
    total_columns = 0
    described_columns = 0
    missing_column_descriptions: list[str] = []
    mapped_code_columns: list[str] = []
    missing_code_mapping_columns: list[str] = []

    for stem, columns in file_columns.items():
        source_filename = f"{stem}.csv"
        for column in columns:
            total_columns += 1
            desc = column_descriptions.get((source_filename.lower(), column.lower()))
            if desc:
                described_columns += 1
            else:
                missing_column_descriptions.append(f"{stem}.{column}")

            mapping = value_mapping_for_column(code_mappings, column)
            if mapping is not None:
                mapped_code_columns.append(f"{stem}.{column}")
            elif column.lower() in {"med_ziatc", "sourcetype", "klinisch", "status", "type_brief"}:
                missing_code_mapping_columns.append(f"{stem}.{column}")

    return {
        "column_description_coverage": {
            "total_columns": total_columns,
            "with_description": described_columns,
            "without_description": sorted(set(missing_column_descriptions)),
        },
        "code_mapping_coverage": {
            "mapped_code_columns": sorted(set(mapped_code_columns)),
            "missing_code_mapping_columns": sorted(set(missing_code_mapping_columns)),
            "available_mapping_sizes": {
                "lab_testcode": len(code_mappings.get("lab_testcode", {})),
                "label": len(code_mappings.get("label", {})),
                "MeasName_ECHO": len(code_mappings.get("measname_echo", {})),
            },
        },
    }


def patient_rows_from_csv(path: Path, patient_id: str) -> tuple[pd.DataFrame | None, str | None]:
    df = pd.read_csv(path, low_memory=False)
    key_col = get_patient_key_column(df)
    if key_col is None:
        return None, None

    patient_series = df[key_col].astype(str).str.strip()
    mask = patient_series == str(patient_id)
    return df.loc[mask].copy(), key_col


def row_to_text(
    source_stem: str,
    row: pd.Series,
    source_filename: str,
    key_col: str,
    column_descriptions: dict[tuple[str, str], str],
    code_mappings: dict[str, dict[str, str]],
    stats: TranslationStats,
    unmapped_details: set[str],
) -> str:
    datediff_value = normalize_text(row.get("datediff"))
    time_prefix = f"t={datediff_value}" if datediff_value else "t=unknown"

    parts = []
    for col, value in row.items():
        if col == key_col:
            continue
        if normalize_text(value) == "":
            continue
        translated = translate_value(source_filename, col, value, code_mappings, stats, unmapped_details)
        col_desc = get_column_description(column_descriptions, source_filename, col)
        parts.append(f"{col_desc}: {translated}")

    if not parts:
        return ""
    return f"[{source_stem}] {time_prefix} | " + "; ".join(parts)


def build_patient_narrative(
    ehr_data_dir: Path,
    patient_id: str,
    file_columns: dict[str, list[str]],
    column_descriptions: dict[tuple[str, str], str],
    code_mappings: dict[str, dict[str, str]],
    max_rows_per_file: int,
) -> tuple[str, dict[str, Any]]:
    lines = [f"Patient m3life_no={patient_id}"]
    stats = TranslationStats()
    unmapped_details: set[str] = set()
    rows_seen = 0
    files_with_rows = 0
    skipped_files: list[str] = []

    for stem in sorted(file_columns.keys()):
        csv_path = ehr_data_dir / f"{stem}.csv"
        if not csv_path.exists():
            skipped_files.append(stem)
            continue

        patient_rows, key_col = patient_rows_from_csv(csv_path, patient_id)
        if patient_rows is None or key_col is None:
            skipped_files.append(stem)
            continue
        if patient_rows.empty:
            continue

        files_with_rows += 1
        if "datediff" in patient_rows.columns:
            patient_rows = patient_rows.sort_values("datediff")
        patient_rows = patient_rows.head(max_rows_per_file)

        source_filename = csv_path.name
        lines.append(f"\nSource: {stem} ({len(patient_rows)} rows)")
        for _, row in patient_rows.iterrows():
            text_row = row_to_text(
                source_stem=stem,
                row=row,
                source_filename=source_filename,
                key_col=key_col,
                column_descriptions=column_descriptions,
                code_mappings=code_mappings,
                stats=stats,
                unmapped_details=unmapped_details,
            )
            if text_row:
                lines.append(f"- {text_row}")
                rows_seen += 1

    narrative = "\n".join(lines)
    runtime_report = {
        "files_with_patient_rows": files_with_rows,
        "rows_rendered": rows_seen,
        "translation_stats": {
            "replaced_values": stats.replaced_values,
            "passthrough_values": stats.passthrough_values,
            "unmapped_coded_values": stats.unmapped_coded_values,
        },
        "unmapped_coded_value_examples": sorted(unmapped_details)[:100],
        "skipped_or_missing_files": sorted(skipped_files),
    }
    return narrative, runtime_report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert structured SmartEHR records to plain text and report mapping coverage."
    )
    parser.add_argument(
        "--columns-dir",
        type=Path,
        default=Path("tests/fixtures/smartehr_columns"),
        help="Folder with extracted column names per source file.",
    )
    parser.add_argument(
        "--data-dicts-dir",
        type=Path,
        default=Path("data/smartehr/data_dicts"),
        help="Folder containing data_dict.csv and optional code dictionaries (lab.csv, meting.csv, echo.csv).",
    )
    parser.add_argument(
        "--ehr-data-dir",
        type=Path,
        default=None,
        help="Folder containing the real EHR CSV files (optional).",
    )
    parser.add_argument(
        "--patient-id",
        type=str,
        default=None,
        help="Patient m3life_no to render as plain text (requires --ehr-data-dir).",
    )
    parser.add_argument(
        "--output-text",
        type=Path,
        default=Path("outputs/smartehr_patient_plaintext.txt"),
        help="Where to write the generated patient text.",
    )
    parser.add_argument(
        "--output-report",
        type=Path,
        default=Path("outputs/smartehr_mapping_report.json"),
        help="Where to write mapping/linkage coverage report.",
    )
    parser.add_argument(
        "--max-rows-per-file",
        type=int,
        default=50,
        help="Upper bound on rendered rows per source when building patient text.",
    )
    args = parser.parse_args()

    if not args.columns_dir.exists():
        raise FileNotFoundError(f"columns dir not found: {args.columns_dir}")
    if not args.data_dicts_dir.exists():
        raise FileNotFoundError(f"data dicts dir not found: {args.data_dicts_dir}")

    file_columns = load_fixture_columns(args.columns_dir)
    data_dict_df = load_data_dictionary(args.data_dicts_dir / "data_dict.csv")
    column_descriptions = build_column_description_map(data_dict_df)
    code_mappings = build_code_mappings(args.data_dicts_dir)

    report: dict[str, Any] = {
        "link_hints": infer_link_hints(file_columns),
        "source_files": sorted(file_columns.keys()),
    }
    report.update(compute_coverage_report(file_columns, column_descriptions, code_mappings))

    if args.ehr_data_dir is not None and args.patient_id is not None:
        narrative, runtime_report = build_patient_narrative(
            ehr_data_dir=args.ehr_data_dir,
            patient_id=args.patient_id,
            file_columns=file_columns,
            column_descriptions=column_descriptions,
            code_mappings=code_mappings,
            max_rows_per_file=args.max_rows_per_file,
        )
        args.output_text.parent.mkdir(parents=True, exist_ok=True)
        args.output_text.write_text(narrative, encoding="utf-8")
        report["patient_rendering"] = runtime_report
        report["patient_text_output"] = str(args.output_text)
    else:
        report["patient_rendering"] = {
            "status": "skipped",
            "reason": "Provide both --ehr-data-dir and --patient-id to render patient plain text.",
        }

    args.output_report.parent.mkdir(parents=True, exist_ok=True)
    args.output_report.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Report written to: {args.output_report}")
    if "patient_text_output" in report:
        print(f"Patient text written to: {report['patient_text_output']}")


if __name__ == "__main__":
    main()