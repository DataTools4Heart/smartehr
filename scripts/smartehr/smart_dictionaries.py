"""Human-readable enrichment of SMARTEHR field names and coded values.

Feeding raw coded column names (e.g. ``vgok_nie: 0.0``) to a text-embedding LLM
wastes its semantic prior — the token is near-arbitrary. This module maps field
names to their descriptions and coded values to their labels, using the dictionaries
already shipped in the repo:

  - EHR longitudinal columns:  data/smartehr/data_dicts/data_dict.csv  (column -> description)
  - coded VALUE maps:          lab.csv / meting.csv / echo.csv         (code -> readable name)
  - baseline SMART registry:   smart.csv (converted from SmartEPjan22dd12072023.xls;
                               var -> label; value -> label)

This is semantic labeling, not value transformation: no imputation, no
standardization — it only makes the recorded data legible. Missing fields
(including coded-missing baseline values, e.g. "Missend") are omitted.

``vgok_nie: 0.0``  ->  ``Voorgeschiedenis; nier-operatie: Nooit``
"""

import csv
from collections import Counter
from pathlib import Path

# Field keys (in the merged JSONL events) whose VALUE is itself a code, and the
# value-map that translates it. For these the translated value IS the concept, so we
# use a short static label instead of data_dict.csv's column note (which for these
# columns is a long data-curation comment, not a clean field name).
_VALUE_CODE_FIELDS = {
    "lab_testcode": "lab",
    "label": "meting",
    "MeasName_ECHO": "echo",
}
_VALUE_CODE_LABEL = {
    "lab_testcode": "Lab test",
    "label": "Measurement",
    "MeasName_ECHO": "Echo measurement",
}

# Clean short labels for the common structured companion fields, whose data_dict.csv
# descriptions are long curation notes rather than usable names.
_CLEAN_LABELS = {
    "lab_result": "Lab result", "lab_result_txt": "Lab result (text)",
    "lab_testunit": "Unit", "material": "Sample material",
    "data1": "Value", "data2": "Value 2", "data3": "Value 3", "eenheid": "Unit",
    "Value_ECHO": "Value", "UnitName_ECHO": "Unit",
    "med_genNaam": "Medication", "med_ZIatc": "ATC code", "klinisch": "Clinical",
    "med_duur": "Duration (days)",
    "diag_omschrijving": "Diagnosis", "verr_omschrijving": "Procedure", "OMSCHR": "Operation",
    "SpecialismeNaam": "Specialty", "specialisme_omschrijving": "Specialty", "title": "Title",
}

# Above this length a data_dict.csv "description" is really a curation note, not a
# label — fall back to the raw column code instead of injecting a paragraph.
_MAX_LABEL_LEN = 60

# Resolved value labels that actually mean "missing" — omit these (matches the
# builder's omit-missing policy for None/""/NaN).
_MISSING_LABELS = {"missend", "missing", "onbekend", "unknown"}


def _norm_val(v) -> str:
    """Normalize a value for matching against the xls Value column.

    Data values arrive as floats (0.0, 1.0, 9.0); the dictionary stores "0"/"1"/"9".
    Collapse integer-valued floats to their int string so they match.
    """
    s = str(v).strip()
    try:
        f = float(s)
        return str(int(f)) if f == int(f) else str(f)
    except (ValueError, TypeError):
        return s


def _fmt(v):
    return round(v, 4) if isinstance(v, float) else v


class SmartDictionary:
    def __init__(self, dict_dir: str):
        dict_dir = Path(dict_dir)
        self.col_desc: dict[str, str] = {}            # EHR column -> description
        self.value_maps: dict[str, dict[str, str]] = {}  # 'lab'/'meting'/'echo' -> {code: name}
        self.baseline_label: dict[str, str] = {}      # baseline var -> readable label
        self.baseline_valuelabel: dict[tuple, str] = {}  # (var, norm_value) -> value label

        self._load_data_dict(dict_dir / "data_dict.csv")
        self._load_value_map(dict_dir / "lab.csv", "lab", "lab_testcode", "Local Name")
        self._load_value_map(dict_dir / "meting.csv", "meting", "label", "explanation", fallback="Omschrijving")
        self._load_value_map(dict_dir / "echo.csv", "echo", "MeasName_ECHO", "Name")
        self._load_smart(dict_dir / "smart.csv")

        self.reset_stats()

    # ---- coverage stats ------------------------------------------------------
    def reset_stats(self):
        self.n_fields = 0            # non-missing fields passed to enrich()
        self.n_label_hit = 0         # got a human-readable label (not the raw code)
        self.n_value_translated = 0  # coded value mapped to a readable name/label
        self.n_value_omitted = 0     # coded-missing value dropped
        self.missed_labels = Counter()  # field names with no label mapping (kept as raw code)

    def coverage_report(self) -> dict:
        rendered = self.n_fields - self.n_value_omitted
        return {
            "fields_seen": self.n_fields,
            "label_hit": self.n_label_hit,
            "label_hit_pct": round(100 * self.n_label_hit / max(rendered, 1), 1),
            "values_translated": self.n_value_translated,
            "coded_missing_omitted": self.n_value_omitted,
            "distinct_unmapped_fields": len(self.missed_labels),
            "top_unmapped": self.missed_labels.most_common(15),
        }

    # ---- loading -------------------------------------------------------------
    def _load_data_dict(self, path: Path):
        if not path.exists():
            return
        with open(path, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                col = (r.get("column") or "").strip()
                desc = (r.get("Additional0_Info") or "").strip()
                if col and desc:
                    self.col_desc.setdefault(col, desc)

    def _load_value_map(self, path: Path, name: str, key_col: str, val_col: str, fallback: str | None = None):
        m: dict[str, str] = {}
        if path.exists():
            with open(path, encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    k = (r.get(key_col) or "").strip()
                    v = (r.get(val_col) or "").strip()
                    if not v and fallback:
                        v = (r.get(fallback) or "").strip()
                    if k and v:
                        m[k] = v
        self.value_maps[name] = m

    def _load_smart(self, path: Path):
        """Baseline SMART dictionary (smart.csv, converted from the SMART EP .xls)."""
        if not path.exists():
            return
        with open(path, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                var = (r.get("Var Name") or "").strip()
                if not var:
                    continue
                label = (r.get("VaR lab English") or "").strip() or (r.get("Variable Label") or "").strip()
                if label:
                    self.baseline_label.setdefault(var, label)
                val = (r.get("Value") or "").strip()
                vlab = (r.get("VaL lab English") or "").strip() or (r.get("Value Label") or "").strip()
                if val and vlab:
                    self.baseline_valuelabel[(var, _norm_val(val))] = vlab

    # ---- rendering -----------------------------------------------------------
    def _label_and_hit(self, key: str) -> tuple[str, bool]:
        if key in _VALUE_CODE_LABEL:
            return _VALUE_CODE_LABEL[key], True
        if key in _CLEAN_LABELS:
            return _CLEAN_LABELS[key], True
        desc = self.col_desc.get(key) or self.baseline_label.get(key)
        if desc:
            desc = desc.splitlines()[0].strip()
            if len(desc) <= _MAX_LABEL_LEN:
                return desc, True
        return key, False  # code is more compact than a paragraph-length curation note

    def label_for(self, key: str) -> str:
        return self._label_and_hit(key)[0]

    def _render_value(self, key, value) -> tuple[object, str]:
        """Return (rendered_value_or_None, status) where status is
        'translated' | 'plain' | 'omitted'."""
        if key in _VALUE_CODE_FIELDS:
            m = self.value_maps.get(_VALUE_CODE_FIELDS[key], {})
            code = str(value).strip()
            if code in m:
                return m[code], "translated"
            return _fmt(value), "plain"
        vlab = self.baseline_valuelabel.get((key, _norm_val(value)))
        if vlab is not None:
            if vlab.strip().lower() in _MISSING_LABELS:
                return None, "omitted"
            return vlab, "translated"
        return _fmt(value), "plain"

    def enrich(self, key: str, value) -> str | None:
        """Render one ``key: value`` pair as ``<label>: <readable value>``, updating
        coverage stats. Returns None when the value is a coded-missing indicator (omit).
        """
        self.n_fields += 1
        rendered, status = self._render_value(key, value)
        if status == "omitted":
            self.n_value_omitted += 1
            return None
        label, hit = self._label_and_hit(key)
        if hit:
            self.n_label_hit += 1
        else:
            self.missed_labels[key] += 1
        if status == "translated":
            self.n_value_translated += 1
        return f"{label}: {rendered}"
