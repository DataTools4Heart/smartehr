"""Pivoted event features from the RAW event CSVs — replaces the pipeline's same-day merge.

Why this exists: `smartehr_pipeline.merge_event_rows` merges rows sharing
`(m3life_no, datediff)` with `merged[col] = val`, keyed on the COLUMN NAME. The big
sources are long/key-value (the variable's name is in one column, its value in another),
so one day legitimately holds many DIFFERENT variables under the same column names and
all but the last are silently discarded — a 341-lab day collapses to a single test.
`prepare_event_numeric_features.py --pivot-codes` cannot fix this because it reads the
already-merged JSONL. So this builder reads the raw CSVs and pivots BEFORE any merge.

Three column roles, and one source may use all three:

  numeric pivot     (name_col, value_col) -> one feature block per distinct name
                    e.g. lab_testcode/lab_result, MeasName_ECHO/Value_ECHO, label/data1
  occurrence pivot  code_col              -> per-code event COUNT (no numeric value)
                    e.g. med_ZIatc (ATC, optionally truncated to a class prefix)
  wide numeric      every remaining numeric column, aggregated directly
                    e.g. the 12 ecg_measmatrix columns, hos_nr/hos_duur

Aggregators per feature block: last, mean, min, max, slope (per year), count, present.
`last` is the value closest to the origin; `slope` is the trajectory.

LANDMARK: --landmark-days L matches eda_events_survival.py exactly — features use events
with datediff < L, patients whose outcome is at/before L are excluded, and survival is
measured FROM L. The three move together so the feature window cannot outrun the origin.

DIMENSIONALITY: with ~1.2k training events, thousands of features would overfit outright.
Codes are therefore kept only if they occur in >= --min-patients TRAIN patients (selection
on train only, never on val/test), then capped at --max-codes-per-source by coverage.
Everything dropped is reported, never silently truncated.

    python scripts/smartehr/prepare_pivoted_event_features.py \
        --smart-csv <smart.csv> --event-csv-folder <ALL_event_csvs> \
        --split-json <splits.json> --legacy --landmark-days 180 \
        --horizon-days 3650 --out-dir <PIVOT_OUT>

    # then: dataset=smartehr_embeddings dataset.root_path=<PIVOT_OUT> \
    #       model=mlp model.input_size=<n_features printed at the end>
"""

import argparse
import gc
import json
import math
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import ID, TIME, apply_censoring, build_cohort  # shared definitions
from smartehr_pipeline import _SMART_OUTCOME_COLS

CHUNK = 200_000
AGGS = ("last", "mean", "min", "max", "slope", "count", "present")

# Defaults for the SMART EHR extract; keys match a CSV stem by prefix, so the date
# suffixes (lab_ezis_20250709) need not be spelled out.
NUMERIC_PIVOT_DEFAULT = "lab_ezis:lab_testcode:lab_result,echo:MeasName_ECHO:Value_ECHO,meting:label:data1"
OCCURRENCE_DEFAULT = "med:med_ZIatc:4,dbc:Diagnose,diag:diag_omschrijving,ok:OMSCHR"


def parse_specs(s, n_parts):
    """'src:colA:colB,src2:colC' -> {src: (colA, colB), src2: (colC, None)}"""
    out = {}
    for item in (s or "").split(","):
        item = item.strip()
        if not item:
            continue
        parts = item.split(":")
        if len(parts) < 2:
            raise SystemExit(f"bad spec {item!r}: expected src:col[:col]")
        key, cols = parts[0], parts[1:]
        cols = (cols + [None] * n_parts)[:n_parts]
        out[key] = tuple(cols)
    return out


def match_spec(stem, specs):
    for key, val in specs.items():
        if stem == key or stem.startswith(key):
            return val
    return None


def safe(name):
    return re.sub(r"\s+", "_", str(name).strip())[:60]


class Block:
    """Streaming accumulator for one source: (n_patients x n_codes) stats per code."""

    # occurrence blocks only ever produce count/present, so `lean` allocates the single
    # count array instead of nine — auto-occurrence can add a lot of blocks
    STATS = ("n", "sum", "min", "max", "last_t", "last_v", "sum_t", "sum_tv", "sum_tt")

    def __init__(self, source, codes, n_patients, kind, lean=False):
        self.source, self.kind, self.lean = source, kind, lean
        self.codes = list(codes)
        self.cindex = {c: j for j, c in enumerate(self.codes)}
        shape = (n_patients, len(self.codes))
        f = lambda v: np.full(shape, v, dtype=np.float64)
        self.n = f(0.0)
        if lean:
            return
        self.sum = f(0.0)
        self.min = f(np.inf)
        self.max = f(-np.inf)
        self.last_t = f(-np.inf)
        self.last_v = f(np.nan)
        self.sum_t = f(0.0)
        self.sum_tv = f(0.0)
        self.sum_tt = f(0.0)

    def update(self, pi, ci, t, v):
        """Fold a chunk in. (pi, ci) pairs are made unique by the groupby first."""
        df = pd.DataFrame({"pi": pi, "ci": ci, "t": t, "v": v}).dropna()
        if df.empty:
            return
        if self.lean:                      # counts only
            g = df.groupby(["pi", "ci"], sort=False).size()
            ii = g.index.get_level_values(0).to_numpy(np.int64)
            jj = g.index.get_level_values(1).to_numpy(np.int64)
            self.n[ii, jj] += g.to_numpy()
            return
        df["tv"] = df["t"] * df["v"]
        df["tt"] = df["t"] * df["t"]
        g = df.groupby(["pi", "ci"], sort=False)
        agg = g.agg(cnt=("v", "size"), s=("v", "sum"), mn=("v", "min"), mx=("v", "max"),
                    st=("t", "sum"), stv=("tv", "sum"), stt=("tt", "sum"))
        last_rows = df.loc[g["t"].idxmax()]
        ii = agg.index.get_level_values(0).to_numpy(np.int64)
        jj = agg.index.get_level_values(1).to_numpy(np.int64)
        # (ii, jj) unique within the chunk, so plain fancy indexing is safe and fast
        self.n[ii, jj] += agg["cnt"].to_numpy()
        self.sum[ii, jj] += agg["s"].to_numpy()
        self.min[ii, jj] = np.minimum(self.min[ii, jj], agg["mn"].to_numpy())
        self.max[ii, jj] = np.maximum(self.max[ii, jj], agg["mx"].to_numpy())
        self.sum_t[ii, jj] += agg["st"].to_numpy()
        self.sum_tv[ii, jj] += agg["stv"].to_numpy()
        self.sum_tt[ii, jj] += agg["stt"].to_numpy()
        li = last_rows["pi"].to_numpy(np.int64)
        lj = last_rows["ci"].to_numpy(np.int64)
        lt = last_rows["t"].to_numpy()
        newer = lt > self.last_t[li, lj]
        self.last_t[li[newer], lj[newer]] = lt[newer]
        self.last_v[li[newer], lj[newer]] = last_rows["v"].to_numpy()[newer]

    def train_coverage(self, train_rows):
        """Number of TRAIN patients with at least one observation, per code."""
        return (self.n[train_rows] > 0).sum(axis=0)

    def features(self, aggs, keep=None):
        """-> (DataFrame, feature_names). Absent (patient, code) pairs stay NaN.

        `keep` is a boolean mask over codes, applied uniformly so the coverage floor
        also reaches wide-numeric columns (which have no pass-1 vocabulary step).
        """
        if keep is not None and not keep.all():
            idx = np.where(keep)[0]
            self.codes = [self.codes[j] for j in idx]
            for attr in (("n",) if self.lean else self.STATS):
                setattr(self, attr, getattr(self, attr)[:, idx])
            self.cindex = {c: j for j, c in enumerate(self.codes)}
        if not self.codes:
            return pd.DataFrame(), []
        present = self.n > 0
        cols, names = [], []
        for agg in aggs:
            if self.kind == "occurrence" and agg not in ("count", "present"):
                continue  # an occurrence code has no numeric value to summarise
            if agg == "last":
                m = np.where(present, self.last_v, np.nan)
            elif agg == "mean":
                m = np.where(present, self.sum / np.maximum(self.n, 1), np.nan)
            elif agg == "min":
                m = np.where(present, self.min, np.nan)
            elif agg == "max":
                m = np.where(present, self.max, np.nan)
            elif agg == "count":
                m = np.where(present, self.n, 0.0)  # a count of zero is meaningful
            elif agg == "present":
                m = present.astype(float)
            elif agg == "slope":
                den = self.n * self.sum_tt - self.sum_t ** 2
                num = self.n * self.sum_tv - self.sum_t * self.sum
                with np.errstate(invalid="ignore", divide="ignore"):
                    m = np.where((self.n >= 2) & (np.abs(den) > 1e-12), num / den, np.nan)
            else:
                raise SystemExit(f"unknown aggregator {agg}")
            cols.append(m)
            names += [f"{self.source}.{safe(c)}_{agg}" for c in self.codes]
        if not cols:
            return pd.DataFrame(), []
        return pd.DataFrame(np.concatenate(cols, axis=1), columns=names), names


def iter_chunks(path, usecols=None):
    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False, usecols=usecols):
        yield chunk


def source_roles(path, num_specs, occ_specs, probe_rows=50_000,
                 auto_occurrence=False, max_card=5000):
    """Decide which columns of one CSV are numeric-pivot / occurrence / wide-numeric.

    With auto_occurrence, EVERY remaining categorical column becomes an occurrence block.
    Without it five real sources (consult, radiologie_verslag, uitgaandebrief, ok_verslag,
    mri_verslag) contribute nothing at all, because they hold no numeric columns and only
    one column per source is named in --occurrence-pivot. That silently discards the
    "what care did this patient receive" signal: which specialism was consulted, which
    scan was ordered, and ok_verslag.STELLING, whose values include Complication.
    Long free text is left out — that belongs to the text arm, not a code counter.
    """
    stem = Path(path).stem
    head = pd.read_csv(path, nrows=0)
    cols = [c for c in head.columns if c not in (ID, TIME)]
    num_spec = match_spec(stem, num_specs)
    occ_spec = match_spec(stem, occ_specs)
    num_spec = num_spec if (num_spec and num_spec[0] in cols and num_spec[1] in cols) else None
    occ_cols = []
    if occ_spec and occ_spec[0] in cols:
        occ_cols.append((occ_spec[0], int(occ_spec[1]) if occ_spec[1] else None))
    used = set(num_spec or ()) | {c for c, _ in occ_cols}
    probe = pd.read_csv(path, nrows=probe_rows, low_memory=False)
    wide = [c for c in cols if c not in used
            and c in probe.columns and pd.api.types.is_numeric_dtype(probe[c])]
    if auto_occurrence:
        for c in cols:
            if c in used or c in wide or c not in probe.columns:
                continue
            s = probe[c].dropna().astype(str)
            if s.empty:
                continue
            med_len = float(s.str.len().median())
            med_words = float((s.str.count(r"\s+") + 1).median())
            if med_len >= 40 and med_words >= 5:
                continue                      # long free text -> text arm
            if not (2 <= s.nunique() <= max_card):
                continue
            occ_cols.append((c, None))
    return stem, num_spec, occ_cols, wide


def smart_baseline_features(smart_csv, pids):
    """Numeric SMART baseline columns, aligned to `pids`. DIAGNOSTIC USE ONLY.

    These are the hand-extracted variables the project is trying to do without. Emitting
    them through the identical cohort/landmark/split/target code is a positive control: if
    even these score ~0.5 the plumbing is broken, so an event-feature null means nothing.
    """
    df = pd.read_csv(smart_csv)
    if "SmrtRisk" in df.columns:
        df = df[list(df.columns[:df.columns.get_loc("SmrtRisk")])]
    drop = set(_SMART_OUTCOME_COLS) | {ID, "first_event", "cd_event"}
    cols = [c for c in df.columns if c not in drop and pd.api.types.is_numeric_dtype(df[c])]
    df = df[[ID] + cols].groupby(ID, as_index=True).first()
    X = df.reindex(pids)
    X.columns = [f"smart_baseline.{c}" for c in X.columns]
    return X.reset_index(drop=True)


def build(args):
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    LM, H = args.landmark_days, args.horizon_days
    log = []

    def say(msg):
        print(msg, flush=True)
        log.append(msg)

    # ---- cohort + landmark (identical semantics to the EDA)
    cohort, notes = build_cohort(args.smart_csv, args.legacy, args.censoring_time)
    for n in notes:
        say(f"  {n}")
    if LM > 0:
        n0, e0 = len(cohort), int((cohort["cd_event"] == 1).sum())
        cohort = cohort[cohort["first_event"] > LM].copy()
        cohort["first_event"] = cohort["first_event"] - LM
        say(f"  landmark {LM}d: dropped {n0-len(cohort):,} patients whose outcome was at/before "
            f"the landmark ({e0-int((cohort['cd_event']==1).sum()):,} events); survival now "
            f"measured from day {LM}")
    cohort = cohort.reset_index(drop=True)
    pids = cohort[ID].astype(int).to_numpy()
    pindex = {p: i for i, p in enumerate(pids)}
    n_pat = len(pids)

    with open(args.split_json) as f:
        sp = json.load(f)
    if "val" in sp and "validation" not in sp:
        sp["validation"] = sp.pop("val")
    splits = {k: [pindex[int(p)] for p in v if int(p) in pindex] for k, v in sp.items()}
    for k in ("train", "validation", "test"):
        splits.setdefault(k, [])
    train_rows = np.array(sorted(splits["train"]), dtype=np.int64)
    is_train = np.zeros(n_pat, bool)
    is_train[train_rows] = True
    say(f"  cohort {n_pat:,} patients | train={len(splits['train']):,} "
        f"val={len(splits['validation']):,} test={len(splits['test']):,}")

    if args.positive_control:
        X = smart_baseline_features(args.smart_csv, pids)
        say(f"  POSITIVE CONTROL: {X.shape[1]} numeric SMART baseline features "
            f"(diagnostic reference, not a baseline-free model)")
        finish(args, out_dir, X, cohort, splits, train_rows, LM, H, say, log, [], ctrl=True)
        return

    num_specs = parse_specs(args.numeric_pivot, 2)
    occ_specs = parse_specs(args.occurrence_pivot, 2)
    aggs = [a.strip() for a in args.aggregators.split(",") if a.strip()]
    for a in aggs:
        if a not in AGGS:
            raise SystemExit(f"--aggregators must come from {AGGS}")

    csvs = sorted(Path(args.event_csv_folder).glob("*.csv"))
    if not csvs:
        raise SystemExit(f"no CSVs in {args.event_csv_folder}")
    blocks = []

    for path in csvs:
        stem, num_spec, occ_cols, wide = source_roles(
            path, num_specs, occ_specs,
            auto_occurrence=args.auto_occurrence, max_card=args.auto_occurrence_max_card)
        if not (num_spec or occ_cols or wide):
            say(f"  {stem}: no usable columns, skipped")
            continue

        # ---- pass 1: code vocabulary and TRAIN coverage (selection never sees val/test)
        cov = defaultdict(lambda: defaultdict(set))   # role_key -> code -> train pids
        need = [ID, TIME] + ([num_spec[0], num_spec[1]] if num_spec else []) \
               + [c for c, _ in occ_cols]
        if num_spec or occ_cols:
            for chunk in iter_chunks(path, usecols=sorted(set(need))):
                dd = pd.to_numeric(chunk[TIME], errors="coerce")
                keep = dd.notna() & (dd < LM)
                if not keep.any():
                    continue
                pr = chunk[ID][keep].map(pindex)
                tr = pr.notna() & pr.astype("Float64").apply(
                    lambda i: bool(is_train[int(i)]) if pd.notna(i) else False)
                if num_spec:
                    cc = chunk[num_spec[0]][keep].astype(str).str.strip()
                    vv = pd.to_numeric(chunk[num_spec[1]][keep], errors="coerce")
                    ok = tr & vv.notna() & cc.notna()
                    for code, p in zip(cc[ok], pr[ok].astype(int)):
                        cov[("numeric", num_spec[0])][code].add(p)
                for col, prefix in occ_cols:
                    cc = chunk[col][keep].astype(str).str.strip()
                    if prefix:
                        cc = cc.str.slice(0, prefix)
                    ok = tr & cc.notna() & (cc != "nan")
                    for code, p in zip(cc[ok], pr[ok].astype(int)):
                        cov[("occurrence", col)][code].add(p)
                del chunk
            gc.collect()

        roles = ([("numeric", num_spec[0], num_spec)] if num_spec else []) + \
                [("occurrence", col, (col, prefix)) for col, prefix in occ_cols]
        for kind, col, spec in roles:
            counts = {c: len(s) for c, s in cov[(kind, col)].items()}
            kept = sorted((c for c, n in counts.items() if n >= args.min_patients),
                          key=lambda c: (-counts[c], str(c)))
            dropped_cov = len(counts) - len(kept)
            if len(kept) > args.max_codes_per_source:
                say(f"  {stem}.{col} [{kind}]: capping {len(kept)} -> "
                    f"{args.max_codes_per_source} codes by train coverage")
                kept = kept[:args.max_codes_per_source]
            say(f"  {stem}.{col} [{kind}]: {len(counts):,} distinct codes -> kept {len(kept):,} "
                f"(>= {args.min_patients} train patients; {dropped_cov:,} below the floor)")
            if kept:
                # occurrence blocks only ever need counts, so allocate 1 array not 9
                blocks.append((Block(f"{stem}.{col}", kept, n_pat, kind, lean=(kind == "occurrence")),
                               path, kind, spec, None))

        if wide:
            say(f"  {stem} [wide]: {len(wide)} numeric columns aggregated directly")
            blocks.append((Block(f"{stem}.wide", wide, n_pat, "numeric"), path, "wide", None, None))

    if not blocks:
        raise SystemExit("no feature blocks survived the coverage floor — lower --min-patients")

    # ---- pass 2: accumulate statistics per (patient, code)
    for block, path, kind, spec_cols, prefix in blocks:
        stem = Path(path).stem
        if kind == "wide":
            need = [ID, TIME] + block.codes
        elif kind == "numeric":
            need = [ID, TIME, spec_cols[0], spec_cols[1]]
        else:
            need = [ID, TIME, spec_cols[0]]
        print(f"  accumulating {block.source} ...", flush=True)
        for chunk in iter_chunks(path, usecols=sorted(set(need))):
            dd = pd.to_numeric(chunk[TIME], errors="coerce")
            keep = dd.notna() & (dd < LM)
            if not keep.any():
                continue
            pr = chunk[ID][keep].map(pindex)
            ok0 = pr.notna()
            if not ok0.any():
                continue
            t_years = (dd[keep] - LM) / 365.0  # negative: days before the origin
            if kind == "wide":
                for c in block.codes:
                    v = pd.to_numeric(chunk[c][keep], errors="coerce")
                    m = ok0 & v.notna()
                    if not m.any():
                        continue
                    block.update(pr[m].to_numpy(np.int64),
                                 np.full(int(m.sum()), block.cindex[c], np.int64),
                                 t_years[m].to_numpy(), v[m].to_numpy())
            else:
                cc = chunk[spec_cols[0]][keep].astype(str).str.strip()
                pfx = spec_cols[1] if kind == "occurrence" else None
                if pfx:
                    cc = cc.str.slice(0, int(pfx))
                ci = cc.map(block.cindex)
                if kind == "numeric":
                    v = pd.to_numeric(chunk[spec_cols[1]][keep], errors="coerce")
                else:
                    v = pd.Series(1.0, index=cc.index)  # occurrence: count the event
                m = ok0 & ci.notna() & v.notna()
                if not m.any():
                    continue
                block.update(pr[m].to_numpy(np.int64), ci[m].to_numpy(np.int64),
                             t_years[m].to_numpy(), v[m].to_numpy())
            del chunk
        gc.collect()

    # ---- assemble, clip, impute, standardise (all statistics fitted on TRAIN only)
    frames, all_names = [], []
    n_floored = 0
    for block, *_ in blocks:
        cov = block.train_coverage(train_rows)
        keep = cov >= args.min_patients
        n_floored += int((~keep).sum())
        if not keep.any():
            say(f"  {block.source}: every code below the {args.min_patients}-train-patient "
                f"floor, block dropped")
            continue
        df, names = block.features(aggs, keep)
        if len(names):
            frames.append(df)
            all_names += names
    if n_floored:
        say(f"  coverage floor removed {n_floored:,} codes across all blocks "
            f"(applies to wide columns too, not just pivoted codes)")
    if not frames:
        raise SystemExit("no features survived the coverage floor — lower --min-patients")
    X = pd.concat(frames, axis=1)
    X.columns = all_names
    finish(args, out_dir, X, cohort, splits, train_rows, LM, H, say, log, aggs)


def screen_raw(X, cohort, train_rows, H, say, top):
    """Univariate Harrell C on the RAW matrix, BEFORE imputation.

    Screening the written parquet is misleading for low-coverage features: filling the
    unmeasured majority with the train median drags a real signal toward 0.5 (at ~43%
    coverage a true 0.80 presents as ~0.65, and a true 0.65 as ~0.52 — under the noise
    floor). Here the NaNs still exist, so each feature is scored only on the patients who
    actually have it, and its coverage is reported alongside.
    """
    from eda_events_survival import calibrate_null_scale, harrell_c, null_floor
    t_abs = cohort["first_event"].to_numpy(float)[train_rows]
    e_abs = cohort["cd_event"].to_numpy(int)[train_rows]
    cens = [apply_censoring(t, e, H) for t, e in zip(t_abs, e_abs)]
    t = np.array([c[0] for c in cens])
    e = np.array([c[1] for c in cens])
    n_ev = int(e.sum())
    k = calibrate_null_scale(t, e)
    say(f"\n  --- univariate screen on RAW (un-imputed) features, train, horizon {H}d ---")
    say(f"  {n_ev:,} events; each feature scored only on the patients who HAVE it")
    say(f"  permutation-calibrated null: SE(C) = {k:.3f}/sqrt(events) "
        f"(the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)")
    say("  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that")
    say("  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)")
    rows = []
    Xtr = X.iloc[train_rows]
    for c in Xtr.columns:
        v = Xtr[c].to_numpy(float)
        ok = ~np.isnan(v)
        cov = int(ok.sum())
        if cov < 50:
            continue
        ci = harrell_c(t, e, v)[0]
        if ci is None:
            continue
        med = np.nanmedian(v)
        cu = harrell_c(t, e, np.abs(v - med))[0]
        ev_c = int(e[ok].sum())
        thr = null_floor(k, ev_c)
        best = max(abs(ci - 0.5), abs((cu or 0.5) - 0.5))
        rows.append((best - thr, c, ci, cu, cov, ev_c, thr))
    rows.sort(reverse=True)
    n_clear = sum(1 for r in rows if r[0] >= 0)
    say(f"  features clearing their own 2-SE floor (either form): {n_clear:,} of {len(rows):,}")
    say(f"  {'feature':<46s} {'C_mono':>7s} {'C_udev':>7s} {'cov':>7s} {'ev':>6s} {'floor':>6s}")
    for margin, c, ci, cu, cov, ev_c, thr in rows[:top]:
        say(f"  {c[:46]:<46s} {ci:7.4f} {(f'{cu:.4f}' if cu else '   -  '):>7s} "
            f"{cov:7,} {ev_c:6,} {thr:6.3f}" + ("  <-" if margin >= 0 else ""))
    exp = 0.05 * len(rows)
    if not n_clear and len(rows) >= 40:
        say(f"  ** 0 of {len(rows):,} features clear the floor, but ~{exp:.0f} would be expected")
        say("     from pure noise alone. That is ANOMALOUS: suspect degenerate/near-constant")
        say("     columns or over-aggregation rather than concluding 'no signal'. **")
    elif not n_clear:
        say("  ** nothing clears its floor even before imputation: not an imputation artefact **")
    say("")


def finish(args, out_dir, X, cohort, splits, train_rows, LM, H, say, log, aggs, ctrl=False):
    """Clip, impute, standardise (train-only statistics) and write the split parquets.

    Shared by the feature path and --positive-control so both go through byte-identical
    target, split and alignment code — that is what makes the control informative.
    """
    say(f"  raw feature matrix: {X.shape[0]:,} patients x {X.shape[1]:,} features")

    if args.screen_features:
        screen_raw(X, cohort, train_rows, H, say, args.screen_top)

    tr = X.iloc[train_rows]
    if args.clip_quantile > 0:
        lo = tr.quantile(args.clip_quantile)
        hi = tr.quantile(1 - args.clip_quantile)
        X = X.clip(lower=lo, upper=hi, axis=1)   # tames echo's -2e6 outliers
        say(f"  winsorised at train quantiles [{args.clip_quantile}, {1-args.clip_quantile}]")
        tr = X.iloc[train_rows]

    # drop features that are constant or entirely missing on train (no information)
    nunique = tr.nunique(dropna=True)
    dead = [c for c in X.columns if nunique.get(c, 0) < 2]
    if dead:
        X = X.drop(columns=dead)
        say(f"  dropped {len(dead):,} features constant or all-missing on train")
        tr = X.iloc[train_rows]

    med = tr.median(numeric_only=True)
    n_missing = int(X.isna().to_numpy().sum())
    X = X.fillna(med).fillna(0.0)
    mean, std = tr.fillna(med).mean(), tr.fillna(med).std().replace(0.0, 1.0)
    Xs = ((X - mean) / std).fillna(0.0)
    say(f"  imputed {n_missing:,} missing cells with the train median, then standardised")

    feat_names = list(Xs.columns)
    n_feat = len(feat_names)
    dur_abs = cohort["first_event"].to_numpy(float)
    evt_abs = cohort["cd_event"].to_numpy(int)
    for name in ("train", "validation", "test"):
        rows = np.array(sorted(splits[name]), dtype=np.int64)
        if not len(rows):
            say(f"  {name}: EMPTY split, skipped")
            continue
        cens = [apply_censoring(t, e, H) for t, e in zip(dur_abs[rows], evt_abs[rows])]
        ds = Dataset.from_dict({
            "inputs": Xs.iloc[rows].to_numpy(dtype=np.float32).tolist(),
            "duration": [c[0] for c in cens],
            "event": [float(c[1]) for c in cens],
        })
        ds.to_parquet(out_dir / f"{name}.parquet")
        ne = int(sum(c[1] for c in cens))
        say(f"  {name:11s}: {len(rows):5,} patients | events={ne:,} "
            f"({100*ne/max(len(rows),1):.1f}%) | features={n_feat}")

    with open(out_dir / "metadata.json", "w") as f:
        json.dump({
            "representation": "smart_baseline_positive_control" if ctrl else "pivoted_events",
            "landmark_days": LM, "horizon_days": H, "aggregators": aggs,
            "min_patients": args.min_patients, "max_codes_per_source": args.max_codes_per_source,
            "clip_quantile": args.clip_quantile,
            "n_features": n_feat, "feature_names": feat_names,
            "dropped_constant_features": dead,
            "numeric_pivot": None if ctrl else args.numeric_pivot,
            "occurrence_pivot": None if ctrl else args.occurrence_pivot,
            "log": log,
        }, f, indent=2)
    print(f"\nSaved to {out_dir}")
    print(f"Train with:  dataset=smartehr_embeddings dataset.root_path={out_dir} "
          f"model=mlp model.input_size={n_feat}")
    print("(feature_names in metadata.json — use them to interpret the fitted model)")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True, help="Used ONLY for the survival target.")
    p.add_argument("--event-csv-folder", required=True)
    p.add_argument("--split-json", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--landmark-days", type=int, default=0,
                   help="Prediction origin, in days after the SMART baseline. Features use "
                        "datediff < LANDMARK; patients whose outcome is at/before it are dropped; "
                        "survival is measured from it. Matches eda_events_survival.py.")
    p.add_argument("--horizon-days", type=int, default=3650,
                   help="Administrative censoring horizon, measured FROM the landmark. "
                        "Default 3650 (10 years), which the follow-up supports better than 15.")
    p.add_argument("--legacy", action="store_true", help="Use the SMART legacy outcome columns.")
    p.add_argument("--censoring-time", type=int, default=None)
    p.add_argument("--numeric-pivot", default=NUMERIC_PIVOT_DEFAULT,
                   help="Comma-separated src:name_col:value_col. src matches a CSV stem by prefix.")
    p.add_argument("--occurrence-pivot", default=OCCURRENCE_DEFAULT,
                   help="Comma-separated src:code_col[:prefix_len]; prefix_len truncates the code "
                        "(e.g. 4 turns ATC C07AB02 into C07A).")
    p.add_argument("--aggregators", default="last,mean,slope,count",
                   help=f"Subset of {AGGS}. Fewer aggregators means fewer features to overfit.")
    p.add_argument("--min-patients", type=int, default=200,
                   help="Keep a code only if it occurs in at least this many TRAIN patients.")
    p.add_argument("--max-codes-per-source", type=int, default=150,
                   help="Cap on codes kept per source, by train coverage.")
    p.add_argument("--clip-quantile", type=float, default=0.001,
                   help="Winsorise features at these train quantiles; 0 disables.")
    p.add_argument("--auto-occurrence", action="store_true",
                   help="Occurrence-encode EVERY remaining categorical column in EVERY source. "
                        "Without this, sources holding only categorical columns (consult, "
                        "radiologie_verslag, uitgaandebrief, ok_verslag, mri_verslag) contribute "
                        "NO features at all, discarding specialism / exam-type / complication "
                        "information. Long free text is still excluded.")
    p.add_argument("--auto-occurrence-max-card", type=int, default=5000,
                   help="Skip auto-occurrence on columns with more distinct values than this.")
    p.add_argument("--screen-features", action="store_true",
                   help="Print a univariate Harrell C screen of the RAW features before "
                        "imputation, each scored only on the patients who have it. Median-filling "
                        "a low-coverage feature drags its C toward 0.5, so screening the written "
                        "parquet can hide real signal; this does not.")
    p.add_argument("--screen-top", type=int, default=30)
    p.add_argument("--positive-control", action="store_true",
                   help="DIAGNOSTIC: emit ONLY the numeric SMART baseline variables through the "
                        "identical cohort/landmark/split/target code. If this also scores ~0.5 the "
                        "plumbing is broken and any event-feature null is uninterpretable; if it "
                        "scores well, the plumbing is sound. Not a baseline-free model.")
    build(p.parse_args())
