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
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import ID, TIME
from feature_matrix import smart_baseline_numeric
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


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True)
    p.add_argument("--event-csv-folder", required=True)
    p.add_argument("--landmark-days", type=int, default=180)
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
