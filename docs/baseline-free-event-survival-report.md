# Can 15-year cardiovascular risk be predicted from raw EHR events, without manually extracted variables?

**Experimentation journal — SMART EHR cohort, UMC Utrecht**
Status: **numeric/structured arm complete (negative). Free-text arm not yet tested.**
Last updated: 2026-07-28

---

## 1. Question, thesis, and what would count as success

The SMART risk score rests on ~20 variables extracted by hand from the clinical record at a
dedicated study visit. Hand extraction does not scale, so:

> **Research question.** Can 15-year risk of the SMART composite endpoint (vascular death,
> stroke, myocardial infarction) be predicted from the raw hospital EHR event stream alone,
> without any manually curated baseline variables?

**Thesis under test.** Routinely collected EHR data contains enough prognostic information
to replace manual curation.

**Success criterion, fixed before the final experiments.** A model built from EHR events
(optionally plus demographics, which need no chart review) reaches a test C-index close to
the curated baseline. The curated baseline is the benchmark, not chance — beating 0.5 is
not the bar.

**Outcome.** The thesis is **not supported** for structured/numeric event data. Events add
+0.0007 C over age and sex alone.

---

## 2. Data

| | |
|---|---|
| Cohort | 13,806 raw rows → **13,805 unique patients** (1 dropped for a missing outcome column) |
| Event sources | **16 CSVs**, ~28.2M rows: labs, vitals, ECG, echo, medications, diagnoses, DBC, hospitalisations, procedures, plus free-text reports and letters |
| Endpoint | SMART composite: vascular death, or stroke/MI of the target subtypes, via the pipeline's own `compute_legacy_targets` |
| Follow-up | median **8.47 years**; 1,252 patients flagged lost to follow-up |
| Events at 15y | **1,937 (14.0%)** before landmarking |
| Splits | fixed patient-level train/validation/test from the project's `splits.json` |

Targets and cohort construction are imported from `smartehr_pipeline.py` rather than
reimplemented, so every arm shares byte-identical labels.

---

## 3. Methodology

### 3.1 Landmarking

**Observation that forced this.** 24.42M of 28.24M event rows (**86.5%**) are dated at or
after the baseline visit. The prior assumption that events were exclusively pre-baseline was
false; one source (`verr`) is 100% post-baseline (min `datediff` +1018) and contributes
nothing to a baseline-anchored model.

Post-baseline events are usable, but only under a landmark. `--landmark-days L` performs
three coupled operations:

1. features may use events with `datediff < L`;
2. patients whose outcome occurred at or before `L` are **excluded** — otherwise their
   features describe their own outcome (its admission, imaging, medication changes);
3. survival is measured **from** `L`, so all horizons are landmark-relative.

Doing (1) without (2) and (3) is the classic leak, and additionally makes "few post-baseline
events" a proxy for "died early".

**Landmark chosen: 180 days.** Cost is 371 patients / 130 events. Benefit is substantial:

| | LM 0 | LM 180 |
|---|---|---|
| patients with no usable event | 1,018 (7.4%) | **221 (1.6%)** |
| patients with any free text | 89.0% | **95.0%** |
| free-text corpus | 23.1M tokens | **33.7M tokens** |

At LM180: **13,434 patients, 1,827 events (13.6%)**; train 8,599 (1,136 events),
validation 2,141 (310), test 2,694 (381).

### 3.2 Feature construction: pivoting before merging

The project pipeline merges rows sharing `(patient, datediff)` via `merged[col] = val`,
keyed on the **column name**. The largest sources are long/key-value, so a single day holds
many *different* variables under identical column names and all but the last are discarded.

Measured on the real data (pre-baseline rows only):

| source | day-groups with >1 row | max rows/day |
|---|---|---|
| echo | 96.4% | 156 |
| lab_ezis | 93.1% | 267 |
| meting | 85.4% | 11,592 |
| med | 55.2% | 40 |

`prepare_pivoted_event_features.py` therefore reads the raw CSVs and pivots before any
merge, with three column roles per source: **numeric pivot** `(name, value)`,
**occurrence pivot** (per-code counts), **wide numeric** (remaining numeric columns).
Aggregators: `last`, `mean`, `min`, `max`, `slope` (per year), `count`, `present`.

Demonstrated necessity, on a fixture where one signal-carrying test is buried among 6–10
same-day noise tests: pivoted, `Creat_mean` C=0.850 and end-to-end test CI 0.750; through
the merge, the signal column does not survive at all (best C=0.528, CI 0.551).

### 3.3 Statistical discipline

- **Permutation-calibrated null.** The analytic `sqrt(0.25/n_events)` is ~1.6× too wide
  under this censoring: only ~1 in 400 pure-noise features cleared its nominal 2-SE band
  instead of the expected ~5%. Measured on the real target, **SE(C) = 0.323/√events**.
- **Per-feature floors.** A feature is judged against a floor scaled to the events in *its
  own* subcohort, not the cohort total.
- **Multiple testing.** Benjamini-Hochberg FDR and Bonferroni, applied over the number of
  **effective independent tests** (principal components reaching 95% of the correlation
  matrix's variance) rather than the nominal column count — `last/mean/slope/count` of one
  code are near-duplicates.
- **Pre-imputation screening.** Features are screened on the raw matrix, scored only on
  patients who actually have each value. Median-filling a low-coverage feature drags its C
  toward 0.5 (at 43% coverage a true 0.806 reads 0.652).
- **Selection on train only.** Coverage floors and code caps never see validation or test.

### 3.4 Controls

- **Positive control.** The curated SMART baseline emitted through byte-identical
  cohort/landmark/split/target/standardisation code. If it scores ~0.5, the plumbing is
  broken and any null is uninterpretable.
- **Arm self-check.** Appended baseline columns are protected from filtering and their
  univariate C is printed, flagged if absent or suspiciously flat.
- **Leakage invariant.** Zero feature events may be dated at or after a patient's own
  outcome. Asserted and confirmed **= 0** at landmarks 0, 90 and 180.
- **Argument echo.** The arm-defining flags are logged, because a flag that never reached
  the process is otherwise indistinguishable in the output from a genuine null.

---

## 4. Hypotheses and outcomes

| # | Hypothesis | Test | Outcome |
|---|---|---|---|
| H1 | Crude event aggregates (counts, presence, recency, history span) predict risk | Univariate C at 3 landmarks | **Rejected.** All 37 features 0.492–0.506; 0 cleared the floor at LM90/LM180 |
| H2 | Per-code values predict risk once the same-day merge is bypassed | Pivoted features, pre-imputation screen | **Rejected.** Of 532 event features, **0** clear their floors after correction |
| H3 | A model can combine weak signals the univariate screen misses | Penalised Cox (ridge and lasso), validation-tuned; MLP | **Rejected.** Events-only: MLP test 0.48; Cox ridge train 0.605 → test 0.496; lasso train 0.555 → val 0.49 |
| H4 | The curated baseline's skill is mostly demographics, making the comparison unfair | Baseline decomposition | **Rejected.** Curated variables *without* age/sex reach **0.7547** vs full 0.7553; demographics alone 0.6883 |
| H5 | Events add information on top of demographics | events + age/sex vs age/sex | **Rejected.** **0.6890 vs 0.6883 (+0.0007)** |
| H6 | The null is an artefact of unit heterogeneity within a test code | Per-code unit tally | **Rejected.** 0 of 330 / 682 / 33 codes report a second unit in >1% of rows |
| H7 | Free text carries signal the structured data does not | — | **Not yet tested** |

---

## 5. Results

All values are **test** C-index at a 15-year horizon (5475 days, landmark-relative),
landmark 180, identical cohort and splits.

| arm | features | test C |
|---|---|---|
| Full curated SMART baseline | ~20 | **0.7553** |
| Curated baseline **without** age/sex | ~18 | **0.7547** |
| Events + demographics | 534 | **0.6890** |
| Demographics (age + sex) only | 2 | **0.6883** |
| Events only | 532 | **≈0.50** |

Feature-level result, which is the cleanest statement of the finding:

> Of **532** structured event features, **zero** clear the calibrated noise floor.
> Of the **2** appended demographic features, **both** do.

Arm validity confirmed by self-check: `leeftijd` C=0.6742, `geslacht` C=0.4448.

### 5.1 Why scattered C values of 0.4–0.6 are not signal

Pre-imputation, low-coverage features show C values that look far from 0.5. Under a true
null the deviation must shrink as 1/√events:

| events in subcohort | 2-SE half-width | noise range for C |
|---|---|---|
| 72 | 0.076 | 0.424 – 0.576 |
| 150 | 0.053 | 0.447 – 0.553 |
| 660 | 0.025 | 0.475 – 0.525 |
| 1,136 | 0.019 | 0.481 – 0.519 |

The observed large deviations occur **only** on low-coverage features and vanish on
high-coverage ones — a funnel, which is the signature of noise. Genuine signal behaves
oppositely: it persists at high coverage. The one feature that survived Bonferroni in an
early run (`zuurstofspven`, venous blood gas) covered **4% of the cohort**, is measured
almost exclusively in acutely ill patients, and cannot drive a cohort-level model.

### 5.2 Statistical power

With 1,827 events and SE(C) = 0.323/√events, any single feature with **C ≥ 0.52** would be
detected at 80% power. A validation-tuned penalised Cox additionally excludes linear
combinations. What remains genuinely undetectable is complex non-linear interaction — but
1,136 training events cannot support learning that regardless, which is a structural limit
of the cohort rather than a modelling shortfall.

---

## 6. Threats to validity, and how each was addressed

Nine defects were found and fixed during the work. Several **changed the result**, and two
produced *false positives* that would otherwise have been reported as findings.

| # | Threat | Resolution | Did it change the verdict? |
|---|---|---|---|
| 1 | Post-baseline events treated as pre-baseline; `recency` and `last` computed from the future | Pre-baseline mask on every feature aggregate; leakage invariant asserted | Yes — invalidated the first screen |
| 2 | Long-format panels destroyed by the same-day merge | Pivot from raw CSVs | Yes — merge loses the signal entirely on a fixture |
| 3 | Noise floor 1.6× too wide, discarding real signal | Permutation-calibrated `k=0.323` | Borderline features moved to z≈1.6; verdict unchanged |
| 4 | U-shaped risk invisible to a monotone C-index | Also screen `|value − median|` | No further signal found |
| 5 | Five sources contributed **zero** features (no numeric columns, one occurrence column nameable) | `--auto-occurrence` over all categorical columns | No — but was a real coverage gap |
| 6 | Thresholded lab results (`>90` = normal eGFR) stranded in the text column, removing healthy patients **and manufacturing a fake signal** (`gfr_count` C=0.851 from missingness alone) | Text-fallback parser; artefact collapsed to 0.506 while `gfr_last` became significant and correctly inverse | Yes — removed a false positive |
| 7 | Diagnosis descriptions fragmented across 9,024 spellings, each below the coverage floor | Per-word tokenisation | No further signal found |
| 8 | Coverage floor as an absolute count admitted 1.5%-coverage codes → near-constant columns, Cox convergence warnings | Fractional floor (`--min-coverage-frac`) | Yes — cleaned the matrix |
| 9 | Unit heterogeneity within a test code | Per-code unit tally | No — 0 codes affected |

Two further corrections were to the *analysis*, not the data: standardisation divided by
near-zero standard deviations (exploding degenerate columns and swamping the penalised
model), and multiple-testing expectations assumed independence among correlated
aggregators, making "0 features cleared" look anomalous when it was not.

---

## 7. Interpretation

The negative result is **not** "EHR data contains no prognostic information". The clinical
analogues of the curated variables — creatinine, eGFR, cholesterol, glucose, haemoglobin,
roughly 12–13 concepts — **are present** in the pivoted features, pass the coverage floor,
are single-unit, and still score at chance. Meanwhile the curated versions of those same
quantities reach 0.7547 without demographics.

The defensible claim is therefore about **measurement context**:

> The same clinical quantities, measured opportunistically during routine care, do not
> carry the prognostic signal that protocol-measured baseline values do.

Three non-exclusive mechanisms:

1. **Indication bias.** A routine lab is drawn *because* something prompted it, so its
   value is entangled with the clinical reason for ordering it. A protocol measurement is
   unconditional.
2. **Timing heterogeneity.** The most recent pre-landmark value may be days or years old,
   drawn during an acute admission or a routine check. The study visit is standardised in
   time and setting.
3. **Acute versus chronic.** A creatinine drawn during an admission reflects transient
   injury, not the stable kidney function SMART's eGFR represents.

A supporting observation: pre-baseline lab coverage is only ~43% of the cohort, whereas the
curated variables are near-complete. The EHR extract records prior hospital *encounters*,
not the study's own baseline assessment.

---

## 8. Limitations

- **Event count, not cohort size, is binding.** 1,136 training events cap model complexity;
  a null here does not generalise to cohorts with far more events.
- **Non-linear interactions are untested** and untestable at this event count.
- **15 years is weakly observed.** 67–69% of patients are censored before the horizon and
  only 2,556 remain at risk at 15 years; 10 years is better supported and was checked as a
  secondary horizon throughout.
- **Single centre, single extract.** A different extract that included the baseline visit's
  measurements could plausibly change the result — that is the natural next test of the
  mechanism proposed in §7.
- **Free text is untested**, and is the one arm with material remaining upside.

---

## 9. Reproduction

```bash
# 1. EDA and landmark sensitivity (also the leakage invariant)
python scripts/smartehr/eda_events_survival.py --smart-csv <smart.csv> \
    --event-csv-folder <ALL_event_csvs> --split-json <splits.json> --legacy \
    --landmark-days 180 --out-dir eda_lm180

# 2. Baseline column names
python scripts/smartehr/prepare_pivoted_event_features.py --smart-csv <smart.csv> \
    --event-csv-folder <ALL_event_csvs> --split-json <splits.json> \
    --out-dir /tmp/x --list-baseline-cols

# 3. Arms (positive control, demographics, curation-without-demographics, events+demographics)
python scripts/smartehr/prepare_pivoted_event_features.py ... --positive-control --out-dir arm_full
python scripts/smartehr/prepare_pivoted_event_features.py ... --positive-control \
    --baseline-cols "leeftijd,geslacht"  --out-dir arm_demo
python scripts/smartehr/prepare_pivoted_event_features.py ... --positive-control \
    --baseline-cols "~leeftijd,geslacht" --out-dir arm_nodemo
python scripts/smartehr/prepare_pivoted_event_features.py ... --auto-occurrence \
    --add-baseline-cols "leeftijd,geslacht" --screen-features --out-dir arm_events_demo

# 4. Screen each arm
python scripts/smartehr/screen_parquet_features.py --parquet-dir <ARM> --cox --l1-ratio 1.0
```

Common flags for step 3: `--legacy --landmark-days 180 --horizon-days 5475`.

**Code.** `eda_events_survival.py` (EDA, landmarking, leakage invariant, null calibration),
`prepare_pivoted_event_features.py` (pivoting, arms, raw screen),
`screen_parquet_features.py` (label sanity, univariate screen, penalised Cox).

---

## 10. Conclusion

Structured EHR event data in this cohort carries **no detectable 15-year prognostic signal**
beyond age and sex, while ~20 expert-curated baseline variables reach C=0.755 and ~18 of
them reach 0.7547 without any demographics. The result survives landmarking at three
origins, pivoting that recovers the full same-day panels, recovery of thresholded lab
values, tokenised diagnosis codes, permutation-calibrated significance, multiple-testing
correction over effective tests, a validated positive control, and an explicit demographics
decomposition confirming the comparison is fair.

Manual curation is therefore not redundant here, and the likely reason is that the
information it captures is a *protocol measurement*, not merely a *measurement*. The
untested free-text arm remains the open question.
