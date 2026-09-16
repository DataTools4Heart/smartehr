"""Is `smart_22nov2022_corrected.csv` the file that fixes the identifier join?

CONTEXT. The 16 EHR extracts and the SMART registry export do not identify the same
patients: 1,047 patients have a prostate-specific PSA test and 35% of them are recorded as
women, weight agrees at rho +0.011 over 39,249 readings, and the UCN delivery sits in the
registry's id space while the EHR extracts sit in neither. A corrected registry export has
now surfaced in an inbox folder alongside a copy of the EHR data.

Two questions, answered in one run so the VM is touched once:

  1. Are the inbox EHR files the same bytes as the ones we have been using? The data manager
     reports no discrepancies, so establishing exactly which files were analysed is the
     first thing to settle -- and a sha1 per file is the answer to give them.
  2. Does the corrected registry actually join to the EHR data? That is decided by the same
     value-level checks as before, never by id overlap, which is what misled this project
     once already.

It also reports WHAT the correction did: whether only the id column changed, whether the
clinical rows are the same data, and how many ids moved. A file that merely renumbers rows
looks very different from one that reorders them.

    python scripts/smartehr/check_corrected_delivery.py \
      --inbox /mnt/data/inbox/SMART_EHRDATA \
      --current-events data/smartehr --current-smart data/smart/smart_utf8.csv
"""

import argparse
import hashlib
import sys
from argparse import Namespace
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_event_join as vej
from diagnose_normalization import find_id, read_any, to_num
from results_log import add_results_arg, emit, results_block


def sha1(path, chunk=1 << 20):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def compare_hashes(inbox, current, say):
    """sha1 every CSV on both sides. -> (identical?, per-file table).

    The per-file table is what to send the data manager: it names exactly which bytes were
    analysed, which is the question they actually asked.
    """
    # The inbox also holds the registry exports. Those are not EHR extracts and must not
    # count toward "the two folders differ" -- an earlier version let them, which triggered
    # a redundant second join run against an events folder that was byte-identical.
    def is_registry(name):
        return name.lower().startswith("smart")

    inbox_all = {p.name: p for p in sorted(Path(inbox).glob("*.csv"))}
    inbox_files = {n: p for n, p in inbox_all.items() if not is_registry(n)}
    cur_files = {p.name: p for p in sorted(Path(current).glob("*.csv"))
                 if not is_registry(p.name)}
    names = sorted(set(inbox_files) | set(cur_files))
    reg_files = {n: p for n, p in inbox_all.items() if is_registry(n)}
    say(f"=== 1. EHR csv hashes: inbox vs currently used " + "=" * 28)
    say(f"  inbox   {inbox} ({len(inbox_files)} csv)")
    say(f"  current {current} ({len(cur_files)} csv)")
    say(f"\n  {'file':<34s} {'status':<12s} {'sha1 (current)':<42s} {'MB':>7s}")
    same = differ = only_in = 0
    rows = []
    for n in names:
        ip, cp = inbox_files.get(n), cur_files.get(n)
        if ip and cp:
            hi, hc = sha1(ip), sha1(cp)
            ok = hi == hc
            same += ok
            differ += (not ok)
            status = "IDENTICAL" if ok else "** DIFFERS **"
            say(f"  {n[:34]:<34s} {status:<12s} {hc:<42s} "
                f"{cp.stat().st_size / 1e6:7.1f}")
            if not ok:
                say(f"  {'':34s} {'':12s} inbox: {hi}  ({ip.stat().st_size/1e6:.1f} MB)")
            rows.append((n, status, hc, hi))
        else:
            only_in += 1
            where = "inbox only" if ip else "current only"
            p = ip or cp
            say(f"  {n[:34]:<34s} {where:<12s} {sha1(p):<42s} {p.stat().st_size/1e6:7.1f}")
            rows.append((n, where, sha1(p), None))
    if reg_files:
        say(f"\n  registry exports in the inbox (not EHR extracts, not counted above):")
        for n, p in sorted(reg_files.items()):
            say(f"  {n[:34]:<34s} {'':<12s} {sha1(p):<42s} {p.stat().st_size/1e6:7.1f}")
    say(f"\n  EHR extracts: {same} identical, {differ} differing, {only_in} present on "
        "one side only")
    emit("EHR csv hashes: {} identical, {} differ, {} on one side only", same, differ,
         only_in)
    if differ:
        emit("** {} EHR FILES DIFFER between the inbox and what was analysed **: the "
             "analysis was not run on the inbox copies", differ)
    return differ == 0 and only_in == 0, rows


def compare_registry(orig_path, corr_path, say):
    """What did the correction change: the ids, the data, or the row order?"""
    say(f"\n=== 2. registry: original vs corrected " + "=" * 36)
    o, oenc, osep = read_any(orig_path, say=say)
    c, cenc, csep = read_any(corr_path, say=say)
    if o is None or c is None:
        return
    oid, cid = find_id(o), find_id(c)
    say(f"  original  {Path(orig_path).name}: enc={oenc} sep={osep} rows={len(o):,} "
        f"cols={o.shape[1]} id={oid!r}")
    say(f"  corrected {Path(corr_path).name}: enc={cenc} sep={csep} rows={len(c):,} "
        f"cols={c.shape[1]} id={cid!r}")
    if oid is None or cid is None:
        say("  ** no id column found on one side **")
        return
    if list(o.columns) != list(c.columns):
        onlyo = [x for x in o.columns if x not in set(c.columns)]
        onlyc = [x for x in c.columns if x not in set(o.columns)]
        say(f"  column sets differ: only-original {onlyo[:6]} | only-corrected {onlyc[:6]}")

    def ints(df, col):
        v = pd.to_numeric(df[col], errors="coerce").dropna()
        return {int(x) for x in v}

    oi, ci = ints(o, oid), ints(c, cid)
    say(f"  ids: original {len(oi):,} distinct in [{min(oi):,}, {max(oi):,}]; "
        f"corrected {len(ci):,} in [{min(ci):,}, {max(ci):,}]")
    say(f"  identical id sets? {oi == ci}   |  shared {len(oi & ci):,}  "
        f"only-original {len(oi - ci):,}  only-corrected {len(ci - oi):,}")
    emit("corrected registry ids: {} distinct vs {} original; identical={}; shared {}",
         len(ci), len(oi), oi == ci, len(oi & ci))

    # Did the CLINICAL data move, or only the labels? A per-row signature over the
    # non-id columns answers it: identical multisets mean the same rows are present and
    # only their ids or order changed.
    common = [x for x in o.columns if x in set(c.columns) and x != oid and x != cid]
    if common:
        def sigs(df):
            return df[common].astype(str).agg("\x1f".join, axis=1).map(
                lambda s: hashlib.sha1(s.encode("utf-8", "ignore")).hexdigest())
        so, sc = sigs(o), sigs(c)
        say(f"  row content over {len(common)} shared non-id columns:")
        say(f"    same multiset of rows? {sorted(so) == sorted(sc)}")
        # and did a given id keep its own row?
        mo = dict(zip(pd.to_numeric(o[oid], errors="coerce"), so))
        mc = dict(zip(pd.to_numeric(c[cid], errors="coerce"), sc))
        both = [k for k in mo if k in mc and not pd.isna(k)]
        if both:
            kept = sum(1 for k in both if mo[k] == mc[k])
            say(f"    of {len(both):,} ids present in both, {kept:,} ({kept/len(both):.1%}) "
                "still carry the SAME row")
            same_rows = sorted(so) == sorted(sc)
            emit("corrected registry: {} of {} shared ids keep the same row content "
                 "({:.1%}); same multiset of rows={}", kept, len(both),
                 kept / len(both), same_rows)
            # The two causes look identical in the "kept" number and are NOT the same
            # thing. Only a matching multiset means the rows were merely moved; if the
            # multiset differs, the VALUES changed and "kept" issimply because every
            # row's text differs. An earlier version called this a relabelling either way.
            if kept / len(both) < 0.5 and same_rows:
                say("    -> the same rows are present but attached to different ids: a")
                say("       RELABELLING, which is what a corrected linkage looks like")
            elif not same_rows:
                say("    -> the row multiset differs, so the DATA itself changed. A low")
                say("       'kept' share here does NOT indicate relabelling: comparing 260")
                say("       columns as text, any reformatting makes every row differ.")


def normalize_registry(src, dst, say):
    """Rewrite a raw export in the format the analysis code expects: utf-8, comma, dots.

    Needed because the corrected export is the RAW delivery -- cp1252, semicolon-delimited,
    European decimal commas -- while everything downstream expects the normalised form the
    user already produced for the original. Feeding the raw file straight in fails with
    "Expected 1 fields in line 30, saw 3": pandas reads the whole row as one column.

    Decimal columns are converted only when the comma is demonstrably the decimal
    separator, i.e. when substituting a dot turns a column that mostly does NOT parse as
    numeric into one that mostly does. A column that already parses is left alone, so a
    comma inside free text is never touched.
    """
    df, enc, sep = read_any(src, say=say)
    if df is None:
        return None
    converted = []
    for c in df.columns:
        v = df[c].astype(str).str.strip()
        nonempty = v[v != ""]
        if len(nonempty) < 20:
            continue
        before = pd.to_numeric(nonempty, errors="coerce").notna().mean()
        after = pd.to_numeric(nonempty.str.replace(",", ".", regex=False),
                              errors="coerce").notna().mean()
        if after > 0.9 and before < 0.9:
            df[c] = v.str.replace(",", ".", regex=False)
            converted.append(c)
    idc = find_id(df)
    if idc:
        # the id must be a plain integer: the original export zero-pads it to 5 characters
        df[idc] = pd.to_numeric(df[idc], errors="coerce").astype("Int64")
        n_bad = int(df[idc].isna().sum())
        if n_bad:
            say(f"    {n_bad} rows have a non-numeric id and are dropped "
                "(field-shifted rows, as in the original export)")
            df = df[df[idc].notna()]
        df = df.rename(columns={idc: "m3life_no"})
    df.to_csv(dst, index=False, encoding="utf-8")
    say(f"    normalised {Path(src).name}: {enc}/{sep!r} -> utf-8/',' | "
        f"{len(converted)} decimal-comma column(s) converted | id -> 'm3life_no' | "
        f"{len(df):,} rows -> {dst}")
    emit("normalised the corrected export: {} decimal-comma columns converted, {} rows",
         len(converted), len(df))
    return dst


def compare_ehr_content(inbox, current, say):
    """Bytes differ by construction (raw vs normalised). Is it the same DATA?

    The comparison that matters is rows and patient ids per file, not the sha1: the copies
    we analysed were re-encoded locally, so identical content will never hash the same.
    """
    say(f"\n=== 1b. EHR content: same data, or different data? " + "=" * 24)
    say("  'ids/rows/values' = id sets equal / per-id row counts equal / per-id values equal")
    say("  a two-part entry means the file has no numeric value column to compare (text or")
    say("  code-only sources); ids and row counts are still verified for it")
    say(f"  {'file':<34s} {'inbox rows':>11s} {'cur rows':>10s} {'inbox ids':>10s} "
        f"{'cur ids':>9s} {'ids/rows/values':>16s}")
    same_all = True
    for cp in sorted(Path(current).glob("*.csv")):
        if cp.name.lower().startswith("smart"):
            continue
        ip = Path(inbox) / cp.name
        if not ip.exists():
            say(f"  {cp.name[:34]:<34s} {'(absent from the inbox)':>50s}")
            continue
        idf, _e, _s = read_any(ip, say=say)
        cdf, _e2, _s2 = read_any(cp, say=say)
        if idf is None or cdf is None:
            continue
        ii, ci = find_id(idf), find_id(cdf)
        iset = ({int(x) for x in pd.to_numeric(idf[ii], errors="coerce").dropna()}
                if ii else set())
        cset = ({int(x) for x in pd.to_numeric(cdf[ci], errors="coerce").dropna()}
                if ci else set())
        eq = iset == cset
        # Matching id SETS does not prove each id kept its own rows: a shuffle across
        # patients preserves the set exactly. This is the same half-check that made the
        # registry id verification look clean when it had covered only 38% of ids, so it
        # gets closed here too -- per-id row counts, and per-id values where a numeric
        # column exists. A shuffle changes both.
        rows_eq = vals_eq = None
        if ii and ci and eq:
            icnt = pd.to_numeric(idf[ii], errors="coerce").value_counts()
            ccnt = pd.to_numeric(cdf[ci], errors="coerce").value_counts()
            rows_eq = bool(icnt.sort_index().equals(ccnt.sort_index()))
            # Widen beyond the long-format value columns: echo and ECG carry their
            # numbers elsewhere, and with the first list those two files -- which do have
            # real numeric content -- were only checked on ids and row counts.
            vcol = next((c for c in ("data1", "lab_result", "hos_duur", "med_duur",
                                     "Value_ECHO", "QRS_Duration", "QT_Interval",
                                     "VentRate")
                         if c in idf.columns and c in cdf.columns), None)
            if vcol is not None:
                def per_id(df, idcol):
                    g = pd.DataFrame({"i": pd.to_numeric(df[idcol], errors="coerce"),
                                      "v": to_num(df[vcol])}).dropna()
                    return g.groupby("i")["v"].median()
                a, b = per_id(idf, ii), per_id(cdf, ci)
                j = a.index.intersection(b.index)
                if len(j):
                    vals_eq = bool(np.allclose(a.loc[j], b.loc[j], rtol=1e-6, atol=1e-9))
        same_all &= eq and len(idf) == len(cdf) and (rows_eq is not False) \
            and (vals_eq is not False)
        flag = (str(eq) if rows_eq is None else
                f"{eq}/{rows_eq}" + ("" if vals_eq is None else f"/{vals_eq}"))
        say(f"  {cp.name[:34]:<34s} {len(idf):>11,} {len(cdf):>10,} {len(iset):>10,} "
            f"{len(cset):>9,} {flag:>16s}")
        if rows_eq is False or vals_eq is False:
            emit("** {} CHANGED across the local re-encode **: per-id row counts match={}, "
                 "per-id values match={}", cp.name, rows_eq, vals_eq)
    emit("EHR content comparison: inbox and analysed copies agree on ids, per-id row "
         "counts and per-id values in every file: {}", same_all)
    return same_all


PROBE_COLS = ("gewicht", "lengte", "bm_indx", "labchol", "labkrea", "leeftijd")


def compare_values(orig_path, corr_path, current_smart, say):
    """Median of a few known columns in all three files, to locate any value change.

    Three copies exist: the original raw export, the corrected raw export, and the locally
    normalised copy the analysis actually read. If a value differs between the raw original
    and the local copy, the local conversion changed it; if it differs between the two raw
    files, the correction changed it. Without this the two are indistinguishable.
    """
    say(f"\n=== 2b. where did any value change come from? " + "=" * 29)
    frames = {}
    for label, path in (("original raw", orig_path), ("corrected raw", corr_path),
                        ("local normalised", current_smart)):
        df, _e, _s = read_any(path, say=say)
        if df is not None:
            frames[label] = df
    say(f"  {'column':<12s} " + " ".join(f"{k:>18s}" for k in frames))
    for c in PROBE_COLS:
        cells = []
        for k, df in frames.items():
            col = next((x for x in df.columns if str(x).strip().lower() == c), None)
            if col is None:
                cells.append(f"{'(absent)':>18s}")
                continue
            v = to_num(df[col]).dropna()
            v = v[v < 900] if c in ("lengte", "labchol", "bm_indx") else v
            cells.append(f"{v.median():18.2f}" if len(v) else f"{'(empty)':>18s}")
        say(f"  {c:<12s} " + " ".join(cells))
    emit("value triangulation across original raw / corrected raw / local normalised "
         "written for {} columns", len(PROBE_COLS))


def run_join(smart_csv, events, label, say, landmark=180):
    """The decisive check, reusing the audited join code unchanged."""
    say(f"\n--- {label}")
    say(f"    registry: {smart_csv}")
    say(f"    events:   {events}")
    ns = Namespace(smart_csv=str(smart_csv), event_csv_folder=str(events),
                   landmark_days=landmark, whole_timeline=False,
                   demographics_file=None, probe_keys=False)
    try:
        vej.main(ns)
    except SystemExit as e:
        say(f"    join check exited: {e}")
    except Exception as e:                                  # noqa: BLE001
        say(f"    join check failed: {type(e).__name__}: {e}")


def main(a):
    say = print
    identical, _rows = compare_hashes(a.inbox, a.current_events, say)
    # Byte equality is the wrong test when one side was re-encoded locally, so compare the
    # content too before concluding the inbox holds different data.
    if not identical:
        same_content = compare_ehr_content(a.inbox, a.current_events, say)
        identical = identical or same_content

    inbox = Path(a.inbox)
    corr = next((p for p in inbox.glob("*corrected*.csv")), None)
    orig_in_inbox = next((p for p in inbox.glob("smart_22nov2022.csv")), None)
    if corr is None:
        say("\n  no *corrected*.csv in the inbox; nothing further to test")
        return
    base = orig_in_inbox or Path(a.current_smart)
    compare_registry(base, corr, say)
    compare_values(base, corr, a.current_smart, say)

    say(f"\n=== 3. THE TEST: does the corrected registry join to the EHR data? " + "=" * 8)
    say("  Value-level checks only. Id overlap is never the evidence here -- two")
    say("  independent assignments over one range overlap at the chance rate, which is how")
    say("  this project was misled before.")
    # The inbox holds its own EHR copies; use them when they differ from ours, since the
    # corrected registry was presumably prepared against that copy.
    ev_sets = [("current events", a.current_events)]
    if not identical:
        ev_sets.append(("inbox events", a.inbox))
    # The corrected export is the RAW delivery; normalise it the way the analysed copy was
    # normalised, or the join code cannot read it at all.
    scratch = Path(a.out_dir or ".")
    scratch.mkdir(parents=True, exist_ok=True)
    corr_norm = normalize_registry(corr, scratch / "smart_corrected_utf8.csv", say)
    if corr_norm is None:
        say("  could not normalise the corrected export; cannot test it")
        return
    for ev_label, ev in ev_sets:
        run_join(corr_norm, ev, f"CORRECTED registry + {ev_label}", say, a.landmark_days)
    # control: the uncorrected file against the same events, so the comparison is like for
    # like and a pass cannot be attributed to anything else that changed
    run_join(a.current_smart, ev_sets[0][1],
             f"control: UNCORRECTED registry + {ev_sets[0][0]}", say, a.landmark_days)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--inbox", required=True, help="Folder holding the corrected delivery.")
    p.add_argument("--current-events", required=True, help="The event CSVs analysed so far.")
    p.add_argument("--current-smart", required=True, help="The registry analysed so far.")
    p.add_argument("--landmark-days", type=int, default=180)
    p.add_argument("--out-dir", default="data/smart",
                   help="Where to write the normalised copy of the corrected export.")
    add_results_arg(p)
    args = p.parse_args()
    with results_block(args.results_file, "corrected delivery check",
                       {"inbox": args.inbox}):
        main(args)
