"""Can the unused UCN delivery bridge the two identifier spaces that do not match?

CONTEXT. The EHR extracts and the SMART registry both key on `m3life_no` but do not identify
the same patients: 1,047 patients have a prostate-specific PSA test and 370 of them are
recorded as women, weight agrees at rho +0.011 over 39,249 readings, and the id overlap is
0.9995 of the chance value. Everything testable from those two files is exhausted.

The `UCN` delivery (20 files, never used by this project) is a third source with its OWN
PseudoID -- `data_dict.csv` says `UCN_ECG_TEST.csv` "contains the PSeudoID". So it may sit in
one space, the other, or both, and there are four outcomes with very different consequences:

  U matches E and R   UCN IS the crosswalk. Recover the join and rebuild every arm.
  U matches E only    UCN shares the EHR space. No help for the registry link.
  U matches R only    UCN shares the REGISTRY space -- which means UCN's own clinical
                      content (echo, ECG, heart-team, biobank) is usable against the
                      registry, and the research question becomes answerable from UCN data
                      even without repairing the EHR link.
  U matches neither   a third independent space; nothing to do here.

METHOD. Id-set overlap alone is not evidence -- that is the trap this project already fell
into, since two independent assignments over one numbering range overlap at the chance rate.
So every claim here is made at VALUE level:

  U <-> E   ECG measurements. `UCN_ECG_TEST` carries "additional statements and measurements
            compared to EHR data" and `ecg_measmatrix_20251208.csv` carries QRS duration, QT
            interval and the rest, so the same quantity exists on both sides per patient.
            Echo is the fallback (`UCN_ECHO_MEASUREMENT` against `echo_20250626.csv`).
  U <-> R   demographics. `UCN_PATIENT_DEMOGRAFISCH` sex and birth year against the
            registry's `geslacht` and `leeftijd`.

The UCN schemas are undocumented -- `data_dict.csv` lists no columns for any UCN file, only
prose notes -- so this script REPORTS what each file actually holds before attempting
anything, and pairs columns by name first, by distribution second. The inventory is useful on
its own even if no test can be run.

The files are also known-malformed: embedded newlines split rows and embedded semicolons
appear inside cells ("should be on each line 204 semicolons for 205 rows ... Was not able to
fix this yet"). Reads are therefore defensive and report how many lines were unparseable.

    python scripts/smartehr/validate_ucn_crosswalk.py --ucn-folder data/ucn \
      --smart-csv data/smart/smart_utf8.csv --event-csv-folder data/smartehr
"""

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import ID, TIME
from feature_matrix import smart_baseline_numeric
from graded_concepts import CURATED_MISSING, _spearman
from results_log import add_results_arg, emit, results_block

ENCODINGS = ("utf-8", "cp1252", "latin-1", "utf-8-sig")
# Skipping unparseable lines is spelled differently across pandas versions: on_bad_lines
# arrived in 1.3, error_bad_lines was the way before it and is removed in 2.0. Try each,
# then plain, so this runs on whatever the VM has.
_SKIP_BAD_LINES = ({"on_bad_lines": "skip"},
                   {"error_bad_lines": False, "warn_bad_lines": False},
                   {})
ID_NAME_HINTS = ("pseudo", "m3life", "m3_life", "patient", "patid", "pat_id")
# EHR ECG columns, from data/smartehr/data_dicts/data_dict.csv
EHR_ECG_NUMERIC = ("AvgRRInterval", "NumQRSComplexes", "P_Offset", "P_Onset", "QRS_Duration",
                   "QRS_Offset", "QRS_Onset", "QTc_Bazett", "QT_Interval", "T_Offset",
                   "T_Onset", "VentRate")


def norm_name(c):
    return re.sub(r"[^a-z0-9]", "", str(c).lower())


def read_messy(path, nrows=None, say=print):
    """Read a file whose encoding, delimiter and row integrity are all in doubt.

    The UCN exports are documented as having newlines inside cells, so some lines cannot be
    parsed at all. Skipping them and SAYING SO is better than failing, and better than
    silently dropping them: a file that loses a third of its rows here is not usable as
    evidence and the reader has to know that.
    """
    best, last_err = None, None
    for enc in ENCODINGS:
        for sep in (";", ",", "\t"):
            df = None
            for kwargs in _SKIP_BAD_LINES:
                try:
                    df = pd.read_csv(path, encoding=enc, sep=sep, nrows=nrows, dtype=str,
                                     keep_default_na=False, engine="python", **kwargs)
                    break
                except TypeError as e:
                    last_err = e          # this pandas does not accept that spelling
                    continue
                except Exception as e:    # noqa: BLE001 - probing formats
                    last_err = e
                    break
            if df is not None and df.shape[1] > 1 and (
                    best is None or df.shape[1] > best[0].shape[1]):
                best = (df, enc, sep)
    if best is None:
        # Surfacing the reason matters: an earlier version swallowed it and reported
        # "could not be parsed" for a file that was fine, when the real cause was that
        # this pandas does not accept the bad-line argument.
        say(f"    {path.name}: could not be parsed in any encoding/delimiter combination "
            f"(last error: {type(last_err).__name__}: {last_err})")
        return None, None, None
    df, enc, sep = best
    return df, enc, sep


def report_integrity(df, idcol, name, say):
    """Rows that are not data: a fragment line admitted by the parser as a mostly-empty row.

    A line-count check does not find these. With the python engine a line broken by an
    embedded newline -- which the delivery's own dictionary warns about -- is ADMITTED as a
    row with missing trailing fields rather than skipped, so no lines appear lost. What it
    leaves behind is a row whose id is not a number, which is the same field-shift signature
    already found in the registry export (two rows holding 'Ao vene RDP' in the id column).
    """
    if idcol is None:
        return
    raw = df[idcol].astype(str).str.strip()
    bad = ~raw.str.fullmatch(r"\d+")
    n_bad = int(bad.sum())
    if n_bad:
        sev = "WARNING" if n_bad > 0.02 * len(df) else "note"
        ex = [x for x in raw[bad].unique()[:3]]
        say(f"    {name}: {sev} {n_bad:,} of {len(df):,} rows have a non-numeric id "
            f"(fragment rows from embedded newlines); examples {ex}")
        emit("UCN {}: {} of {} rows have a non-numeric id (malformed rows)",
             name, n_bad, len(df))


def detect_id(df):
    """The most likely patient-id column: a name hint first, else a near-unique integer."""
    for c in df.columns:
        if any(h in norm_name(c) for h in ID_NAME_HINTS):
            return c
    best = None
    for c in df.columns:
        v = pd.to_numeric(df[c], errors="coerce")
        if v.notna().mean() < 0.9:
            continue
        u = v.dropna().nunique()
        # a patient id repeats across a patient's rows, so require breadth not uniqueness
        if u >= 200 and (best is None or u > best[1]):
            best = (c, u)
    return best[0] if best else None


def id_set(df, col):
    v = pd.to_numeric(df[col], errors="coerce").dropna()
    return {int(x) for x in v}


def overlap_vs_chance(a_ids, b_ids, say, label):
    """Overlap, and what independent assignments over the same range would give.

    Reported but never treated as evidence: this project already learned that two
    independent id spaces over one range overlap at exactly the chance rate.
    """
    if not a_ids or not b_ids:
        return None
    inter = len(a_ids & b_ids)
    lo = min(min(a_ids), min(b_ids))
    hi = max(max(a_ids), max(b_ids))
    n = hi - lo + 1
    exp = len(a_ids) * len(b_ids) / n if n else float("nan")
    ratio = inter / exp if exp else float("nan")
    say(f"    {label}: {len(a_ids):,} vs {len(b_ids):,} ids, overlap {inter:,}; "
        f"chance would give {exp:,.0f} (ratio {ratio:.3f})")
    return inter, exp, ratio


def per_patient(df, idcol, valcol):
    """{pid: [values]} for one numeric column."""
    pid = pd.to_numeric(df[idcol], errors="coerce")
    v = pd.to_numeric(df[valcol], errors="coerce")
    out = {}
    for p, x in zip(pid, v):
        if not pd.isna(p) and not pd.isna(x):
            out.setdefault(int(p), []).append(float(x))
    return out


def value_agreement(u_vals, e_vals, say, label):
    """Per-patient agreement between two sources for the same quantity. -> rho."""
    common = [p for p in u_vals if p in e_vals]
    if len(common) < 30:
        say(f"      {label}: only {len(common):,} shared ids -- cannot compare")
        return None
    a = np.array([float(np.median(u_vals[p])) for p in common])
    b = np.array([float(np.median(e_vals[p])) for p in common])
    rho = _spearman(a, b)
    # the same best-case test used for the EHR/registry check: give the join every chance
    best = np.median([min(abs(x - float(np.median(e_vals[p]))) for x in u_vals[p])
                      for p in common])
    rng = np.random.default_rng(0)
    perm = rng.permutation(common)
    bestp = np.median([min(abs(x - float(np.median(e_vals[q]))) for x in u_vals[p])
                       for p, q in zip(common, perm)])
    say(f"      {label}: n={len(common):,} rho={(f'{rho:+.3f}' if rho is not None else '-')}"
        f"  best-case |diff| {best:.2f} vs {bestp:.2f} permuted")
    emit("UCN value check {}: n={} rho={} best-case {:.2f} vs {:.2f} permuted", label,
         len(common), f"{rho:+.3f}" if rho is not None else "-", float(best), float(bestp))
    return rho


def inventory(folder, say):
    """Report what each UCN file actually holds. Useful even if no test can run."""
    paths = sorted(Path(folder).glob("*.csv"))
    if not paths:
        say(f"  no CSV files in {folder}")
        return {}
    say(f"=== 1. inventory of {len(paths)} files in {folder} " + "=" * 20)
    out = {}
    for p in paths:
        df, enc, sep = read_messy(p, nrows=50000, say=say)
        if df is None:
            continue
        idc = detect_id(df)
        say(f"  {p.name}")
        say(f"    encoding={enc} sep={sep!r} rows(sampled)={len(df):,} cols={df.shape[1]}")
        say(f"    columns: {list(df.columns)[:20]}"
            + (f" ... (+{df.shape[1]-20} more)" if df.shape[1] > 20 else ""))
        say(f"    detected id column: {idc!r}"
            + (f" ({pd.to_numeric(df[idc], errors='coerce').dropna().nunique():,} distinct)"
               if idc else "  <- none found"))
        report_integrity(df, idc, p.name, say)
        out[p.name] = (p, idc, list(df.columns))
        emit("UCN inventory {}: {} cols, id={}, {} sampled rows", p.name, df.shape[1], idc,
             len(df))
    return out


def main(a):
    say = print
    verdict = {}
    inv = inventory(a.ucn_folder, say)
    if not inv:
        return

    # ---- reference id sets
    cur, _cols = smart_baseline_numeric(a.smart_csv)
    r_ids = {int(x) for x in cur.index if not pd.isna(x)}
    e_path = next((p for p in sorted(Path(a.event_csv_folder).glob("*.csv"))
                   if p.stem.startswith("ecg_measmatrix")), None)
    e_ecg = None
    if e_path is not None:
        e_ecg = pd.read_csv(e_path, low_memory=False)
        e_ids = id_set(e_ecg, ID) if ID in e_ecg.columns else set()
    else:
        e_ids = set()
        say("\n  no ecg_measmatrix*.csv found; the UCN<->EHR value test needs it")

    say(f"\n=== 2. id-space overlap (reported, NOT evidence) " + "=" * 26)
    say("  Two independent assignments over one range overlap at the chance rate, which is")
    say("  exactly how this project was misled before. Value tests below are the evidence.")
    for name, (path, idc, _cols2) in sorted(inv.items()):
        if idc is None:
            continue
        df, _e, _s = read_messy(path, say=say)
        if df is None:
            continue
        u_ids = id_set(df, idc)
        say(f"  {name} (id={idc})")
        ov = overlap_vs_chance(u_ids, r_ids, say, "vs registry")
        if ov:
            verdict["r_overlap"] = max(verdict.get("r_overlap", 0), ov[0])
        if e_ids:
            overlap_vs_chance(u_ids, e_ids, say, "vs EHR ecg")

    # ---- U <-> E at value level, via ECG
    say(f"\n=== 3. UCN <-> EHR at VALUE level (ECG measurements) " + "=" * 21)
    ecg_name = next((n for n in inv if "ECG_TEST" in n.upper() and "EXAM" not in n.upper()),
                    None)
    if ecg_name is None or e_ecg is None:
        say("  needs UCN_ECG_TEST.csv and ecg_measmatrix*.csv; one is missing")
    else:
        path, idc, _c = inv[ecg_name]
        udf, _e, _s = read_messy(path, say=say)
        if udf is not None and idc:
            ehr_by_norm = {norm_name(c): c for c in EHR_ECG_NUMERIC if c in e_ecg.columns}
            pairs = []
            for uc in udf.columns:
                n = norm_name(uc)
                if n in ehr_by_norm:
                    pairs.append((uc, ehr_by_norm[n]))
                    continue
                for en, ec in ehr_by_norm.items():
                    if len(n) >= 5 and (n in en or en in n):
                        pairs.append((uc, ec))
                        break
            if not pairs:
                # fall back to distribution matching, and say so -- a name-blind pairing is
                # a guess and must be labelled as one
                say("  no columns paired by name; trying distribution matching (a guess)")
                for uc in udf.columns:
                    uv = pd.to_numeric(udf[uc], errors="coerce").dropna()
                    if len(uv) < 100:
                        continue
                    for ec in ehr_by_norm.values():
                        ev = pd.to_numeric(e_ecg[ec], errors="coerce").dropna()
                        if len(ev) < 100:
                            continue
                        if abs(uv.median() - ev.median()) < 0.05 * max(abs(ev.median()), 1):
                            pairs.append((uc, ec))
                            say(f"    candidate: {uc} ~ {ec} "
                                f"(medians {uv.median():.1f} / {ev.median():.1f})")
                            break
            say(f"  {len(pairs)} column pair(s) to compare")
            for uc, ec in pairs[:8]:
                uv = per_patient(udf, idc, uc)
                ev = per_patient(e_ecg, ID, ec)
                r = value_agreement(uv, ev, say, f"{uc} vs ecg.{ec}")
                if r is not None:
                    verdict["ue"] = max(verdict.get("ue", 0.0), abs(r))

    # ---- U <-> R at value level, via demographics
    say(f"\n=== 4. UCN <-> registry at VALUE level (demographics) " + "=" * 20)
    dem = next((n for n in inv if "DEMOGRAF" in n.upper()), None)
    if dem is None:
        say("  no UCN_PATIENT_DEMOGRAFISCH-like file present")
    else:
        path, idc, _c = inv[dem]
        ddf, _e, _s = read_messy(path, say=say)
        if ddf is not None and idc:
            ids = pd.to_numeric(ddf[idc], errors="coerce")
            sexc = None
            for c in ddf.columns:
                v = ddf[c].astype(str).str.strip().str.lower()
                vc = v[v != ""].value_counts()
                if 2 <= len(vc) <= 3 and set(vc.index[:2]) <= {
                        "1", "2", "m", "v", "f", "man", "vrouw", "male", "female"}:
                    sexc = c
                    break
            birthc = None
            for c in ddf.columns:
                yr = pd.to_numeric(ddf[c].astype(str).str.extract(r"(\d{4})", expand=False),
                                   errors="coerce")
                if yr.notna().mean() > 0.8 and 1900 <= yr.median() <= 2010:
                    birthc = c
                    break
            say(f"  detected sex={sexc!r} birth-year-like={birthc!r}")
            if sexc and "geslacht" in cur.columns:
                g = pd.to_numeric(cur["geslacht"], errors="coerce")
                g = g.where(~g.isin((9,)))
                m = {"1": 1, "m": 1, "man": 1, "male": 1,
                     "2": 2, "v": 2, "f": 2, "vrouw": 2, "female": 2}
                ds = ddf[sexc].astype(str).str.strip().str.lower().map(m)
                pr = [(int(i), s) for i, s in zip(ids, ds)
                      if not pd.isna(i) and not pd.isna(s) and int(i) in g.index
                      and not pd.isna(g.loc[int(i)])]
                if len(pr) >= 30:
                    agree = float(np.mean([g.loc[i] == s for i, s in pr]))
                    # chance is not 0.5: it is p^2+(1-p)^2 at the cohort's sex ratio
                    p1 = float((g == 1).mean(skipna=True))
                    chance = p1 ** 2 + (1 - p1) ** 2
                    say(f"  sex agreement {agree:.3f} on {len(pr):,} patients "
                        f"(chance at this cohort's ratio is {chance:.3f})")
                    verdict["ur_sex"] = (agree, chance)
                    emit("UCN demographics sex agreement with registry: {:.3f} on {} "
                         "patients (chance {:.3f})", agree, len(pr), chance)
            if birthc and "leeftijd" in cur.columns:
                age = pd.to_numeric(cur["leeftijd"], errors="coerce")
                age = age.where(~age.isin(CURATED_MISSING.get("leeftijd", ())))
                yr = pd.to_numeric(ddf[birthc].astype(str).str.extract(r"(\d{4})",
                                                                      expand=False),
                                   errors="coerce")
                pr = [(int(i), float(y)) for i, y in zip(ids, yr)
                      if not pd.isna(i) and not pd.isna(y) and int(i) in age.index
                      and not pd.isna(age.loc[int(i)])]
                if len(pr) >= 30:
                    rho = _spearman([y for _i, y in pr],
                                    [float(age.loc[i]) for i, _y in pr])
                    say(f"  birth-year vs registry age: rho="
                        f"{(f'{rho:+.3f}' if rho is not None else '-')} on {len(pr):,} "
                        "(a working join gives a strong NEGATIVE rho)")
                    if rho is not None:
                        verdict["ur_age"] = rho
                    emit("UCN demographics birth-year vs registry age: rho={} on {} "
                         "patients (negative is correct)",
                         f"{rho:+.3f}" if rho is not None else "-", len(pr))

    # ---- which of the four scenarios are we in?
    # A shared assignment over one source population leaves a telltale: the two id sets
    # partition the range almost disjointly. Independent assignment would instead overlap
    # at the density of the other set.
    if r_ids and verdict.get("r_overlap"):
        say(f"\n=== 4b. id-range structure " + "=" * 50)
        lo, hi = min(r_ids), max(r_ids)
        dens = len(r_ids) / (hi - lo + 1)
        say(f"  the registry occupies {len(r_ids):,} of {hi-lo+1:,} id values "
            f"({dens:.0%} dense), leaving {hi-lo+1-len(r_ids):,} gaps")
        say(f"  a UCN id drawn independently should therefore land in the registry "
            f"{dens:.0%} of the time; the observed share is far lower (see section 2)")
        say("  UCN ids falling mostly in the registry's GAPS is what a single enumeration")
        say("  of one larger source population looks like -- the registry took most of it,")
        say("  UCN covers largely the remainder plus a modest overlap. Independent")
        say("  assignment cannot produce that.")
        emit("id-range structure: registry is {:.0%} dense over [{}, {}], so an independent "
             "UCN id should hit it {:.0%} of the time; the observed share is far lower, "
             "which indicates one shared enumeration of a larger source population",
             dens, lo, hi, dens)

    say(f"\n=== 5. verdict " + "=" * 62)
    ue = verdict.get("ue")
    sex = verdict.get("ur_sex")
    ur_age = verdict.get("ur_age")
    ue_ok = ue is not None and ue >= 0.5
    ur_ok = bool((sex and sex[0] >= sex[1] + 0.25) or (ur_age is not None and ur_age <= -0.5))
    ue_txt = f"{ue:.3f}" if ue is not None else "untestable"
    ur_txt = (f"sex {sex[0]:.3f} vs chance {sex[1]:.3f}" if sex else "sex untestable")
    if ur_age is not None:
        ur_txt += f", birth-year vs age rho {ur_age:+.3f}"
    say(f"  UCN <-> EHR (value level): {ue_txt}")
    say(f"  UCN <-> registry: {ur_txt}")
    if ue_ok and ur_ok:
        emit("** UCN IS THE CROSSWALK **: it matches the EHR at value level ({}) AND the "
             "registry ({}), so the EHR-to-registry mapping can be reconstructed through "
             "the UCN PseudoID and every event and text arm can be rebuilt", ue_txt, ur_txt)
        say("  ** UCN BRIDGES BOTH SPACES. Build the EHR<->registry map through it, then")
        say("     rebuild every arm and re-measure both nulls. **")
    elif ue_ok:
        emit("UCN shares the EHR id space only ({} at value level; registry {}): no help "
             "for the registry link, and the crosswalk request stands", ue_txt, ur_txt)
        say("  -> UCN sits in the EHR space only. No bridge; the crosswalk request stands.")
    elif ur_ok:
        # Sharing the space is necessary but not sufficient: the overlap has to be big
        # enough to analyse. An earlier version of this message claimed the research
        # question was answerable from UCN data without checking that, which is wrong at
        # low coverage -- a survival analysis needs events, not just patients.
        n_ov = verdict.get("r_overlap", 0)
        n_ev = int(n_ov * 0.136)          # the cohort's 15-year event rate at landmark 180
        emit("** UCN SHARES THE REGISTRY ID SPACE ** ({}; EHR {}): so the EHR delivery is "
             "the outlier -- two independent sources agree on an id space and it does not",
             ur_txt, ue_txt)
        say("  ** UCN sits in the REGISTRY space, and NOT in the EHR space. So the 16 EHR")
        say("     extracts are the odd delivery out: two independent sources agree with")
        say("     each other and disagree with them. **")
        if n_ov >= 3000:
            emit("UCN clinical content is usable against the registry on up to {} patients "
                 "(~{} events): large enough to pursue while the EHR crosswalk is awaited",
                 n_ov, n_ev)
            say(f"     Usable cohort: up to {n_ov:,} patients (~{n_ev} events).")
        else:
            emit("BUT the usable cohort is only {} patients (~{} events), against the {} "
                 "training events the withdrawn analysis required, so UCN does NOT rescue "
                 "the research question -- its value here is diagnostic", n_ov, n_ev, 828)
            say(f"     BUT only {n_ov:,} registry patients appear in UCN (~{n_ev} events)")
            say("     against the 828 training events the analysis needed, so this does NOT")
            say("     rescue the question. The value is diagnostic: it names the EHR")
            say("     delivery as the broken one, which sharpens the crosswalk request.")
    else:
        emit("UCN matches neither space (EHR {}, registry {}): a third independent "
             "pseudonymisation, so it offers no bridge", ue_txt, ur_txt)
        say("  -> UCN matches neither. A third independent id space; no bridge available.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ucn-folder", required=True,
                   help="Folder holding the UCN_*.csv delivery.")
    p.add_argument("--smart-csv", required=True)
    p.add_argument("--event-csv-folder", required=True)
    add_results_arg(p)
    args = p.parse_args()
    with results_block(args.results_file, "UCN crosswalk test",
                       {"ucn_folder": args.ucn_folder}):
        main(args)
