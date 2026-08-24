# Runbook — free-text arm, baseline-free 15-year survival

How to run every phase of the free-text experiment, in order, with what to look at and
what each result would mean. Companion to the plan and to
`docs/baseline-free-event-survival-report.md` (which records the closed structured arm).

**Keep this file updated as phases land.**

## Status

| phase | what | script | state |
|---|---|---|---|
| 0 | text metadata / corpus measurement | `eda_text_events.py` | **DONE — see §1.1** |
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

### 1.1 Phase 0 results (run 2026-08-24, landmark 180, horizon 5475)

**Corpus**: 46.4M real tokens across 121,778 documents, ~4,815 tokens per text-bearing
patient. `consult_tekst` 20.8M, `inhoud` 18.8M, `verslagtekst` 6.4M, `rad_report` 0.33M.

Five findings, three of which change the plan:

1. **Coverage is 71.8%, not 95% — the empty-text confound is still present.**
   9,644/13,434 patients have narrative text; **3,790 (28%) have none** (train 2,389,
   test 770, validation 631). The earlier 95% figure came from the structured EDA's §7,
   which counted all ten `free_text`-classified columns including the six short *label*
   fields (`diag_omschrijving` alone covers 12,287 patients). Those are out of scope here.
   → **`--require-text` is a PRIMARY arm, not a sensitivity check.** On the full cohort,
   28% of rows are an all-zero text vector and will dilute every content estimate.

2. **Boilerplate is absent.** 0% of a median document's 8-grams are shared with ≥30% of
   documents, in all four sources, and 96.2–99.6% of documents are distinct. These are
   genuinely varied narratives.
   → the `--max-df` and single-section defences are **demoted to sensitivity arms**; the
   headline TF-IDF run does not need them. (The metric is not blind: the same code reports
   71–100% on a templated fixture.)

3. **T0 volume control is inert.** Every volume feature sits at 0.4931–0.4973 against a
   0.0149 floor; nothing clears it. → **any content gain is attributable to content**, not
   to note-taking intensity. Gate 0 is satisfied.

4. **De-identification risk is high, and names are not yet removed by default.** NL dates
   appear in 42.5% (consult) to 94.1% (letters) of documents and clinician tokens in 24.7%
   to 99.5%; letters carry a median of **50 name-like tokens each**. Dates and titles are
   stripped by default, but the names themselves are not — once lowercased they survive
   `min_df` and can encode the treating physician or site.
   → run the headline arm and a `--strip-nameish` arm and compare.

5. **`rad_report` is truncated** (1024 chars in 59.3% of documents) and small (461
   patients, 53.7% distinct). → exclude from the primary `--text-cols`; keep as sensitivity.

Section availability (share of documents): `conclusie` 29.3% consult / 64.2% letters /
17.6% radiology; `voorgeschiedenis` 79.9% letters; `anamnese` 69.1% letters. Prior
conditions live in `voorgeschiedenis,anamnese`, so prefer those over `conclusie` for the
concept arm; `conclusie` alone would discard most radiology documents.

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
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --require-text --svd-components 256 --screen-features --out-dir T1_tfidf_word
```

`--require-text` is included because 28% of patients have no narrative text; without it
those rows are all-zero and dilute the estimate. Also run it **without** the flag, to see
the full-cohort number the model would face in deployment.

Variants worth running (each is a separate falsifiable arm, not tuning):

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --analyzer char --ngram-max 5 --svd-components 256 --out-dir T1_tfidf_char
```

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --section conclusie --svd-components 128 --out-dir T1_tfidf_conclusie
```

`--analyzer char` uses char_wb 3–N grams, robust to Dutch compounding and typos.
`--section` takes a comma-separated list; prefer `voorgeschiedenis,anamnese` over
`conclusie` (Phase 0: prior conditions are stated there, and `conclusie` is missing from
82% of radiology reports).
`--max-df 0.8` (default) drops terms appearing in more than 80% of train documents. Phase 0
measured **zero** boilerplate, so this is not doing much work here — it is retained as a
guard, not a needed defence.

De-identification sensitivity arm (letters carry ~50 name-like tokens each):

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --require-text --strip-nameish --svd-components 256 --out-dir T1_tfidf_nonames
```

If this differs materially from the headline arm, part of the signal was physician or site
identity rather than clinical content.

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

Exclude the truncated source (Phase 0: `rad_report` is capped at 1024 chars in 59.3% of
its documents and covers only 461 patients):

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode tfidf --require-text --text-cols "consult:consult_tekst,uitgaandebrief:inhoud,radiologie_verslag:verslagtekst" --rebuild-cache --svd-components 256 --out-dir T1_tfidf_3src
```

`--keep-dates` and `--keep-names` quantify the calendar-era and site/physician confounds
instead of assuming them away. Changing `--text-cols` needs `--rebuild-cache`.

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
