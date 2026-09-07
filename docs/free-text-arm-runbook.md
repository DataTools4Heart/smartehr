# Runbook — free-text arm, baseline-free 15-year survival

How to run every phase of the free-text experiment, in order, with what to look at and
what each result would mean. Companion to the plan and to
`docs/baseline-free-event-survival-report.md` (which records the closed structured arm).

**This file is the single source of truth for the free-text arm, and is updated whenever
anything material changes** — a new phase, a corrected figure, a new flag, a revised
benchmark. See the changelog at the end. If a methodological point is worth saying, it
belongs here, not only in conversation.

## Status

| phase | what | script | state |
|---|---|---|---|
| 0 | text metadata / corpus measurement | `eda_text_events.py` | **DONE — see §1.1** |
| 1 | document cache + T0 volume | `prepare_text_features.py --mode volume` | **ready** |
| 1 | T1 TF-IDF (+ variants) | `--mode tfidf` | **ready** |
| 1 | T2 clinical concepts | `--mode concepts` | **DONE (re-run 2026-09-03 with tiered terms) — see §5.1** |
| 1 | `incr` — text on top of the FULL curated baseline | `--add-baseline-cols all` | **DONE — see §5.1** |
| 1 | `sens` — structured arm without `ok.OMSCHR` | `prepare_pivoted_event_features.py` | **DONE — see §5.1** |
| 2 | **T3-0 headroom check (no GPU)** | `--baseline-cols group:chart` / `group:protocol` | **ready — run this before any T3 work, see §7.0** |
| 2 | T3 frozen LLM embeddings | `--mode documents` → `extract_qwen_embeddings_longitudinal.py` | **planned — see `docs/t3-frozen-llm-plan.md`** |
| — | **matched control** for any subcohort arm | `prepare_text_features.py --mode baseline` | **ready** |
| — | evaluation of any arm | `screen_parquet_features.py` | ready |
| — | **one-file results log** (all scripts append) | `results_log.py` → `$RESULTS` | **ready** |
| — | **run every phase in order** | `bash_scripts/run_all_phases.sh` | **ready** |

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
export RESULTS=$PWD/results/ALL_RESULTS.md
export COMMON="--smart-csv $SMART --event-csv-folder $EVENTS --split-json $SPLITS --legacy --landmark-days 180 --horizon-days 5475 --results-file $RESULTS"
```

### Run everything with one script

`bash_scripts/run_all_phases.sh` contains every command below, in order. Export the three
data paths (above) and run:

```bash
./bash_scripts/run_all_phases.sh
```

```bash
./bash_scripts/run_all_phases.sh t1 t2 screens
```

- Phases: `p0 t0 t1 t2 incr sens t3headroom ctrl struct screens t3`. With no arguments it
  runs everything except `t3`.
- **Arms that already exist are skipped**, so re-running after adding one arm is cheap.
  `FORCE=1` redoes them.
- `DRY_RUN=1` prints the commands without running any.
- **A failing arm does not abort the batch.** The failure is recorded in `$RESULTS` — by the
  script itself, so even a bad flag or a killed process leaves a trace — and listed in the
  summary. An unattended overnight batch is never wasted.
- Overridable: `LANDMARK HORIZON CACHE RESULTS OUT DEMOG SVD TOKENIZER PY`.
- `t3headroom` is CPU-only and takes seconds (it reads no text); run it before any T3 work,
  see §7.0.
- **A preflight compiles every script and checks `$PY` is Python 3 before any arm runs**, so
  a syntax error or a Python-2 `python` aborts locally instead of costing a VM round-trip.
  Use `compile()`/`py_compile`, not `ast.parse`, if you add checks: a stray `return` at
  module level is a compile error, and a parse-only check waves it through.
- `t3` needs `RUN_T3=1` plus a GPU and `pip install sentence-transformers`; it stays gated
  behind §6 Gate 1.

The individual commands are kept below so a single arm can be run or varied by hand.

### Getting results off the VM — read this first

Results cannot be copied out of the VM by hand; files must be requested from the admin and
that is slow. So **every script appends to one shared file**, `$RESULTS`. Run as many arms
as you like, then make **a single download request for that one file**.

- The file regenerates an **`## Index`** at the top on every run, so its first ~20 lines are
  the complete summary of every run so far: timestamp, arm, and the headline numbers
  (`n_features`, cohort/event counts, univariate hits, Cox **test C** and verdict).
- Full per-run output is kept below in collapsed `<details>` blocks, capped at 400 lines
  each. Four runs is ~190 lines total, so the whole file stays pasteable for a long time.
- **Failures are recorded too** — a crashed arm writes `status: FAILED` with its traceback,
  so a broken run is not lost effort.
- No raw clinical text is ever written to it.
- Keep blocks small with `--screen-top` / `--top` if a screen lists hundreds of features.

Because `--results-file` is inside `$COMMON`, every command below already writes there. For
scripts that do not take `$COMMON` (the screen), pass `--results-file $RESULTS` explicitly —
the examples do.

When you download it, paste the whole file — or drop it into the repo, which is easier and
avoids the paste limit entirely. `results/` is gitignored, so a snapshot worth keeping goes
to `docs/results-log.md` and is committed alongside the report it supports.

If the file has grown large, the `## Index` section alone is enough for me to decide the
next step.

Landmark 180 and horizon 5475 are fixed so every arm is comparable with the structured
results. Landmark 180 is what raises text coverage from 89% to 95%; it excludes patients
whose outcome falls at or before day 180 and measures survival from there.

**Benchmarks — and which one applies.** There are two denominators, because 28% of the
cohort has no narrative text (§1.1).

*Full cohort (13,434 patients), measured:*

| reference | test C |
|---|---|
| full curated SMART baseline | 0.7576 |
| curated baseline without age/sex | 0.7547 |
| structured events + demographics | 0.6890 |
| structured events + demographics, **without `ok.OMSCHR`** | 0.6884 |
| **demographics (age+sex) only** | **0.6883** ← the bar for a FULL-cohort text arm |
| structured events only | ~0.50 |

*`--require-text` subcohort (9,644 patients), measured:* full curated baseline **0.7394**,
demographics **0.6727**, best text arm 0.6750, text alone 0.482–0.520. Text **on top of the
full curated baseline**: concepts 0.7397, volume 0.7394, TF-IDF 0.7388 — so the bar for any
future text method that would change practice is **0.7394**, not 0.6727. The full-cohort
numbers above DO NOT APPLY to this subcohort. A text arm run
with `--require-text` sits on a healthier-or-sicker, differently-sized cohort, so it must be
compared against a control built on **exactly those patients**:

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode baseline --baseline-cols "leeftijd,geslacht" --require-text --out-dir CTRL_demo_requiretext
```

`--mode baseline` emits only the numeric SMART baseline on whatever cohort the text flags
define, so the control and the text arm contain the identical patients and labels (verified:
same n and same duration/event vectors in every split). Also build the full-baseline control
the same way for the upper reference:

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode baseline --baseline-cols all --require-text --out-dir CTRL_full_requiretext
```

Comparing a `--require-text` arm against 0.6883 is invalid and was a live trap until
`--mode baseline` existed.

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
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode concepts --require-text --screen-features --out-dir T2_concepts
```

**Read the prevalence table before the C-indices.** The builder prints, per concept, how
many patients have it asserted / negated / uncertain, and emits a `concepts NEVER matched`
line. A concept that fires for 40 patients and one that fires for 8,000 both give C ≈ 0.5,
for opposite reasons — a flat C is uninterpretable without knowing which. If a core SMART
variable such as diabetes never matched, the terminology is wrong, not the hypothesis.

Encoding defaults to `--concept-encoding binary`: whether the patient *has* the concept.
A raw count mostly tracks how many notes they have (up to 589 documents per patient) and
note volume is inert, so counts inject noise. Use `--concept-encoding both` only to check
whether frequency adds anything.

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
python scripts/smartehr/screen_parquet_features.py --parquet-dir T1_tfidf_word --cox --l1-ratio 1.0 --results-file $RESULTS
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
- **text + demographics ≈ the matched demographics control** → text adds nothing over age
  and sex. Same verdict the structured arm reached; the negative result then covers both
  representations. Use 0.6883 only for full-cohort arms, and `CTRL_demo_requiretext` for
  `--require-text` arms.
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
- **Gate 0.5 — the headroom check (§7.0).** Cheaper than T3 and can make it unnecessary:
  if the chart-derivable curated variables cannot beat demographics, no text method can, and
  the negative becomes structural rather than another null.
- **Gate 1.** Escalate to T3 (frozen LLM) **only if** T1 or T2 clears its floor on the
  pre-imputation screen, or beats 0.6883 with demographics. If both are null, a null LLM
  arm adds no information.
  **Status: gate 1 was NOT met** — every T1/T2 variant is null, including after the
  2026-09-03 concept correction, and text adds +0.0003 over the full curated baseline. T3
  proceeds as a deliberate override (see `docs/t3-frozen-llm-plan.md`), which is why the
  plan front-loads the **no-GPU headroom check**: bounding what any text method could
  achieve is worth more than a fourth null.
- **Gate 2.** If two consecutive methodology fixes fail to move the verdict, stop. That
  criterion is what closed the structured arm.

---

## 7.0 T3-0 — the headroom check (no GPU, run this FIRST)

Bounds what *any* text method could achieve, by asking what the curated variables reach when
restricted to facts our narrative corpus could plausibly contain. It can close the arm with a
mechanism instead of a fourth null, and it costs seconds — `--mode baseline` reads no text.

```bash
./bash_scripts/run_all_phases.sh t3headroom screens
```

**Review the split before believing the numbers.** It is the whole experiment, so it is
written out by exact name in `scripts/smartehr/feature_matrix.py` rather than guessed from
prefixes, and an unassigned curated column is a hard error (otherwise it would vanish from
both halves and they would stop summing to the full baseline):

```bash
python scripts/smartehr/prepare_text_features.py --smart-csv $SMART --event-csv-folder $EVENTS --split-json $SPLITS --list-baseline-groups
```

| group | n | what it is |
|---|---|---|
| `chart` | 114 | history, diagnoses, **medication**, smoking/alcohol, disease onset + `imaging` |
| `chart_strict` | 97 | the same without imaging findings |
| `imaging` | 17 | carotid stenosis grade, aortic diameter, kidney size — radiology reports are IN our corpus |
| `protocol` | 69 | research ultrasound (IMT/ABI), anthropometry, study labs, SF-36, METs |
| `demographics` | 2 | age/sex — in **neither** half by design |

Two traps this encodes, both of which the first draft of the plan fell into:

- the 44 medication flags (`mht*`/`mli*`/`mas*`/`mgl*`) and the four `KliMa*` onset
  variables are **chart-derivable**, and no prefix rule puts them there. Getting them wrong
  shrinks the chart half and biases the check toward the answer we already expect;
- `hyptns_n` (derived from the measured pressure) is protocol while `hyptns_b`
  ("behandeling; vraag 6.03", reported treatment) is chart — same for the hyperglycaemia and
  hyperlipidaemia pairs. Substring selection cannot express that, which is why groups match
  exact names.

Compare `HR_chart_demo_rt` against **0.6727** (the matched demographics control), never
0.6883 (a full-cohort number). `≈ 0.673` means no text method can help and the ceiling for
text is demographics; `0.69–0.72` means partial headroom; `≈ 0.74` means T1/T2 simply failed
to extract what is there. Full interpretation table in `docs/t3-frozen-llm-plan.md` §3.3.

Note `~group:chart` is **not** the protocol half — it also contains demographics and admin
columns. Use `group:protocol` explicitly; the builder prints which columns sit in neither
half so this is visible in the log.

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
| `trn%` looks low for a count/indicator feature | it is the share of the TRAIN split with a value; counts are never missing so they read 100%. (Before 2026-08-26 this column was mislabelled `cov%` and divided by the full cohort, understating every value by the train fraction) | none needed; re-read old screens with that scaling in mind |
| every concept C sits at ~0.5 | may be genuine, or the concept never matched | read the prevalence table and the `concepts NEVER matched` line first |
| `ABORT: $PY (...) is not Python 3.8+` | the preflight found `python` pointing at Python 2, under which every script dies on f-strings and reads as "the code is broken" | `PY=python3 ./bash_scripts/run_all_phases.sh ...`, or activate the venv |
| `ABORT: a script under scripts/smartehr does not compile` | the preflight naming a file and line. It runs before any arm, because a syntax error otherwise costs a full VM round-trip and — like an argparse failure — exits before `results_block` opens, leaving no trace in `$RESULTS` | fix the reported line; `git pull` if the break came from upstream |
| a `--require-text` arm looks better/worse than 0.6883 | that benchmark is a full-cohort number and does not apply to the subcohort | build `--mode baseline --require-text` and compare against that |
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

---

## 10. Changelog

- **2026-09-03 — the three clinical-review items are answered; nothing changes the
  verdict.** 91 runs in the log. (1) **`ok.OMSCHR` never mattered**: the structured arm
  without it reaches 0.6884 versus 0.6890 with it, so its post-baseline skew (p50 = +98
  days) has no bearing on the result. (2) **The conflated concept terms were a real defect
  in meaning and irrelevant to the outcome**: prevalences move as predicted (renal
  21.0% → 5.2%, PAD 14.3% → 8.4% with aneurysm split out at 10.4%, hyperlipidaemia
  36.5% → 26.2%) while test C goes 0.5114 → **0.5098**, with the all-tier variant at 0.5092
  and 0 of 39 features clearing the floor in every variant. (3) **Text adds nothing to the
  full curated baseline**: 0.7394 → concepts 0.7397, volume 0.7394, TF-IDF 0.7388. That last
  number is the one that matters for T3 — the bar is **0.7394**, not 0.6727. Report §10.2 and
  §10.3 are new.

- **2026-08-27 — clinical review: tiered concept terms, incremental-value arms, OMSCHR
  sensitivity.** The concept term lists conflated disease assertions with measurements and
  medications: `nierfunctie` contained `egfr`/`creatinineklaring`, which fire on a NORMAL
  eGFR, so the feature measured "renal function was reported" rather than renal disease;
  `hyperlipidemie` contained `cholesterol`; and `perifeer_vaatlijden` contained `aneurysma`,
  a different disease. Terms are now tiered (disease / symptom / measurement / medication /
  procedure), default `disease,symptom`, `aneurysma` is its own concept, and
  `--concept-terms all` reproduces the old behaviour for comparison. **T2 needs re-running.**
  New `incr` phase adds text on top of the FULL 183-variable curated baseline — the
  practically relevant increment, and never previously run. New `sens` phase rebuilds the
  structured arm without `ok.OMSCHR`, whose median row is +98 days and which therefore
  contributes mostly post-baseline treatment.

- **2026-08-27 — T3 planned (`docs/t3-frozen-llm-plan.md`).** T3 is motivated by the
  report's own §10.1 interpretation rather than by model size: the grading that TF-IDF and
  binary concepts discard *is* present in the prose, so representations preserving it are a
  falsifiable next test. Two design points matter most. A **headroom check runs first with
  no GPU** — splitting the curated variables into chart-derivable versus protocol-measured
  bounds what any text method could achieve, and can end the arm early with a stronger
  result than another null. And **model, prompt, pooling and dimensionality are selected
  outcome-blind**, by probing whether an embedding recovers curated variables we already
  have labels for, which both avoids selecting on 828 events and makes a third null
  informative rather than inconclusive.

- **2026-08-27 — upper references recovered; arm complete.** Re-screening after the
  convergence fix produced the four numbers that were previously missing: full curated
  baseline **0.7576** (full cohort) and **0.7394** (text subcohort). The cause was confirmed
  from the log — `dropped 21 effectively-constant columns before fitting` — after which
  lasso converged at every penalizer, so it was the singular design and not the penalty
  type. Unplanned bonus: `CTRL_full_full` (text builder `--mode baseline`) and
  `STRUCT_ctrl` (pivot builder `--positive-control`) both return **0.7576**, identical to
  four decimals from two independently written code paths — the strongest available check
  that the two builders really do share cohort, target, splits and standardisation.
  `results/` is gitignored (runtime outputs), so the log snapshot is committed at
  `docs/results-log.md` (58 runs) as provenance for every number in the report.

- **2026-08-26 — free-text arm closed (negative), and a Cox convergence fix.** 39 runs.
  Every text-only arm sits between 0.482 and 0.521; text+demographics reaches 0.6750 against
  a cohort-identical demographics control at 0.6727 (**+0.0023**, inside a ±0.062 band).
  0 of 39 concept features clear their floor and 0 of 256 TF-IDF components survive
  FDR/Bonferroni. Concept extraction is confirmed working (diabetes 28.2%, smoking 39.4%,
  prior MI 26.2%), so this is not a terminology failure — see the curated-versus-extracted
  table in the report's §10.1. Fix: lasso Cox failed to converge on all four 183-feature
  baseline arms, silently removing the most important reference number. The screen now drops
  effectively-constant columns before fitting (21 of 183 were constant and made the design
  singular), falls back from lasso to ridge, extends the penalizer grid to 100, and emits an
  explicit `COX FAILED` line so a missing headline number cannot be overlooked.

- **2026-08-26 — `run_all_phases.sh`.** One script holding all 20 arms plus the screens, in
  order: phase selection, skip-if-already-built, `DRY_RUN`, and a summary. Two bugs found
  while smoke-testing it on a fixture: it passed `--screen-top` to the screen (which only
  has `--top`), and — more importantly — an argparse error exits before the Python
  `results_block` is entered, so a bad flag left **no trace in the one file that leaves the
  VM**. The script now captures each step's output with `tee` and writes its own
  `SHELL FAILURE` block on a non-zero exit, so command-line errors and killed processes are
  recorded too.

- **2026-08-26 — first text results, and three fixes they exposed.** T0 volume is inert on
  real data (9 features, 0 clear the 0.0149 floor, max z=1.30), so Gate 0 holds and any
  content gain is attributable to content. T1 TF-IDF word on the text subcohort: 20 of 256
  components clear the raw 2-SE floor against ~12 expected from noise, but **0 survive
  FDR or Bonferroni**. T2 concepts: all 39 features between 0.4886 and 0.5045, nothing
  clearing. Fixes: (1) the screen's coverage column divided train-row counts by the FULL
  cohort, understating every `cov%` by the train fraction — now reported as `trn%` against
  the train split; (2) concept features were counts, which mostly track note volume, so
  `--concept-encoding` now defaults to **binary**; (3) the builder now prints per-concept
  prevalence and a `concepts NEVER matched` line, without which a flat concept C cannot be
  interpreted at all. The ARGS echo and results context now include `strip_nameish`,
  `require_text` and `concept_encoding`, which were previously unverifiable from the log.
  Note the unsupervised `--expand-terms` output is mixed: plausible additions
  (`novomix`/`solostar` for diabetes, `chadsvasc`/`aflutter` for atrial fibrillation)
  alongside clear noise (`uitspreken`, `trials`, `smart1`), so keep it off by default.

- **2026-08-26 — one-file results log.** Every script now appends its run to a single
  append-only markdown file (`--results-file`, folded into `$COMMON`), because results
  cannot be copied off the VM by hand and each download is a slow admin request. The file
  regenerates an index of all runs at the top, hoisting each run's headline numbers
  (`RESULT:` lines) out of the collapsed full output, and records failures with their
  traceback. One download now covers arbitrarily many experiments. The canonical arm
  summary is emitted from the shared `finish()` stage, so every builder reports identically.

- **2026-08-24 — matched controls, and two fixes they exposed.** Added
  `--mode baseline`, which emits only the SMART baseline on whatever cohort the text flags
  define, so a `--require-text` arm can be compared against demographics on identical
  patients. Before this no valid comparison existed for subcohort arms. In the process:
  `--require-text` is now applied before the mode dispatch and always means "has ≥1
  narrative document", which also fixes it being silently ignored by `--mode volume`.
  Benchmarks section now separates the full-cohort and subcohort denominators.
- **2026-08-24 — Phase 0 results recorded (§1.1).** Narrative coverage is **71.8%, not
  95%**: the earlier figure came from the structured EDA's §7, which counted the six short
  label fields that are out of scope here. `--require-text` promoted to a primary arm.
  Boilerplate measured at 0% in all four sources, so `--max-df`/section restriction demoted
  to sensitivity arms. T0 volume control inert (0.4931–0.4973 vs a 0.0149 floor), so Gate 0
  is satisfied and content gains are attributable to content. Added `--strip-nameish`
  (letters carry ~50 name-like tokens each, previously unstripped); `--section` now takes a
  comma-separated list; `rad_report` dropped from the primary sources (truncated at 1024
  chars in 59.3% of its documents, 461 patients).
- **2026-08-24 — initial runbook**, covering Phase 0, the document cache, arms T0/T1/T2,
  evaluation, gates, and Phase 2 (T3, gated).
