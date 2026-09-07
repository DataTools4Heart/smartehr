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

import argparse
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


# ---------------------------------------------------------------- curated-variable provenance
#
# The T3 headroom check asks: what do the curated variables achieve when restricted to facts
# our narrative corpus could plausibly contain? That bounds what ANY text method could reach,
# and can end the free-text arm with a mechanism rather than a fourth null.
#
# The answer depends entirely on how the 183 variables are split, so the split is written out
# by name and reviewed against the registry's own labels (data/smartehr/data_dicts/smart.csv)
# rather than guessed from name prefixes. Prefix matching got two groups badly wrong:
# the ~44 medication flags (mht*/mli*/mas*/mgl*) and the disease-onset block (KliMa*) are
# among the MOST chart-derivable variables here — a letter always lists medication and states
# "myocardinfarct in 2003" — yet no sensible prefix rule puts them on the chart side. Both
# errors shrink the chart half, which biases the check toward "no headroom": the conclusion we
# already expect. A check that can only confirm the prior is not worth running.
#
# Groups:
#   CHART      history, diagnoses, medication, smoking/alcohol status, disease onset. A
#              discharge letter or consult note states these in prose.
#   IMAGING    findings our corpus could carry because radiology/MRI reports are IN it:
#              carotid stenosis grade, aortic diameter, kidney size, renal failure. Study
#              measurements in origin, but a report in the record can state the same number.
#   PROTOCOL   exists only because a study visit produced it: research ultrasound (IMT, ABI),
#              anthropometry, study labs, and the questionnaire instruments (SF-36, METs,
#              diet, education, country of birth).
#   DEMOG      age and sex — the floor BOTH halves are measured against, so they belong to
#              neither. Leaving them in one half hands that half 0.673 for free and the
#              comparison measures nothing.
#   ADMIN      identifiers and dates, carried only so the partition can be proved exhaustive.
#
# The generous chart half is CHART + IMAGING: if even that cannot beat demographics, no text
# method can, and the negative is structural. CHART alone is the strict variant, reported
# alongside so the assignment of the arguable group is visibly not doing the work.

CURATED_CHART = {
    # first vascular diagnosis and disease at inclusion
    "diagnsco", "vaatzkt1", "DiagSide", "IncInt_p", "IncInt_v", "klinman",
    # symptom history
    "V0402", "V0405",
    # histories: per-territory questionnaire, operation, total, and ever-composite
    "vg_0410", "vgok_car", "vgt_kop", "vz_kop",
    "vg_0321", "vg_0323", "vgok_har", "vgt_hart", "vz_hart",
    "vg_0325", "vgok_aaa", "vgt_aaa", "vz_aaa",
    "vg_0606c", "vgok_nie", "vgt_nier", "vz_nier",
    "vg_0519", "vgok_bee", "vgt_been", "vz_been",
    # disease labels a letter states, and the reported-treatment questionnaire items.
    # NB the _n/_b pair splits: hyptns_n is derived from the MEASURED pressure (protocol),
    # hyptns_b is "behandeling; vraag 6.03" — reported treatment (chart). Same for the
    # hyperglycaemia and hyperlipidaemia pairs.
    "vz_hypt", "hyptns_b", "vz_DM", "vz_t1d", "vz_t2d", "hypgly_b",
    "vz_HypLp", "hyplip_b", "VgBh_HpL",
    # smoking and alcohol status, including the graded forms — packyrs is the grading test
    "roken", "packyrs", "alcohol", "AlchlGlz",
    # medication: the most chart-derivable data in any EHR
    "mht01", "mht02", "mht02a", "mht02b", "mht02c", "mht02d", "mht03", "mht04", "mht05",
    "mht06", "mht07", "mht12", "mht33", "mht41", "mht_all", "mht_alln",
    "mliphoop", "mli01", "mli02", "mli03", "mli04", "lipmid", "statine",
    "mas01", "mas01a", "mas01b", "mas01c", "mas01d", "mas02", "mas02a", "mas02b", "mas02c",
    "mas03", "pamid", "aspirine", "pa_stolmid",
    "mgl01", "mgl02", "mgl03", "mmpr", "mhmc",
    "TCA", "SSRI", "MAO", "OthADep", "Benzo", "BenzoDer", "BenzoRel",
    "Thyr", "Amiodar", "Lithium",
    # onset and duration of clinically manifest vascular disease ("MI in 2003")
    "KliMaC", "KliMaYr", "KliMaDur", "KliMaDrD",
}

CURATED_IMAGING = {
    "stenACIr", "stenACIl", "csten_50", "csten_70",
    "AortProx", "AortDist", "aorta_hg", "aorta_gm", "aaaech_n",
    "nrlng_re", "nrlng_li", "nrlng_gm", "nratrof",
    "nrvol_re", "nrvol_li", "nrvol_gm",
    "nrfaln_n",
}

CURATED_PROTOCOL = {
    # questionnaire instruments that never appear in a clinical letter
    "opleiding", "RespLand", "PaLand", "MaLand", "WereldDl",
    "V0821", "V082201", "V082202", "V0823",
    "kl1fysfc", "kl2socfc", "kl3rolfy", "kl4rolem", "kl5mengz", "kl6vital", "kl7pijn",
    "kl8alggz", "kl9gezva",
    "spMEThw", "acMEThw", "bwMEThw",
    # measured pressure and its derived flag
    "bdsys", "bddia", "plsprs", "hyptns_n",
    # anthropometry
    "gewicht", "lengte", "bm_indx", "bmi_30", "tail_gm", "heup_gm", "tlhp_rat",
    "vet_subc", "vet_gm",
    # research ultrasound: ankle-brachial index and carotid intima-media thickness
    "abi_lg", "abi_gm", "abivrl_n", "ABiRe", "ABiLi", "imt_gm",
    # study labs and everything derived from them
    "labgluc", "hypgly_n", "labhb", "labht", "labchol", "labtrig", "labhdl", "ldlchol",
    "hyplip_n", "labkrea", "labmalb", "labkrur", "mpkr_rat", "AlbCr", "albminur",
    "klar_coc", "klar_gst", "MDRD", "labhcyst", "hyphmc_n", "labins", "labtsh",
    "labcrp", "labhba1c", "labapob",
    # metabolic-syndrome criteria, counted from the measurements above
    "MBSc", "MBS", "MBSc_mis", "MBScgr",
}

CURATED_DEMOG = {"leeftijd", "geslacht"}
CURATED_ADMIN = {"studienr", "IncDatum", "IncInt_d", "abidatum", "afkapdat"}

CURATED_GROUPS = {
    "chart": CURATED_CHART | CURATED_IMAGING,   # the generous half: what text COULD contain
    "chart_strict": CURATED_CHART,              # history/meds/diagnoses only
    "imaging": CURATED_IMAGING,
    "protocol": CURATED_PROTOCOL,               # complement of `chart`, demographics aside
    "demographics": CURATED_DEMOG,
}


# ---------------------------------------------------------------- SMART baseline selection

def select_baseline(cols, spec, say=None):
    """Pick baseline columns by case-insensitive substring patterns, or by provenance group.

    'leeftijd,geslacht'  -> only those (demographics-only arm)
    '~leeftijd,geslacht' -> everything EXCEPT those (curation-without-demographics arm)
    'all' / empty        -> everything
    'group:chart'        -> a named provenance group (see CURATED_GROUPS); '~group:chart'
                            gives its complement.

    Groups select by EXACT name, not substring, because the headroom check's whole value
    rests on the split being reviewable: a substring rule cannot express that `hyptns_b`
    (reported treatment) is chart-derivable while `hyptns_n` (derived from the measured
    pressure) is not, and it silently mis-sorted the 44 medication flags.
    """
    if not spec or spec.strip().lower() == "all":
        return list(cols)
    spec = spec.strip()
    negate = spec.startswith("~")
    body = spec.lstrip("~").strip()
    if body.lower().startswith("group:"):
        # 'group:chart' or 'group:chart,leeftijd,geslacht' — the group plus exact extras,
        # which is how a half gets its +demographics comparator without loosening the
        # exact-name rule into substring matching again.
        parts = [t.strip() for t in body.split(":", 1)[1].split(",") if t.strip()]
        return _select_group(cols, parts[0], negate, say, extra=parts[1:])
    pats = [p.strip().lower() for p in spec.lstrip("~").split(",") if p.strip()]
    if not pats:
        return list(cols)

    def hit(c):
        return any(p in c.lower() for p in pats)

    return [c for c in cols if (not hit(c)) == negate]


def _select_group(cols, name, negate, say=None, extra=()):
    """Exact-name selection from CURATED_GROUPS, with an exhaustiveness audit.

    The audit is the point. A curated variable that belongs to no group would silently
    vanish from both halves of the headroom check, and the two halves would no longer sum
    to the full baseline whose 0.7394 they are being compared against — so an unassigned
    column is a hard error naming the offenders, not a warning.
    """
    if name not in CURATED_GROUPS:
        raise SystemExit(f"unknown baseline group {name!r}; available: "
                         f"{', '.join(sorted(CURATED_GROUPS))}")
    known = CURATED_CHART | CURATED_IMAGING | CURATED_PROTOCOL | CURATED_DEMOG | CURATED_ADMIN
    unassigned = [c for c in cols if c not in known]
    if unassigned:
        raise SystemExit(
            f"{len(unassigned)} numeric baseline columns belong to no provenance group, so "
            f"the chart/protocol split would not be exhaustive: {unassigned}\n"
            "Add each to CURATED_CHART, CURATED_IMAGING, CURATED_PROTOCOL, CURATED_DEMOG "
            "or CURATED_ADMIN in feature_matrix.py (the registry labels are in "
            "data/smartehr/data_dicts/smart.csv).")
    want = set(CURATED_GROUPS[name])
    unknown_extra = [e for e in extra if e not in cols]
    if unknown_extra:
        raise SystemExit(f"--baseline-cols group:{name} named extra columns that do not "
                         f"exist: {unknown_extra}; run --list-baseline-cols for the names")
    want |= set(extra)
    keep = [c for c in cols if (c not in want) == negate]
    if say:
        # Demographics and admin sit in neither half, so a complement is not the other half.
        excl = [c for c in cols if c in (CURATED_DEMOG | CURATED_ADMIN) and c not in want]
        say(f"  baseline group {'~' if negate else ''}{name}"
            f"{'+' + ','.join(extra) if extra else ''}: {len(keep)} of {len(cols)} "
            f"numeric baseline columns")
        if not negate:
            say(f"  members: {keep}")
        if excl:
            say(f"  age/sex and admin columns are in NEITHER half by design ({len(excl)}: "
                f"{excl}) — leaving them in one half would hand it ~0.673 for free")
    return keep


def list_baseline_groups(smart_csv):
    """Print the provenance partition for clinical review, with per-group membership."""
    _, cols = smart_baseline_numeric(smart_csv)
    known = CURATED_CHART | CURATED_IMAGING | CURATED_PROTOCOL | CURATED_DEMOG | CURATED_ADMIN
    named = [("chart (history/diagnoses/medication)", CURATED_CHART),
             ("imaging (report-derivable findings)", CURATED_IMAGING),
             ("protocol (study visit only)", CURATED_PROTOCOL),
             ("demographics (neither half)", CURATED_DEMOG),
             ("admin (ids/dates, neither half)", CURATED_ADMIN)]
    print(f"{len(cols)} numeric SMART baseline columns, by provenance:\n")
    for label, grp in named:
        present = [c for c in cols if c in grp]
        print(f"--- {label}: {len(present)}")
        for i in range(0, len(present), 6):
            print("      " + ", ".join(present[i:i + 6]))
    unassigned = [c for c in cols if c not in known]
    print(f"\nunassigned: {len(unassigned)}" + (f" -> {unassigned}" if unassigned else " (partition is exhaustive)"))
    print("\nThe generous chart half is chart+imaging ('group:chart'); 'group:chart_strict'")
    print("drops the imaging findings. 'group:protocol' is what only a study visit produced.")


def smart_baseline_numeric(smart_csv):
    """-> (DataFrame indexed by patient id, column list). Numeric SMART baseline only."""
    df = pd.read_csv(smart_csv)
    if "SmrtRisk" in df.columns:
        df = df[list(df.columns[:df.columns.get_loc("SmrtRisk")])]
    drop = set(_SMART_OUTCOME_COLS) | {ID, "first_event", "cd_event"}
    cols = [c for c in df.columns if c not in drop and pd.api.types.is_numeric_dtype(df[c])]
    return df[[ID] + cols].groupby(ID, as_index=True).first(), cols


def smart_baseline_features(smart_csv, pids, spec=None, say=None):
    """Selected numeric SMART baseline columns, aligned to `pids`. -> (DataFrame, kept).

    Used two ways. As a positive control it validates the cohort/split/target plumbing.
    With a column spec it also decomposes WHERE the curated variables' skill comes from:
    the event CSVs contain no age or sex at all, so comparing raw events against the full
    baseline attributes to "expert curation" whatever is really just demographics.
    """
    df, cols = smart_baseline_numeric(smart_csv)
    keep = select_baseline(cols, spec, say)
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


def handle_listing_flags(argv):
    """Serve the --list-baseline-* flags from --smart-csv alone, before the main parser.

    These flags only inspect the SMART registry, but both builders mark --out-dir, --mode,
    --event-csv-folder and --split-json required, so argparse would reject a listing
    command for missing arguments the listing never uses. Returns True when it handled the
    request and the caller should stop.
    """
    if not ({"--list-baseline-cols", "--list-baseline-groups"} & set(argv)):
        return False
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--smart-csv", required=True)
    pre.add_argument("--list-baseline-cols", action="store_true")
    pre.add_argument("--list-baseline-groups", action="store_true")
    a, _ = pre.parse_known_args(argv)
    if a.list_baseline_groups:
        list_baseline_groups(a.smart_csv)
    else:
        list_baseline_cols(a.smart_csv)
    return True


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
