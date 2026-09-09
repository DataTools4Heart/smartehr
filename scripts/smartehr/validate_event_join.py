"""Is the event data joined to the right patients? No text, no extraction, no outcome.

WHY THIS EXISTS. The graded text arm's join control failed: extracted sex agrees with the
registry at 0.506 on 2,619 patients (chance) and extracted age at rho -0.004. Two causes
survive and they need opposite responses -- the documents are attached to the wrong
patients, or the extractors are noise -- and the sex marginals did not separate them
cleanly (extracted P(male) 0.553 against a registry 0.653, with my own threshold at 0.12).

This check removes the extractor from the question entirely. Several quantities are measured
BOTH in the routine EHR event stream and at the SMART study visit, so per-patient agreement
between the two is a direct test of the identifier join, with no language processing in the
path:

  meting.Gewicht     (Weight, 121,417 rows)   <->  gewicht   "Gewicht (kg.)"
  meting.Lengte      (Height, 68,918 rows)    <->  lengte    "Lengte (m.)"
  meting.BMI         (19,229 rows)            <->  bm_indx   "Body mass index (kg./m.^2)"
  lab_ezis.Creat-BL  (Creatinine, 149,294)    <->  labkrea   "Kreatinine bloed (umol/l.)"
  lab_ezis.Chol-BL   (Cholesterol, 44,236)    <->  labchol   "Cholesterol (mmol/l.)"

Every code string above is taken from the project's own dictionaries -- meting.csv and
lab.csv give the event codes, smart.csv gives the registry labels and units -- so no code
name here is guessed.

Weight is the sharpest of them: a person's weight is stable over years, it is recorded
121,417 times, and it needs no interpretation. If routine weight does not agree with study
weight for the same patient identifier, the join is broken.

Spearman is used throughout, so a unit difference (cm versus m) cannot affect the verdict;
both medians are printed anyway so a unit mismatch is visible rather than silent.

WHAT THE ANSWER MEANS
  rho high (> 0.7 for weight)  the identifier join is sound. The structured arm's null
                               stands, and the text arm's failure is specific to the
                               document cache or to the extractors.
  rho ~ 0                      the join is broken for event data generally. Then BOTH
                               arms' nulls measure plumbing, and every event and text
                               result in this project has to be withdrawn.

    python scripts/smartehr/validate_event_join.py --smart-csv S --event-csv-folder E
"""

import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import ID, TIME
from feature_matrix import smart_baseline_numeric
from diagnose_normalization import find_id, read_any   # encoding/delimiter sniffing
from graded_concepts import CURATED_MISSING, _spearman
from results_log import add_results_arg, emit, results_block

CHUNK = 200_000

# (event file prefix, code column, code value, value column, registry column, label).
# Code strings from data/smartehr/data_dicts/{meting,lab}.csv; registry names and units
# from smart.csv. Nothing here is invented.
PAIRS = (
    ("meting",   "label",         "Gewicht",  "data1",      "gewicht", "weight kg"),
    ("meting",   "label",         "Lengte",   "data1",      "lengte",  "height (m vs cm)"),
    ("meting",   "label",         "BMI",      "data1",      "bm_indx", "BMI"),
    ("lab_ezis", "lab_testcode",  "Creat-BL", "lab_result", "labkrea", "creatinine umol/l"),
    ("lab_ezis", "lab_testcode",  "Chol-BL",  "lab_result", "labchol", "cholesterol mmol/l"),
)


def nearest_baseline_value(folder, prefix, code_col, code, val_col, landmark, say):
    """Per patient, the value measured closest to the baseline visit. -> {pid: value}."""
    path = next((p for p in sorted(Path(folder).glob("*.csv")) if p.stem.startswith(prefix)),
                None)
    if path is None:
        say(f"    no {prefix}*.csv in {folder}, skipped")
        return {}
    head = pd.read_csv(path, nrows=0)
    need = [c for c in (ID, TIME, code_col, val_col) if c in head.columns]
    if len(need) < 4:
        say(f"    {path.stem}: missing one of {ID}/{TIME}/{code_col}/{val_col}, skipped")
        return {}
    best = {}
    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False, usecols=need):
        sub = chunk[chunk[code_col].astype(str).str.strip().str.lower() == code.lower()]
        if sub.empty:
            continue
        dd = pd.to_numeric(sub[TIME], errors="coerce")
        v = pd.to_numeric(sub[val_col], errors="coerce")
        pid = pd.to_numeric(sub[ID], errors="coerce")
        ok = dd.notna() & v.notna() & pid.notna() & (dd < landmark)
        for p, d, x in zip(pid[ok].astype(int), dd[ok].abs(), v[ok]):
            prev = best.get(p)
            if prev is None or d < prev[0]:
                best[p] = (d, float(x))
    return {p: x for p, (d, x) in best.items()}


def all_values(folder, prefix, code_col, code, val_col, landmark, say):
    """EVERY pre-landmark reading per patient. -> {pid: [values]}.

    The single-reading version below answers "does the one measurement nearest baseline
    agree?", which invites a fair objection: one reading could be an outlier, a wrong value
    slot, or a unit mixture, and a single noisy value attenuates any correlation. These
    sources are longitudinal -- meting holds 121,417 weight rows for ~15,800 patients -- so
    the whole timeline is available and the join should be tested against all of it.
    """
    path = next((p for p in sorted(Path(folder).glob("*.csv")) if p.stem.startswith(prefix)),
                None)
    if path is None:
        return {}
    head = pd.read_csv(path, nrows=0)
    need = [c for c in (ID, TIME, code_col, val_col) if c in head.columns]
    if len(need) < 4:
        return {}
    out = {}
    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False, usecols=need):
        sub = chunk[chunk[code_col].astype(str).str.strip().str.lower() == code.lower()]
        if sub.empty:
            continue
        dd = pd.to_numeric(sub[TIME], errors="coerce")
        v = pd.to_numeric(sub[val_col], errors="coerce")
        pid = pd.to_numeric(sub[ID], errors="coerce")
        ok = dd.notna() & v.notna() & pid.notna() & (dd < landmark)
        for p, x in zip(pid[ok].astype(int), v[ok]):
            out.setdefault(p, []).append(float(x))
    return out


def whole_timeline_check(a, say):
    """Test the join against EVERY reading, not just the one nearest baseline.

    Three progressively more generous tests, so that a negative cannot be blamed on the
    aggregation:

      1. nearest baseline  -- one reading (what the headline check used)
      2. median            -- robust to outliers, wrong value slots and unit strays
      3. BEST CASE         -- per patient, the SMALLEST absolute difference between ANY of
                              their readings and their registry value. This gives the join
                              every possible chance: if even one of a patient's weights
                              matches their registry weight, it shows here. Read against the
                              same statistic under a permutation, which is the floor.

    If the best case is no better than the permuted floor, no aggregation choice can rescue
    the join, and the objection "you only compared one measurement" is answered.
    """
    cur, _cols = smart_baseline_numeric(a.smart_csv)
    say("\n=== whole-timeline check: every reading, not just the nearest " + "=" * 11)
    for prefix, code_col, code, val_col, reg, label in PAIRS:
        if reg not in cur.columns:
            continue
        vals = all_values(a.event_csv_folder, prefix, code_col, code, val_col,
                          a.landmark_days, say)
        if not vals:
            continue
        rv = pd.to_numeric(cur[reg], errors="coerce")
        rv = rv.where(~rv.isin(CURATED_MISSING.get(reg, ())))
        pids = [p for p in vals if p in rv.index and not pd.isna(rv.loc[p])]
        if len(pids) < 30:
            continue
        counts = np.array([len(vals[p]) for p in pids])
        c = np.array([float(rv.loc[p]) for p in pids], float)
        near = np.array([vals[p][0] for p in pids], float)      # first pre-landmark reading
        med = np.array([float(np.median(vals[p])) for p in pids], float)
        # best case: the reading closest to this patient's own registry value
        best = np.array([min(abs(x - cv) for x in vals[p]) for p, cv in zip(pids, c)], float)
        rng = np.random.default_rng(0)
        cperm = rng.permutation(c)
        bestp = np.array([min(abs(x - cv) for x in vals[p]) for p, cv in zip(pids, cperm)],
                         float)
        say(f"\n  {prefix}.{code} vs {reg}  ({len(pids):,} patients)")
        say(f"    readings per patient: median {int(np.median(counts))}, "
            f"p90 {int(np.percentile(counts, 90))}, max {int(counts.max())}, "
            f"total {int(counts.sum()):,}")
        # a unit mixture would show as a second mode far from the first
        allv = np.concatenate([np.asarray(vals[p], float) for p in pids])
        say(f"    value range p1/p50/p99: {np.percentile(allv, 1):.1f} / "
            f"{np.percentile(allv, 50):.1f} / {np.percentile(allv, 99):.1f}")
        for nm, arr in (("first reading", near), ("median of all", med)):
            rho = _spearman(arr, c)
            say(f"    rho({nm:<14s}) = {(f'{rho:+.3f}' if rho is not None else '   -  ')}")
        say(f"    BEST CASE |closest reading - registry|: median {np.median(best):.2f}, "
            f"under permutation {np.median(bestp):.2f}")
        emit("whole-timeline {} vs {}: n={} readings={} rho(median)={} | best-case closest "
             "match median {:.2f} vs {:.2f} permuted", f"{prefix}.{code}", reg, len(pids),
             int(counts.sum()),
             f"{_spearman(med, c):+.3f}" if _spearman(med, c) is not None else "-",
             float(np.median(best)), float(np.median(bestp)))
        if np.median(best) < 0.6 * np.median(bestp):
            emit("** {} SHOWS REAL AGREEMENT once the whole timeline is used **: the "
                 "closest reading per patient is much nearer the registry value than "
                 "permutation gives, so the join is NOT dead for this quantity",
                 f"{prefix}.{code}")
            say("    ** this quantity DOES agree when all readings are used -- revisit **")


# Sex-specific lab tests, from data/smartehr/data_dicts/lab.csv. A CATEGORICAL join test:
# it needs no units, no scale and no aggregation choice, which is what makes it the easiest
# version of this evidence to state. Codes and row counts are the dictionary's own.
SEX_TESTS = (
    ("PSAtot-BL",       1, "Totaal PSA (5,312 rows)"),
    ("PSAvrij-BL",      1, "Vrij PSA (367)"),
    ("PSAratio-BL",     1, "PSA F/T-ratio (349)"),
    ("PSAtot_plasma-BL", 1, "Totaal PSA plasma (80)"),
    ("Zwanger-UP",      2, "Zwangerschapstest (52)"),
    ("AMH-BL",          2, "Anti-Mullerian Hormoon (93)"),
)
SEX_LABEL = {1: "Man", 2: "Vrouw"}


def sex_via_specific_tests(a, say):
    """Do patients given a sex-specific test have that sex in the registry?

    Answers "can the join be checked on gender?" -- yes, and more cleanly than on any
    continuous quantity, because there is nothing to aggregate, no unit to reconcile and no
    outlier to argue about. PSA is prostate-specific: a patient with a PSA result is male,
    give or take a rare exception.

    Under a CORRECT join the male fraction among PSA-tested patients should be ~0.98+.
    Under a broken join it can only be the cohort base rate, because the tested set is then
    an arbitrary sample of patients. The z-score below is against that base rate, so it
    measures exactly the excess a working join would produce.
    """
    cur, _cols = smart_baseline_numeric(a.smart_csv)
    if "geslacht" not in cur.columns:
        say("  registry has no `geslacht`; cannot check sex")
        return
    g = pd.to_numeric(cur["geslacht"], errors="coerce")
    g = g.where(~g.isin((9,)))                      # 9 -> Missend, per smart.csv
    base_m = float((g == 1).mean(skipna=True))
    say("\n=== sex check: do sex-specific lab tests land on that sex? " + "=" * 13)
    say(f"  registry base rate: P(Man)={base_m:.3f} on {int(g.notna().sum()):,} patients")
    say(f"  {'test':<20s} {'implies':<7s} {'patients':>9s} {'observed':>9s} "
        f"{'expected':>9s} {'z':>7s}")
    path = next((p for p in sorted(Path(a.event_csv_folder).glob("*.csv"))
                 if p.stem.startswith("lab_ezis")), None)
    if path is None:
        say("  no lab_ezis*.csv found")
        return
    head = pd.read_csv(path, nrows=0)
    code_col = next((c for c in head.columns if c.strip().lower() == "lab_testcode"), None)
    if code_col is None or ID not in head.columns:
        say(f"  {path.name}: need lab_testcode and {ID}")
        return
    wanted = {c.lower(): (sex, lab) for c, sex, lab in SEX_TESTS}
    seen = {c: set() for c in wanted}
    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False,
                             usecols=[ID, code_col]):
        codes = chunk[code_col].astype(str).str.strip().str.lower()
        pid = pd.to_numeric(chunk[ID], errors="coerce")
        for c in wanted:
            hit = codes == c
            if hit.any():
                seen[c].update(int(x) for x in pid[hit].dropna())
    rows = []
    for c, (sex, lab) in wanted.items():
        pats = [p for p in seen[c] if p in g.index and not pd.isna(g.loc[p])]
        if len(pats) < 20:
            say(f"  {lab[:20]:<20s} {SEX_LABEL[sex]:<7s} {len(pats):>9,}   too few")
            continue
        vals = np.array([float(g.loc[p]) for p in pats])
        obs = float((vals == sex).mean())
        exp = base_m if sex == 1 else 1 - base_m
        se = math.sqrt(max(exp * (1 - exp), 1e-9) / len(pats))
        z = (obs - exp) / se
        say(f"  {lab[:20]:<20s} {SEX_LABEL[sex]:<7s} {len(pats):>9,} {obs:>9.3f} "
            f"{exp:>9.3f} {z:>+7.1f}")
        rows.append((c, sex, len(pats), obs, exp, z))
        emit("sex check {} (implies {}): {} patients, observed {:.3f} vs base rate {:.3f} "
             "(z={:+.1f})", c, SEX_LABEL[sex], len(pats), obs, exp, z)
    if not rows:
        say("  no sex-specific test had enough patients to check")
        return
    # PSA carries the weight: it is the only one with thousands of patients.
    psa = [r for r in rows if r[0].startswith("psa")]
    lead = max(psa, key=lambda r: r[2]) if psa else max(rows, key=lambda r: r[2])
    if lead[3] >= 0.90 and lead[5] > 3:
        emit("** SEX CHECK PASSES **: {:.1f}% of {} patients given {} are recorded {} "
             "against a base rate of {:.1f}%, so the join carries real patient identity",
             100 * lead[3], lead[2], lead[0], SEX_LABEL[lead[1]], 100 * lead[4])
        say("\n  -> The sex check PASSES: the join carries real patient identity.")
    else:
        emit("** SEX CHECK FAILS **: only {:.1f}% of {} patients given {} are recorded {}, "
             "against a base rate of {:.1f}% (z={:+.1f}) -- a prostate-specific test lands "
             "on the cohort's sex ratio, which is what an arbitrary sample of patients "
             "gives. Categorical confirmation of the broken join, with no units, no "
             "aggregation and no outliers involved",
             100 * lead[3], lead[2], lead[0], SEX_LABEL[lead[1]], 100 * lead[4], lead[5])
        say("\n  ** The sex check FAILS: a prostate-specific test lands on the cohort's own")
        say("     sex ratio. Categorical confirmation, with nothing to aggregate. **")


def demographics_probe(a, say):
    """Inspect a demographics extract, if one is reachable, and check sex/age against it.

    Age cannot be checked from the 16 EHR event extracts: none of them carries an age or a
    birth date (data_dict.csv documents only clinical columns plus the patient id). The one
    candidate is the separate UCN delivery's `UCN_PATIENT_DEMOGRAFISCH.csv`, described there
    as "Demographics data", which this project has never read.

    Its schema is unknown here, so this function reports what the file holds before trying
    anything: columns, and which of them look like an identifier, a sex and a birth year.
    That report is useful on its own -- if the file carries a patient id and a sex, it gives
    both a direct sex check and, via birth year, the age check that the event extracts
    cannot support. It may also reveal WHICH id space it uses, which would be a bridge.
    """
    cands = []
    if a.demographics_file:
        cands.append(Path(a.demographics_file))
    for base in (Path(a.event_csv_folder), Path(a.event_csv_folder).parent):
        cands += sorted(base.glob("*DEMOGRAFISCH*.csv")) + sorted(base.glob("*demograf*.csv"))
    path = next((p for p in cands if p.exists()), None)
    say("\n=== demographics extract (the only route to an AGE check) " + "=" * 14)
    if path is None:
        say("  not found. Age cannot be checked from the 16 event extracts: none carries an")
        say("  age or birth date. If UCN_PATIENT_DEMOGRAFISCH.csv can be made available,")
        say("  pass it with --demographics-file and this will report what it holds.")
        emit("demographics extract not found: age is not checkable from the event files, "
             "which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only "
             "candidate and was not reachable")
        return
    df, enc, sep = read_any(path, nrows=20000, say=say)
    if df is None:
        return
    say(f"  {path.name}: encoding={enc} sep={sep} rows(sampled)={len(df):,} "
        f"cols={df.shape[1]}")
    say(f"  columns: {list(df.columns)[:24]}")
    idc = find_id(df)
    # a sex column holds two dominant values from a small known vocabulary
    sexc = None
    for c in df.columns:
        v = df[c].astype(str).str.strip().str.lower()
        vc = v[v != ""].value_counts()
        if 2 <= len(vc) <= 3 and set(vc.index[:2]) <= {"1", "2", "m", "v", "f", "man",
                                                       "vrouw", "male", "female"}:
            sexc = c
            break
    # a birth column holds plausible years, or dates whose year is plausible
    birthc = None
    for c in df.columns:
        yr = pd.to_numeric(df[c].astype(str).str.extract(r"(\d{4})", expand=False),
                           errors="coerce")
        if yr.notna().mean() > 0.8 and 1900 <= yr.median() <= 2010:
            birthc = c
            break
    say(f"  detected: id={idc!r} sex={sexc!r} birth-year-like={birthc!r}")
    emit("demographics extract {}: id={} sex={} birth={}", path.name, idc, sexc, birthc)
    if idc is None or (sexc is None and birthc is None):
        say("  -> not enough to run a check; report the columns above to the data manager.")
        return
    cur, _cols = smart_baseline_numeric(a.smart_csv)
    ids = pd.to_numeric(df[idc], errors="coerce")
    if sexc is not None and "geslacht" in cur.columns:
        g = pd.to_numeric(cur["geslacht"], errors="coerce")
        g = g.where(~g.isin((9,)))
        m = {"1": 1, "m": 1, "man": 1, "male": 1,
             "2": 2, "v": 2, "f": 2, "vrouw": 2, "female": 2}
        dsex = df[sexc].astype(str).str.strip().str.lower().map(m)
        pairs = [(int(i), s) for i, s in zip(ids, dsex)
                 if not pd.isna(i) and not pd.isna(s) and int(i) in g.index
                 and not pd.isna(g.loc[int(i)])]
        if len(pairs) >= 30:
            agree = float(np.mean([g.loc[i] == s for i, s in pairs]))
            say(f"  sex agreement with the registry: {agree:.3f} on {len(pairs):,} patients")
            emit("demographics sex agreement with registry: {:.3f} on {} patients "
                 "(chance is ~0.55 at this cohort's sex ratio)", agree, len(pairs))
    if birthc is not None and "leeftijd" in cur.columns:
        age = pd.to_numeric(cur["leeftijd"], errors="coerce")
        age = age.where(~age.isin((999,)))
        yr = pd.to_numeric(df[birthc].astype(str).str.extract(r"(\d{4})", expand=False),
                           errors="coerce")
        pairs = [(int(i), float(y)) for i, y in zip(ids, yr)
                 if not pd.isna(i) and not pd.isna(y) and int(i) in age.index
                 and not pd.isna(age.loc[int(i)])]
        if len(pairs) >= 30:
            # birth year runs OPPOSITE to age, so a working join gives a NEGATIVE rho
            rho = _spearman([y for _i, y in pairs], [float(age.loc[i]) for i, _y in pairs])
            say(f"  birth-year vs registry age: rho={(f'{rho:+.3f}' if rho else '-')} on "
                f"{len(pairs):,} patients (a working join gives a strong NEGATIVE rho)")
            emit("demographics birth-year vs registry age: rho={} on {} patients "
                 "(negative is correct: older patients were born earlier)",
                 f"{rho:+.3f}" if rho is not None else "-", len(pairs))


def probe_keys(a, say):
    """Which column of smart.csv, used as the join key, actually recovers event weight?

    Needed because `m3life_no` is NOT one of the 287 documented SMART registry variables --
    the registry's own identifier is `studienr`, and data_dict.csv describes the EHR's
    `M3LIFE_no` as a "PseudoID to be linked with the SMART dataset". So the column joining
    them was added to smart.csv by hand, and if it was added wrongly, the fix is to find the
    column that was meant.

    For each plausible key column K: index the registry's WEIGHT by K, look up each event
    patient's id in that index, and correlate. Weight is the probe because it is stable,
    recorded 121,417 times, and needs no interpretation. A column that lights up at rho ~
    0.9 is the real key; if none does, the linkage itself has to be re-derived upstream and
    that is a question for the data manager, not for this code.
    """
    ev = nearest_baseline_value(a.event_csv_folder, "meting", "label", "Gewicht", "data1",
                                a.landmark_days, say)
    if not ev:
        say("  no meting.Gewicht available; cannot probe keys")
        return
    raw = pd.read_csv(a.smart_csv)
    if "gewicht" not in raw.columns:
        say("  smart.csv has no `gewicht`; cannot probe keys")
        return
    w = pd.to_numeric(raw["gewicht"], errors="coerce")
    say(f"\n  --- which smart.csv column, used as the join key, recovers routine weight? ---")
    say(f"  probe: {len(ev):,} patients with a routine weight near baseline")
    say(f"  {'candidate key':<24s} {'unique':>8s} {'matched':>8s} {'rho':>8s}  note")
    out = []
    for c in raw.columns:
        v = pd.to_numeric(raw[c], errors="coerce")
        if v.notna().sum() < 0.5 * len(raw):
            continue
        if v.dropna().nunique() < 0.5 * len(raw):      # a key is near-unique per row
            continue
        idx = pd.Series(w.to_numpy(), index=v.to_numpy())
        idx = idx[~idx.index.duplicated()]
        pairs = [(ev[p], idx.get(p)) for p in ev if p in idx.index]
        pairs = [(x, y) for x, y in pairs if y is not None and not pd.isna(y)]
        note = ""
        if np.array_equal(np.sort(v.dropna().to_numpy()),
                          np.arange(len(v.dropna()))) or np.array_equal(
                          np.sort(v.dropna().to_numpy()), np.arange(1, len(v.dropna()) + 1)):
            note = "<- looks like a ROW COUNTER, not a real id"
        rho = _spearman([x for x, _ in pairs], [y for _, y in pairs]) if len(pairs) >= 30 else None
        say(f"  {c[:24]:<24s} {v.dropna().nunique():8,} {len(pairs):8,} "
            f"{(f'{rho:+.3f}' if rho is not None else '   -  '):>8s}  {note}")
        if rho is not None:
            out.append((abs(rho), c, rho, len(pairs)))
    out.sort(reverse=True)
    if out and out[0][0] >= 0.5:
        _, c, rho, n = out[0]
        emit("KEY FOUND: joining on smart.csv column `{}` recovers routine weight "
             "(rho={:+.3f}, n={}). The current key is wrong; re-run every event and text "
             "arm with this one", c, rho, n)
        say(f"\n  -> USE `{c}`. It recovers weight at rho={rho:+.3f}; every event and text")
        say("     arm must be rebuilt with it, and their nulls re-measured.")
    else:
        best = f"{out[0][2]:+.3f} ({out[0][1]})" if out else "none testable"
        emit("NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best {}): the EHR-to-registry "
             "linkage cannot be repaired from the files we hold and must be re-derived by "
             "the data manager", best)
        say(f"\n  -> No column in smart.csv recovers weight (best {best}). The linkage")
        say("     cannot be fixed from these files: the EHR extracts and the registry need")
        say("     to be re-linked at source. This is a question for the data manager.")


def internal_consistency(a, say):
    """Is each file self-consistent? BMI = weight / height^2 must hold WITHIN a file.

    This localises the corruption, which is what makes the escalation actionable. The
    identity involves three columns of a single row, so it holds regardless of how rows are
    keyed:

      * both files internally consistent, but not with each other -> the two extracts carry
        pseudo-IDs from DIFFERENT pseudonymisation runs, and the linkage must be re-derived
        at source;
      * a file inconsistent with ITSELF -> that file's values were shuffled relative to its
        own rows, and the problem is in producing it.

    Also reports the identifier spaces, since an overlap that is merely numeric coincidence
    looks very different from two extracts that were meant to share a key.
    """
    say("\n  --- is each file self-consistent? BMI = weight / height^2 within one row ---")
    raw = pd.read_csv(a.smart_csv)
    have = [c for c in ("gewicht", "lengte", "bm_indx") if c in raw.columns]
    if len(have) == 3:
        g = pd.to_numeric(raw["gewicht"], errors="coerce")
        l = pd.to_numeric(raw["lengte"], errors="coerce")
        b = pd.to_numeric(raw["bm_indx"], errors="coerce")
        g = g.where(~g.isin((999,))); b = b.where(~b.isin((99, 999)))
        # "Lengte (m.)" per smart.csv, but accept centimetres if that is what it holds
        lm = l.where((l > 1.2) & (l < 2.3))
        if lm.notna().sum() < 0.2 * l.notna().sum():
            lm = (l / 100.0).where((l > 120) & (l < 230))
            say("  registry `lengte` looks like CENTIMETRES despite the label saying metres")
        ok = g.notna() & lm.notna() & b.notna()
        if ok.sum() >= 30:
            implied = g[ok] / (lm[ok] ** 2)
            rho = _spearman(implied.to_numpy(), b[ok].to_numpy())
            med = float(np.median(np.abs(implied.to_numpy() - b[ok].to_numpy())))
            say(f"  REGISTRY  n={int(ok.sum()):,}  rho(implied BMI, stated BMI)="
                f"{(f'{rho:+.3f}' if rho is not None else '-')}  median |diff|={med:.2f}")
            emit("registry self-consistency: BMI vs weight/height^2 rho={} on {} rows "
                 "(median abs diff {:.2f})",
                 f"{rho:+.3f}" if rho is not None else "-", int(ok.sum()), med)
        else:
            say("  REGISTRY  too few rows with all three of gewicht/lengte/bm_indx")
    else:
        say(f"  REGISTRY  missing {set(('gewicht','lengte','bm_indx')) - set(have)}")

    ev_g = nearest_baseline_value(a.event_csv_folder, "meting", "label", "Gewicht", "data1",
                                  a.landmark_days, say)
    ev_l = nearest_baseline_value(a.event_csv_folder, "meting", "label", "Lengte", "data1",
                                  a.landmark_days, say)
    ev_b = nearest_baseline_value(a.event_csv_folder, "meting", "label", "BMI", "data1",
                                  a.landmark_days, say)
    common = [p for p in ev_b if p in ev_g and p in ev_l]
    if len(common) >= 30:
        gg = np.array([ev_g[p] for p in common], float)
        ll = np.array([ev_l[p] for p in common], float)
        bb = np.array([ev_b[p] for p in common], float)
        ll = np.where(ll > 100, ll / 100.0, ll)          # cm -> m if needed
        good = (ll > 1.2) & (ll < 2.3) & (gg > 30) & (gg < 250)
        if good.sum() >= 30:
            implied = gg[good] / ll[good] ** 2
            rho = _spearman(implied, bb[good])
            med = float(np.median(np.abs(implied - bb[good])))
            say(f"  EVENTS    n={int(good.sum()):,}  rho(implied BMI, stated BMI)="
                f"{(f'{rho:+.3f}' if rho is not None else '-')}  median |diff|={med:.2f}")
            emit("event self-consistency: BMI vs weight/height^2 rho={} on {} patients "
                 "(median abs diff {:.2f})",
                 f"{rho:+.3f}" if rho is not None else "-", int(good.sum()), med)
    else:
        say(f"  EVENTS    only {len(common):,} patients have all three of "
            "Gewicht/Lengte/BMI near baseline")

    # identifier spaces: are these two extracts even meant to share a key?
    rid = pd.to_numeric(raw[ID], errors="coerce").dropna().astype(int) if ID in raw.columns else None
    if rid is not None and ev_g:
        eid = pd.Series(sorted(ev_g))
        inter = len(set(rid) & set(eid))
        say(f"\n  identifier spaces: registry {rid.nunique():,} ids in "
            f"[{rid.min():,}, {rid.max():,}] | events {eid.nunique():,} ids in "
            f"[{eid.min():,}, {eid.max():,}] | overlap {inter:,}")
        # Is that overlap a shared key, or coincidence? If the two files assigned their
        # pseudo-ids INDEPENDENTLY over the same numbering range, the expected overlap is
        # R*E/N. An observed value at that number means the "matching" patients match by
        # arithmetic, not by identity -- which is a completely different problem from a
        # shared key that has been scrambled, and points at two pseudonymisation runs.
        R, E = int(rid.nunique()), int(eid.nunique())
        lo = int(min(rid.min(), eid.min()))
        hi = int(max(rid.max(), eid.max()))
        N = hi - lo + 1
        exp = R * E / N if N else float("nan")
        say(f"  expected overlap if the two id sets were INDEPENDENT draws from "
            f"[{lo:,}, {hi:,}] (N={N:,}): {exp:,.0f}")
        say(f"  observed / expected = {inter / exp:.4f}" if exp else "")
        emit("identifier spaces: registry {} ids [{}, {}], events {} ids [{}, {}], "
             "overlap {} vs {:.0f} expected under independence (ratio {:.4f})",
             R, int(rid.min()), int(rid.max()), E, int(eid.min()), int(eid.max()),
             inter, exp, inter / exp if exp else float("nan"))
        if exp and 0.9 <= inter / exp <= 1.1:
            emit("** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent "
                 "id assignments over the same numbering range would produce by arithmetic "
                 "alone, so the {} 'matching' patients match by coincidence. The extracts "
                 "come from different pseudonymisation runs and a crosswalk is required",
                 inter)
            say("  -> The overlap IS the chance value. These are independent id assignments")
            say("     over one numbering range: the files share a range, not a key. Ask the")
            say("     data manager for the crosswalk; no code change can recover this.")


def main(a):
    say = print
    cur, _cols = smart_baseline_numeric(a.smart_csv)
    say(f"  registry: {len(cur):,} patients")
    say(f"\n  {'event source':<28s} {'registry':<10s} {'both':>7s} {'rho':>7s} "
        f"{'shuffled':>9s} {'med(event)':>11s} {'med(reg)':>10s}")
    verdicts = []
    rng = np.random.default_rng(0)
    for prefix, code_col, code, val_col, reg, label in PAIRS:
        vals = nearest_baseline_value(a.event_csv_folder, prefix, code_col, code, val_col,
                                      a.landmark_days, say)
        if not vals or reg not in cur.columns:
            say(f"  {prefix + '.' + code:<28s} {reg:<10s}   unavailable")
            continue
        rv = pd.to_numeric(cur[reg], errors="coerce")
        rv = rv.where(~rv.isin(CURATED_MISSING.get(reg, ())))
        pids = [p for p in vals if p in rv.index and not pd.isna(rv.loc[p])]
        if len(pids) < 30:
            say(f"  {prefix + '.' + code:<28s} {reg:<10s} {len(pids):7,}   too few")
            continue
        e = np.array([vals[p] for p in pids], float)
        c = np.array([float(rv.loc[p]) for p in pids], float)
        rho = _spearman(e, c)
        # The shuffled column is the floor: it shows what "no join" looks like on exactly
        # these patients and values, so the real rho is read against a measured zero rather
        # than an assumed one.
        sh = _spearman(e, rng.permutation(c))
        say(f"  {prefix + '.' + code:<28s} {reg:<10s} {len(pids):7,} "
            f"{(f'{rho:+.3f}' if rho is not None else '   -  '):>7s} "
            f"{(f'{sh:+.3f}' if sh is not None else '   -  '):>9s} "
            f"{np.median(e):11.2f} {np.median(c):10.2f}")
        verdicts.append((label, rho, len(pids)))
        emit("join check {} vs {}: n={} rho={} (shuffled {})", f"{prefix}.{code}", reg,
             len(pids), f"{rho:+.3f}" if rho is not None else "-",
             f"{sh:+.3f}" if sh is not None else "-")

    strong = [(l, r) for l, r, n in verdicts if r is not None and abs(r) >= 0.5]
    if not verdicts:
        emit("join check INCONCLUSIVE: no pair had enough overlap to compare -- which for "
             "sources this large is itself a sign the identifiers do not correspond")
        say("\n  No pair had enough overlapping patients to compare. For sources with "
            "121,417 weight rows that is itself a linkage failure.")
        probe_keys(a, say)
    elif strong:
        emit("EVENT JOIN IS SOUND ({}): routine and study measurements agree per patient, "
             "so the identifier join works and the text arm's failure is specific to the "
             "document cache or to the extractors",
             ", ".join(f"{l} rho={r:+.2f}" for l, r in strong))
        say("\n  -> The event join is sound. The structured arm's null stands. Look for the")
        say("     text problem in the document cache or the extractors, not the identifiers.")
    else:
        best = max((abs(r) for _l, r, _n in verdicts if r is not None), default=0.0)
        emit("** EVENT JOIN IS BROKEN ** (best |rho|={:.3f} across {} pairs): quantities "
             "measured in BOTH the EHR and the study visit do not agree for the same "
             "patient id, so every event AND text result in this project measures plumbing "
             "and must be withdrawn", best, len(verdicts))
        say("\n  ** THE EVENT JOIN IS BROKEN. Weight, height and creatinine are measured in")
        say("     both sources and cannot legitimately disagree for the same patient. Every")
        say("     null in this project -- structured and text -- is uninterpretable until")
        say("     the identifier join is fixed. **")
        probe_keys(a, say)
    # Always run: it localises the corruption when the join fails, and confirms both files
    # are coherent when it passes.
    internal_consistency(a, say)
    if a.whole_timeline:
        whole_timeline_check(a, say)
    sex_via_specific_tests(a, say)
    demographics_probe(a, say)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True)
    p.add_argument("--event-csv-folder", required=True)
    p.add_argument("--landmark-days", type=int, default=180)
    p.add_argument("--whole-timeline", action="store_true", default=True,
                   help="Test the join against EVERY pre-landmark reading per patient, not "
                        "only the one nearest baseline: median across the timeline, plus a "
                        "best-case test taking each patient's reading closest to their own "
                        "registry value. On by default -- it answers the objection that a "
                        "single measurement was compared.")
    p.add_argument("--no-whole-timeline", dest="whole_timeline", action="store_false")
    p.add_argument("--demographics-file", default=None,
                   help="Path to a demographics extract (e.g. the UCN delivery's "
                        "UCN_PATIENT_DEMOGRAFISCH.csv). The 16 event extracts carry no age "
                        "or birth date, so this is the only route to an AGE check. Its "
                        "columns are reported before anything is attempted.")
    p.add_argument("--probe-keys", action="store_true",
                   help="Always probe which smart.csv column works as the join key, not "
                        "only when the join check fails.")
    add_results_arg(p)
    args = p.parse_args()
    with results_block(args.results_file, "join check: events vs registry",
                       {"landmark": args.landmark_days, "probe_keys": args.probe_keys}):
        main(args)
        if args.probe_keys:
            probe_keys(args, print)
