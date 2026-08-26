"""Free-text features from the RAW event CSVs, for the baseline-free survival arms.

Reads the narrative columns directly from the CSVs, never the merged JSONL: the pipeline's
`merge_event_rows` keys on the column name, so several reports written on one day collapse
to whichever landed last — `consult` alone has 53,236 such day-groups. The existing
`prepare_text_tfidf_features.py` reads the merged JSONL and is landmark-unaware, so it
cannot see the full corpus.

Four modes, run cheapest-first. Each is a separate falsifiable arm:

  volume     document/token counts only, NO content. Run this FIRST. Every content arm has
             to be shown to beat it, or a "text signal" is only saying that sicker patients
             accumulate more notes — the artefact that made gfr_count read C=0.851 in the
             structured arm.
  tfidf      TF-IDF -> TruncatedSVD, fitted on TRAIN ONLY. Word 1-2 grams or char 3-5 grams
             (char is robust to Dutch compounding and typos). Optionally restricted to one
             report section, which cuts boilerplate.
  concepts   the SMART-adjacent clinical concepts stated in prose (smoking, diabetes, prior
             MI/CVA, heart failure, CKD, PAD, ...), with NEGATION and UNCERTAINTY handling:
             "geen diabetes" must not count as diabetes, and "verdenking infarct" is
             prognostically different from an assertion. This is the arm that most directly
             tests whether the hand-curated variables can be extracted automatically.
  documents  writes the per-patient text parquet in the schema
             extract_qwen_embeddings_longitudinal.py already consumes, so the frozen-LLM arm
             reuses that extractor unchanged.

A document CACHE is built once (~550M chars) and reused by every mode; re-streaming the
CSVs per arm would cost 20-60 minutes each time.

LANDMARK semantics and the cohort/target/standardisation stage are shared with the
structured arm (`feature_matrix.py`, `eda_events_survival.py`), so arms are comparable.

    # once
    python scripts/smartehr/prepare_text_features.py ... --mode volume   --out-dir T0_volume
    python scripts/smartehr/prepare_text_features.py ... --mode tfidf    --out-dir T1_tfidf
    python scripts/smartehr/prepare_text_features.py ... --mode concepts --out-dir T2_concepts
"""

import argparse
import gc
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import ID, TIME, apply_censoring, build_cohort
from feature_matrix import finish, list_baseline_cols, smart_baseline_features
from results_log import add_results_arg, emit, results_block

CHUNK = 50_000
DOC_SEP = " || "          # hard boundary: negation must not bleed across documents

TEXT_COLS_DEFAULT = ("consult:consult_tekst,uitgaandebrief:inhoud,"
                     "radiologie_verslag:verslagtekst,mri_verslag:rad_report")

ISO_DATE_PAT = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
NL_DATE_PAT = re.compile(r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b")
CLINICIAN_PAT = re.compile(r"\b(dr|drs|arts|aios|anios|prof|mw|hr|collega|specialist|"
                           r"cardioloog|neuroloog|internist|radioloog)\b", re.I)
SECTION_SPLIT = re.compile(
    r"\b(conclusie|bevinding(?:en)?|anamnese|beleid|indicatie|voorgeschiedenis|"
    r"lichamelijk onderzoek|samenvatting|advies|klinische gegevens)\b\s*:?", re.I)
TOKEN_PAT = re.compile(r"[a-z0-9]+")

# --- Dutch clinical concepts: the SMART-adjacent variables that get stated in prose -----
CONCEPTS = {
    "roken":            ["roken", "roker", "rookt", "nicotine", "sigaretten", "pakjaren"],
    "diabetes":         ["diabetes", "suikerziekte", "insuline", "metformine", "dm2", "dm ii"],
    "myocardinfarct":   ["myocardinfarct", "hartinfarct", "stemi", "nstemi", "infarct"],
    "cva_tia":          ["cva", "herseninfarct", "tia", "beroerte", "hersenbloeding"],
    "hartfalen":        ["hartfalen", "decompensatio cordis", "decompensatie",
                         "ejectiefractie verlaagd", "hfref", "hfpef"],
    "nierfunctie":      ["nierinsufficientie", "nierfalen", "chronische nierschade",
                         "dialyse", "egfr", "creatinineklaring"],
    "perifeer_vaatlijden": ["perifeer arterieel vaatlijden", "claudicatio", "etalagebenen",
                            "pav", "aneurysma"],
    "hypertensie":      ["hypertensie", "hoge bloeddruk", "antihypertensiva"],
    "hyperlipidemie":   ["hypercholesterolemie", "dyslipidemie", "statine", "cholesterol"],
    "atriumfibrilleren": ["atriumfibrilleren", "boezemfibrilleren", "vkf"],
    "angina":           ["angina pectoris", "thoracale klachten", "pijn op de borst"],
    "stenose":          ["stenose", "vernauwing", "occlusie"],
    "revascularisatie": ["pci", "dotter", "stent", "cabg", "bypass"],
}
NEG_CUES = {"geen", "niet", "zonder", "negatief", "uitgesloten", "nooit", "afwezig",
            "ontkent", "nee"}
UNC_CUES = {"mogelijk", "verdenking", "verdacht", "waarschijnlijk", "twijfel",
            "differentiaal", "eventueel", "suspect", "vermoeden"}


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


# ---------------------------------------------------------------- document cache

def build_cache(event_csv_folder, specs, LM, LB, cohort_ids, cache_path, say):
    """Stream the narrative columns once into a parquet the every mode reads."""
    rows = []
    for path in sorted(Path(event_csv_folder).glob("*.csv")):
        col = match_prefix(path.stem, specs)
        if not col:
            continue
        head = pd.read_csv(path, nrows=0)
        if col not in head.columns:
            say(f"  {path.stem}: no column `{col}`, skipped")
            continue
        n = 0
        for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False,
                                 usecols=[c for c in (ID, TIME, col) if c in head.columns]):
            dd = pd.to_numeric(chunk[TIME], errors="coerce")
            keep = dd.notna() & (dd < LM)
            if LB is not None:
                keep &= dd >= (LM - LB)
            sub = chunk[col][keep].dropna().astype(str)
            if sub.empty:
                continue
            pid = chunk[ID][keep].loc[sub.index]
            ddv = dd[keep].loc[sub.index]
            m = pid.notna()
            for p, d, t in zip(pid[m].astype(int).tolist(), ddv[m].astype(int).tolist(),
                               sub[m].tolist()):
                if p in cohort_ids and t.strip():
                    rows.append((p, path.stem, d, t))
                    n += 1
            del chunk
        say(f"  cached {n:,} documents from {path.stem}.{col}")
        gc.collect()
    if not rows:
        raise SystemExit("no documents found — check --text-cols and --landmark-days")
    df = pd.DataFrame(rows, columns=[ID, "source", TIME, "text"])
    df.to_parquet(cache_path, index=False)
    say(f"  document cache: {len(df):,} documents -> {cache_path}")
    return df


# ---------------------------------------------------------------- cleaning

NAMEISH_PAT = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b")


def clean_text(t, strip_dates=True, strip_names=True, strip_nameish=False):
    if strip_nameish:
        # Mid-sentence capitalised words, removed BEFORE lowercasing. Phase 0 measured a
        # median of 50 such tokens per uitgaandebrief letter; once lowercased they survive
        # min_df and can encode the treating physician or site rather than the patient.
        # Blunt by design: it also removes capitalised proper medical nouns, which is why
        # it is opt-in and paired with a without-it arm.
        t = NAMEISH_PAT.sub(" ", t)
    t = t.lower()
    if strip_dates:
        t = ISO_DATE_PAT.sub(" ", t)
        t = NL_DATE_PAT.sub(" ", t)
    if strip_names:
        t = CLINICIAN_PAT.sub(" ", t)
    t = (t.encode("ascii", "ignore").decode("ascii")
         if not any(ord(c) > 127 for c in t[:200]) else
         t.translate(str.maketrans("àáâäèéêëìíîïòóôöùúûüç", "aaaaeeeeiiiioooouuuuc")))
    return re.sub(r"\s+", " ", t).strip()


def take_section(t, wanted):
    """Return only the named section(s) of a report, or '' if none are present.

    `wanted` is a list of header prefixes: Phase 0 found `voorgeschiedenis` in 79.9% and
    `anamnese` in 69.1% of discharge letters (where prior conditions are stated), whereas
    `conclusie` appears in only 17.6% of radiology reports, so restricting to a single
    section discards most documents.
    """
    parts = SECTION_SPLIT.split(t)
    if len(parts) < 3:
        return ""
    out = []
    # split() yields [pre, header, body, header, body, ...]
    for i in range(1, len(parts) - 1, 2):
        h = parts[i].lower()
        if any(h.startswith(w) for w in wanted):
            out.append(parts[i + 1])
    return " ".join(out).strip()


# ---------------------------------------------------------------- feature builders

def volume_features(docs, pids, sources):
    """Counts only — no content. The control every content arm must beat."""
    per = defaultdict(Counter)
    chars = Counter()
    recency = {}
    oldest = {}
    for p, src, dd, txt in docs:
        per[p][src] += 1
        chars[p] += len(txt)
        recency[p] = max(recency.get(p, -10 ** 9), dd)
        oldest[p] = min(oldest.get(p, 10 ** 9), dd)
    cols = {
        "text.n_documents": [float(sum(per[p].values())) for p in pids],
        "text.n_chars": [float(chars.get(p, 0)) for p in pids],
        "text.n_sources": [float(len(per[p])) for p in pids],
        "text.recency": [float(recency[p]) if p in recency else np.nan for p in pids],
        "text.history_span": [float(-oldest[p]) if p in oldest else np.nan for p in pids],
    }
    for s in sources:
        cols[f"text.n_docs[{s}]"] = [float(per[p].get(s, 0)) for p in pids]
    return pd.DataFrame(cols)


def compile_concepts(concepts):
    """One word-boundary alternation per concept.

    Plain substring matching is wrong for Dutch: `roken` (smoking) is a substring of
    `afgesproken` (agreed), so a substring match invents a smoking history out of routine
    scheduling text. Compounding makes such collisions common, so every term is anchored
    with word boundaries.
    """
    return {c: re.compile(r"\b(?:" + "|".join(re.escape(t) for t in sorted(terms, key=len,
                                                                          reverse=True)) + r")\b")
            for c, terms in concepts.items()}


def concept_features(text_by_pid, pids, concepts, window=6):
    """Assertion / negation / uncertainty counts per concept.

    Negation and uncertainty are scoped to the preceding `window` tokens and never cross a
    document boundary or sentence punctuation, so "geen diabetes" is not counted as
    diabetes and "verdenking infarct" is separated from an assertion.
    """
    names = sorted(concepts)
    pats = compile_concepts(concepts)
    data = {f"concept.{c}_{k}": np.zeros(len(pids))
            for c in names for k in ("present", "negated", "uncertain")}
    idx = {p: i for i, p in enumerate(pids)}
    for pid, text in text_by_pid.items():
        i = idx.get(pid)
        if i is None:
            continue
        for concept in names:
            for m in pats[concept].finditer(text):
                left = text[max(0, m.start() - 240):m.start()]
                for stop in ("||", ".", ";", "!", "?"):     # do not cross a boundary
                    k = left.rfind(stop)
                    if k >= 0:
                        left = left[k + len(stop):]
                toks = TOKEN_PAT.findall(left)[-window:]
                if any(t in NEG_CUES for t in toks):
                    data[f"concept.{concept}_negated"][i] += 1
                elif any(t in UNC_CUES for t in toks):
                    data[f"concept.{concept}_uncertain"][i] += 1
                else:
                    data[f"concept.{concept}_present"][i] += 1
    return pd.DataFrame(data)


def expand_concepts(concepts, train_texts, top_k, say, min_lift=3.0, min_docs=25):
    """Unsupervised synonym expansion: terms that co-occur with a seed far above base rate.

    Uses the TRAIN corpus only and never looks at the outcome, so it cannot bias the
    estimate the way supervised term selection would. Every added term is logged.
    """
    if not top_k:
        return concepts, {}
    _pats = compile_concepts(concepts)
    df_term = Counter()
    df_joint = defaultdict(Counter)
    n_docs = 0
    for txt in train_texts:
        n_docs += 1
        toks = set(TOKEN_PAT.findall(txt))
        df_term.update(toks)
        hit = [c for c, pat in _pats.items() if pat.search(txt)]
        for c in hit:
            df_joint[c].update(toks)
    added = {}
    seeds = {t for terms in concepts.values() for term in terms for t in term.split()}
    for c in concepts:
        base_c = sum(1 for txt in train_texts if _pats[c].search(txt))
        if base_c < min_docs:
            continue
        cand = []
        for term, joint in df_joint[c].items():
            if term in seeds or len(term) < 4 or df_term[term] < min_docs:
                continue
            lift = (joint / base_c) / max(df_term[term] / n_docs, 1e-9)
            if lift >= min_lift:
                cand.append((lift, term))
        cand.sort(reverse=True)
        new = [t for _, t in cand[:top_k]]
        if new:
            concepts[c] = concepts[c] + new
            added[c] = new
    if added:
        say("  unsupervised concept expansion (train corpus only, outcome never used):")
        for c, terms in added.items():
            say(f"    {c}: +{terms}")
    return concepts, added


def tfidf_features(texts, train_rows, analyzer, ngram, max_features, min_df, max_df,
                   n_components, say):
    from sklearn.decomposition import TruncatedSVD
    from sklearn.feature_extraction.text import TfidfVectorizer
    kw = dict(max_features=max_features, min_df=min_df, max_df=max_df, sublinear_tf=True,
              lowercase=True, strip_accents="unicode")
    if analyzer == "char":
        vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, ngram), **kw)
    else:
        vec = TfidfVectorizer(analyzer="word", ngram_range=(1, ngram), **kw)
    train_texts = [texts[i] for i in train_rows]
    Xtr = vec.fit_transform(train_texts)                    # TRAIN ONLY
    vocab = len(vec.vocabulary_)
    say(f"  TF-IDF analyzer={analyzer} vocab={vocab:,} (max_df={max_df} drops boilerplate)")
    if n_components and n_components > 0:
        k = min(n_components, max(Xtr.shape[1] - 1, 1))
        svd = TruncatedSVD(n_components=k, random_state=42).fit(Xtr)
        say(f"  SVD dim={k} (explained var={svd.explained_variance_ratio_.sum():.2f}; "
            "a low share is normal for text LSA)")
        M = svd.transform(vec.transform(texts))
        names = [f"tfidf.svd_{i}" for i in range(M.shape[1])]
    else:
        M = vec.transform(texts).toarray()
        names = [f"tfidf.{t}" for t in vec.get_feature_names_out()]
        say(f"  no SVD: {M.shape[1]:,} dense TF-IDF columns")
    return pd.DataFrame(M, columns=names)


def write_documents(text_by_pid, docs_by_pid, cohort, splits, out_dir, H, say):
    """Per-patient text parquet in the schema the Qwen extractor already consumes."""
    dur = cohort["first_event"].to_numpy(float)
    evt = cohort["cd_event"].to_numpy(int)
    pids = cohort[ID].astype(int).to_numpy()
    for name in ("train", "validation", "test"):
        rows = np.array(sorted(splits[name]), dtype=np.int64)
        if not len(rows):
            continue
        texts, deltas, d_, e_ = [], [], [], []
        for i in rows:
            p = int(pids[i])
            items = docs_by_pid.get(p, [])
            texts.append([t for _, t in items] or [""])
            deltas.append([float(dd) / 365.0 for dd, _ in items] or [0.0])
            c = apply_censoring(dur[i], evt[i], H)
            d_.append(c[0])
            e_.append(float(c[1]))
        Dataset.from_dict({"texts": texts, "time_deltas_list": deltas,
                           "duration": d_, "event": e_}).to_parquet(out_dir / f"{name}.parquet")
        say(f"  {name:11s}: {len(rows):,} patients | docs/patient median "
            f"{int(np.median([len(t) for t in texts]))}")
    say(f"  wrote per-patient documents -> feed to extract_qwen_embeddings_longitudinal.py "
        f"--parquet-dir {out_dir} --mode pool")


# ---------------------------------------------------------------- main

def main(args):
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    LM, H, LB = args.landmark_days, args.horizon_days, args.lookback_days
    log = []

    def say(msg):
        print(msg, flush=True)
        log.append(msg)

    say(f"  ARGS: mode={args.mode} landmark={LM} lookback={LB} horizon={H} "
        f"section={args.section} analyzer={args.analyzer} svd={args.svd_components} "
        f"add_baseline_cols={args.add_baseline_cols!r} min_coverage_frac={args.min_coverage_frac}")

    cohort, notes = build_cohort(args.smart_csv, args.legacy, args.censoring_time)
    for n in notes:
        say(f"  {n}")
    if LM > 0:
        n0 = len(cohort)
        e0 = int((cohort["cd_event"] == 1).sum())
        cohort = cohort[cohort["first_event"] > LM].copy()
        cohort["first_event"] = cohort["first_event"] - LM
        say(f"  landmark {LM}d: dropped {n0-len(cohort):,} patients whose outcome was at/before "
            f"the landmark ({e0-int((cohort['cd_event']==1).sum()):,} events)")
    cohort = cohort.reset_index(drop=True)
    pids = cohort[ID].astype(int).to_numpy()
    pindex = {p: i for i, p in enumerate(pids)}
    cohort_ids = set(int(p) for p in pids)

    with open(args.split_json) as f:
        sp = json.load(f)
    if "val" in sp and "validation" not in sp:
        sp["validation"] = sp.pop("val")
    splits = {k: [pindex[int(p)] for p in v if int(p) in pindex] for k, v in sp.items()}
    for k in ("train", "validation", "test"):
        splits.setdefault(k, [])
    train_rows = np.array(sorted(splits["train"]), dtype=np.int64)
    say(f"  cohort {len(pids):,} | train={len(splits['train']):,} "
        f"val={len(splits['validation']):,} test={len(splits['test']):,}")

    # ---- document cache
    specs = parse_text_cols(args.text_cols)
    cache = Path(args.cache) if args.cache else (out_dir / "documents_cache.parquet")
    if cache.exists() and not args.rebuild_cache:
        df = pd.read_parquet(cache)
        say(f"  reusing document cache {cache} ({len(df):,} documents)")
    else:
        cache.parent.mkdir(parents=True, exist_ok=True)
        df = build_cache(args.event_csv_folder, specs, LM, LB, cohort_ids, cache, say)
    df = df[df[ID].isin(cohort_ids)]
    sources = sorted(df["source"].unique())

    docs = list(zip(df[ID].astype(int), df["source"], df[TIME].astype(int), df["text"]))
    n_with = df[ID].nunique()
    emit("documents={} patients_with_text={}/{} ({:.1f}%)",
         len(docs), n_with, len(pids), 100*n_with/max(len(pids), 1))
    say(f"  {len(docs):,} documents, {n_with:,}/{len(pids):,} patients have text "
        f"({100*n_with/max(len(pids),1):.1f}%)")

    # --require-text is applied HERE, before the mode dispatch, and always means "has at
    # least one narrative document". Defining it once and uniformly is what lets a
    # demographics-only control be built on exactly the same subcohort, which is the
    # correct denominator for a require-text arm: 28% of the full cohort has no narrative
    # text, so 0.6883 (measured on the full cohort) is not the right bar for these arms.
    if args.require_text:
        has_doc = set(df[ID].astype(int))
        mask = np.array([p in has_doc for p in pids])
        keep_idx = sorted(int(i) for i in np.where(mask)[0])
        remap = {i: j for j, i in enumerate(keep_idx)}
        cohort = cohort[mask].reset_index(drop=True)
        pids = cohort[ID].astype(int).to_numpy()
        splits = {k: [remap[i] for i in v if i in remap] for k, v in splits.items()}
        train_rows = np.array(sorted(splits["train"]), dtype=np.int64)
        ev = int((cohort["cd_event"] == 1).sum())
        say(f"  --require-text: cohort restricted to {len(pids):,} patients with text "
            f"({ev:,} events) | train={len(splits['train']):,} "
            f"val={len(splits['validation']):,} test={len(splits['test']):,}")
        say("  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. "
            "Build the matched control with --mode baseline --require-text.")

    # ---- assemble the requested representation
    if args.mode == "baseline":
        # MATCHED CONTROL. Emits only the numeric SMART baseline, but on the cohort the
        # text flags define, so a --require-text text arm can be compared against
        # demographics on identical patients rather than against a full-cohort number.
        X, kept = smart_baseline_features(args.smart_csv, pids, args.baseline_cols)
        say(f"  MATCHED CONTROL ({args.baseline_cols or 'all'}): {X.shape[1]} baseline "
            f"features -> {kept}")
        finish(out_dir, X, cohort, splits, train_rows, H, say, log,
               clip_quantile=args.clip_quantile, min_coverage_frac=args.min_coverage_frac,
               screen_features=args.screen_features, screen_top=args.screen_top,
               rep=f"matched_baseline[{args.baseline_cols or 'all'}]", baseline_cols=kept,
               extra_meta={"landmark_days": LM, "lookback_days": LB, "mode": "baseline",
                           "require_text": args.require_text,
                           "text_cols": args.text_cols})
        return
    if args.mode == "volume":
        X = volume_features(docs, pids, sources)
        rep = "text_volume"
    else:
        # cleaned, per-patient concatenation with a hard document boundary
        docs_by_pid = defaultdict(list)
        for p, src, dd, txt in docs:
            t = clean_text(txt, args.strip_dates, args.strip_names, args.strip_nameish)
            if args.section:
                t = take_section(t, [w.strip().lower()
                                     for w in args.section.split(",") if w.strip()])
                if not t:
                    continue
            if t:
                docs_by_pid[p].append((dd, t))
        for p in docs_by_pid:
            docs_by_pid[p].sort()
        text_by_pid = {p: DOC_SEP.join(t for _, t in v) for p, v in docs_by_pid.items()}
        kept = len(text_by_pid)
        say(f"  after cleaning{' + section=' + args.section if args.section else ''}: "
            f"{kept:,} patients retain text ({100*kept/max(len(pids),1):.1f}%)")
        n_empty = sum(1 for p in pids if not text_by_pid.get(p))
        if n_empty:
            say(f"  {n_empty:,} patients have no text after cleaning"
                f"{'/section' if args.section else ''} and get an all-zero vector")
        texts = [text_by_pid.get(p, "") for p in pids]

        if args.mode == "documents":
            write_documents(text_by_pid, docs_by_pid, cohort, splits, out_dir, H, say)
            with open(out_dir / "metadata.json", "w") as f:
                json.dump({"representation": "text_documents", "landmark_days": LM,
                           "lookback_days": LB, "horizon_days": H, "section": args.section,
                           "n_patients": len(pids), "log": log}, f, indent=2)
            return
        if args.mode == "tfidf":
            X = tfidf_features(texts, train_rows, args.analyzer, args.ngram_max,
                               args.max_features, args.min_df, args.max_df,
                               args.svd_components, say)
            rep = f"text_tfidf[{args.analyzer}]" + (f"+section:{args.section}" if args.section else "")
        elif args.mode == "concepts":
            concepts = {k: list(v) for k, v in CONCEPTS.items()}
            concepts, added = expand_concepts(
                concepts, [texts[i] for i in train_rows], args.expand_terms, say)
            X = concept_features(text_by_pid, pids, concepts)
            nz = int((X.to_numpy() > 0).any(axis=0).sum())
            say(f"  {X.shape[1]} concept features ({nz} non-empty) from "
                f"{len(concepts)} concepts x present/negated/uncertain")
            rep = "text_concepts"
        else:
            raise SystemExit(f"unknown --mode {args.mode}")

    added_base = []
    if args.add_baseline_cols:
        B, added_base = smart_baseline_features(args.smart_csv, pids, args.add_baseline_cols)
        say(f"  appending {B.shape[1]} baseline columns -> {added_base}")
        X = pd.concat([X.reset_index(drop=True), B.reset_index(drop=True)], axis=1)
        rep += f"+baseline[{args.add_baseline_cols}]"

    finish(out_dir, X, cohort, splits, train_rows, H, say, log,
           clip_quantile=args.clip_quantile, min_coverage_frac=args.min_coverage_frac,
           screen_features=args.screen_features, screen_top=args.screen_top,
           rep=rep, baseline_cols=added_base,
           extra_meta={"landmark_days": LM, "lookback_days": LB, "mode": args.mode,
                       "section": args.section, "analyzer": args.analyzer,
                       "svd_components": args.svd_components, "text_cols": args.text_cols,
                       "require_text": args.require_text,
                       "strip_dates": args.strip_dates, "strip_names": args.strip_names,
                       "strip_nameish": args.strip_nameish,
                       "expand_terms": args.expand_terms})


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True, help="Used for the target, and for "
                                                     "--add-baseline-cols only.")
    p.add_argument("--event-csv-folder", required=True)
    p.add_argument("--split-json", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--mode", required=True,
                   choices=("volume", "tfidf", "concepts", "documents", "baseline"))
    p.add_argument("--landmark-days", type=int, default=180)
    p.add_argument("--lookback-days", type=int, default=None)
    p.add_argument("--horizon-days", type=int, default=5475)
    p.add_argument("--legacy", action="store_true")
    p.add_argument("--censoring-time", type=int, default=None)
    p.add_argument("--text-cols", default=TEXT_COLS_DEFAULT,
                   help="src:column of NARRATIVE columns only. The short label fields were "
                        "already tested as occurrence codes in the structured arm.")
    p.add_argument("--cache", default=None,
                   help="Document cache parquet. Defaults to <out-dir>/documents_cache.parquet; "
                        "point every arm at one shared path to stream the CSVs only once.")
    p.add_argument("--rebuild-cache", action="store_true")
    p.add_argument("--section", default=None,
                   help="Restrict to these report sections, comma-separated, e.g. "
                        "'voorgeschiedenis,anamnese' (where prior conditions are stated) or "
                        "'conclusie'. Documents lacking every named section are dropped.")
    p.add_argument("--strip-nameish", action="store_true",
                   help="Also remove mid-sentence capitalised words before lowercasing. "
                        "Discharge letters carry ~50 such tokens each, which can encode the "
                        "treating physician or site; blunt, so pair it with a run without it.")
    p.add_argument("--analyzer", default="word", choices=("word", "char"),
                   help="char uses char_wb 3-N grams, robust to Dutch compounding and typos.")
    p.add_argument("--ngram-max", type=int, default=2)
    p.add_argument("--max-features", type=int, default=50000)
    p.add_argument("--min-df", type=int, default=5)
    p.add_argument("--max-df", type=float, default=0.8,
                   help="Drop terms appearing in more than this share of TRAIN documents — the "
                        "main lever against templated boilerplate.")
    p.add_argument("--svd-components", type=int, default=256,
                   help="0 disables SVD and feeds dense TF-IDF (watch the event budget).")
    p.add_argument("--expand-terms", type=int, default=0,
                   help="Unsupervised synonyms per concept, mined from the TRAIN corpus by "
                        "co-occurrence lift. The outcome is never used. 0 disables.")
    p.add_argument("--require-text", action="store_true",
                   help="Restrict the cohort to patients who have text, so a null is not the "
                        "empty-text confound.")
    p.add_argument("--strip-dates", action="store_true", default=True)
    p.add_argument("--keep-dates", dest="strip_dates", action="store_false",
                   help="Sensitivity arm: leave dates in, which lets calendar era leak.")
    p.add_argument("--strip-names", action="store_true", default=True)
    p.add_argument("--keep-names", dest="strip_names", action="store_false",
                   help="Sensitivity arm: leave clinician/department tokens in.")
    p.add_argument("--baseline-cols", default=None,
                   help="With --mode baseline: which baseline columns the matched control "
                        "emits, e.g. 'leeftijd,geslacht'. Prefix with ~ to exclude instead.")
    p.add_argument("--add-baseline-cols", default=None,
                   help="Append baseline columns, e.g. 'leeftijd,geslacht' for the fair "
                        "text+demographics arm.")
    p.add_argument("--list-baseline-cols", action="store_true")
    p.add_argument("--clip-quantile", type=float, default=0.001)
    p.add_argument("--min-coverage-frac", type=float, default=0.10)
    p.add_argument("--screen-features", action="store_true")
    p.add_argument("--screen-top", type=int, default=30)
    add_results_arg(p)
    a = p.parse_args()
    if a.list_baseline_cols:
        list_baseline_cols(a.smart_csv)
    else:
        with results_block(a.results_file, f"text arm: {a.mode}",
                           {"mode": a.mode, "landmark": a.landmark_days,
                            "lookback": a.lookback_days, "horizon": a.horizon_days,
                            "section": a.section, "analyzer": a.analyzer,
                            "require_text": a.require_text,
                            "add_baseline": a.add_baseline_cols,
                            "baseline_cols": a.baseline_cols, "out": a.out_dir}):
            main(a)
