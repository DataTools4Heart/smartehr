"""Did the UTF-8 / id-normalisation step break the EHR-to-registry linkage?

CONTEXT. Joined on `m3life_no`, quantities measured in both the registry and the EHR show
zero per-patient agreement (weight rho +0.011 over 10,923 patients), and the identifier
overlap is exactly the chance value: registry 13,806 ids in [1, 16096], events 12,771 in
[2, 15877], observed overlap 10,949 against 10,954 expected if the two sets were independent
draws from that range (ratio 0.9995). Both files are internally coherent. That looked like
two pseudonymisation runs -- but the same signature is produced by a normalisation step that
altered id VALUES on one side, which is what this script tests.

The files were preprocessed: a non-UTF-8 original was converted to UTF-8, the `m3life_no`
column name was normalised across files, and its dtype was normalised (string in the
registry, integer/float elsewhere). Each of those can change which patient an id denotes:

  * a string id parsed as a float and back loses leading zeros ("00123" -> 123), so it
    still matches SOME id -- just the wrong patient's;
  * a string id that is not purely numeric coerces to NaN and may then be replaced,
    reindexed or dropped, shifting every subsequent row;
  * a re-encode that changes the delimiter, quoting or decimal separator can split rows
    differently, misaligning the id column from the data columns on affected rows;
  * a float round-trip on ids near 2^53 loses precision (not a risk at ~16k, but checked).

WHAT THIS DOES
  1. reads the ORIGINAL registry and event files (encoding and delimiter sniffed) and the
     NORMALISED ones, and compares row counts, id dtype, and id value sets;
  2. reports the id FORMAT on each side -- string length, whether purely numeric, leading
     zeros, whitespace -- because that is where a lossy conversion shows;
  3. checks whether the id -> weight mapping survived normalisation on each side
     independently, which localises damage to one file;
  4. THE DECISIVE TEST: runs the weight-versus-weight join on the ORIGINAL pair. If the
     originals agree and the normalised ones do not, the normalisation is the culprit and
     the linkage is recoverable without going back to the data provider.

    python scripts/smartehr/diagnose_normalization.py \
      --orig-smart data/smart/smart_22nov2022.csv --norm-smart data/smart/smart_utf8.csv \
      --orig-events data/smartehr --norm-events data/smartehr-utf-8
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from graded_concepts import _spearman
from results_log import add_results_arg, emit, results_block

ENCODINGS = ("utf-8", "cp1252", "latin-1", "iso-8859-1", "utf-8-sig")
ID_LOWER = "m3life_no"


def to_num(series):
    """Numeric conversion that survives a European decimal comma.

    Necessary, and caught by a fixture: the original export is semicolon-delimited with
    "80,3" for 80.3. Plain pd.to_numeric turns every such value into NaN, which silently
    emptied both the registry weights and the event weights and made this script report
    that the normalisation was exonerated -- a false negative in exactly the direction that
    matters most here.
    """
    s = series.astype(str).str.strip()
    both = s.str.contains(r"\.", regex=True) & s.str.contains(",", regex=False)
    # dot present too -> the comma is a thousands separator; otherwise it is the decimal
    s = s.mask(both, s.str.replace(",", "", regex=False))
    s = s.mask(~both, s.str.replace(",", ".", regex=False))
    return pd.to_numeric(s, errors="coerce")


def read_any(path, nrows=None, say=print):
    """Read a CSV whose encoding and delimiter are unknown. -> (df, encoding, sep)."""
    last = None
    for enc in ENCODINGS:
        for sep in (None, ",", ";", "\t"):
            try:
                df = pd.read_csv(path, encoding=enc, sep=sep, nrows=nrows,
                                 engine="python" if sep is None else "c",
                                 dtype=str, keep_default_na=False, low_memory=False)
            except Exception as e:                     # noqa: BLE001 - probing formats
                last = e
                continue
            if df.shape[1] > 1:
                return df, enc, (sep or "sniffed")
    say(f"    could not parse {path} ({last})")
    return None, None, None


def find_id(df):
    """The id column, whatever its casing or surrounding whitespace."""
    for c in df.columns:
        if str(c).strip().lower().replace("-", "_") == ID_LOWER:
            return c
    return None


def id_format(vals):
    """Describe the id format, which is where a lossy conversion shows."""
    v = [str(x).strip() for x in vals if str(x).strip() != ""]
    lens = Counter(len(x) for x in v)
    numeric = sum(1 for x in v if x.isdigit())
    leading0 = sum(1 for x in v if len(x) > 1 and x[0] == "0")
    spaces = sum(1 for x in vals if str(x) != str(x).strip())
    nonnum = [x for x in v if not x.isdigit()][:5]
    return {
        "n": len(v), "unique": len(set(v)),
        "lengths": dict(sorted(lens.items())[:6]),
        "purely_numeric": numeric, "leading_zeros": leading0,
        "surrounding_whitespace": spaces,
        "non_numeric_examples": nonnum,
    }


def describe(label, path, say, nrows=None):
    df, enc, sep = read_any(path, nrows=nrows, say=say)
    if df is None:
        return None, None
    idc = find_id(df)
    say(f"  {label}")
    say(f"    path      {path}")
    say(f"    parsed as encoding={enc} sep={sep}  rows={len(df):,} cols={df.shape[1]}")
    say(f"    id column {idc!r}")
    if idc is None:
        say("    ** no m3life_no-like column found **")
        return df, None
    f = id_format(df[idc])
    say(f"    ids       n={f['n']:,} unique={f['unique']:,} purely_numeric="
        f"{f['purely_numeric']:,} leading_zeros={f['leading_zeros']:,} "
        f"whitespace={f['surrounding_whitespace']:,}")
    say(f"    id lengths (chars) {f['lengths']}")
    if f["non_numeric_examples"]:
        say(f"    NON-NUMERIC id examples: {f['non_numeric_examples']}")
    return df, idc


def id_sets(df, idc):
    """Ids as strings and as ints, so the two comparisons can be told apart."""
    raw = {str(x).strip() for x in df[idc] if str(x).strip() != ""}
    ints = set()
    for x in raw:
        try:
            ints.add(int(float(x)))
        except ValueError:
            pass
    return raw, ints


def weight_map_from_events(folder, say, landmark=180):
    """{id(str): weight} from meting.Gewicht, ids kept as raw strings."""
    path = next((p for p in sorted(Path(folder).glob("*.csv")) if p.stem.startswith("meting")),
                None)
    if path is None:
        say(f"    no meting*.csv in {folder}")
        return {}
    df, enc, sep = read_any(path, say=say)
    if df is None:
        return {}
    idc = find_id(df)
    cols = {str(c).strip().lower(): c for c in df.columns}
    lab, val, tim = cols.get("label"), cols.get("data1"), cols.get("datediff")
    if not all((idc, lab, val, tim)):
        say(f"    {path.name}: need m3life_no/label/data1/datediff, have {list(cols)[:8]}")
        return {}
    sub = df[df[lab].astype(str).str.strip().str.lower() == "gewicht"]
    best = {}
    for i, d, v in zip(sub[idc].astype(str).str.strip(),
                       to_num(sub[tim]), to_num(sub[val])):
        if pd.isna(d) or pd.isna(v) or d >= landmark or i == "":
            continue
        prev = best.get(i)
        if prev is None or abs(d) < prev[0]:
            best[i] = (abs(d), float(v))
    say(f"    {path.name} (encoding={enc}, sep={sep}): weights for {len(best):,} ids")
    return {k: v for k, (d, v) in best.items()}


def join_rho(smart_df, idc, ev_weights, say, label):
    """Weight-versus-weight agreement for one (registry, events) pair. -> rho."""
    gcol = next((c for c in smart_df.columns if str(c).strip().lower() == "gewicht"), None)
    if gcol is None:
        say(f"    {label}: registry has no `gewicht`")
        return None, 0
    w = to_num(smart_df[gcol])
    reg = {}
    for i, x in zip(smart_df[idc].astype(str).str.strip(), w):
        if i != "" and not pd.isna(x):
            reg[i] = float(x)
    # Compare on raw strings first, then on integer-normalised ids, because the difference
    # between those two IS the normalisation under suspicion.
    out = {}
    for mode in ("string", "int"):
        if mode == "string":
            pairs = [(ev_weights[k], reg[k]) for k in ev_weights if k in reg]
        else:
            def norm(d):
                o = {}
                for k, v in d.items():
                    try:
                        o[int(float(k))] = v
                    except ValueError:
                        pass
                return o
            e2, r2 = norm(ev_weights), norm(reg)
            pairs = [(e2[k], r2[k]) for k in e2 if k in r2]
        rho = _spearman([a for a, _ in pairs], [b for _, b in pairs]) if len(pairs) >= 30 else None
        out[mode] = (rho, len(pairs))
        if not pairs:
            say(f"    {label} matched on {mode:<6s} ids: NO comparable rows -- check that "
                "both sides parsed their values (a decimal comma read as text gives this)")
        say(f"    {label} matched on {mode:<6s} ids: n={len(pairs):6,}  rho="
            f"{(f'{rho:+.3f}' if rho is not None else '   -  ')}")
    return out, len(reg)


def main(a):
    say = print
    say("=== 1. registry: original vs normalised " + "=" * 34)
    o_sm, o_idc = describe("ORIGINAL registry", a.orig_smart, say)
    n_sm, n_idc = describe("NORMALISED registry", a.norm_smart, say)

    if o_sm is not None and n_sm is not None and o_idc and n_idc:
        if len(o_sm) != len(n_sm):
            emit("** ROW COUNT CHANGED in the registry: {} -> {} **", len(o_sm), len(n_sm))
            say(f"  ** rows changed {len(o_sm):,} -> {len(n_sm):,}: the re-encode altered "
                "how rows were split, which misaligns every column from its id **")
        o_raw, o_int = id_sets(o_sm, o_idc)
        n_raw, n_int = id_sets(n_sm, n_idc)
        say(f"\n  registry id sets: original {len(o_raw):,} | normalised {len(n_raw):,}")
        say(f"    identical as strings? {o_raw == n_raw}")
        say(f"    identical as ints?    {o_int == n_int}")
        say(f"    string overlap {len(o_raw & n_raw):,} | int overlap {len(o_int & n_int):,}")
        if o_int != n_int:
            lost, gained = sorted(o_int - n_int)[:5], sorted(n_int - o_int)[:5]
            emit("** REGISTRY IDS CHANGED VALUE during normalisation: {} lost, {} gained **",
                 len(o_int - n_int), len(n_int - o_int))
            say(f"    ids only in the ORIGINAL (first 5): {lost}")
            say(f"    ids only in the NORMALISED (first 5): {gained}")
        # did each id keep its own weight?
        gco = next((c for c in o_sm.columns if str(c).strip().lower() == "gewicht"), None)
        gcn = next((c for c in n_sm.columns if str(c).strip().lower() == "gewicht"), None)
        if gco and gcn:
            mo = dict(zip(o_sm[o_idc].astype(str).str.strip(), to_num(o_sm[gco])))
            mn = dict(zip(n_sm[n_idc].astype(str).str.strip(), to_num(n_sm[gcn])))
            common = [k for k in mo if k in mn and not pd.isna(mo[k]) and not pd.isna(mn[k])]
            if len(common) >= 30:
                rho = _spearman([mo[k] for k in common], [mn[k] for k in common])
                say(f"    id -> weight preserved across normalisation? n={len(common):,} "
                    f"rho={(f'{rho:+.3f}' if rho is not None else '-')}")
                emit("registry id->weight preserved by normalisation: n={} rho={}",
                     len(common), f"{rho:+.3f}" if rho is not None else "-")

    say("\n=== 2. THE DECISIVE TEST: does the ORIGINAL pair join? " + "=" * 18)
    say("  ORIGINAL events:")
    o_ev = weight_map_from_events(a.orig_events, say)
    say("  NORMALISED events:")
    n_ev = weight_map_from_events(a.norm_events, say)

    res = {}
    if o_sm is not None and o_idc and o_ev:
        r, _ = join_rho(o_sm, o_idc, o_ev, say, "ORIGINAL pair")
        res["original"] = r
    if n_sm is not None and n_idc and n_ev:
        r, _ = join_rho(n_sm, n_idc, n_ev, say, "NORMALISED pair")
        res["normalised"] = r
    # also the crossed pairs: they say WHICH side was damaged
    if o_sm is not None and o_idc and n_ev:
        r, _ = join_rho(o_sm, o_idc, n_ev, say, "orig registry + norm events")
        res["orig_reg_norm_ev"] = r
    if n_sm is not None and n_idc and o_ev:
        r, _ = join_rho(n_sm, n_idc, o_ev, say, "norm registry + orig events")
        res["norm_reg_orig_ev"] = r

    # Rank by agreement first, then by how many patients it covers: string and int id
    # matching can give the same rho on very different n, and the wider one is the one to
    # rebuild from.
    cands = [(k, mode, rho, n) for k, v in res.items()
             for mode, (rho, n) in (v or {}).items() if rho is not None]
    best = max(cands, key=lambda t: (round(abs(t[2]), 3), t[3])) if cands else None
    if best and abs(best[2]) >= 0.5:
        emit("** LINKAGE RECOVERED **: {} matched on {} ids gives rho={:+.3f} on {} "
             "patients. The normalisation broke the join; rebuild every arm from that "
             "combination", best[0], best[1], best[2], best[3])
        say(f"\n  ** RECOVERED: `{best[0]}` on {best[1]} ids -> rho={best[2]:+.3f} "
            f"(n={best[3]:,}). **")
        say("     Rebuild every event and text arm from that pairing, then re-measure both")
        say("     nulls. Nothing needs to be requested from the data provider.")
        # The crossed pairings say WHICH file the normalisation damaged.
        def got(k, m="int"):
            return (res.get(k) or {}).get(m, (None, 0))[0]
        o_n, n_o = got("orig_reg_norm_ev"), got("norm_reg_orig_ev")
        if o_n is not None and n_o is not None:
            if abs(o_n) >= 0.5 > abs(n_o):
                emit("the damaged file is the NORMALISED REGISTRY: original registry + "
                     "normalised events gives {:+.3f} while normalised registry + original "
                     "events gives {:+.3f}", o_n, n_o)
                say(f"     Damaged file: the NORMALISED REGISTRY (orig reg + norm ev "
                    f"{o_n:+.3f} vs norm reg + orig ev {n_o:+.3f}).")
            elif abs(n_o) >= 0.5 > abs(o_n):
                emit("the damaged file is the NORMALISED EVENTS: normalised registry + "
                     "original events gives {:+.3f} while original registry + normalised "
                     "events gives {:+.3f}", n_o, o_n)
                say(f"     Damaged file: the NORMALISED EVENTS (norm reg + orig ev "
                    f"{n_o:+.3f} vs orig reg + norm ev {o_n:+.3f}).")
    else:
        got = ", ".join(f"{k}/{m}={r:+.3f}" for k, v in res.items()
                        for m, (r, _n) in (v or {}).items() if r is not None) or "none"
        emit("normalisation is NOT the culprit (best agreement across all four pairings: "
             "{}): the originals do not join either, so the two extracts genuinely carry "
             "independent pseudonymisation runs and a crosswalk is required", got)
        say(f"\n  -> The ORIGINAL files do not join either ({got}). The normalisation is")
        say("     exonerated: the two extracts carry independent pseudonymisation runs, and")
        say("     the crosswalk has to come from the data provider.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--orig-smart", required=True)
    p.add_argument("--norm-smart", required=True)
    p.add_argument("--orig-events", required=True)
    p.add_argument("--norm-events", required=True)
    add_results_arg(p)
    args = p.parse_args()
    with results_block(args.results_file, "diagnose: did normalisation break the join?",
                       {"orig_smart": args.orig_smart, "norm_smart": args.norm_smart}):
        main(args)
