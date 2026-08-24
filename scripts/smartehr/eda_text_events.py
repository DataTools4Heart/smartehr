"""Phase 0 of the free-text arm: measure the clinical narrative before modelling it.

The structured/numeric arm is a confirmed negative (docs/baseline-free-event-survival-report.md).
Free text is the one untested representation, and the confound that killed the earlier attempt
is gone: at landmark 180, 95% of patients have text (up from 89% at landmark 0). Before
building features, this quantifies what the corpus actually is.

SCOPE. Only genuine NARRATIVE columns are in scope. The event CSVs contain ten columns the
structured EDA labelled `free_text`, but six of them (`Diagnose`, `Behandeling`,
`diag_omschrijving`, `locatie`, `OMSCHR`, `verr_omschrijving`) are 3-5 word LABEL fields that
were already tested as tokenised occurrence codes and found null. Re-testing them as "text"
would relabel a settled result. `verr_omschrijving` is additionally 100% post-baseline.

Reports, per source and per split:
  coverage      patients with >=1 document; documents per patient
  volume        chars / words / real tokens per document and per patient
  temporal      document datediff distribution; pre-baseline vs [0, landmark) share
  boilerplate   what fraction of a typical document is template shared with other documents
                (the main threat to TF-IDF: if most of a report is boilerplate the model
                learns the template, not the patient)
  truncation    document lengths piling up at one value (catches rad_report at 1024 chars)
  structure     Dutch section-header frequency (Conclusie / Bevindingen / Anamnese / Beleid)
  deid risk     ISO dates, name-like tokens, physician/department tokens -> drives the stoplist
  T0 control    univariate Harrell C of document and token COUNT, i.e. signal available from
                text VOLUME alone with no content. Every later content arm must beat this,
                or it is only saying "sicker patients have more notes".

LANDMARK semantics are identical to eda_events_survival.py: documents with
`datediff < --landmark-days` are usable, patients whose outcome falls at or before the
landmark are excluded, and survival is measured from the landmark.

PRIVACY: no raw clinical text is ever written. Sampled documents live in memory only.
Any term or value is shown only if it occurs in at least --min-show-count patients.

    python scripts/smartehr/eda_text_events.py \
        --smart-csv <smart.csv> --event-csv-folder <ALL_event_csvs> \
        --split-json <splits.json> --legacy --landmark-days 180 --out-dir eda_text_lm180
"""

import argparse
import gc
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import (
    ID,
    TIME,
    Reservoir,
    apply_censoring,
    build_cohort,
    calibrate_null_scale,
    harrell_c,
    null_floor,
    q,
)

CHUNK = 50_000          # text columns are wide; smaller chunks keep memory flat
DOC_SAMPLE = 4_000      # documents sampled per source for text-shape analysis

# The four narrative columns. src matches a CSV stem by prefix, so date suffixes
# (consult_20251208) need not be spelled out.
TEXT_COLS_DEFAULT = ("consult:consult_tekst,uitgaandebrief:inhoud,"
                     "radiologie_verslag:verslagtekst,mri_verslag:rad_report")

SECTION_PAT = re.compile(
    r"\b(conclusie|bevinding(?:en)?|anamnese|beleid|indicatie|voorgeschiedenis|"
    r"lichamelijk onderzoek|samenvatting|advies|klinische gegevens)\b\s*:?", re.I)
ISO_DATE_PAT = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
NL_DATE_PAT = re.compile(r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b")
WORD_PAT = re.compile(r"[A-Za-zÀ-ÿ]{2,}")
# name-like: capitalised, not sentence-initial, not an all-caps heading
NAMEISH_PAT = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-ZÀ-Þ][a-zà-ÿ]{2,}\b")
CLINICIAN_PAT = re.compile(r"\b(dr|drs|arts|aios|anios|prof|mw|hr|collega|specialist)\b", re.I)


def parse_text_cols(spec):
    out = {}
    for item in (spec or "").split(","):
        item = item.strip()
        if not item:
            continue
        parts = item.split(":")
        if len(parts) != 2:
            raise SystemExit(f"bad --text-cols entry {item!r}: expected src:column")
        out[parts[0]] = parts[1]
    return out


def match_prefix(stem, specs):
    for key, val in specs.items():
        if stem == key or stem.startswith(key):
            return val
    return None


def norm_for_dup(text):
    """Aggressive normalisation so near-identical templates hash alike."""
    t = re.sub(r"\d+", "0", text.lower())
    return re.sub(r"\s+", " ", t).strip()


def boilerplate_fraction(docs, n=8, common_df=0.30):
    """Median share of a document's n-grams that are shared with >= common_df of documents.

    Directly answers "how much of a typical report is template". Computed on a sample.
    """
    if len(docs) < 20:
        return None, 0
    grams_per_doc, df = [], Counter()
    for d in docs:
        w = WORD_PAT.findall(d.lower())
        if len(w) < n:
            grams_per_doc.append(set())
            continue
        g = {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}
        grams_per_doc.append(g)
        df.update(g)
    total = sum(1 for g in grams_per_doc if g)
    if not total:
        return None, 0
    thresh = common_df * total
    common = {g for g, c in df.items() if c >= thresh}
    fracs = [len(g & common) / len(g) for g in grams_per_doc if g]
    return (float(np.median(fracs)) if fracs else None), len(common)


class TextSourceStats:
    def __init__(self, source, column, seed=0):
        self.source, self.column = source, column
        self.n_docs = 0
        self.n_docs_window = 0
        self.chars = Reservoir(seed=seed)
        self.words = Reservoir(seed=seed + 1)
        self.tokens = Reservoir(seed=seed + 2)
        self.dd = Reservoir(seed=seed + 3)
        self.n_pre_baseline = 0
        self.n_post_baseline_in_window = 0
        self.char_hist = Counter()          # exact lengths, to spot truncation caps
        self.doc_hashes = Counter()         # exact-duplicate detection (normalised)
        self.sample = []                    # reservoir of document texts, in memory only
        self._seen = 0
        self.rng = np.random.default_rng(seed)
        self.per_patient_docs = Counter()
        self.per_patient_chars = Counter()
        self.per_patient_tokens = Counter()
        self.total_chars = 0
        self.total_tokens = 0

    def add(self, pid, datediff, text, n_tok):
        self.n_docs_window += 1
        L = len(text)
        w = len(WORD_PAT.findall(text))
        self.chars.add_many([L])
        self.words.add_many([w])
        self.dd.add_many([datediff])
        self.total_chars += L
        if n_tok is not None:
            self.tokens.add_many([n_tok])
            self.total_tokens += n_tok
            self.per_patient_tokens[pid] += n_tok
        if datediff < 0:
            self.n_pre_baseline += 1
        else:
            self.n_post_baseline_in_window += 1
        self.char_hist[L] += 1
        self.doc_hashes[hashlib.blake2b(norm_for_dup(text).encode(),
                                        digest_size=8).hexdigest()] += 1
        self.per_patient_docs[pid] += 1
        self.per_patient_chars[pid] += L
        # reservoir-sample documents for shape analysis
        self._seen += 1
        if len(self.sample) < DOC_SAMPLE:
            self.sample.append(text)
        else:
            j = int(self.rng.integers(0, self._seen))
            if j < DOC_SAMPLE:
                self.sample[j] = text

    def summary(self, min_show):
        d = {
            "source": self.source, "column": self.column,
            "documents_in_window": self.n_docs_window,
            "patients": len(self.per_patient_docs),
            "pre_baseline_docs": self.n_pre_baseline,
            "post_baseline_docs_in_window": self.n_post_baseline_in_window,
            "chars_per_doc": self.chars.quantiles((5, 50, 95, 100)),
            "words_per_doc": self.words.quantiles((5, 50, 95, 100)),
            "datediff": self.dd.quantiles((0, 5, 50, 95, 100)),
            "docs_per_patient": q(list(self.per_patient_docs.values()), (50, 95, 100)),
            "chars_per_patient": q(list(self.per_patient_chars.values()), (5, 50, 95, 100)),
            "total_chars": self.total_chars,
        }
        if self.total_tokens:
            d["tokens_per_doc"] = self.tokens.quantiles((5, 50, 95, 100))
            d["tokens_per_patient"] = q(list(self.per_patient_tokens.values()), (5, 50, 95, 100))
            d["total_tokens"] = self.total_tokens
        # truncation: a single exact length holding an implausible share of documents
        if self.char_hist:
            top_len, top_n = self.char_hist.most_common(1)[0]
            share = top_n / max(self.n_docs_window, 1)
            d["modal_length"] = {"length": top_len, "share": round(share, 4)}
            d["truncation_suspected"] = bool(share >= 0.20 and top_len >= 200)
        # exact duplicates after normalisation
        dup_docs = sum(c for c in self.doc_hashes.values() if c > 1)
        d["exact_duplicate_docs"] = dup_docs
        d["exact_duplicate_share"] = round(dup_docs / max(self.n_docs_window, 1), 4)
        d["distinct_documents"] = len(self.doc_hashes)
        d["distinct_share"] = round(len(self.doc_hashes) / max(self.n_docs_window, 1), 4)
        # sampled text shape
        s = self.sample
        if s:
            bp, n_common = boilerplate_fraction(s)
            d["boilerplate_fraction_median"] = None if bp is None else round(bp, 3)
            d["common_ngrams"] = n_common
            d["docs_sampled"] = len(s)
            d["iso_date_share"] = round(sum(1 for x in s if ISO_DATE_PAT.search(x)) / len(s), 4)
            d["nl_date_share"] = round(sum(1 for x in s if NL_DATE_PAT.search(x)) / len(s), 4)
            d["clinician_token_share"] = round(
                sum(1 for x in s if CLINICIAN_PAT.search(x)) / len(s), 4)
            nameish = [len(NAMEISH_PAT.findall(x)) for x in s]
            d["nameish_tokens_per_doc"] = q(nameish, (50, 95))
            sec = Counter()
            for x in s:
                for m in set(w.lower() for w in SECTION_PAT.findall(x)):
                    sec[m] += 1
            d["section_headers"] = {k: round(v / len(s), 3)
                                    for k, v in sec.most_common(10) if v >= min_show}
        return d


def scan_source(path, column, LM, LB, cohort_ids, tokenizer, min_show, seed):
    stem = Path(path).stem
    st = TextSourceStats(stem, column, seed=seed)
    head = pd.read_csv(path, nrows=0)
    if column not in head.columns:
        return None
    usecols = [c for c in (ID, TIME, column) if c in head.columns]
    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False, usecols=usecols):
        dd = pd.to_numeric(chunk[TIME], errors="coerce")
        keep = dd.notna() & (dd < LM)
        if LB is not None:
            keep &= dd >= (LM - LB)
        txt = chunk[column][keep]
        st.n_docs += int(chunk[column].notna().sum())
        sub = txt.dropna().astype(str)
        if sub.empty:
            del chunk
            continue
        pids = chunk[ID][keep].loc[sub.index]
        dds = dd[keep].loc[sub.index]
        toks = None
        if tokenizer is not None:
            enc = tokenizer(list(sub.values), add_special_tokens=False)["input_ids"]
            toks = [len(x) for x in enc]
        for i, (pid, ddv, text) in enumerate(zip(pids.tolist(), dds.tolist(), sub.tolist())):
            if pd.isna(pid) or int(pid) not in cohort_ids or not text.strip():
                continue
            st.add(int(pid), int(ddv), text, toks[i] if toks else None)
        del chunk
    gc.collect()
    return st


def main(args):
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    LM, H, LB = args.landmark_days, args.horizon_days, args.lookback_days
    L, J = [], {}

    def w(line=""):
        L.append(line)

    tokenizer = None
    if args.tokenizer:
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained(args.tokenizer)
        print(f"tokenizer: {args.tokenizer}", flush=True)

    w("# EDA — clinical free text for baseline-free survival")
    w()
    w(f"- landmark: **{LM} days**; lookback: {LB if LB is not None else 'unbounded'}; "
      f"horizon: {H} days from the landmark")
    w(f"- privacy: no raw clinical text is written; terms/values shown only at "
      f">= {args.min_show_count} occurrences")
    w()

    # ---- cohort + landmark, identical to the structured arm
    cohort, notes = build_cohort(args.smart_csv, args.legacy, args.censoring_time)
    if LM > 0:
        n0 = len(cohort)
        ev0 = int((cohort["cd_event"] == 1).sum())
        cohort = cohort[cohort["first_event"] > LM].copy()
        cohort["first_event"] = cohort["first_event"] - LM
        notes.append(f"landmark {LM}d: dropped {n0-len(cohort):,} patients whose outcome was "
                     f"at/before the landmark ({ev0-int((cohort['cd_event']==1).sum()):,} events)")
    cohort = cohort.reset_index(drop=True)
    ids = cohort[ID].astype(int).to_numpy()
    cohort_ids = set(int(x) for x in ids)
    t_raw = cohort["first_event"].to_numpy(float)
    e_raw = cohort["cd_event"].to_numpy(int)
    cens = [apply_censoring(t, e, H) for t, e in zip(t_raw, e_raw)]
    t_h = np.array([c[0] for c in cens])
    e_h = np.array([c[1] for c in cens])

    w("## §1 Cohort")
    w()
    for n in notes:
        w(f"- {n}")
    w(f"- **{len(ids):,} patients, {int(e_h.sum()):,} events ({100*e_h.mean():.1f}%)** "
      f"at the {H}-day horizon")
    splits = {}
    if args.split_json:
        with open(args.split_json) as f:
            sp = json.load(f)
        if "val" in sp and "validation" not in sp:
            sp["validation"] = sp.pop("val")
        for k, v in sp.items():
            splits[k] = set(int(x) for x in v) & cohort_ids
        w("- splits: " + ", ".join(f"{k}={len(v):,}" for k, v in splits.items()))
    w()

    # ---- per-source scan
    specs = parse_text_cols(args.text_cols)
    csvs = sorted(Path(args.event_csv_folder).glob("*.csv"))
    stats = []
    for p in csvs:
        col = match_prefix(p.stem, specs)
        if not col:
            continue
        print(f"scanning {p.name}.{col} ...", flush=True)
        try:
            st = scan_source(p, col, LM, LB, cohort_ids, tokenizer,
                             args.min_show_count, seed=len(stats))
        except Exception as exc:
            w(f"> **ERROR scanning {p.name}.{col}: {type(exc).__name__}: {exc}**")
            print(f"  ERROR: {exc}", flush=True)
            continue
        if st is None:
            w(f"> note: {p.stem} has no column `{col}`, skipped")
            continue
        stats.append(st)
    if not stats:
        raise SystemExit("no narrative columns matched --text-cols in the given folder")

    # ---- §2 coverage
    all_docs, all_chars, all_tokens = Counter(), Counter(), Counter()
    for st in stats:
        all_docs.update(st.per_patient_docs)
        all_chars.update(st.per_patient_chars)
        all_tokens.update(st.per_patient_tokens)
    with_text = set(all_docs)
    w("## §2 Coverage — is the empty-text confound still present?")
    w()
    w(f"- patients with >= 1 narrative document: **{len(with_text):,} / {len(cohort_ids):,} "
      f"({100*len(with_text)/max(len(cohort_ids),1):.1f}%)**")
    w(f"- patients with NO narrative text: **{len(cohort_ids)-len(with_text):,}** "
      "<- these get an all-zero text vector and are unrankable from text alone")
    for k, v in splits.items():
        nt = len(v - with_text)
        w(f"  - {k}: {len(v & with_text):,} with text, **{nt:,} without** "
          f"({100*nt/max(len(v),1):.1f}%)")
    w(f"- documents per patient (text-bearing only): {q(list(all_docs.values()), (50,95,100))}")
    w(f"- chars per patient: {q(list(all_chars.values()), (5,50,95,100))}")
    if all_tokens:
        tot = sum(all_tokens.values())
        w(f"- **total corpus: {tot:,} tokens** "
          f"(~{int(tot/max(len(all_tokens),1)):,}/patient, real tokenizer)")
    else:
        tot_c = sum(all_chars.values())
        w(f"- total corpus: {tot_c:,} chars (~{int(tot_c/4):,} tokens estimated; "
          "pass --tokenizer for exact counts)")
    w()
    w("| source | docs | patients | pre-bl docs | post-bl docs in window | chars/doc p50 | words/doc p50 |")
    w("|---|---|---|---|---|---|---|")
    for st in stats:
        s = st.summary(args.min_show_count)
        w(f"| {st.source}.{st.column} | {s['documents_in_window']:,} | {s['patients']:,} | "
          f"{s['pre_baseline_docs']:,} | {s['post_baseline_docs_in_window']:,} | "
          f"{s['chars_per_doc'].get('p50')} | {s['words_per_doc'].get('p50')} |")
    w()

    # ---- §3 text shape: boilerplate, truncation, structure, de-id risk
    w("## §3 Text shape — boilerplate, truncation, structure, de-identification risk")
    w()
    J["sources"] = {}
    for st in stats:
        s = st.summary(args.min_show_count)
        J["sources"][f"{st.source}.{st.column}"] = s
        w(f"### {st.source}.{st.column}")
        w()
        w(f"- documents in window: {s['documents_in_window']:,} across {s['patients']:,} patients; "
          f"docs/patient {s['docs_per_patient']}")
        w(f"- chars/doc {s['chars_per_doc']} | words/doc {s['words_per_doc']}")
        if "tokens_per_doc" in s:
            w(f"- tokens/doc {s['tokens_per_doc']} | tokens/patient {s['tokens_per_patient']} "
              f"| total {s['total_tokens']:,}")
        w(f"- `datediff` of documents: {s['datediff']}")
        ml = s.get("modal_length", {})
        flag = "  **<- TRUNCATION SUSPECTED**" if s.get("truncation_suspected") else ""
        w(f"- modal document length: {ml.get('length')} chars in {100*ml.get('share',0):.1f}% "
          f"of documents{flag}")
        w(f"- **{s['distinct_documents']:,} distinct documents** of "
          f"{s['documents_in_window']:,} ({100*s['distinct_share']:.1f}% distinct); "
          f"{s['exact_duplicate_docs']:,} share their text with another document")
        bp = s.get("boilerplate_fraction_median")
        if bp is not None:
            w(f"- **boilerplate: {100*bp:.0f}% of a median document's 8-grams are shared with "
              f">=30% of documents** ({s['common_ngrams']:,} common n-grams, "
              f"{s['docs_sampled']:,} sampled)")
            if bp >= 0.5:
                w("  - over half the text is template: TF-IDF will largely model the template. "
                  "Plan a deduplicated / section-restricted variant.")
        w(f"- de-id risk: ISO dates in {100*s.get('iso_date_share',0):.1f}% of docs, "
          f"NL dates {100*s.get('nl_date_share',0):.1f}%, clinician tokens "
          f"{100*s.get('clinician_token_share',0):.1f}%, name-like tokens/doc "
          f"{s.get('nameish_tokens_per_doc')}")
        sec = s.get("section_headers") or {}
        w(f"- section headers (share of docs): {sec if sec else '(none above threshold)'}")
        w()

    # ---- §4 T0 control: signal from VOLUME alone
    w("## §4 T0 control — how much signal is in text VOLUME alone (no content)?")
    w()
    n_ev = int(e_h.sum())
    k = calibrate_null_scale(t_h, e_h, n_perm=args.permutations)
    thr = null_floor(k, n_ev)
    w(f"Permutation-calibrated null: SE(C) = {k:.3f}/sqrt(events); with {n_ev:,} events the "
      f"2-SE floor is **{thr:.4f}**.")
    w()
    w("**Every content arm must be shown to beat these numbers.** Otherwise a text 'signal' "
      "is only saying that sicker patients accumulate more notes — the same artefact as the "
      "`gfr_count` C=0.851 that turned out to be pure missingness.")
    w()
    feats = {
        "n_documents_total": np.array([float(all_docs.get(p, 0)) for p in ids]),
        "n_chars_total": np.array([float(all_chars.get(p, 0)) for p in ids]),
        "has_any_text": np.array([1.0 if p in with_text else 0.0 for p in ids]),
        "n_sources_with_text": np.array(
            [float(sum(1 for st in stats if p in st.per_patient_docs)) for p in ids]),
    }
    if all_tokens:
        feats["n_tokens_total"] = np.array([float(all_tokens.get(p, 0)) for p in ids])
    for st in stats:
        feats[f"n_docs[{st.source}]"] = np.array(
            [float(st.per_patient_docs.get(p, 0)) for p in ids])
    rows = []
    for name, v in feats.items():
        c, _ = harrell_c(t_h, e_h, v)
        if c is not None:
            rows.append((abs(c - 0.5), name, c))
    rows.sort(reverse=True)
    w("| volume feature | C | clears 2-SE floor? |")
    w("|---|---|---|")
    for m, name, c in rows:
        w(f"| {name} | {c:.4f} | {'**YES**' if m >= thr else 'no'} |")
    w()
    J["t0_volume"] = {"null_k": k, "floor": thr, "n_events": n_ev,
                      "features": [{"feature": n, "c_index": round(c, 4)} for _, n, c in rows]}
    n_clear = sum(1 for m, _, _ in rows if m >= thr)
    if n_clear:
        w(f"> **{n_clear} volume feature(s) clear the floor.** Text volume alone is prognostic, "
          "so the content arms must be compared against this baseline, not against 0.5.")
    else:
        w("> No volume feature clears the floor. A later content gain can therefore be "
          "attributed to content rather than to note-taking intensity.")
    w()

    (out_dir / "eda_text_report.md").write_text("\n".join(L))
    with open(out_dir / "eda_text_report.json", "w") as f:
        json.dump(J, f, indent=2, default=str)
    print("\n".join(L))
    print(f"\n=== wrote {out_dir/'eda_text_report.md'} and eda_text_report.json ===")
    print("Paste eda_text_report.md back into the chat.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True, help="Used ONLY for the survival target.")
    p.add_argument("--event-csv-folder", required=True)
    p.add_argument("--split-json", default=None)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--landmark-days", type=int, default=180)
    p.add_argument("--lookback-days", type=int, default=None,
                   help="Only use documents within this many days before the landmark.")
    p.add_argument("--horizon-days", type=int, default=5475)
    p.add_argument("--legacy", action="store_true")
    p.add_argument("--censoring-time", type=int, default=None)
    p.add_argument("--text-cols", default=TEXT_COLS_DEFAULT,
                   help="Comma-separated src:column of NARRATIVE columns. Short label fields "
                        "are deliberately excluded: they were already tested as occurrence "
                        "codes in the structured arm and found null.")
    p.add_argument("--tokenizer", default=None,
                   help="HF tokenizer name for exact token counts (e.g. "
                        "Qwen/Qwen3-Embedding-0.6B). Omit to report chars/words only.")
    p.add_argument("--min-show-count", type=int, default=20)
    p.add_argument("--permutations", type=int, default=200)
    main(p.parse_args())
