# The free-text arm: what was tested, and what came out

**Question.** Can 15-year risk of the SMART composite endpoint (vascular death, stroke,
myocardial infarction) be predicted from clinical free text in the hospital EHR, without the
hand-curated SMART baseline variables?

**Answer.** No. Across **14 text arms**, every text-only configuration lands between
**0.482 and 0.521** test C-index. Adding text to age and sex moves the model from
**0.6727 → 0.6750** (+0.0023, inside a ±0.062 noise band), while the curated baseline on the
same patients reaches **0.7394**.

This is not an extraction failure: the clinical concepts *are* found in the notes at
clinically plausible rates, and they still do not predict. §6 is the decisive evidence.

Companion documents: `baseline-free-event-survival-report.md` (both arms, full journal),
`free-text-arm-runbook.md` (how to run it), `results-log.md` (all 58 runs, provenance for
every number here).

---

## 1. Bottom line

All values are **test** C-index, landmark 180 days, horizon 5475 days (15 years,
landmark-relative), fixed patient-level splits.

### On the text subcohort (9,644 patients; train 6,210 / 828 events; test 1,924 / 257 events)

Every arm below sits on the **identical** patients, so these are directly comparable.

| arm | features | test C | verdict |
|---|---|---|---|
| **full curated baseline** (183 vars) | 183 | **0.7394** | signal |
| TF-IDF + demographics | 258 | 0.6750 | signal |
| concepts + demographics | 41 | 0.6749 | signal |
| **demographics only** (age, sex) | 2 | **0.6727** | signal |
| concepts, history sections | 38 | 0.5209 | chance |
| volume only (T0 gate) | 9 | 0.5197 | chance |
| concepts, binary | 39 | 0.5120 | chance |
| concepts, binary + counts | 78 | 0.5101 | chance |
| TF-IDF, conclusion section | 128 | 0.5089 | chance |
| TF-IDF, char 3–5 grams | 256 | 0.4963 | chance |
| TF-IDF, word 1–2 grams | 256 | 0.4914 | chance |
| TF-IDF, 3 sources (drop truncated) | 256 | 0.4907 | chance |
| TF-IDF, history sections | 128 | 0.4897 | chance |
| TF-IDF, physician names stripped | 256 | 0.4821 | chance |

### On the full cohort (13,434 patients; train 8,599 / 1,136 events; test 2,694 / 381 events)

| arm | features | test C |
|---|---|---|
| full curated baseline | 183 | **0.7576** |
| demographics only | 2 | 0.6883 |
| volume only | 9 | 0.5202 |
| TF-IDF, word | 256 | 0.4957 |

The ladder on the subcohort reads **0.7394 curated → 0.6750 text+demographics → 0.6727
demographics → ~0.49 text alone**. Curation contributes **+0.064** over text plus
demographics; text contributes **+0.0023** over demographics.

---

## 2. What the text actually is

Measured before modelling (`eda_text_events.py`), landmark 180.

Only the four genuine **narrative** columns are in scope. The event CSVs contain ten columns
an automatic classifier calls free text, but six are 3–5 word **label** fields
(`diag_omschrijving`, `Diagnose`, `Behandeling`, `locatie`, `OMSCHR`, `verr_omschrijving`)
that were already tested as tokenised occurrence codes in the structured arm and found null.
Re-testing those as "text" would relabel a settled result.

| source.column | documents | patients | tokens | median chars/doc |
|---|---|---|---|---|
| `consult.consult_tekst` | 75,445 | 4,957 | 20.8M | 418 |
| `uitgaandebrief.inhoud` | 12,244 | 4,164 | 18.8M | 3,571 |
| `radiologie_verslag.verslagtekst` | 33,087 | 7,478 | 6.4M | 691 |
| `mri_verslag.rad_report` | 1,002 | 461 | 0.33M | 1,024 |

**121,778 documents, 46.4M tokens** (real tokenizer), ~4,815 tokens per text-bearing patient.

Five properties that shaped the design:

- **Coverage is 71.8%.** 9,644 of 13,434 patients have narrative text; **3,790 have none**
  (train 27.8%, test 28.6%, validation 29.5%). On the full cohort those patients contribute
  an all-zero text vector, which is why the headline arms use the text subcohort with a
  cohort-matched control.
- **Boilerplate is absent.** 0% of a median document's 8-grams are shared with ≥30% of
  documents, in all four sources; 96.2–99.6% of documents are distinct. Templating was the
  main anticipated threat to TF-IDF and it is not present. (The measure is not blind: the
  same code reports 71–100% on a deliberately templated fixture.)
- **`rad_report` is truncated** at exactly 1024 chars in 59.3% of its documents, and covers
  461 patients. Excluded from the primary source set; kept as a sensitivity arm.
- **De-identification risk is high.** Dutch-format dates appear in 42.5% (consult) to 94.1%
  (letters) of documents, clinician tokens in 11.6% to 99.5%, and letters carry a median of
  **50 name-like tokens each**. Dates and titles are stripped by default; a separate arm
  strips capitalised mid-sentence words too.
- **Section headers are uneven.** `conclusie` appears in 29.3% of consults, 64.2% of letters
  and 17.6% of radiology reports; `voorgeschiedenis` in 79.9% of letters, `anamnese` in
  69.1%. Restricting to sections therefore costs coverage: conclusion-only retains 5,730
  patients (59.4% of the subcohort), history-sections 5,085 (52.7%).

---

## 3. What was tested

Text is read **directly from the raw CSVs**, never from the merged JSONL: the project
pipeline merges rows sharing `(patient, datediff)` keyed on the column name, so several
reports written on one day collapse to whichever landed last — `consult` alone has 53,236
such day-groups. All arms share one document cache.

### T0 — volume only (the gate)

Document counts, character counts, per-source counts, recency, history span. **No content at
all.** Run first, because a text "signal" that merely reflects how many notes a patient has
would be indistinguishable from prognosis. Both cohorts.

### T1 — TF-IDF (7 variants)

TF-IDF → TruncatedSVD, vectoriser and SVD fitted on **train only**, `max_df` 0.8:

1. word 1–2 grams, 256 components, subcohort — the headline
2. word 1–2 grams, full cohort
3. **char_wb 3–5 grams** — robust to Dutch compounding and typos
4. **conclusion section only**, 128 components
5. **history sections** (`voorgeschiedenis,anamnese`) — where prior conditions are stated
6. **physician names stripped** — de-identification sensitivity
7. **three sources**, dropping the truncated `rad_report`
8. word 1–2 grams **+ age and sex**

### T2 — clinical concepts (4 variants)

Thirteen SMART-adjacent Dutch concepts (smoking, diabetes, prior MI, stroke/TIA, heart
failure, renal function, peripheral disease, hypertension, hyperlipidaemia, atrial
fibrillation, angina, stenosis, revascularisation), matched on **word boundaries** and scoped
for **negation** and **uncertainty**: cues (`geen`, `niet`, `zonder`, `uitgesloten`, …;
`mogelijk`, `verdenking`, `verdacht`, …) within six tokens before a mention, never crossing a
document or sentence boundary. Each concept yields asserted / negated / uncertain features.

1. binary (does the patient *have* it) — the primary encoding
2. binary + counts
3. history sections only
4. binary **+ age and sex**

Word-boundary matching is not cosmetic: plain substring matching makes `roken` (smoking)
match `afgesproken` (agreed), which — inheriting polarity from a nearby negation cue — read
as a strong predictor at C=0.910 on a fixture before the fix.

### Controls

Four, all through byte-identical cohort/target/split/standardisation code: demographics and
full curated baseline, each on the full cohort and on the text subcohort. A `--require-text`
arm sits on a different cohort, so the full-cohort benchmarks do not transfer to it; the
matched control is what makes those arms interpretable.

### Not tested: frozen LLM embeddings

Gated by design. Escalation required T1 or T2 to clear its floor or beat the matched
control; neither did. A null embedding arm on top of a null bag-of-words arm and a null
concept arm adds no information, and the builder can emit the per-patient document parquet
whenever that changes.

---

## 4. Univariate evidence, before any model

Each feature is screened on the **raw, un-imputed** matrix, scored only on the patients who
have it, against a floor scaled to that feature's own event count. The null is
permutation-calibrated: SE(C) = 0.292/√events on the subcohort, giving a 2-SE floor of
**0.0203** (828 events); 0.0192 on the full cohort (1,136 events).

| arm | features clearing the raw floor | expected from noise | survive FDR / Bonferroni |
|---|---|---|---|
| T0 volume | **0 of 9** | ~0 | 0 |
| concepts, binary | **0 of 39** | ~2 | 0 |
| concepts, binary+counts | **0 of 78** | ~3 | 0 |
| concepts, history | **0 of 38** | ~2 | 0 |
| TF-IDF word | 20 of 256 | ~12 | **0** |
| TF-IDF char | 30 of 256 | ~12 | **0** |
| TF-IDF 3 sources | 27 of 256 | ~12 | **0** |
| curated baseline | **106 of 183** | ~6 | many |

TF-IDF's raw counts sit near what noise produces once the 256 components are recognised as
only ~242 independent tests, and nothing survives correction. The concept arms clear
**nothing at all**, not even at an uncorrected threshold.

---

## 5. The volume gate holds

Every T0 feature sits between 0.4881 and 0.5039 univariately (max z = 1.44), 0 of 9 clear
the floor, and the fitted model reaches 0.5197 / 0.5202. Note volume carries no signal, so
any content result would have been attributable to content. This mattered because the
structured arm produced exactly this artefact once: a `gfr_count` feature read C=0.851 purely
because only sick patients had numeric eGFR results.

---

## 6. The decisive comparison: extraction works, and still does not predict

The obvious objection to a concept null is that the Dutch terminology missed. It did not.
Prevalence among the 9,644 patients with text:

| concept | asserted | negated | uncertain | % asserted |
|---|---|---|---|---|
| revascularisatie | 4,477 | 1,297 | 216 | 46.4% |
| hypertensie | 3,860 | 1,186 | 249 | 40.0% |
| roken | 3,796 | 1,155 | 88 | 39.4% |
| hyperlipidemie | 3,516 | 874 | 119 | 36.5% |
| stenose | 3,009 | 1,584 | 275 | 31.2% |
| diabetes | 2,724 | 947 | 74 | 28.2% |
| myocardinfarct | 2,530 | 604 | 259 | 26.2% |
| angina | 2,132 | 1,610 | 155 | 22.1% |
| nierfunctie | 2,024 | 367 | 61 | 21.0% |
| cva_tia | 1,660 | 453 | 304 | 17.2% |
| perifeer_vaatlijden | 1,381 | 455 | 97 | 14.3% |
| hartfalen | 1,004 | 1,678 | 97 | 10.4% |
| atriumfibrilleren | 747 | 187 | 76 | 7.7% |

These are plausible rates for a vascular cohort, and negation behaves sensibly — heart
failure is negated in 1,678 patients versus asserted in 1,004, which is what phrases like
"geen decompensatie" in a routine letter should produce.

**The same clinical concept predicts when curated and does not when extracted from text**,
on the same patients, the same outcome and the same screen (train C, subcohort):

| concept | curated variable | text-extracted |
|---|---|---|
| diabetes | `vz_DM` 0.5441, `vz_t2d` 0.5446 | **0.4859** |
| smoking | `roken` 0.5674, `packyrs` 0.6182 | **≈0.50** (below the printed cut) |
| cardiac history | `vz_hart` 0.5646, `vgt_hart` 0.5706 | **0.4917** |
| renal function | `labkrea` 0.6233, `MDRD` 0.3839, `klar_coc` 0.3625 | **0.4893** |
| carotid stenosis | `stenACIl` 0.6471, `stenACIr` 0.6468 | **0.4924** |
| hypertension | `vz_hypt` 0.5473, `bdsys` 0.5812 | **0.4965** |
| lipids | `labtrig` 0.5339, `labhdl` 0.4614 | **0.4873** |

**106 of 183 curated features clear the floor; 0 of 39 text concepts do.**

The difference is not *which facts* are recorded but *how*. A curated variable is a graded,
protocol-measured quantity — pack-years, systolic pressure, creatinine, percent stenosis.
Its text counterpart is a binary mention, undated within the window, written for clinical
communication rather than measurement. Mentioning diabetes does not encode how long or how
severe; mentioning stenosis does not distinguish 40% from 90%. That graded information is
what the curated variables carry and the prose does not.

---

## 7. Why the null is trustworthy

- **Positive control, twice.** The curated baseline reaches 0.7394 on the subcohort and
  0.7576 on the full cohort through the same code, so the pipeline can detect signal when it
  is present.
- **Cross-path agreement.** The full curated baseline returns **0.7576** whether built by the
  structured builder's `--positive-control` or the text builder's
  `--mode baseline --baseline-cols all` — two independently written code paths, identical to
  four decimals. Cohort, target, splits and standardisation are demonstrably shared.
- **Matched denominators.** Every subcohort arm is compared against a control built on the
  *same* patients, because the full-cohort benchmarks do not apply to a `--require-text` arm.
- **Leakage invariant.** Zero feature documents may be dated at or after a patient's own
  outcome; asserted and confirmed 0.
- **Permutation-calibrated null.** The analytic floor is ~1.6× too wide under this censoring,
  which would have discarded real signal; the floor used is measured on the actual target.
- **Multiple testing on effective tests.** 256 SVD components are ~242 independent tests;
  correction uses that, not the nominal count.
- **Pre-imputation screening.** Features are scored on patients who actually have them, so a
  low-coverage feature is not flattened toward 0.5 before being judged.
- **Train-only fitting.** Vectoriser, SVD, coverage floors, clipping and standardisation
  never see validation or test.
- **Arguments echoed.** Every run records its resolved flags, because a flag that never
  reached the process is otherwise indistinguishable from a genuine null. This was not
  hypothetical: one arm was silently invalid until the echo was added.

---

## 8. Limitations

- **Events, not patients, are binding.** 828 training events on the subcohort cap model
  complexity; a null here does not generalise to cohorts with far more events.
- **Non-linear interactions are untested** and untestable at this event count.
- **Frozen LLM embeddings are untested** (gated, §3). If a reviewer requires it, the
  document-level parquet is one command away.
- **15 years is weakly observed** — 67–69% of patients are censored before the horizon —
  though a 10-year secondary horizon was checked throughout the structured arm.
- **Single centre, single extract.** A different extract that included the study visit's own
  documentation could change the result; that is the natural next test.
- **Concept list is a seed list.** Unsupervised expansion was tried and produced a mix of
  plausible additions (`novomix`, `solostar` for diabetes; `chadsvasc`, `aflutter` for atrial
  fibrillation) and clear noise (`uitspreken`, `trials`, `smart1`), so it stays off by
  default. Prevalence (§6) suggests the seed list is adequate rather than the bottleneck.

---

## 9. Reproduction

```bash
export SMART=/path/to/smart.csv EVENTS=/path/to/all_event_csvs SPLITS=/path/to/splits.json
./bash_scripts/run_all_phases.sh
```

Phases `p0 t0 t1 t2 ctrl struct screens`. Every run appends to one results file; the
committed snapshot of the 58 runs behind this document is `results-log.md`. Scripts:
`eda_text_events.py` (corpus), `prepare_text_features.py` (all arms),
`feature_matrix.py` (shared standardise/screen/write), `screen_parquet_features.py`
(evaluation), `eda_events_survival.py` (cohort, landmark, null calibration).

---

## 10. Conclusion

Clinical free text in this EHR extract carries **no detectable 15-year prognostic signal
beyond age and sex**. Fourteen arms spanning bag-of-words, character n-grams, section
restriction, de-identification and targeted concept extraction all land between 0.482 and
0.521; adding text to demographics gains +0.0023 against a ±0.062 noise band.

The finding is specific rather than a shrug. The concepts the curated variables encode are
present in the notes at plausible rates and correctly polarity-scoped, and they still do not
predict, while their curated counterparts do on the same patients. What manual curation
contributes is **graded protocol measurement**, not the presence of the fact — and that is
what the prose does not record.
