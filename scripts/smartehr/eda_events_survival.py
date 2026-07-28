"""EDA for baseline-free (no-SMART) 15-year survival prediction from event CSVs.

Question this answers: can we predict 15y risk from the raw EHR event stream alone,
with NO manually extracted SMART baseline variables? Before modelling we need to know
whether the events can even support that, so this reports:

  §1 Cohort + 15y target feasibility  — is 15 years of follow-up actually there?
  §2 Event coverage                   — how many patients have NO events at all?
                                        (with no baseline they are unrankable: the
                                        structural ceiling on achievable C-index)
  §3 Per-CSV inventory                — every event CSV: columns, types, missingness,
                                        numeric/categorical/free-text, datediff span
  §4 Merge-collision audit            — data silently lost by the pipeline's same-day
                                        merge (shared column names across CSVs; several
                                        rows on one day collapsing to the last value)
  §5 Leakage audit                    — post-baseline rows, outcome-ish columns, events
                                        after first_event, suspiciously strong features
  §6 Univariate signal screen         — Harrell's C of simple event-derived features, so
                                        we learn if ANY prognostic signal exists before
                                        training a single model
  §7 Text budget                      — chars/tokens per patient, vocabulary size, for
                                        sizing the TF-IDF and LLM-embedding arms

Runs on the remote VM with only pandas + numpy. All CSVs are streamed in chunks, so
multi-million-row lab/med files are fine.

LANDMARKING (--landmark-days). Most rows in these CSVs are POST-baseline, and they are
not automatically unusable — but admitting them requires moving the prediction origin,
not just the feature cutoff. `--landmark-days 180` does all three parts together:

  1. features may use events with datediff < 180 (so post-baseline up to 6 months),
  2. patients whose outcome occurred at/before day 180 are EXCLUDED — otherwise their
     features would describe their own outcome (its admission, imaging, medication),
  3. survival is measured FROM day 180, so horizons are landmark-relative.

Doing (1) without (2) and (3) is the classic leak: it also makes "few post-baseline
events" a proxy for "died early". §5 asserts the invariant that zero feature events are
dated at/after a patient's own outcome; it must print 0.

Run several landmarks (0 / 90 / 180) and compare §6: a signal that appears only at the
longest landmark is more likely outcome contamination than prognosis, so the landmark
sensitivity curve doubles as a leakage detector.

PRIVACY: no raw free text, no row-level values, and no rare category values are ever
written to the report. Any value or term is shown only if it occurs in at least
--min-show-count patients/rows (default 20), so nothing patient-identifying is emitted.

    python scripts/smartehr/eda_events_survival.py \
        --smart-csv <smart.csv> --event-csv-folder <folder_with_ALL_event_csvs> \
        --split-json <splits.json> --legacy --landmark-days 180 --out-dir eda_out_lm180

Then paste eda_out/eda_report.md back into the chat.
"""

import argparse
import gc
import json
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from smartehr_pipeline import (  # reuse the EXACT target definition the pipeline uses
    compute_cd_event,
    compute_first_event,
    compute_legacy_targets,
    drop_rows_with_missing_smart_outcomes,
)

ID = "m3life_no"
TIME = "datediff"
CHUNK = 200_000
SAMPLE_CAP = 300_000       # reservoir cap for quantile estimation
DISTINCT_CAP = 20_000      # stop growing per-column value sets beyond this

# Column names that would be alarming as *inputs* (outcome-adjacent / absolute dates)
LEAK_PAT = re.compile(
    r"(dood|overl|sterf|death|mort|obiit|bero|stroke|cva|infarct|myoc|"
    r"^e[a-z]*_(f|n|s)$|smrtrisk|outcome|endpoint|event_date|datum|date)",
    re.I,
)
DATE_VAL_PAT = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
WORD_PAT = re.compile(r"[a-zA-Zà-üÀ-Ü]{2,}")


# ---------------------------------------------------------------- survival helpers

def harrell_c(time, event, risk):
    """Harrell's C-index. Higher risk should mean shorter time. Ignores NaN risks.

    Only patients with an observed event can open a comparable pair, so the loop is
    over events with a vectorized inner comparison — fast even for large cohorts.
    """
    time, event, risk = np.asarray(time, float), np.asarray(event, int), np.asarray(risk, float)
    ok = ~np.isnan(risk)
    time, event, risk = time[ok], event[ok], risk[ok]
    if len(time) < 10 or event.sum() == 0:
        return None, 0
    num = den = 0.0
    for i in np.where(event == 1)[0]:
        comp = time > time[i]
        n_comp = int(comp.sum())
        if not n_comp:
            continue
        rj = risk[comp]
        num += float((risk[i] > rj).sum()) + 0.5 * float((risk[i] == rj).sum())
        den += n_comp
    if den == 0:
        return None, 0
    return num / den, int(den)


def effective_n_tests(X, frac=0.95):
    """Number of INDEPENDENT tests among correlated features: PCs reaching `frac` variance.

    last/mean/slope/count of one code are near-duplicates, so a nominal 532 features may be
    only ~250 independent tests. Multiple-testing expectations and Bonferroni thresholds
    must use this, or "0 features cleared the floor" gets compared against a false
    expectation and looks anomalous when it is not.
    """
    A = np.asarray(X, float)
    A = A[:, np.isfinite(A).all(axis=0)] if A.ndim == 2 else A
    if A.ndim != 2 or A.shape[1] < 2:
        return max(A.shape[1] if A.ndim == 2 else 1, 1)
    sd = A.std(axis=0)
    sd[sd < 1e-12] = 1.0
    R = np.nan_to_num(np.corrcoef(((A - A.mean(axis=0)) / sd).T), nan=0.0)
    lam = np.sort(np.clip(np.linalg.eigvalsh(R), 0, None))[::-1]
    if lam.sum() <= 0:
        return A.shape[1]
    return int(np.searchsorted(np.cumsum(lam) / lam.sum(), frac) + 1)


def calibrate_null_scale(time, event, n_perm=200, seed=0):
    """Empirical null scale k, where SE(C) ~= k / sqrt(n_events).

    The analytic sqrt(0.25/n_events) (k=0.5) is far too wide under heavy censoring: at
    ~14% events only ~1 in 400 pure-noise features clears its 2-SE band instead of the
    expected ~5%, so a too-strict floor discards real signal. Measuring k by permutation
    on the actual (time, event) pattern fixes that; it comes out near 0.32 here.
    """
    rng = np.random.default_rng(seed)
    cs = []
    for _ in range(n_perm):
        c, _ = harrell_c(time, event, rng.normal(size=len(time)))
        if c is not None:
            cs.append(c)
    ev = max(int(np.asarray(event).sum()), 1)
    if len(cs) < 20:
        return 0.5
    return float(np.std(cs, ddof=1) * math.sqrt(ev))


def null_floor(k, n_events, n_sigma=2.0):
    """|C-0.5| threshold for a feature whose subcohort contains n_events events."""
    return n_sigma * k / math.sqrt(max(int(n_events), 1))


def km_survival(time, event, eval_times):
    """Kaplan-Meier S(t) at eval_times (plain numpy)."""
    time, event = np.asarray(time, float), np.asarray(event, int)
    order = np.argsort(time)
    time, event = time[order], event[order]
    surv, out, n = 1.0, [], len(time)
    uniq = np.unique(time[event == 1])
    ui = 0
    for et in eval_times:
        while ui < len(uniq) and uniq[ui] <= et:
            t = uniq[ui]
            at_risk = int((time >= t).sum())
            d = int(((time == t) & (event == 1)).sum())
            if at_risk > 0:
                surv *= 1.0 - d / at_risk
            ui += 1
        out.append(surv)
    return out


def apply_censoring(t, e, horizon):
    if e == 0:
        return float(min(t, horizon)), 0
    return (float(t), 1) if t <= horizon else (float(horizon), 0)


def q(vals, ps=(0, 5, 25, 50, 75, 95, 100)):
    if not len(vals):
        return {}
    a = np.asarray(vals, float)
    a = a[~np.isnan(a)]
    if not len(a):
        return {}
    return {f"p{p}": round(float(np.percentile(a, p)), 2) for p in ps}


class Reservoir:
    """Fixed-memory sample for quantiles over a stream."""

    def __init__(self, cap=SAMPLE_CAP, seed=0):
        self.cap, self.n, self.buf, self.rng = cap, 0, [], random.Random(seed)

    def add_many(self, values):
        for v in values:
            self.n += 1
            if len(self.buf) < self.cap:
                self.buf.append(v)
            else:
                j = self.rng.randint(0, self.n - 1)
                if j < self.cap:
                    self.buf[j] = v

    def quantiles(self, ps=(0, 5, 25, 50, 75, 95, 100)):
        return q(self.buf, ps)


# ---------------------------------------------------------------- per-column accumulator

class ColStats:
    def __init__(self, name, forced_text=False):
        self.name = name
        self.forced_text = forced_text
        self.n_rows = 0
        self.n_missing = 0
        self.distinct = set()
        self.distinct_capped = False
        self.counts = Counter()
        self.counts_capped = False
        self.is_numeric_dtype = False
        self.num_n = 0
        self.num_sum = 0.0
        self.num_sumsq = 0.0
        self.num_min = math.inf
        self.num_max = -math.inf
        self.num_res = Reservoir()
        self.len_res = Reservoir()
        self.word_res = Reservoir()
        self.len_sum = 0
        self.n_text_nonempty = 0
        self.n_datelike = 0
        self.patients = set()
        self.patients_capped = False

    def update(self, series, pids):
        self.n_rows += len(series)
        isna = series.isna()
        self.n_missing += int(isna.sum())
        vals = series[~isna]
        if len(pids) and len(vals):
            if not self.patients_capped:
                self.patients.update(pids[~isna].tolist())
                if len(self.patients) > 2_000_000:
                    self.patients_capped = True
        if not len(vals):
            return
        if pd.api.types.is_numeric_dtype(series):
            self.is_numeric_dtype = True
            a = vals.to_numpy(float)
            self.num_n += len(a)
            self.num_sum += float(a.sum())
            self.num_sumsq += float((a * a).sum())
            self.num_min = min(self.num_min, float(a.min()))
            self.num_max = max(self.num_max, float(a.max()))
            self.num_res.add_many(a.tolist())
        else:
            s = vals.astype(str)
            lens = s.str.len()
            self.len_sum += int(lens.sum())
            self.len_res.add_many(lens.tolist())
            self.word_res.add_many((s.str.count(r"\s+") + 1).tolist())
            self.n_text_nonempty += int((s.str.strip() != "").sum())
            self.n_datelike += int(s.str.contains(DATE_VAL_PAT, regex=True, na=False).sum())
        if not self.distinct_capped:
            self.distinct.update(vals.astype(str).unique().tolist())
            if len(self.distinct) > DISTINCT_CAP:
                self.distinct_capped = True
                self.distinct = set(list(self.distinct)[:DISTINCT_CAP])
        if not self.counts_capped:
            vc = vals.astype(str).value_counts()
            if len(self.counts) < 50_000:
                self.counts.update(vc.to_dict())
            else:
                self.counts_capped = True

    def kind(self):
        """numeric | numeric_discrete | free_text | categorical | empty

        Free text is detected by LENGTH + WORD COUNT rather than uniqueness: a code or
        label ("Cardiologie", "C07AB") is short and single-token, while any real report
        is multi-word. Uniqueness alone misfires on templated reports that repeat.
        """
        if self.forced_text:
            return "free_text"
        if self.n_rows == self.n_missing:
            return "empty"
        if self.is_numeric_dtype:
            nd = len(self.distinct)
            return "numeric_discrete" if (not self.distinct_capped and nd <= 15) else "numeric"
        lq = self.len_res.quantiles((50, 95))
        med, p95 = lq.get("p50", 0), lq.get("p95", 0)
        med_words = self.word_res.quantiles((50,)).get("p50", 1)
        if (med >= 20 or p95 >= 60) and med_words >= 3:
            return "free_text"
        return "categorical"

    def summary(self, min_show):
        n_present = self.n_rows - self.n_missing
        d = {
            "kind": self.kind(),
            "missing_pct": round(100 * self.n_missing / max(self.n_rows, 1), 1),
            "n_present": n_present,
            "n_patients": (f">{len(self.patients)}" if self.patients_capped else len(self.patients)),
            "n_distinct": (f">={DISTINCT_CAP}" if self.distinct_capped else len(self.distinct)),
        }
        if self.n_datelike:
            d["rows_with_iso_date"] = self.n_datelike
        k = d["kind"]
        if k in ("numeric", "numeric_discrete") and self.num_n:
            mean = self.num_sum / self.num_n
            var = max(self.num_sumsq / self.num_n - mean * mean, 0.0)
            d["mean"] = round(mean, 3)
            d["std"] = round(math.sqrt(var), 3)
            d["min"] = round(self.num_min, 3)
            d["max"] = round(self.num_max, 3)
            d["quantiles"] = self.num_res.quantiles((5, 50, 95))
        if not self.is_numeric_dtype and n_present:
            # emitted for free_text AND categorical, so a misclassified text column is visible
            d["char_len"] = self.len_res.quantiles((50, 95, 100))
            d["median_words"] = self.word_res.quantiles((50,)).get("p50")
            d["total_chars"] = self.len_sum
            d["est_tokens"] = int(self.len_sum / 4)
            d["n_nonempty"] = self.n_text_nonempty
        if k in ("categorical", "numeric_discrete"):
            top = [(v, c) for v, c in self.counts.most_common(12) if c >= min_show]
            d["top_values"] = top or f"(all values occur <{min_show}x — withheld)"
        return d


# ---------------------------------------------------------------- CSV scanning

def scan_csv(path, min_show, want_text_terms, forced_text=(), origin=0):
    """Stream one event CSV; return column stats, per-patient aggregates, dup info."""
    head = pd.read_csv(path, nrows=0)
    cols = list(head.columns)
    has_id, has_time = ID in cols, TIME in cols
    stem = Path(path).stem

    def _forced(c):
        return c in forced_text or f"{stem}.{c}" in forced_text

    stats = {c: ColStats(c, _forced(c)) for c in cols if c not in (ID, TIME)}
    dd_res, dd_min, dd_max = Reservoir(), math.inf, -math.inf
    n_rows = n_post_baseline = 0
    patients = set()
    rows_per_patient = Counter()
    day_keys = Counter()          # (pid, datediff) -> n rows  (same-day collapse, all rows)
    day_keys_pre = Counter()      # ... restricted to pre-baseline rows (what the pipeline merges)
    per_patient_days = defaultdict(set)
    text_chars = Counter()        # pid -> chars in columns classified free_text
    str_chars = Counter()         # pid -> chars in ANY string column (fallback for §7)
    numeric_last = defaultdict(dict)   # pid -> {col: (datediff, value)}
    term_patients = defaultdict(set)   # term -> pids (capped)

    # first pass to classify columns cheaply (types need data)
    probe = pd.read_csv(path, nrows=min(50_000, CHUNK), low_memory=False)
    for c in stats:
        if c in probe.columns:
            stats[c].update(probe[c], probe[ID] if has_id else pd.Series(dtype=float))
    probe_kinds = {c: s.kind() for c, s in stats.items()}
    text_cols = [c for c, k in probe_kinds.items() if k == "free_text"]
    num_cols = [c for c, k in probe_kinds.items() if k in ("numeric", "numeric_discrete")]
    # any string column is streamed for the text budget, even if classified categorical,
    # so §7 can report a fallback total and never look like "no text exists"
    str_cols = [c for c, k in probe_kinds.items() if k in ("free_text", "categorical")]
    # reset: the probe rows are re-counted in the full stream below
    stats = {c: ColStats(c, _forced(c)) for c in stats}

    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False):
        n_rows += len(chunk)
        pids = chunk[ID] if has_id else pd.Series([np.nan] * len(chunk))
        if has_id:
            patients.update(pids.dropna().astype("int64").tolist())
            rows_per_patient.update(pids.dropna().astype("int64").tolist())
        # PRE-BASELINE MASK: every FEATURE aggregate below must use only rows the model is
        # allowed to see (datediff < origin). Post-baseline rows are the outcome window —
        # using them would leak the future. Descriptive column stats still cover all rows.
        if has_time:
            dd = pd.to_numeric(chunk[TIME], errors="coerce")
            pre = dd.notna() & (dd < origin)
            valid = dd.dropna()
            if len(valid):
                dd_min, dd_max = min(dd_min, float(valid.min())), max(dd_max, float(valid.max()))
                dd_res.add_many(valid.tolist())
                n_post_baseline += int((valid >= origin).sum())
            if has_id:
                pair = pd.Series(list(zip(pids.tolist(), dd.tolist())))
                day_keys.update(pair.value_counts().to_dict())
                ppre, dpre = pids[pre], dd[pre]
                if len(ppre):
                    day_keys_pre.update(pd.Series(list(zip(ppre.tolist(), dpre.tolist())))
                                        .value_counts().to_dict())
                for p, d in zip(ppre.tolist(), dpre.tolist()):
                    if not (pd.isna(p) or pd.isna(d)):
                        per_patient_days[int(p)].add(int(d))
        else:
            pre = pd.Series(False, index=chunk.index)
        for c, st in stats.items():
            if c in chunk.columns:
                st.update(chunk[c], pids)
        # per-patient text volume + vocabulary (pre-baseline rows only)
        if has_id and str_cols and pre.any():
            for c in str_cols:
                if c not in chunk.columns:
                    continue
                s = chunk[c][pre].dropna().astype(str)
                if not len(s):
                    continue
                sub = pids.loc[s.index]
                is_text = c in text_cols
                # aggregate char counts per patient with groupby (per-row Python would
                # crawl on multi-million-row lab/med files)
                agg = pd.DataFrame({"p": sub.to_numpy(), "n": s.str.len().to_numpy()}).dropna()
                if len(agg):
                    for p, n in agg.groupby("p")["n"].sum().items():
                        str_chars[int(p)] += int(n)
                        if is_text:
                            text_chars[int(p)] += int(n)
                if not is_text:
                    continue
                if want_text_terms and len(term_patients) < 200_000:
                    for p, txt in zip(sub.tolist(), s.tolist()):
                        if pd.isna(p):
                            continue
                        for w in set(WORD_PAT.findall(txt.lower())):
                            if len(term_patients) < 200_000 or w in term_patients:
                                term_patients[w].add(int(p))
        # per-patient last numeric value: the most recent PRE-baseline row (largest
        # datediff among datediff < origin, i.e. closest to baseline without crossing it)
        if has_id and has_time and num_cols and pre.any():
            for c in num_cols:
                if c not in chunk.columns:
                    continue
                v = pd.to_numeric(chunk[c], errors="coerce")
                sub = pd.DataFrame({"p": pids[pre].to_numpy(), "t": dd[pre].to_numpy(),
                                    "v": v[pre].to_numpy()}).dropna()
                if not len(sub):
                    continue
                # keep only each patient's most recent row in this chunk, then reconcile
                # across chunks — avoids a per-row Python loop over the whole file
                best = sub.loc[sub.groupby("p")["t"].idxmax()]
                for p, t, val in zip(best["p"].tolist(), best["t"].tolist(), best["v"].tolist()):
                    prev = numeric_last[int(p)].get(c)
                    if prev is None or t > prev[0]:
                        numeric_last[int(p)][c] = (t, val)
        del chunk
    gc.collect()

    multi_row_days = sum(1 for k, v in day_keys.items() if v > 1)
    multi_row_days_pre = sum(1 for k, v in day_keys_pre.items() if v > 1)
    return {
        "n_rows_pre_baseline": n_rows - n_post_baseline,
        "n_day_groups_pre": len(day_keys_pre),
        "n_day_groups_multirow_pre": multi_row_days_pre,
        "max_rows_one_day_pre": max(day_keys_pre.values()) if day_keys_pre else 0,
        "path": str(path),
        "name": Path(path).stem,
        "n_rows": n_rows,
        "columns": cols,
        "has_id": has_id,
        "has_datediff": has_time,
        "n_patients": len(patients),
        "patients": patients,
        "rows_per_patient_q": q(list(rows_per_patient.values()), (50, 95, 100)),
        "datediff": {"min": dd_min if dd_min != math.inf else None,
                     "max": dd_max if dd_max != -math.inf else None,
                     "quantiles": dd_res.quantiles((0, 5, 25, 50, 75, 95, 100))},
        "n_rows_post_baseline": n_post_baseline,
        "n_day_groups": len(day_keys),
        "n_day_groups_multirow": multi_row_days,
        "max_rows_one_day": max(day_keys.values()) if day_keys else 0,
        "col_stats": {c: st.summary(min_show) for c, st in stats.items()},
        "col_kinds": {c: st.kind() for c, st in stats.items()},
        "text_cols": text_cols,
        "str_cols": str_cols,
        "numeric_cols": num_cols,
        "kind_shift": {c: (probe_kinds[c], stats[c].kind()) for c in stats
                       if probe_kinds.get(c) != stats[c].kind()},
        "text_chars": text_chars,
        "str_chars": str_chars,
        "numeric_last": numeric_last,
        "per_patient_days": per_patient_days,
        "term_patients": {t: len(p) for t, p in term_patients.items()} if want_text_terms else {},
    }


# ---------------------------------------------------------------- cohort / targets

def build_cohort(smart_csv, legacy, censoring_time):
    """Replicate the pipeline's cohort + target construction exactly."""
    df = pd.read_csv(smart_csv)
    n_raw = len(df)
    notes = []
    if legacy:
        before = len(df)
        df = drop_rows_with_missing_smart_outcomes(df)
        notes.append(f"legacy: dropped {before - len(df):,} rows with a missing SMART outcome column")
        ltfu_cols = [c for c in ["edoodvas", "ebero_n", "emi_n"] if c in df.columns]
        n_ltfu = int(df[ltfu_cols].isin([2]).any(axis=1).sum()) if ltfu_cols else 0
        notes.append(f"legacy: {n_ltfu:,} patients flagged lost-to-follow-up (indicator==2)")
        df = compute_legacy_targets(df, censoring_time=censoring_time)
    else:
        if any(c.startswith("e") and c.endswith("_f") for c in df.columns):
            df["first_event"] = df.apply(compute_first_event, axis=1)
            df["cd_event"] = df.apply(compute_cd_event, axis=1)
        elif "cd_event" not in df.columns:
            df["cd_event"] = 1
    df = df[~df["first_event"].isna()]
    df = df[df[ID] >= 0]
    n_dup = len(df) - df[ID].nunique()
    df = df.loc[df.groupby(ID)["first_event"].idxmin()].reset_index(drop=True)
    notes.append(f"{n_raw:,} raw rows -> {len(df):,} unique patients (deduplicated {n_dup:,} extra rows)")
    return df[[ID, "first_event", "cd_event"]].copy(), notes


# ---------------------------------------------------------------- report

def main(args):
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    L, J = [], {}
    H = args.horizon_days

    def w(line=""):
        L.append(line)

    w("# EDA — baseline-free (no-SMART) survival from event CSVs")
    w()
    w(f"- horizon: **{H} days ({H/365.25:.1f} years)**")
    w(f"- privacy: values/terms shown only if they occur in >= {args.min_show_count} patients/rows; "
      "no raw free text is included")
    w()

    # ---------------- §1 cohort + target feasibility
    cohort, notes = build_cohort(args.smart_csv, args.legacy, args.censoring_time)
    cohort["first_event_abs"] = cohort["first_event"]  # unshifted, for the §5 leakage check
    LM = args.landmark_days
    if LM > 0:
        # LANDMARK ANALYSIS. Using events in [0, LM] as features is only fair if the
        # prediction origin also moves to LM: patients whose outcome falls inside the
        # window must be dropped (their features would describe their own outcome) and
        # survival must be measured FROM the landmark. Doing one without the other leaks.
        n_before = len(cohort)
        ev_before = int((cohort["cd_event"] == 1).sum())
        cohort = cohort[cohort["first_event"] > LM].copy()
        cohort["first_event"] = cohort["first_event"] - LM
        n_drop = n_before - len(cohort)
        ev_drop = ev_before - int((cohort["cd_event"] == 1).sum())
        notes.append(
            f"**landmark = {LM}d**: features may use events with datediff < {LM} (incl. "
            f"post-baseline up to the landmark); dropped {n_drop:,} patients whose outcome "
            f"occurred at/before the landmark ({ev_drop:,} of them events), and survival is "
            f"now measured FROM day {LM}, so all horizons below are landmark-relative")
    t_raw = cohort["first_event"].to_numpy(float)
    e_raw = cohort["cd_event"].to_numpy(int)
    cens = [apply_censoring(t, e, H) for t, e in zip(t_raw, e_raw)]
    t_h = np.array([c[0] for c in cens])
    e_h = np.array([c[1] for c in cens])

    w(f"## §1 Cohort and target feasibility"
      + (f" (landmark {LM}d)" if LM else ""))
    w()
    for n in notes:
        w(f"- {n}")
    w(f"- follow-up (`first_event`, days): {q(t_raw)}")
    w(f"- follow-up (years): { {k: round(v/365.25, 2) for k, v in q(t_raw).items()} }")
    w(f"- events (uncensored) overall: **{int(e_raw.sum()):,} / {len(e_raw):,} "
      f"({100*e_raw.mean():.1f}%)**")
    w(f"- at the {H}-day horizon: **{int(e_h.sum()):,} events ({100*e_h.mean():.1f}%)**, "
      f"{int((e_h==0).sum()):,} censored")
    n_admin = int(((e_raw == 1) & (t_raw > H)).sum())
    n_short = int(((e_raw == 0) & (t_raw < H)).sum())
    w(f"- events occurring AFTER the horizon (censored at {H}d): {n_admin:,}")
    w(f"- **censored BEFORE the horizon (incomplete follow-up): {n_short:,} "
      f"({100*n_short/len(t_raw):.1f}%)** <- if this is large, 15y is only partly observed")
    w()
    yrs = list(range(1, 16))
    w("| year | at risk | cum. events | cum. censored | KM S(t) |")
    w("|---|---|---|---|---|")
    km = km_survival(t_raw, e_raw, [y * 365.25 for y in yrs])
    for y, s in zip(yrs, km):
        d = y * 365.25
        at_risk = int((t_raw >= d).sum())
        ce = int(((e_raw == 1) & (t_raw <= d)).sum())
        cc = int(((e_raw == 0) & (t_raw <= d)).sum())
        w(f"| {y} | {at_risk:,} | {ce:,} | {cc:,} | {s:.3f} |")
    w()
    J["cohort"] = {"n": len(t_raw), "events_raw": int(e_raw.sum()),
                   "events_at_horizon": int(e_h.sum()), "censored_before_horizon": n_short,
                   "followup_quantiles_days": q(t_raw), "km_by_year": dict(zip(yrs, km))}

    splits = {}
    if args.split_json:
        with open(args.split_json) as f:
            sp = json.load(f)
        if "val" in sp and "validation" not in sp:
            sp["validation"] = sp.pop("val")
        cohort_ids = set(cohort[ID].astype(int))
        w("- splits (from --split-json), intersected with the cohort:")
        for k, v in sp.items():
            ids = set(int(x) for x in v)
            splits[k] = ids & cohort_ids
            sub = cohort[cohort[ID].astype(int).isin(splits[k])]
            ev = int(((sub["cd_event"] == 1) & (sub["first_event"] <= H)).sum())
            w(f"  - {k}: {len(splits[k]):,} patients (of {len(ids):,} listed; "
              f"{len(ids - cohort_ids):,} not in cohort) | events@{H}d={ev:,}")
        w()

    # ---------------- §3 per-CSV scan (needed before §2 aggregates)
    folder = Path(args.event_csv_folder)
    csvs = sorted(folder.glob("*.csv"))
    if not csvs:
        raise SystemExit(f"No CSVs found in {folder}")
    forced = {x.strip() for x in (args.force_text_cols or "").split(",") if x.strip()}
    print(f"Scanning {len(csvs)} event CSVs ...", flush=True)
    scans = []
    for p in csvs:
        print(f"  - {p.name}", flush=True)
        try:
            scans.append(scan_csv(p, args.min_show_count, not args.no_text_terms, forced, LM))
        except Exception as exc:  # keep going: one bad CSV shouldn't kill the report
            w(f"> **ERROR scanning {p.name}: {type(exc).__name__}: {exc}**")
            print(f"    ERROR: {exc}", flush=True)
    w()

    # ---------------- §2 coverage
    cohort_ids = set(cohort[ID].astype(int))
    ev_per_patient = Counter()
    days_per_patient = defaultdict(set)
    src_patients = {}
    for s in scans:
        # patients with >=1 PRE-baseline event from this source (per_patient_days is
        # already pre-baseline only); s["patients"] counts all rows and would leak future
        src_patients[s["name"]] = set(s["per_patient_days"]) & cohort_ids
        for pid, days in s["per_patient_days"].items():
            if pid in cohort_ids:
                days_per_patient[pid] |= days
        for pid, n in Counter({p: len(d) for p, d in s["per_patient_days"].items()}).items():
            if pid in cohort_ids:
                ev_per_patient[pid] += n
    any_event = set(days_per_patient)
    n_no_event = len(cohort_ids - any_event)

    w("## §2 Event coverage — the ceiling for a baseline-free model")
    w()
    w(f"- cohort patients: **{len(cohort_ids):,}**")
    w(f"- with >= 1 usable event (datediff < {LM}): **{len(any_event):,} "
      f"({100*len(any_event)/max(len(cohort_ids),1):.1f}%)**")
    w(f"- **with NO events at all: {n_no_event:,} "
      f"({100*n_no_event/max(len(cohort_ids),1):.1f}%)** <- with no baseline these have an "
      "empty feature vector and cannot be ranked")
    if splits:
        for k, ids in splits.items():
            ne = len(ids - any_event)
            w(f"  - {k}: {len(ids)-ne:,} with events, **{ne:,} with none** "
              f"({100*ne/max(len(ids),1):.1f}%)")
    nev = [len(days_per_patient.get(p, ())) for p in cohort_ids]
    w(f"- distinct event-days per patient (0 included): {q(nev, (0,25,50,75,95,100))}")
    buckets = Counter()
    for n in nev:
        buckets["0" if n == 0 else "1" if n == 1 else "2-5" if n <= 5 else
                "6-20" if n <= 20 else "21-100" if n <= 100 else ">100"] += 1
    w(f"- patients by #event-days: { {k: buckets[k] for k in ['0','1','2-5','6-20','21-100','>100'] if k in buckets} }")
    spans = [max(0, LM - min(days_per_patient[p])) for p in any_event if days_per_patient[p]]
    w(f"- history span (days before the origin of the OLDEST event): {q(spans, (5,50,95,100))}")
    w()
    w("Coverage per source and per look-back window (patients with >=1 event):")
    w()
    wins = [90, 180, 365, 730, 1825, 3650, None]
    w("| source | rows | pre-baseline rows | patients (pre) | "
      + " | ".join(f"<={x}d" if x else "all usable history" for x in wins) + " |")
    w("|---" * (4 + len(wins)) + "|")
    for s in scans:
        cells = []
        for x in wins:
            c = sum(1 for pid, days in s["per_patient_days"].items()
                    if pid in cohort_ids and any((x is None) or (LM - x <= d < LM) for d in days))
            cells.append(f"{c:,}")
        w(f"| {s['name']} | {s['n_rows']:,} | {s['n_rows_pre_baseline']:,} | "
          f"{len(src_patients[s['name']]):,} | " + " | ".join(cells) + " |")
    union_cells = []
    for x in wins:
        c = sum(1 for pid, days in days_per_patient.items()
                if any((x is None) or (LM - x <= d < LM) for d in days))
        union_cells.append(f"{c:,}")
    w(f"| **UNION** | | | **{len(any_event):,}** | " + " | ".join(f"**{c}**" for c in union_cells) + " |")
    w()
    n_src = Counter(sum(1 for s in scans if p in src_patients[s["name"]]) for p in cohort_ids)
    w(f"- #sources contributing per patient: {dict(sorted(n_src.items()))}")
    w()
    J["coverage"] = {"n_cohort": len(cohort_ids), "n_with_events": len(any_event),
                     "n_no_events": n_no_event, "event_days_per_patient_q": q(nev),
                     "per_source_patients": {k: len(v) for k, v in src_patients.items()}}

    # ---------------- §3 inventory
    w("## §3 Per-CSV inventory")
    w()
    for s in scans:
        w(f"### {s['name']}  ({s['n_rows']:,} rows, {len(src_patients[s['name']]):,} cohort patients)")
        w()
        w(f"- rows per patient: {s['rows_per_patient_q']}")
        w(f"- `datediff`: min={s['datediff']['min']}, max={s['datediff']['max']}, "
          f"quantiles={s['datediff']['quantiles']}")
        if s["n_rows_post_baseline"]:
            w(f"- **rows with datediff >= 0 (post-baseline, DROPPED by the pipeline): "
              f"{s['n_rows_post_baseline']:,}**")
        w(f"- same-day groups: {s['n_day_groups']:,} | with >1 row: "
          f"**{s['n_day_groups_multirow']:,}** | max rows on one day: {s['max_rows_one_day']}")
        kinds = Counter(s["col_kinds"].values())
        w(f"- column kinds: {dict(kinds)}")
        w()
        shown = list(s["col_stats"].items())
        trunc = ""
        if not args.full and len(shown) > 40:
            shown, trunc = shown[:40], f"  (showing 40 of {len(s['col_stats'])} columns; --full for all)"
        w("| column | kind | missing% | patients | distinct | detail |")
        w("|---|---|---|---|---|---|")
        for c, d in shown:
            det = []
            if d["kind"] in ("numeric", "numeric_discrete"):
                det.append(f"mean={d.get('mean')} sd={d.get('std')} range=[{d.get('min')},{d.get('max')}]")
            if not d.get("kind", "").startswith("numeric") and d.get("char_len"):
                det.append(f"chars={d.get('char_len')} words~{d.get('median_words')} "
                           f"est_tokens={d.get('est_tokens', 0):,}")
            if d["kind"] in ("categorical", "numeric_discrete"):
                tv = d.get("top_values")
                det.append(f"top={tv if isinstance(tv, str) else tv[:4]}")
            if d.get("rows_with_iso_date"):
                det.append(f"**{d['rows_with_iso_date']:,} rows contain an ISO date**")
            w(f"| `{c}` | {d['kind']} | {d['missing_pct']} | {d['n_patients']} | {d['n_distinct']} | "
              + "; ".join(det) + " |")
        if trunc:
            w(trunc)
        w()
    J["per_csv"] = {s["name"]: {k: v for k, v in s.items()
                               if k not in ("patients", "text_chars", "str_chars", "numeric_last",
                                            "per_patient_days", "term_patients")}
                    for s in scans}

    # ---------------- §4 merge-collision audit
    w("## §4 Merge-collision audit (silent data loss in the pipeline)")
    w()
    w("`smartehr_pipeline.merge_event_rows` merges every row sharing `(m3life_no, datediff)` into one "
      "dict, assigning `merged[col] = val` per non-NaN value. Two consequences:")
    w()
    owners = defaultdict(list)
    for s in scans:
        for c in s["columns"]:
            if c not in (ID, TIME):
                owners[c].append(s["name"])
    shared = {c: v for c, v in owners.items() if len(v) > 1}
    w(f"1. **Column names shared across CSVs: {len(shared)}** — these overwrite each other when two "
      "sources report on the same day (last one wins).")
    if shared:
        for c, v in list(shared.items())[:25]:
            w(f"   - `{c}`: {', '.join(v)}")
        if len(shared) > 25:
            w(f"   - ... and {len(shared)-25} more")
    else:
        w("   - none: every CSV uses distinct column names, so no cross-source clobbering.")
    tot_groups = sum(s["n_day_groups_pre"] for s in scans)
    tot_multi = sum(s["n_day_groups_multirow_pre"] for s in scans)
    w(f"2. **Same-day multi-row groups (pre-baseline rows only, i.e. what the pipeline actually "
      f"merges): {tot_multi:,} of {tot_groups:,} ({100*tot_multi/max(tot_groups,1):.1f}%)** — within "
      "one CSV these collapse to the LAST row's value per column.")
    w()
    w("| source | pre-bl day-groups | with >1 row | % | max rows/day | shape |")
    w("|---|---|---|---|---|---|")
    long_fmt = []
    for s in scans:
        g, m = s["n_day_groups_pre"], s["n_day_groups_multirow_pre"]
        # A key-value ("long") source pairs a name column with a value column, so one day
        # holds many rows that are DIFFERENT variables — merging by column name keeps one.
        kinds = s["col_kinds"]
        cat_cols = [c for c, k in kinds.items() if k == "categorical"]
        val_cols = [c for c, k in kinds.items() if k in ("numeric", "numeric_discrete")]
        pct = 100 * m / max(g, 1)
        is_long = bool(cat_cols) and bool(val_cols) and pct >= 50
        if is_long:
            long_fmt.append(s["name"])
        w(f"| {s['name']} | {g:,} | {m:,} | {pct:.1f} | {s['max_rows_one_day_pre']:,} | "
          f"{'**LONG (key-value)**' if is_long else 'wide'} |")
    w()
    if long_fmt:
        w(f"3. **Long-format sources detected: {', '.join(long_fmt)}.** These store one "
          "measurement per row as (name, value) pairs, so a single day legitimately holds many "
          "DIFFERENT variables. `merged[col] = val` keyed on the column name therefore keeps only "
          "ONE (name, value) pair per day and silently discards the rest of the panel. These "
          "sources need **pivoting** (name -> its own column) before merging, not overwriting.")
        w()
    if args.jsonl_dir:
        jd = Path(args.jsonl_dir)
        post = 0
        pats = 0
        for sp in ["train", "validation", "test"]:
            fp = jd / f"{sp}.jsonl"
            if not fp.exists():
                continue
            with open(fp) as f:
                for line in f:
                    r = json.loads(line)
                    pats += 1
                    post += len(r.get("events", []))
        raw_days = sum(len(v) for v in days_per_patient.values())
        w(f"- pipeline output ({jd}): {pats:,} patients, {post:,} merged event time-points vs "
          f"{raw_days:,} distinct raw (patient, day) pairs in the cohort "
          f"-> {raw_days - post:,} lost to merging/filters")
        w()

    # ---------------- §5 leakage audit
    w("## §5 Leakage and sanity audit")
    w()
    tot_post = sum(s["n_rows_post_baseline"] for s in scans)
    w(f"- rows dated at/after baseline across all CSVs: **{tot_post:,}** "
      "(pipeline keeps only `datediff < baseline_time`; with baseline_time=0 these are excluded)")
    sus = []
    for s in scans:
        for c in s["columns"]:
            if c not in (ID, TIME) and LEAK_PAT.search(c):
                sus.append(f"{s['name']}.{c}")
    w(f"- columns whose NAME looks outcome-related or date-like: {len(sus)}")
    for x in sus[:30]:
        w(f"  - `{x}`")
    if len(sus) > 30:
        w(f"  - ... and {len(sus)-30} more")
    dated = [f"{s['name']}.{c}" for s in scans for c, d in s["col_stats"].items()
             if d.get("rows_with_iso_date")]
    w(f"- columns containing ISO dates in their values: {len(dated)}"
      + (f" ({', '.join(dated[:12])}{' ...' if len(dated) > 12 else ''})" if dated else ""))
    fe = dict(zip(cohort[ID].astype(int), cohort["first_event_abs"]))
    after = sum(1 for pid, days in days_per_patient.items()
                for d in days if pid in fe and d >= fe[pid])
    w(f"- FEATURE events dated at/after the patient's own outcome: {after:,} "
      "(must be 0 — otherwise a feature describes the outcome it is meant to predict; "
      "the landmark exclusion is what guarantees this)")
    w()

    # ---------------- §6 univariate signal screen
    w("## §6 Univariate signal screen (Harrell's C, no model trained)")
    w()
    n_ev = int(e_h.sum())
    thr = 2.0 * math.sqrt(0.25 / max(n_ev, 1))  # ~2 SE of C under the null
    w(f"Each row uses ONE feature (from PRE-baseline rows only) as the risk score at the "
      f"{H}-day horizon. C=0.5 is chance.")
    w()
    w(f"With **{n_ev:,} events**, the standard error of C under the null is "
      f"~{thr/2:.4f}, so only **|C-0.5| >= {thr:.3f}** (2 SE) is distinguishable from noise. "
      f"Values are flagged against that threshold, NOT a fixed 0.02. `n_comparable` counts "
      "pairs, which is far larger than the effective sample size (the event count) — do not "
      "read it as precision.")
    w()
    ids = cohort[ID].astype(int).to_numpy()
    tmap = {p: (a, b) for p, a, b in zip(ids, t_h, e_h)}
    feats = {}
    feats["has_any_event"] = np.array([1.0 if p in any_event else 0.0 for p in ids])
    feats["n_event_days"] = np.array([float(len(days_per_patient.get(p, ()))) for p in ids])
    # days_per_patient holds only pre-baseline (negative) offsets, so max() is the event
    # closest to baseline; as a risk score, more recent (closer to 0) = higher risk.
    feats["recency(-days_since_last)"] = np.array(
        [float(max(days_per_patient[p])) if days_per_patient.get(p) else np.nan for p in ids])
    feats["history_span_days"] = np.array(
        [float(LM - min(days_per_patient[p])) if days_per_patient.get(p) else np.nan for p in ids])
    feats["n_sources"] = np.array(
        [float(sum(1 for s in scans if p in src_patients[s["name"]])) for p in ids])
    for s in scans:
        feats[f"has_event[{s['name']}]"] = np.array(
            [1.0 if p in src_patients[s["name"]] else 0.0 for p in ids])
        feats[f"n_days[{s['name']}]"] = np.array(
            [float(len(s["per_patient_days"].get(p, ()))) for p in ids])
    rows = []
    for name, v in feats.items():
        c, n = harrell_c(t_h, e_h, v)
        cov = int((~np.isnan(v)).sum())
        if c is not None:
            rows.append((abs(c - 0.5), name, c, cov, n))
    # numeric event columns: last observed value per patient
    num_rows = []
    for s in scans:
        for c in s["numeric_cols"]:
            vals = np.array([s["numeric_last"].get(p, {}).get(c, (None, np.nan))[1] for p in ids], float)
            cov = int((~np.isnan(vals)).sum())
            if cov < max(args.min_coverage, 30):
                continue
            ci, n = harrell_c(t_h, e_h, vals)
            if ci is not None:
                num_rows.append((abs(ci - 0.5), f"last[{s['name']}.{c}]", ci, cov, n))
    # second, better-observed horizon: a 15y estimate can rest on a thin at-risk tail
    H2 = args.extra_horizon_days
    cens2 = [apply_censoring(t, e, H2) for t, e in zip(t_raw, e_raw)]
    t_h2 = np.array([c[0] for c in cens2])
    e_h2 = np.array([c[1] for c in cens2])
    n_ev2 = int(e_h2.sum())
    thr2 = 2.0 * math.sqrt(0.25 / max(n_ev2, 1))
    c2 = {}
    for name, v in feats.items():
        c2[name] = harrell_c(t_h2, e_h2, v)[0]
    for s in scans:
        for c in s["numeric_cols"]:
            vals = np.array([s["numeric_last"].get(p, {}).get(c, (None, np.nan))[1] for p in ids], float)
            if int((~np.isnan(vals)).sum()) < max(args.min_coverage, 30):
                continue
            c2[f"last[{s['name']}.{c}]"] = harrell_c(t_h2, e_h2, vals)[0]

    def fmt2(name):
        v = c2.get(name)
        if v is None:
            return "-"
        return f"{v:.4f}" + (" **<-**" if abs(v - 0.5) >= thr2 else "")

    rows.sort(reverse=True)
    num_rows.sort(reverse=True)
    w(f"| feature | C @ {H}d ({n_ev:,} ev) | C @ {H2}d ({n_ev2:,} ev) | patients with value |")
    w("|---|---|---|---|")
    for _, name, c, cov, n in rows:
        flag = " **<-**" if abs(c - 0.5) >= thr else ""
        w(f"| {name} | {c:.4f}{flag} | {fmt2(name)} | {cov:,} |")
    w()
    w(f"Top numeric event columns by |C-0.5| (last PRE-baseline value, "
      f">= {max(args.min_coverage,30)} patients):")
    w()
    w(f"| feature | C @ {H}d | C @ {H2}d | patients with value |")
    w("|---|---|---|---|")
    for _, name, c, cov, n in num_rows[:40]:
        flag = " **<-**" if abs(c - 0.5) >= thr else ""
        w(f"| {name} | {c:.4f}{flag} | {fmt2(name)} | {cov:,} |")
    if not num_rows:
        w("| (no numeric column met the coverage threshold) | | | |")
    w()
    w(f"- 2-SE noise floor: |C-0.5| >= {thr:.3f} at {H}d, >= {thr2:.3f} at {H2}d. "
      "A feature flagged at BOTH horizons is far more credible than one flagged at either alone.")
    w()
    # presence vs content: KM split by has-any-event
    have = np.array([p in any_event for p in ids])
    if have.any() and (~have).any():
        k1 = km_survival(t_h[have], e_h[have], [H])[0]
        k0 = km_survival(t_h[~have], e_h[~have], [H])[0]
        w(f"- KM S({H}d): patients WITH events **{k1:.3f}** (n={int(have.sum()):,}) vs "
          f"WITHOUT events **{k0:.3f}** (n={int((~have).sum()):,}) — if these differ a lot, "
          "mere event *presence* is prognostic, separate from event *content*.")
        w()
    J["signal_screen"] = {"aggregate": [{"feature": n, "c_index": round(c, 4), "coverage": cov}
                                        for _, n, c, cov, _ in rows],
                          "numeric_top": [{"feature": n, "c_index": round(c, 4), "coverage": cov}
                                          for _, n, c, cov, _ in num_rows[:60]]}

    # ---------------- §7 text budget
    w("## §7 Free-text budget (sizing the TF-IDF and LLM arms)")
    w()
    all_chars, all_str = Counter(), Counter()
    for s in scans:
        for p, n in s["text_chars"].items():
            if p in cohort_ids:
                all_chars[p] += n
        for p, n in s["str_chars"].items():
            if p in cohort_ids:
                all_str[p] += n
    n_text = len(all_chars)
    n_detected = sum(len(s["text_cols"]) for s in scans)
    w(f"- columns auto-classified as free text: **{n_detected}** "
      f"(across {sum(len(s['str_cols']) for s in scans)} string columns)")
    w(f"- patients with any free text (all history): **{n_text:,} "
      f"({100*n_text/max(len(cohort_ids),1):.1f}%)**")
    w(f"- chars per patient (text-bearing only): {q(list(all_chars.values()), (5,50,95,100))}")
    tot = sum(all_chars.values())
    w(f"- total corpus: {tot:,} chars ~= **{int(tot/4):,} tokens** "
      f"(~{int(tot/4/max(n_text,1)):,} tokens/patient)")
    tot_str = sum(all_str.values())
    w(f"- ALL string columns (incl. codes/labels, upper bound): {len(all_str):,} patients, "
      f"{tot_str:,} chars ~= {int(tot_str/4):,} tokens")
    if n_detected == 0:
        w()
        w("> **WARNING: no column was auto-classified as free text.** Either these CSVs really hold "
          "only codes/labels, or the heuristic (median >= 20 chars AND >= 3 words) missed them. "
          "Check the `char_len`/`median_words` columns in §3 — every string column reports them — and "
          "re-run with `--force-text-cols source.col,...` to force any that look like reports.")
    w()
    w("| source | free-text cols | string cols | text chars | est. tokens | patients w/ text |")
    w("|---|---|---|---|---|---|")
    for s in scans:
        tc = sum(d.get("total_chars", 0) for c, d in s["col_stats"].items() if c in s["text_cols"])
        pt = len([p for p in s["text_chars"] if p in cohort_ids])
        w(f"| {s['name']} | {len(s['text_cols'])} | {len(s['str_cols'])} | {tc:,} | "
          f"{int(tc/4):,} | {pt:,} |")
    w()
    shifts = {s["name"]: s["kind_shift"] for s in scans if s["kind_shift"]}
    if shifts:
        w(f"- note: column kind changed between the 50k-row probe and the full scan (probe -> full): "
          f"{shifts} — the probe drives text/numeric aggregation, so force with `--force-text-cols` "
          "if a text column is listed here.")
        w()
    if not args.no_text_terms:
        terms = Counter()
        for s in scans:
            for t, n in s["term_patients"].items():
                terms[t] += n
        safe = sorted(((t, n) for t, n in terms.items() if n >= args.min_show_count),
                      key=lambda kv: (-kv[1], kv[0]))[:400]  # deterministic on count ties
        w(f"- distinct word types seen: {len(terms):,}; "
          f"appearing in >= {args.min_show_count} patients: {sum(1 for _, n in terms.items() if n >= args.min_show_count):,}")
        w(f"- most frequent terms (patient counts, privacy-filtered): "
          f"{[t for t, _ in safe[:60]]}")
        w()

    (out_dir / "eda_report.md").write_text("\n".join(L))
    with open(out_dir / "eda_report.json", "w") as f:
        json.dump(J, f, indent=2, default=str)
    print("\n".join(L))
    print(f"\n=== wrote {out_dir/'eda_report.md'} and {out_dir/'eda_report.json'} ===")
    print("Paste eda_report.md back into the chat.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True, help="smart.csv — used ONLY for the survival target.")
    p.add_argument("--event-csv-folder", required=True, help="Folder with ALL event CSVs.")
    p.add_argument("--split-json", default=None)
    p.add_argument("--jsonl-dir", default=None,
                   help="Optional pipeline output dir, to measure event loss from merging.")
    p.add_argument("--horizon-days", type=int, default=5475, help="Default 5475 = 15 years.")
    p.add_argument("--legacy", action="store_true",
                   help="Use the SMART legacy outcome columns (matches the pipeline's --legacy).")
    p.add_argument("--censoring-time", type=int, default=None)
    p.add_argument("--out-dir", default="eda_out")
    p.add_argument("--min-show-count", type=int, default=20,
                   help="Privacy floor: never print a value/term seen in fewer patients/rows.")
    p.add_argument("--min-coverage", type=int, default=200,
                   help="Minimum patients with a value for a numeric column to enter the screen.")
    p.add_argument("--no-text-terms", action="store_true",
                   help="Skip the frequent-term listing entirely.")
    p.add_argument("--force-text-cols", default=None,
                   help="Comma-separated columns to treat as free text regardless of the heuristic, "
                        "as 'col' or 'source.col' (e.g. radiologie.verslag,ok_verslag.verslag).")
    p.add_argument("--landmark-days", type=int, default=0,
                   help="LANDMARK: move the prediction origin this many days after the SMART "
                        "baseline. Events with datediff < LANDMARK become usable features (so "
                        "--landmark-days 180 admits post-baseline events up to 6 months), patients "
                        "whose outcome falls at/before the landmark are EXCLUDED, and survival is "
                        "measured from the landmark. All three happen together — setting a feature "
                        "cutoff without the exclusion and time shift would leak the outcome.")
    p.add_argument("--extra-horizon-days", type=int, default=3650,
                   help="Second horizon for the signal screen (default 3650 = 10 years), so a "
                        "weakly-observed 15y horizon can be compared against a better-observed one.")
    p.add_argument("--full", action="store_true", help="Do not truncate long column tables.")
    main(p.parse_args())
