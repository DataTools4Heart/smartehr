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
from feature_matrix import (finish, handle_listing_flags, smart_baseline_features,
                            smart_baseline_numeric)
from graded_concepts import (ANTIHYPERTENSIVE, CURATED_MISSING, MED_CLASSES,
                             VALIDATION_PAIRS, _spearman, compile_med_lexicon,
                             extract_ages, extract_sex,
                             extract_alcohol, extract_aorta_cm, extract_medications,
                             extract_onset_years, extract_packyears,
                             extract_smoking_status, extract_stenosis)
from results_log import add_results_arg, emit, results_block

CHUNK = 50_000
DOC_SEP = " || "          # hard boundary: negation must not bleed across documents

TEXT_COLS_DEFAULT = ("consult:consult_tekst,uitgaandebrief:inhoud,"
                     "radiologie_verslag:verslagtekst,mri_verslag:rad_report")

ISO_DATE_PAT = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
NL_DATE_PAT = re.compile(r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b")
# Year-only replacements, for --date-mode year. The graded arm needs the onset YEAR
# (KliMaYr is one of the four carriers the headroom check identified), and full stripping
# destroys it whenever a letter writes "CABG op 12-05-2003" rather than "CABG in 2003".
# Keeping the year alone preserves what onset needs at the coarsest granularity that
# still works, without leaving full dates in the text.
ISO_YEAR_SUB = re.compile(r"\b(\d{4})-\d{2}-\d{2}\b")
NL_YEAR_SUB = re.compile(r"\b\d{1,2}[-/]\d{1,2}[-/](\d{4})\b")
NL_YEAR2_SUB = re.compile(r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2}\b")
CLINICIAN_PAT = re.compile(r"\b(dr|drs|arts|aios|anios|prof|mw|hr|collega|specialist|"
                           r"cardioloog|neuroloog|internist|radioloog)\b", re.I)
SECTION_SPLIT = re.compile(
    r"\b(conclusie|bevinding(?:en)?|anamnese|beleid|indicatie|voorgeschiedenis|"
    r"lichamelijk onderzoek|samenvatting|advies|klinische gegevens)\b\s*:?", re.I)
TOKEN_PAT = re.compile(r"[a-z0-9]+")

# --- Dutch clinical concepts, TIERED -----------------------------------------------------
# Terms are separated by what a mention actually asserts, because mixing the tiers conflates
# two different questions. `egfr` fires on "eGFR 95 ml/min" — i.e. NORMAL kidney function —
# so a list containing it measures "renal function was reported", not "renal disease is
# present". The same held for `cholesterol` (fires on a normal lipid value), for the
# medication proxies, and for `pakjaren` (a quantity, not a status). `aneurysma` was worse
# than a tier error: an aneurysm is a different disease from peripheral arterial disease, so
# it is now its own concept.
#
# The default tier set is therefore disease+symptom: what the note ASSERTS about the patient.
# `--concept-terms all` reproduces the earlier, conflated behaviour for comparison.
CONCEPTS = {
    "roken": {
        "disease": ["roken", "roker", "rookt", "nicotine", "sigaretten", "rookgedrag"],
        "measurement": ["pakjaren", "packyears"],
    },
    "diabetes": {
        "disease": ["diabetes", "diabetes mellitus", "suikerziekte", "dm2", "dm ii"],
        "medication": ["insuline", "metformine", "gliclazide"],
    },
    "myocardinfarct": {
        "disease": ["myocardinfarct", "hartinfarct", "stemi", "nstemi", "infarct"],
    },
    "cva_tia": {
        "disease": ["cva", "herseninfarct", "tia", "beroerte", "hersenbloeding"],
    },
    "hartfalen": {
        "disease": ["hartfalen", "decompensatio cordis", "hfref", "hfpef"],
        "measurement": ["ejectiefractie verlaagd", "ejectiefractie"],
    },
    "nierfunctie": {
        "disease": ["nierinsufficientie", "nierfalen", "chronische nierschade", "nierschade",
                    "nierfunctiestoornis"],
        "procedure": ["dialyse", "hemodialyse", "niertransplantatie"],
        "measurement": ["egfr", "creatinineklaring", "kreatinineklaring", "mdrd"],
    },
    "perifeer_vaatlijden": {
        "disease": ["perifeer arterieel vaatlijden", "perifeer vaatlijden", "pav",
                    "claudicatio", "etalagebenen"],
    },
    "aneurysma": {          # split out of perifeer_vaatlijden: a distinct disease
        "disease": ["aneurysma", "aneurysmatisch", "aaa"],
    },
    "hypertensie": {
        "disease": ["hypertensie", "hoge bloeddruk"],
        "medication": ["antihypertensiva"],
    },
    "hyperlipidemie": {
        "disease": ["hypercholesterolemie", "dyslipidemie", "hyperlipidemie"],
        "medication": ["statine", "atorvastatine", "simvastatine"],
        "measurement": ["cholesterol", "ldl"],
    },
    "atriumfibrilleren": {
        "disease": ["atriumfibrilleren", "atriumfibrillatie", "boezemfibrilleren", "vkf"],
    },
    "angina": {
        "disease": ["angina pectoris", "angina"],
        "symptom": ["thoracale klachten", "pijn op de borst"],
    },
    "stenose": {
        "disease": ["stenose", "vernauwing", "occlusie"],
    },
    "revascularisatie": {   # procedure-only: absent under the default disease+symptom tiers
        "procedure": ["pci", "dotter", "stent", "cabg", "bypass", "endarteriectomie",
                      "endarterectomie"],
    },
}
CONCEPT_TIERS = ("disease", "symptom", "measurement", "medication", "procedure")


def resolve_concepts(tiered, tiers, say=None):
    """Flatten the tiered definitions down to {concept: [terms]} for the selected tiers."""
    out, dropped = {}, []
    for concept, by_tier in tiered.items():
        terms = [t for tier in tiers for t in by_tier.get(tier, [])]
        if terms:
            out[concept] = terms
        else:
            dropped.append(concept)
    if say:
        say(f"  concept tiers in use: {','.join(tiers)}")
        if dropped:
            say(f"  concepts with no terms in these tiers, skipped: {','.join(dropped)}")
    return out


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


def clean_text(t, strip_dates=True, strip_names=True, strip_nameish=False,
               date_mode="strip"):
    if strip_nameish:
        # Mid-sentence capitalised words, removed BEFORE lowercasing. Phase 0 measured a
        # median of 50 such tokens per uitgaandebrief letter; once lowercased they survive
        # min_df and can encode the treating physician or site rather than the patient.
        # Blunt by design: it also removes capitalised proper medical nouns, which is why
        # it is opt-in and paired with a without-it arm.
        t = NAMEISH_PAT.sub(" ", t)
    t = t.lower()
    if date_mode == "year":
        # keep the year, drop day and month; a 2-digit year is ambiguous, so drop it
        t = ISO_YEAR_SUB.sub(r" \1 ", t)
        t = NL_YEAR_SUB.sub(r" \1 ", t)
        t = NL_YEAR2_SUB.sub(" ", t)
    elif strip_dates:
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


def concept_features(text_by_pid, pids, concepts, window=6, encoding="binary"):
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
    out = {}
    for name, vec in data.items():
        if encoding in ("count", "both"):
            out[name + ("_n" if encoding == "both" else "")] = vec
        if encoding in ("binary", "both"):
            out[name] = (vec > 0).astype(float)
    return pd.DataFrame(out)


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


def build_med_lexicon(event_csv_folder, train_ids, lexicon_path, say):
    """Derive {medication class: [Dutch drug names]} from the cohort's own prescriptions.

    Grounded rather than invented: `med_ZIatc` and `med_genNaam` are documented in
    data/smartehr/data_dicts/data_dict.csv as "Medication ATC code" and "Medication name",
    so the names that express each ATC class IN THIS COHORT come from the data. Writing
    Dutch drug lists by hand is precisely the ungrounded guess that the prefix-partition
    mistake already cost us once (see the report's §10.2b method note).

    TRAIN patients only. The lexicon shapes the feature space, so building it on the full
    cohort would let validation and test influence the representation.
    """
    if lexicon_path and Path(lexicon_path).exists():
        lex = json.load(open(lexicon_path))
        say(f"  reusing medication lexicon {lexicon_path} "
            f"({sum(len(v) for v in lex.values()):,} names, {len(lex)} classes)")
        return lex
    prefixes = [(cls, pre) for cls, spec in MED_CLASSES.items() for pre in spec["atc"]]
    found = {cls: set() for cls in MED_CLASSES}
    path = next((q for q in sorted(Path(event_csv_folder).glob("*.csv"))
                 if q.stem.startswith("med_")), None)
    if path is None:
        raise SystemExit(f"no med_*.csv in {event_csv_folder}; the graded arm needs it to "
                         "derive the medication lexicon")
    train = set(train_ids)
    n_rows = 0
    for chunk in pd.read_csv(path, chunksize=CHUNK, low_memory=False):
        for c in ("med_ZIatc", "med_genNaam"):
            if c not in chunk.columns:
                raise SystemExit(f"{path.name} has no `{c}`; cannot derive the lexicon")
        sub = chunk[chunk[ID].isin(train)]
        n_rows += len(sub)
        atc = sub["med_ZIatc"].astype(str).str.upper()
        nm = sub["med_genNaam"].astype(str)
        for cls, pre in prefixes:
            hit = atc.str.startswith(pre)
            if hit.any():
                found[cls].update(nm[hit].unique())
    lex = {cls: sorted(v) for cls, v in found.items() if v}
    say(f"  medication lexicon derived from {path.name} ({n_rows:,} train rows): "
        f"{len(lex)} of {len(MED_CLASSES)} classes have names in this cohort")
    for cls in sorted(MED_CLASSES):
        names = lex.get(cls, [])
        # Names are drug names, not patient data, so they are safe to log -- and the log
        # is the only way to audit what the text matcher will look for.
        say(f"    {cls:<28s} {MED_CLASSES[cls]['smart']:<7s} "
            f"{'/'.join(MED_CLASSES[cls]['atc']):<14s} {len(names):3d} names"
            + (f": {', '.join(names[:6])}{' ...' if len(names) > 6 else ''}" if names else
               "  <- NONE; this class cannot be detected in text"))
    empty = [c for c in MED_CLASSES if c not in lex]
    if empty:
        emit("medication classes with no names in this cohort (undetectable): {}",
             ",".join(empty))
    if lexicon_path:
        Path(lexicon_path).parent.mkdir(parents=True, exist_ok=True)
        json.dump(lex, open(lexicon_path, "w"), indent=1, ensure_ascii=False)
        say(f"  lexicon written to {lexicon_path}")
    return lex


def graded_features(docs_by_pid, pids, med_compiled, say):
    """Quantities and dates, on the curated variables' own scales.

    Extraction is PER DOCUMENT, not on the per-patient concatenation, so a percentage in
    one radiology report cannot bind to a vessel term in another. Aggregation then mirrors
    each registry variable's own definition: stenosis and aorta take the MAXIMUM
    (aorta_hg is "Grootste diameter"), onset takes the EARLIEST year (KliMaYr is the
    "eerste uiting"), and status fields also report the most recent document's value.

    Unstated quantities are NaN, not 0. A patient whose notes never mention stenosis has
    not been graded 0 -- that is the distinction between "no disease" and "not measured",
    and conflating them is what made `gfr_count` read C=0.851 in the structured arm. Each
    quantity therefore also gets an explicit `_measured` indicator, so the screen can see
    a missingness artefact instead of having it hide inside the value column.
    """
    med_names = sorted(med_compiled)
    cols = (["graded.sex_from_text", "graded.age_from_text",     # the join positive control
             "graded.stenosis_max", "graded.stenosis_last", "graded.stenosis_left_max",
             "graded.stenosis_right_max", "graded.stenosis_ge50", "graded.stenosis_ge70",
             "graded.stenosis_n", "graded.stenosis_measured",
             "graded.packyears", "graded.packyears_stated",
             "graded.packyears_measured",
             "graded.smoking_status_last", "graded.smoking_status_max",
             "graded.alcohol_status_last", "graded.alcohol_glasses_band",
             "graded.onset_year_min", "graded.onset_year_n", "graded.onset_measured",
             "graded.aorta_cm_max", "graded.aorta_measured",
             "graded.n_antihypertensive_classes", "graded.any_antihypertensive",
             "graded.n_med_classes"]
            + [f"graded.med_{c}" for c in med_names])
    X = pd.DataFrame(np.nan, index=range(len(pids)), columns=cols)
    idx = {p: i for i, p in enumerate(pids)}
    hits = {c: 0 for c in cols}
    for pid, items in docs_by_pid.items():
        i = idx.get(pid)
        if i is None:
            continue
        sten, sten_l, sten_r, sten_last = [], [], [], None
        py, py_stated, years, aorta = [], [], [], []
        smoke, smoke_last = [], None
        alc_status, alc_band = [], []
        sexes, ages = [], []
        classes = set()
        for dd, txt in items:                      # already sorted oldest -> newest
            for grade, side in extract_stenosis(txt):
                sten.append(grade)
                sten_last = grade
                (sten_l if side == "left" else sten_r if side == "right" else []).append(grade)
            py += extract_packyears(txt)
            py_stated += extract_packyears(txt, reconstruct=False)
            years += extract_onset_years(txt)
            aorta += extract_aorta_cm(txt)
            sm = extract_smoking_status(txt)
            if sm is not None:
                smoke.append(sm)
                smoke_last = sm
            st, band = extract_alcohol(txt)
            if st is not None:
                alc_status.append(st)
            if band is not None:
                alc_band.append(band)
            sx = extract_sex(txt)
            if sx is not None:
                sexes.append(sx)
            ages += extract_ages(txt)
            classes |= extract_medications(txt, med_compiled)

        def put(col, val):
            X.iat[i, cols.index(col)] = val

        if sexes:
            # majority vote across this patient's documents
            put("graded.sex_from_text", 1.0 if sexes.count(1) >= sexes.count(2) else 2.0)
        if ages:
            put("graded.age_from_text", float(np.median(ages)))
        if sten:
            put("graded.stenosis_max", max(sten))
            put("graded.stenosis_last", sten_last)
            put("graded.stenosis_ge50", 1.0 if max(sten) >= 3 else 0.0)
            put("graded.stenosis_ge70", 1.0 if max(sten) >= 4 else 0.0)
            put("graded.stenosis_n", len(sten))
        if sten_l:
            put("graded.stenosis_left_max", max(sten_l))
        if sten_r:
            put("graded.stenosis_right_max", max(sten_r))
        put("graded.stenosis_measured", 1.0 if sten else 0.0)
        if py:
            put("graded.packyears", max(py))
        if py_stated:
            # Kept apart from the reconstructed value: when the two disagree with the
            # curated `packyrs`, only separate features say which path is at fault.
            put("graded.packyears_stated", max(py_stated))
        put("graded.packyears_measured", 1.0 if py else 0.0)
        if smoke:
            put("graded.smoking_status_last", smoke_last)
            put("graded.smoking_status_max", max(smoke))
        if alc_status:
            put("graded.alcohol_status_last", alc_status[-1])
        if alc_band:
            put("graded.alcohol_glasses_band", max(alc_band))
        if years:
            put("graded.onset_year_min", min(years))     # KliMaYr: the FIRST manifestation
            put("graded.onset_year_n", len(years))
        put("graded.onset_measured", 1.0 if years else 0.0)
        if aorta:
            put("graded.aorta_cm_max", max(aorta))       # aorta_hg: "Grootste diameter"
        put("graded.aorta_measured", 1.0 if aorta else 0.0)
        # mht_alln is "Aantal verschillende groepen antihypertensiva" -- a COUNT of
        # distinct classes, which is why presence flags alone could not reproduce it.
        n_ah = len(classes & set(ANTIHYPERTENSIVE))
        put("graded.n_antihypertensive_classes", float(n_ah))
        put("graded.any_antihypertensive", 1.0 if n_ah else 0.0)
        put("graded.n_med_classes", float(len(classes)))
        for c in med_names:
            put(f"graded.med_{c}", 1.0 if c in classes else 0.0)
    for c in cols:
        hits[c] = int(X[c].notna().sum())
    say(f"  {len(cols)} graded features; coverage over {len(pids):,} patients "
        "(NaN = not stated, which the pre-imputation screen scores separately):")
    for c in cols:
        v = X[c].dropna()
        extra = ""
        if len(v) and not c.endswith(("_measured", "_n")):
            extra = f"  median={v.median():.2f} p90={v.quantile(0.9):.2f}"
        say(f"    {c:<40s} {hits[c]:6,} ({100*hits[c]/max(len(pids),1):5.1f}%){extra}")
    return X


def validate_graded(X, smart_csv, pids, train_rows, say):
    """Agreement between each extracted quantity and the curated variable measuring it.

    Outcome-blind by construction, so it cannot overfit the 828 events and can be read
    before any survival number. It answers the question every previous null left open --
    does the extraction work? -- and settles ASSUMPTIONS.md #4's Dutch severity-word
    mapping empirically rather than by assertion.

    Train patients only, to keep the same discipline as every other selection step.
    """
    df, _cols = smart_baseline_numeric(smart_csv)
    cur = df.reindex([pids[i] for i in train_rows])
    Xtr = X.iloc[list(train_rows)].reset_index(drop=True)
    say("\n  --- extracted vs curated, TRAIN, outcome never consulted ---")
    say("  `both` is the patients where BOTH are present; agreement is only defined there.")
    say(f"  {'extracted':<38s} {'curated':<20s} {'both':>6s} {'rho':>7s} "
        f"{'exact':>7s} {'sens':>6s} {'spec':>6s}")
    rows = []
    for feat, curated, kind in VALIDATION_PAIRS:
        if feat not in Xtr.columns:
            continue
        present = [c for c in curated if c in cur.columns]
        if not present:
            say(f"  {feat[:38]:<38s} {'/'.join(curated):<20s}   <- curated column absent")
            continue
        cv = None
        for c in present:
            v = pd.to_numeric(cur[c], errors="coerce").to_numpy(float)
            v = np.where(np.isin(v, CURATED_MISSING.get(c, ())), np.nan, v)
            cv = v if cv is None else np.fmax(cv, v)      # ordinal_max over both sides
        ev = Xtr[feat].to_numpy(float)
        ok = ~np.isnan(ev) & ~np.isnan(cv)
        n = int(ok.sum())
        if n < 8:
            say(f"  {feat[:38]:<38s} {'/'.join(present):<20s} {n:6,}   too few to compare")
            continue
        e, c_ = ev[ok], cv[ok]
        rho = _spearman(e, c_)
        exact = float((e == c_).mean()) if kind in ("ordinal", "ordinal_max", "categorical",
                                                    "binary") else float("nan")
        sens = spec = float("nan")
        if kind == "binary":
            pos, neg = c_ > 0, c_ == 0
            sens = float((e[pos] > 0).mean()) if pos.any() else float("nan")
            spec = float((e[neg] == 0).mean()) if neg.any() else float("nan")
        say(f"  {feat[:38]:<38s} {'/'.join(present):<20s} {n:6,} "
            f"{(f'{rho:+.3f}' if rho is not None else '   -  '):>7s} "
            f"{(f'{exact:.3f}' if exact == exact else '   -  '):>7s} "
            f"{(f'{sens:.3f}' if sens == sens else '  -   '):>6s} "
            f"{(f'{spec:.3f}' if spec == spec else '  -   '):>6s}")
        rows.append((feat, rho, n))
    ctrl = {f: r for f, r, n in rows if f in ("graded.sex_from_text", "graded.age_from_text")}
    if ctrl:
        worst = min((abs(r) for r in ctrl.values() if r is not None), default=0.0)
        detail = ", ".join(f"{f.split('.')[-1]} rho={r:+.3f}" if r is not None else f
                           for f, r in ctrl.items())
        if worst >= 0.5:
            emit("JOIN CONTROL PASSES ({}): documents are joined to the right patients, so "
                 "a weak graded result is about extraction, not plumbing", detail)
        else:
            emit("** JOIN CONTROL FAILS ({}) **: age and sex are stated in nearly every "
                 "letter, so failing to recover them means the documents are NOT joined to "
                 "the right patients -- and EVERY text arm (T0 volume, T1 TF-IDF, T2 "
                 "concepts) is then invalid, not just this one", detail)
            say("  ** THE JOIN CONTROL FAILED. Stop here: no text result in this project is")
            say("     interpretable until the document-to-patient join is fixed. Note that")
            say("     plausible concept PREVALENCES do not rule this out -- a shuffled cache")
            say("     preserves prevalence exactly. **")
    good = [f"{f.split('.')[-1]} rho={r:+.2f}" for f, r, n in rows
            if r is not None and abs(r) >= 0.3]
    emit("graded vs curated (train, outcome-blind): {} of {} pairs reach |rho|>=0.3{}",
         len(good), len(rows), "; " + ", ".join(good[:5]) if good else "")
    if not good and rows:
        say("  ** nothing reaches |rho|>=0.3: the extraction does not recover the curated")
        say("     quantities, so a null survival result would be about extraction, not text **")
    # Medication flags, class by class against their own SMART flag.
    say(f"\n  {'extracted medication class':<38s} {'curated':<10s} {'both':>6s} "
        f"{'sens':>6s} {'spec':>6s}")
    for cls, spec_ in sorted(MED_CLASSES.items()):
        feat, cc = f"graded.med_{cls}", spec_["smart"]
        if feat not in Xtr.columns or cc not in cur.columns:
            continue
        cv = pd.to_numeric(cur[cc], errors="coerce").to_numpy(float)
        cv = np.where(np.isin(cv, (9,)), np.nan, cv)       # 9 -> Missend, per smart.csv
        ev = Xtr[feat].to_numpy(float)
        ok = ~np.isnan(ev) & ~np.isnan(cv)
        if int(ok.sum()) < 8:
            continue
        e, c_ = ev[ok], cv[ok]
        pos, neg = c_ > 0, c_ == 0
        sn = float((e[pos] > 0).mean()) if pos.any() else float("nan")
        sp = float((e[neg] == 0).mean()) if neg.any() else float("nan")
        say(f"  {cls:<38s} {cc:<10s} {int(ok.sum()):6,} "
            f"{(f'{sn:.3f}' if sn == sn else '  -   '):>6s} "
            f"{(f'{sp:.3f}' if sp == sp else '  -   '):>6s}")
    say("")


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
        f"require_text={args.require_text} strip_dates={args.strip_dates} "
        f"date_mode={args.date_mode} med_lexicon={args.med_lexicon} "
        f"strip_names={args.strip_names} strip_nameish={args.strip_nameish} "
        f"concept_encoding={args.concept_encoding} concept_terms={args.concept_terms} "
        f"expand_terms={args.expand_terms} "
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
        X, kept = smart_baseline_features(args.smart_csv, pids, args.baseline_cols, say)
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
            t = clean_text(txt, args.strip_dates, args.strip_names, args.strip_nameish,
                           date_mode=args.date_mode)
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
            tiers = [t.strip() for t in args.concept_terms.split(",") if t.strip()]
            for t in tiers:
                if t not in CONCEPT_TIERS:
                    raise SystemExit(f"--concept-terms must come from {CONCEPT_TIERS}")
            concepts = resolve_concepts(CONCEPTS, tiers, say)
            concepts, added = expand_concepts(
                concepts, [texts[i] for i in train_rows], args.expand_terms, say)
            X = concept_features(text_by_pid, pids, concepts,
                                 encoding=args.concept_encoding)
            # Prevalence is essential to interpret a flat C: a concept that fires for 40
            # patients and one that fires for 8,000 both produce C ~ 0.5, for opposite
            # reasons. Without this the concept null cannot be read at all.
            say(f"  {X.shape[1]} concept features (encoding={args.concept_encoding}) from "
                f"{len(concepts)} concepts x present/negated/uncertain")
            say(f"  {'concept':<26s} {'asserted':>9s} {'negated':>9s} {'uncertain':>9s}"
                f"   (patients, % of those with text)")
            n_txt = max(len(text_by_pid), 1)
            prev = {}
            for c in sorted(concepts):
                row = []
                for k in ("present", "negated", "uncertain"):
                    col = f"concept.{c}_{k}"
                    col = col if col in X.columns else col + "_n"
                    row.append(int((X[col].to_numpy() > 0).sum()) if col in X.columns else 0)
                prev[c] = row
                say(f"  {c:<26s} {row[0]:9,} {row[1]:9,} {row[2]:9,}"
                    f"   ({100*row[0]/n_txt:.1f}% asserted)")
            top = sorted(prev.items(), key=lambda kv: -kv[1][0])[:4]
            emit("concept prevalence (asserted, of {} patients with text): {}", n_txt,
                 ", ".join(f"{c}={v[0]}" for c, v in top))
            never = [c for c, v in prev.items() if sum(v) == 0]
            if never:
                emit("concepts NEVER matched: {}", ",".join(never))
            rep = f"text_concepts[{args.concept_encoding}/{args.concept_terms}]"
        elif args.mode == "graded":
            # Aimed squarely at the four carriers the headroom check named: percent
            # stenosis, dated onset, pack-years and medication-class count.
            if args.date_mode != "year":
                say("  NOTE: --date-mode is not 'year', so a year written as part of a full "
                    "date is stripped and graded.onset_year_min will under-fire. The paired "
                    "arm exists to measure the calendar-era contribution; read them together.")
            lex = build_med_lexicon(args.event_csv_folder,
                                    [pids[i] for i in train_rows],
                                    args.med_lexicon, say)
            X = graded_features(docs_by_pid, pids, compile_med_lexicon(lex), say)
            n_any = int(X[[c for c in X.columns if c.endswith("_measured")]].fillna(0)
                        .to_numpy().max(axis=1).sum())
            emit("graded: {} features; {} of {} patients have at least one extracted "
                 "quantity", X.shape[1], n_any, len(pids))
            if args.validate_baseline:
                validate_graded(X, args.smart_csv, pids, train_rows, say)
            rep = f"text_graded[dates={args.date_mode}]"
            if args.with_concepts:
                # The headline "everything the text gives us" arm: graded quantities are
                # what T1/T2 lacked, but presence features are not thereby worthless, and
                # the ceiling to beat (0.7310) was set by a model holding both kinds.
                tiers = [t.strip() for t in args.concept_terms.split(",") if t.strip()]
                cc = resolve_concepts(CONCEPTS, tiers, say)
                C = concept_features(text_by_pid, pids, cc, encoding=args.concept_encoding)
                say(f"  + {C.shape[1]} concept features appended "
                    f"({args.concept_encoding}/{args.concept_terms})")
                X = pd.concat([X.reset_index(drop=True), C.reset_index(drop=True)], axis=1)
                rep += f"+concepts[{args.concept_terms}]"
        else:
            raise SystemExit(f"unknown --mode {args.mode}")

    added_base = []
    if args.add_baseline_cols:
        B, added_base = smart_baseline_features(args.smart_csv, pids, args.add_baseline_cols, say)
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
                       "expand_terms": args.expand_terms,
                       "concept_encoding": args.concept_encoding,
                       "concept_terms": args.concept_terms,
                       "date_mode": args.date_mode,
                       "med_lexicon": args.med_lexicon})



if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--smart-csv", required=True, help="Used for the target, and for "
                                                     "--add-baseline-cols only.")
    p.add_argument("--event-csv-folder", required=True)
    p.add_argument("--split-json", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--mode", required=True,
                   choices=("volume", "tfidf", "concepts", "graded", "documents",
                            "baseline"))
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
    p.add_argument("--concept-terms", default="disease,symptom",
                   help=f"Which term tiers count as a concept mention, from {CONCEPT_TIERS}. "
                        "Default disease,symptom = what the note ASSERTS about the patient. "
                        "Measurement terms such as 'egfr' or 'cholesterol' fire on NORMAL "
                        "values, so including them measures whether a quantity was reported "
                        "rather than whether disease is present; 'all' reproduces that "
                        "conflated behaviour for comparison.")
    p.add_argument("--concept-encoding", default="binary",
                   choices=("binary", "count", "both"),
                   help="binary (default) asks whether the patient HAS the concept, which is "
                        "the clinically meaningful question; a raw count mostly tracks how many "
                        "notes the patient has (up to 589) and note volume is inert.")
    p.add_argument("--expand-terms", type=int, default=0,
                   help="Unsupervised synonyms per concept, mined from the TRAIN corpus by "
                        "co-occurrence lift. The outcome is never used. 0 disables.")
    p.add_argument("--require-text", action="store_true",
                   help="Restrict the cohort to patients who have text, so a null is not the "
                        "empty-text confound.")
    p.add_argument("--date-mode", default="strip", choices=("strip", "year", "keep"),
                   help="'strip' removes full dates (default, and what every earlier arm "
                        "used). 'year' replaces a full date with its year alone, which the "
                        "graded arm needs because KliMaYr-style onset is one of the four "
                        "carriers the headroom check identified and full stripping destroys "
                        "it. 'year' reintroduces calendar-era information at year "
                        "granularity, so run the paired 'strip' arm to measure that.")
    p.add_argument("--with-concepts", action="store_true",
                   help="With --mode graded: also append the tiered presence concepts, "
                        "giving one arm holding every text feature we can build.")
    p.add_argument("--validate-baseline", action="store_true",
                   help="With --mode graded: report agreement between each extracted "
                        "quantity and the curated variable measuring the same thing, on "
                        "train patients. Outcome-blind, so it can be read before any "
                        "survival number -- and it is the only direct evidence that the "
                        "extraction works at all.")
    p.add_argument("--med-lexicon", default=None,
                   help="Path for the derived ATC-class -> Dutch drug-name lexicon. Built "
                        "from the cohort's own med_*.csv (train patients only) if absent, "
                        "reused if present. Point every graded arm at one path.")
    p.add_argument("--strip-dates", action="store_true", default=True)
    p.add_argument("--keep-dates", dest="strip_dates", action="store_false",
                   help="Sensitivity arm: leave dates in, which lets calendar era leak. "
                        "Equivalent to --date-mode keep.")
    p.add_argument("--strip-names", action="store_true", default=True)
    p.add_argument("--keep-names", dest="strip_names", action="store_false",
                   help="Sensitivity arm: leave clinician/department tokens in.")
    p.add_argument("--baseline-cols", default=None,
                   help="With --mode baseline: which baseline columns the matched control "
                        "emits, e.g. 'leeftijd,geslacht'. Prefix with ~ to exclude instead. "
                        "'group:chart' / 'group:chart_strict' / 'group:protocol' select by "
                        "curated-variable provenance instead (--list-baseline-groups).")
    p.add_argument("--add-baseline-cols", default=None,
                   help="Append baseline columns, e.g. 'leeftijd,geslacht' for the fair "
                        "text+demographics arm. Accepts 'group:...' too.")
    p.add_argument("--list-baseline-cols", action="store_true")
    p.add_argument("--list-baseline-groups", action="store_true",
                   help="Print the curated variables split by provenance (chart-derivable / "
                        "report-derivable imaging / study-protocol-only) and exit. This is "
                        "the partition the T3 headroom check rests on, so it is meant to be "
                        "read by a clinician before the arms are believed.")
    p.add_argument("--clip-quantile", type=float, default=0.001)
    p.add_argument("--min-coverage-frac", type=float, default=0.10)
    p.add_argument("--screen-features", action="store_true")
    p.add_argument("--screen-top", type=int, default=30)
    add_results_arg(p)
    if not handle_listing_flags(sys.argv[1:]):
        a = p.parse_args()
        # Reconcile the two date flags so they cannot silently disagree: --keep-dates is
        # the older spelling of --date-mode keep.
        if not a.strip_dates and a.date_mode == "strip":
            a.date_mode = "keep"
        if a.date_mode == "keep":
            a.strip_dates = False
        with results_block(a.results_file, f"text arm: {a.mode}",
                           {"mode": a.mode, "landmark": a.landmark_days,
                            "lookback": a.lookback_days, "horizon": a.horizon_days,
                            "section": a.section, "analyzer": a.analyzer,
                            "require_text": a.require_text,
                            "strip_nameish": a.strip_nameish,
                            "concept_encoding": a.concept_encoding,
                            "add_baseline": a.add_baseline_cols,
                            "baseline_cols": a.baseline_cols, "out": a.out_dir}):
            main(a)
