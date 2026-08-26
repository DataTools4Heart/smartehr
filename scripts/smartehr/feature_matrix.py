"""Shared feature-matrix stage: raw screening, standardisation, and split parquet writing.

Lifted out of prepare_pivoted_event_features.py so the structured and free-text arms go
through byte-identical cohort/split/target/standardisation code. That matters for more than
tidiness: this stage has already absorbed several fixes, and duplicating it is the most
likely way to reintroduce one of them.

  * screening happens on the RAW matrix, before imputation — median-filling a low-coverage
    feature drags its C toward 0.5 (at ~43% coverage a true 0.806 reads 0.652), so screening
    the written parquet understates exactly the features most worth finding;
  * standardisation guards std <= 1e-8 rather than std == 0, because dividing a
    near-constant column by 1e-9 explodes it to ~1e9 and swamps a penalised model;
  * appended baseline columns are protected from the constant/coverage filters and
    self-checked, because silently dropping the reference signal makes an arm look like a
    null when it is really a plumbing failure;
  * multiple-testing thresholds use the number of EFFECTIVE independent tests, since
    correlated aggregators of one code are not independent columns.
"""

import json
import math

import numpy as np
import pandas as pd
from datasets import Dataset

from eda_events_survival import (
    ID,
    apply_censoring,
    calibrate_null_scale,
    effective_n_tests,
    harrell_c,
    null_floor,
)
from results_log import emit
from smartehr_pipeline import _SMART_OUTCOME_COLS


# ---------------------------------------------------------------- SMART baseline selection

def select_baseline(cols, spec):
    """Pick baseline columns by case-insensitive substring patterns.

    'leeftijd,geslacht'  -> only those (demographics-only arm)
    '~leeftijd,geslacht' -> everything EXCEPT those (curation-without-demographics arm)
    'all' / empty        -> everything
    """
    if not spec or spec.strip().lower() == "all":
        return list(cols)
    negate = spec.strip().startswith("~")
    pats = [p.strip().lower() for p in spec.lstrip("~").split(",") if p.strip()]
    if not pats:
        return list(cols)

    def hit(c):
        return any(p in c.lower() for p in pats)

    return [c for c in cols if (not hit(c)) == negate]


def smart_baseline_numeric(smart_csv):
    """-> (DataFrame indexed by patient id, column list). Numeric SMART baseline only."""
    df = pd.read_csv(smart_csv)
    if "SmrtRisk" in df.columns:
        df = df[list(df.columns[:df.columns.get_loc("SmrtRisk")])]
    drop = set(_SMART_OUTCOME_COLS) | {ID, "first_event", "cd_event"}
    cols = [c for c in df.columns if c not in drop and pd.api.types.is_numeric_dtype(df[c])]
    return df[[ID] + cols].groupby(ID, as_index=True).first(), cols


def smart_baseline_features(smart_csv, pids, spec=None):
    """Selected numeric SMART baseline columns, aligned to `pids`. -> (DataFrame, kept).

    Used two ways. As a positive control it validates the cohort/split/target plumbing.
    With a column spec it also decomposes WHERE the curated variables' skill comes from:
    the event CSVs contain no age or sex at all, so comparing raw events against the full
    baseline attributes to "expert curation" whatever is really just demographics.
    """
    df, cols = smart_baseline_numeric(smart_csv)
    keep = select_baseline(cols, spec)
    if not keep:
        raise SystemExit(f"baseline column spec {spec!r} matched no numeric baseline column; "
                         "run --list-baseline-cols to see the available names")
    X = df[keep].reindex(pids)
    X.columns = [f"smart_baseline.{c}" for c in X.columns]
    return X.reset_index(drop=True), keep


def list_baseline_cols(smart_csv):
    """Print the numeric baseline columns with coverage, so a spec can be aimed."""
    df, cols = smart_baseline_numeric(smart_csv)
    print(f"{len(cols)} numeric SMART baseline columns in {smart_csv}:\n")
    print(f"  {'column':<34s} {'non-missing':>11s} {'mean':>12s} {'min':>10s} {'max':>10s}")
    for c in cols:
        v = pd.to_numeric(df[c], errors="coerce")
        print(f"  {c[:34]:<34s} {v.notna().sum():11,} {v.mean():12.3f} "
              f"{v.min():10.3f} {v.max():10.3f}")
    print("\nUse these names (case-insensitive substrings) with --baseline-cols /"
          " --add-baseline-cols,")
    print("e.g. --baseline-cols 'leeftijd,geslacht'   (demographics only)")
    print("     --baseline-cols '~leeftijd,geslacht'  (curated variables WITHOUT demographics)")


# ---------------------------------------------------------------- raw (pre-imputation) screen

def screen_raw(X, cohort, train_rows, H, say, top=30):
    """Univariate Harrell C on the RAW matrix, BEFORE imputation.

    Each feature is scored only on the patients who actually have it, against a floor
    scaled to that feature's own subcohort event count, with FDR/Bonferroni over effective
    independent tests. Screening the written parquet instead would understate any
    low-coverage feature, because median-filling the unmeasured majority pulls C to 0.5.
    """
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
    # Screening hundreds of features at an uncorrected 2 SE guarantees false positives:
    # ~5% of pure-noise features clear it. Correct before believing any single hit.
    n_tests = len(rows)
    if not n_tests:
        say("  (no feature had >=50 patients with a value; nothing to screen)\n")
        return
    pvals = []
    for margin, c, ci, cu, cov, ev_c, thr in rows:
        z = (margin + thr) / (thr / 2) if thr > 0 else 0.0
        pvals.append(math.erfc(z / math.sqrt(2)))
    order = np.argsort(pvals)
    bh_cut = 0.0
    for rank, idx in enumerate(order, start=1):
        if pvals[idx] <= 0.05 * rank / n_tests:
            bh_cut = pvals[idx]
    n_eff = effective_n_tests(Xtr.to_numpy(float))
    bonf = 0.05 / max(n_eff, 1)   # correct for INDEPENDENT tests, not nominal columns
    n_bh = sum(1 for pv in pvals if pv <= bh_cut)
    n_bonf = sum(1 for pv in pvals if pv <= bonf)
    say(f"  {n_tests:,} features tested = ~{n_eff:,} independent tests (correlated "
        f"aggregators of the same code) | clearing raw 2-SE: {n_clear:,} "
        f"(~{0.05*n_eff:.0f} expected from noise)")
    say(f"  surviving Benjamini-Hochberg FDR 5%: {n_bh:,} | "
        f"surviving Bonferroni (p<{bonf:.1e}): {n_bonf:,}  <- believe these, not the raw count")
    n_train = max(len(train_rows), 1)
    say(f"  {'feature':<40s} {'C_mono':>7s} {'C_udev':>7s} {'trn%':>6s} {'ev':>5s} "
        f"{'z':>5s} {'sig':>9s}")
    for (margin, c, ci, cu, cov, ev_c, thr), pv in zip(rows[:top],
                                                       [pvals[i] for i in range(min(top, n_tests))]):
        z = (margin + thr) / (thr / 2) if thr > 0 else 0.0
        tag = "BONF" if pv <= bonf else ("FDR" if pv <= bh_cut else ("raw2SE" if margin >= 0 else ""))
        say(f"  {c[:40]:<40s} {ci:7.4f} {(f'{cu:.4f}' if cu else '   -  '):>7s} "
            f"{100*cov/n_train:5.1f}% {ev_c:5,} {z:5.2f} {tag:>9s}")
    say("  trn% is the share of the TRAIN split carrying a value (the screen is train-only);")
    say("  a feature covering a few percent cannot drive a cohort-level model, however real")
    say("  its subcohort signal. Count/indicator features are never missing, so they read 100%.")
    if not n_clear and 0.05 * n_eff >= 3:
        say(f"  ** 0 cleared vs ~{0.05*n_eff:.0f} expected from noise across {n_eff:,} independent")
        say("     tests: mildly surprising, check for flattened columns. **")
    elif not n_clear:
        say("  ** nothing clears its floor even before imputation: not an imputation artefact **")
    say("")


# ---------------------------------------------------------------- assemble and write

def finish(out_dir, X, cohort, splits, train_rows, H, say, log, *,
           clip_quantile=0.001, min_coverage_frac=0.10,
           screen_features=False, screen_top=30,
           rep="features", baseline_cols=(), extra_meta=None):
    """Clip, impute, standardise (train-only statistics) and write the split parquets.

    Every arm goes through this, so cohort/split/target/alignment are identical across
    them — that is what makes the positive control informative.
    """
    say(f"  raw feature matrix: {X.shape[0]:,} patients x {X.shape[1]:,} features")

    if screen_features:
        screen_raw(X, cohort, train_rows, H, say, screen_top)

    tr = X.iloc[train_rows]
    if clip_quantile > 0:
        lo = tr.quantile(clip_quantile)
        hi = tr.quantile(1 - clip_quantile)
        X = X.clip(lower=lo, upper=hi, axis=1)   # tames echo's -2e6 outliers
        say(f"  winsorised at train quantiles [{clip_quantile}, {1-clip_quantile}]")
        tr = X.iloc[train_rows]

    # Appended baseline columns are the reference signal; dropping one silently would make
    # the arm look like a null when it is really a plumbing failure.
    protected = {f"smart_baseline.{c}" for c in baseline_cols}
    # drop features that are constant or entirely missing on train (no information)
    nunique = tr.nunique(dropna=True)
    dead = [c for c in X.columns if nunique.get(c, 0) < 2 and c not in protected]
    if dead:
        X = X.drop(columns=dead)
        say(f"  dropped {len(dead):,} features constant or all-missing on train")
        tr = X.iloc[train_rows]

    med = tr.median(numeric_only=True)
    n_missing = int(X.isna().to_numpy().sum())
    cov_frac = tr.notna().mean()
    thin = [c for c in X.columns
            if cov_frac.get(c, 1.0) < min_coverage_frac and c not in protected]
    if thin:
        X = X.drop(columns=thin)
        say(f"  dropped {len(thin):,} features covered in <{min_coverage_frac:.0%} of train "
            f"(post-imputation they are near-constant and only add noise)")
        tr = X.iloc[train_rows]
        med = tr.median(numeric_only=True)
    X = X.fillna(med).fillna(0.0)
    mean = tr.fillna(med).mean()
    std = tr.fillna(med).std()
    n_tiny = int((std <= 1e-8).sum())
    std = std.where(std > 1e-8, 1.0)   # NOT just ==0: dividing by 1e-9 explodes the column
    Xs = ((X - mean) / std).fillna(0.0)
    if n_tiny:
        say(f"  {n_tiny:,} features had ~zero train variance; left unscaled instead of "
            "divided by ~0 (that would swamp a penalised model)")
    say(f"  imputed {n_missing:,} missing cells with the train median, then standardised")

    feat_names = list(Xs.columns)
    n_feat = len(feat_names)
    if baseline_cols:
        t_a = cohort["first_event"].to_numpy(float)[train_rows]
        e_a = cohort["cd_event"].to_numpy(int)[train_rows]
        cs = [apply_censoring(t, e, H) for t, e in zip(t_a, e_a)]
        tt = np.array([c[0] for c in cs])
        ee = np.array([c[1] for c in cs])
        say("  self-check on the appended baseline columns (each should be clearly off 0.5;")
        say("  if one is missing or ~0.5 the arm is broken, not null):")
        for c in baseline_cols:
            col = f"smart_baseline.{c}"
            if col not in Xs.columns:
                say(f"    {col}: ** ABSENT from the final matrix — this arm is INVALID **")
                continue
            ci = harrell_c(tt, ee, Xs[col].to_numpy(float)[train_rows])[0]
            flag = "" if ci is None or abs(ci - 0.5) > 0.03 else "   ** suspiciously flat **"
            say(f"    {col}: train C={ci:.4f}{flag}")
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

    parts = []
    for name in ("train", "validation", "test"):
        rows = np.array(sorted(splits[name]), dtype=np.int64)
        if len(rows):
            parts.append(f"{name}={len(rows)}/{int(evt_abs[rows].sum())}ev")
    emit("arm={} n_features={} {}", rep, n_feat, " ".join(parts))

    meta = {
        "representation": rep,
        "baseline_cols_included": list(baseline_cols),
        "horizon_days": H,
        "clip_quantile": clip_quantile,
        "min_coverage_frac": min_coverage_frac,
        "n_features": n_feat,
        "feature_names": feat_names,
        "dropped_constant_features": dead,
    }
    meta.update(extra_meta or {})
    meta["log"] = log
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(meta, f, indent=2)
    print(f"\nSaved to {out_dir}")
    print(f"Train with:  dataset=smartehr_embeddings dataset.root_path={out_dir} "
          f"model=mlp model.input_size={n_feat}")
    print("(feature_names in metadata.json — use them to interpret the fitted model)")
    return n_feat
