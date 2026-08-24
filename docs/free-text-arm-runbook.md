# Runbook — free-text arm, baseline-free 15-year survival

How to run every phase of the free-text experiment, in order, with what to look at and
what each result would mean. Companion to the plan and to
`docs/baseline-free-event-survival-report.md` (which records the closed structured arm).

**Keep this file updated as phases land.**

## Status

| phase | what | script | state |
|---|---|---|---|
| 0 | text metadata / corpus measurement | `eda_text_events.py` | **ready** |
| 1 | document cache + T0 volume | `prepare_text_features.py --mode volume` | **ready** |
| 1 | T1 TF-IDF (+ variants) | `--mode tfidf` | **ready** |
| 1 | T2 clinical concepts | `--mode concepts` | **ready** |
| 2 | T3 frozen LLM embeddings | `--mode documents` → `extract_qwen_embeddings_longitudinal.py` | ready, **gated** (see §6) |
| — | evaluation of any arm | `screen_parquet_features.py` | ready |

---

## 0. Setup (once per session)

```bash
git pull origin dev
```

Set these once; every command below uses them.

```bash
export SMART=/path/to/smart.csv
export EVENTS=/path/to/all_event_csvs
export SPLITS=/path/to/splits.json
export CACHE=$PWD/text_cache/documents.parquet
export COMMON="--smart-csv $SMART --event-csv-folder $EVENTS --split-json $SPLITS --legacy --landmark-days 180 --horizon-days 5475"
```

Landmark 180 and horizon 5475 are fixed so every arm is comparable with the structured
results. Landmark 180 is what raises text coverage from 89% to 95%; it excludes patients
whose outcome falls at or before day 180 and measures survival from there.

**Benchmarks to beat** (all test C, same cohort/splits/horizon):

| reference | test C |
|---|---|
| full curated SMART baseline | 0.7553 |
| curated baseline without age/sex | 0.7547 |
| structured events + demographics | 0.6890 |
| **demographics (age+sex) only** | **0.6883** ← the bar a text arm must clear |
| structured events only | ~0.50 |

---

## 1. Phase 0 — measure the corpus

```bash
python scripts/smartehr/eda_text_events.py $COMMON --tokenizer Qwen/Qwen3-Embedding-0.6B --out-dir eda_text_lm180
```

Drop `--tokenizer` to skip the model download (you then get chars/words instead of exact
tokens). Paste `eda_text_lm180/eda_text_report.md` back.

Read, in this order:

1. **§2 coverage per split** — how many patients have no narrative text. This is the
   confound that produced the earlier TF-IDF null.
2. **§3 boilerplate fraction** — share of a median document's 8-grams shared with ≥30% of
   documents. If >50%, make the `--section conclusie` and higher-`--max-df` variants
   primary rather than optional.
3. **§3 truncation** — a modal length holding ≥20% of documents. `rad_report` is known to
   cap at exactly 1024 chars; check whether the others hide a cap too.
4. **§3 de-id risk** — ISO/NL date and clinician-token rates. High rates justify the
   default stripping, and make the `--keep-dates` / `--keep-names` sensitivity arms worth
   running to quantify the site/era confound.
5. **§4 T0 volume control** — the C of document/token count with no content. **If anything
   here clears the floor, every later content result must be compared against it, not
   against 0.5.**

---

## 2. Phase 1 — build the document cache once

The first `prepare_text_features.py` call with `--cache $CACHE` streams ~550M chars and
writes the cache; every later arm reuses it in seconds. Point every arm at the same
`--cache` path. Use `--rebuild-cache` only if the landmark, lookback or `--text-cols`
change.

Scope note: only the four **narrative** columns are in scope
(`consult_tekst`, `inhoud`, `verslagtekst`, `rad_report`). The six short label fields
(`Diagnose`, `Behandeling`, `diag_omschrijving`, `locatie`, `OMSCHR`,
`verr_omschrijving`) were already tested as tokenised occurrence codes in the structured
arm and found null; `verr_omschrijving` is additionally 100% post-baseline.

---

## 3. Phase 1 arms — run in this order

### T0 — volume only (run FIRST, it is the gate)

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode volume --screen-features --out-dir T0_volume
```

### T1 — TF-IDF

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --svd-components 256 --screen-features --out-dir T1_tfidf_word
```

Variants worth running (each is a separate falsifiable arm, not tuning):

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --analyzer char --ngram-max 5 --svd-components 256 --out-dir T1_tfidf_char
```

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --section conclusie --svd-components 128 --out-dir T1_tfidf_conclusie
```

`--analyzer char` uses char_wb 3–N grams, robust to Dutch compounding and typos.
`--section conclusie` cuts boilerplate by keeping only the conclusion.
`--max-df 0.8` (default) drops terms appearing in more than 80% of train documents — the
main lever against templates. Lower it if Phase 0 reports heavy boilerplate.

### T2 — clinical concepts (most directly on-question)

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode concepts --screen-features --out-dir T2_concepts
```

Optional unsupervised synonym expansion (train corpus only; the outcome is never used, so
it cannot bias the estimate the way supervised term selection would). Every added term is
printed:

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode concepts --expand-terms 5 --screen-features --out-dir T2_concepts_expanded
```

### The arm that answers the question — any representation + demographics

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode concepts --add-baseline-cols "leeftijd,geslacht" --screen-features --out-dir T2_concepts_demo
```

Confirm the exact column names first:

```bash
python scripts/smartehr/prepare_text_features.py --smart-csv $SMART --event-csv-folder $EVENTS --split-json $SPLITS --mode volume --out-dir /tmp/x --list-baseline-cols
```

The build log **must** show `appending N baseline columns` and a
`self-check on the appended baseline columns` block with each C clearly off 0.5. If a
column reads `** ABSENT **` or `** suspiciously flat **`, the arm is invalid — that is the
failure mode that cost a full cycle in the structured arm.

### Subcohort and sensitivity arms

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --require-text --svd-components 256 --out-dir T1_tfidf_requiretext
```

`--require-text` restricts to patients who have text, so a null cannot be the empty-text
confound. `--keep-dates` and `--keep-names` quantify the calendar-era and
site/physician confounds instead of assuming them away.

---

## 4. Evaluate every arm the same way

```bash
python scripts/smartehr/screen_parquet_features.py --parquet-dir T1_tfidf_word --cox --l1-ratio 1.0
```

Read: label sanity → feature spread → univariate screen (`C_mono` and `C_udev`, the latter
catching U-shaped risk) → penalised Cox tuned on validation with an explicit **test** C and
verdict. Use lasso (`--l1-ratio 1.0`) when there are many features: ridge spreads weight
across hundreds of nulls.

Report only the **FDR/Bonferroni survivors**, never the raw 2-SE count — with hundreds of
features ~5% clear an uncorrected threshold by chance.

For a significance test on the *difference* between two arms:

```bash
python scripts/predict_survival.py --help
```

then

```bash
python scripts/smartehr/bootstrap_ci_compare.py --pred-a <demographics_preds.parquet> --pred-b <text_plus_demographics_preds.parquet> --n-boot 2000
```

---

## 5. How to read the numbers

- **text-only ≈ 0.50** → no signal in narrative content.
- **text + demographics ≈ 0.6883** → text adds nothing over age and sex. Same verdict the
  structured arm reached; the negative result then covers both representations.
- **text + demographics meaningfully > 0.6883** → text carries signal the structured data
  did not. Confirm it exceeds T0 (volume) before claiming content, then bootstrap the
  difference.
- **text + demographics ≈ 0.7553** → the curated baseline is reproducible without chart
  review. That is the success case.

One framing point worth stating explicitly in any write-up: if text recovers the curated
variables, **that is the goal, not leakage.** The SMART baseline visit may well be
documented in these notes; automating its extraction is the entire point.

---

## 6. Gates — when to escalate, when to stop

- **Gate 0.** T0 runs first. Any later gain must exceed it, or it is note-taking intensity,
  not physiology. This is the `gfr_count` C=0.851 lesson from the structured arm: a
  missingness/volume artifact that looked like strong signal.
- **Gate 1.** Escalate to T3 (frozen LLM) **only if** T1 or T2 clears its floor on the
  pre-imputation screen, or beats 0.6883 with demographics. If both are null, a null LLM
  arm adds no information.
- **Gate 2.** If two consecutive methodology fixes fail to move the verdict, stop. That
  criterion is what closed the structured arm.

---

## 7. Phase 2 — T3 frozen LLM embeddings (gated)

```bash
pip install sentence-transformers
```

Not currently installed, and `extract_qwen_embeddings_longitudinal.py` requires it.

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode documents --out-dir T3_docs
```

```bash
python scripts/smartehr/extract_qwen_embeddings_longitudinal.py --parquet-dir T3_docs --out-dir T3_emb --model-name Qwen/Qwen3-Embedding-0.6B --dtype float16 --device cuda --max-tokens-per-block 512
```

Start at **0.6B, not 4B**: ~34M tokens is minutes-to-an-hour at 0.6B and roughly ten times
that at 4B. Embed per document and pool per patient rather than concatenating — `inhoud`
reaches 22,255 chars (~5.5k tokens) and per-patient concatenation would exceed any context
window. Keep the output dimension modest: 1,136 training events supports roughly 60–120
effective dimensions, so use `--truncate-dim` or an SVD step rather than feeding 1024+ dims
straight in.

---

## 8. Troubleshooting

| symptom | cause | fix |
|---|---|---|
| feature count unchanged after `--add-baseline-cols` | the flag never reached the process | check the `ARGS:` line the builder logs, and `metadata.json` → `baseline_cols_included` |
| `** suspiciously flat **` on a baseline column | that column is mostly missing, so imputation flattened it | pick a better-populated column via `--list-baseline-cols` |
| every univariate C ≈ 0.5 in `screen_parquet_features` but the raw screen found signal | low-coverage features median-imputed into near-constant columns | raise `--min-coverage-frac`; trust the raw screen |
| Cox "low variance" / zero-division warnings | near-constant columns | raise `--min-coverage-frac` |
| TF-IDF vocabulary implausibly small | `--max-df` removed the boilerplate, which was most of the text | expected; check Phase 0's boilerplate fraction |
| a concept fires implausibly often | a term is matching inside a longer Dutch compound | terms are word-boundary anchored, but check `CONCEPTS` for a short term that is a real substring of a common word |
| `0 of N features clear the floor, ~M expected` | correlated features are not N independent tests | the screen reports effective tests; compare against that, not N |

---

## 9. Provenance

Scripts: `eda_text_events.py`, `prepare_text_features.py`, `feature_matrix.py` (shared
standardise/screen/write), `screen_parquet_features.py`, `eda_events_survival.py` (cohort,
landmark, null calibration), `extract_qwen_embeddings_longitudinal.py` (T3).

Every arm shares cohort construction, landmarking, target definition and the
standardisation stage, so differences between arms are attributable to the representation
rather than to plumbing. The positive control
(`prepare_pivoted_event_features.py --positive-control`) should be re-run once per session
to confirm that.
