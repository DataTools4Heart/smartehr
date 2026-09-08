# Can 15-year cardiovascular risk be predicted from raw EHR events, without manually extracted variables?

> ## ⚠ RESULTS UNDER REVIEW — 2026-09-08
>
> **The identifier join between the EHR event CSVs and the SMART registry does not work**,
> so every result derived from event data is withdrawn pending a fix. Quantities measured in
> *both* sources show zero per-patient agreement:
>
> | event source | registry | n | rho | shuffled floor | med(event) | med(registry) |
> |---|---|---|---|---|---|---|
> | `meting.Gewicht` | `gewicht` | 10,923 | **+0.011** | +0.021 | 81.0 kg | 80.0 kg |
> | `meting.Lengte` | `lengte` | 8,202 | −0.017 | +0.006 | 174 cm | — |
> | `meting.BMI` | `bm_indx` | 2,776 | −0.009 | −0.029 | 26.3 | 26.0 |
> | `lab_ezis.Creat-BL` | `labkrea` | 6,010 | +0.002 | −0.007 | 79 | 84 |
> | `lab_ezis.Chol-BL` | `labchol` | 5,161 | −0.012 | +0.020 | 4.7 | 5.0 |
>
> The medians show both sides hold real data for the same population; only the per-patient
> correspondence is absent. A person's routine weight cannot be uncorrelated with their
> study-visit weight, so this is not a null result — it is real data on the wrong rows.
> Note that `m3life_no` is **not** among the 287 documented registry variables (the
> registry's own identifier is `studienr`), and `data_dict.csv` describes the EHR's
> `M3LIFE_no` only as a "PseudoID to be linked with the SMART dataset" — so the joining
> column was added to `smart.csv` outside the documented schema.
>
> **Withdrawn:** every arm built from event CSVs — the structured/pivoted event arms
> (H1, H2, H3, H5, H6, H7) and every free-text arm (H8, H9, H10, and the graded arm),
> including "events add +0.0007" and "text adds +0.0023".
>
> **Not affected**, because they are built only from `smart.csv` and never touch event data:
> the curated baseline **0.7576**, curation-without-demographics **0.7547**, demographics
> **0.6883**, and the whole **§10.2b headroom check** (chart-derivable 0.7310, protocol
> 0.7196, strict chart 0.7024, demographics 0.6727). One caveat on the subcohort numbers:
> the `--require-text` subcohort was *selected* by which patients had documents under the
> broken join, so those 9,644 patients are not "the patients with narrative text" — but
> every arm measured on them uses the same patients and the same labels, so the comparisons
> among them remain internally valid.
>
> ### Diagnosis (complete, 2026-09-08)
>
> **The two extracts do not share a key. They share a numbering range.** The `m3life_no`
> values in `smart.csv` and in the EHR CSVs are independent pseudonymisation assignments
> over the same space, so the patients that appear to match do so by arithmetic:
>
> | | |
> |---|---|
> | registry distinct ids | 13,806 in [1, 16096] |
> | event distinct ids | 12,771 in [2, 15877] |
> | **expected overlap if independent** (R·E/N) | **10,954** |
> | **observed overlap** | **10,949** |
> | ratio | **0.9995** |
>
> Both files are internally coherent, so neither is corrupt on its own — BMI against
> weight/height² within one row gives rho **+0.941** for the events (median |diff| 0.31) and
> **+0.798** for the registry. The registry's lower value is fully explained by its `lengte`
> column being rounded to integer metres (median 2.00): for an 80 kg person that makes the
> implied BMI 80/2² = 20 against a stated 26.1, and the observed median offset is 6.25.
> Nothing here indicates scrambled values.
>
> So no code change can recover the linkage, and no column of `smart.csv` can either
> (`studienr`, the registry's own documented identifier, is absent from the file). **A
> crosswalk between the two pseudonymisation runs is required from the data provider.**
>
> **Preprocessing ruled out (2026-09-08).** Both sources were preprocessed locally — a
> non-UTF-8 original converted to UTF-8, the `m3life_no` column name normalised across
> files, and its dtype normalised (string in the registry, numeric elsewhere) — so that step
> was the obvious suspect. It is not the cause: **the original files do not join either**
> (weight rho **+0.011** on 10,923 patients, the same value, matched as strings and as
> ints). The normalisation was in fact faithful where it matters — the integer-normalised id
> sets are *identical*, and id→weight is preserved at rho **+1.000**.
>
> The original registry is a cp1252, semicolon-delimited, decimal-comma export whose
> `M3LIFE_no` is zero-padded to 5 characters (8,573 of 13,806 carry a leading zero), which
> is why the string-matched id sets differ while the integer-matched sets agree exactly.
>
> Two incidental data-quality findings, neither the cause:
> - the original has **2 rows whose id column holds free text** (`'Ao vene RDP'`), so that
>   export has at least two field-shifted rows — an unescaped delimiter or quote. The
>   normalisation dropped them (13,808 → 13,806 rows), correctly;
> - the registry's `lengte` is rounded to integer metres (median 2.00), making it unusable
>   as a height.
>
> Also ruled out: no second identifier exists on the event side (`hos_nr`, `ECG_TestID` and
> `ECHO_StudyID` are within-modality keys), and rank-matching — the hypothesis that both
> extracts numbered patients sequentially in one shared source order, so the ids differ in
> value but agree in rank — is tested by `diagnose_normalization.py` step 3.
>
> Reproduce with `./bash_scripts/run_all_phases.sh normdiag joincheck`.

**Experimentation journal — SMART EHR cohort, UMC Utrecht**
Status: **UNDER REVIEW (see the banner above): the event-to-registry join is broken,
so all event-derived results are withdrawn. Previously: structured/numeric negative,
free-text negative for every
representation tried, but the headroom check (§10.2b) shows the information is present —
so the null is about extraction, and one further arm (T3) is justified.**
Last updated: 2026-09-07

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

**Outcome.** The thesis is **not supported**, for either representation. Structured events add
**+0.0007** C over age and sex alone; clinical free text adds **+0.002** on the matched
subcohort. Sixteen text arms all sit between 0.482 and 0.520.

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
| patients with any free text (incl. short label fields) | 89.0% | 95.0% |
| patients with any *narrative* text (the 4 report columns) | — | **71.8%** |
| free-text corpus | 23.1M tokens | 33.7M tokens (est.) / **46.4M measured** |

At LM180: **13,434 patients, 1,827 events (13.6%)**; train 8,599 (1,136 events),
validation 2,141 (310), test 2,694 (381).

**Feature history is unbounded backwards by default** — the only filter is
`datediff < landmark`, so aggregates span each patient's entire record (back to
`datediff = -19,734`, ~54 years). Per-patient span at LM180: p50 **334 days**, p95 8,785,
p100 19,914. Because that makes `mean`/`slope`/`count` summarise incomparable windows
across patients, a bounded variant was tested explicitly (H7, §4).

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
- **Cross-path agreement.** The full curated baseline reaches test C = **0.7576** whether
  built by the pivot builder's `--positive-control` or the text builder's
  `--mode baseline --baseline-cols all` — two independently written code paths, identical to
  four decimals. That is the strongest available check that cohort, target, splits and
  standardisation are shared rather than merely intended to be.

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
| H7 | The null is an artefact of unbounded history: aggregating over spans of 334 days to 24 years makes one feature mean different things per patient | 365-day lookback (retains 99.8% of patients) | **Rejected.** events+demographics stayed at **~0.689**, unchanged |
| H8 | Free text carries signal the structured data does not | 16 text arms (TF-IDF word/char/sections/de-identified, concepts binary/count/sections), matched controls, penalised Cox | **Rejected.** Every text-only arm 0.482–0.520; text+demographics 0.6750 vs demographics-only 0.6727 on the identical subcohort (**+0.0023**, inside a ±0.062 band) |
| H9 | A concept null means the Dutch terminology failed, not the hypothesis | Per-concept prevalence | **Rejected.** Extraction works at clinically plausible rates (diabetes 23.9%, smoking 39.4%, prior MI 26.2%, hypertension 39.8%); negation behaves sensibly (heart failure negated 1,245 > asserted 835). The concepts are found and still do not predict |
| H10 | The concept null was an artefact of conflated term lists (measurement and medication terms mixed into disease concepts) | Terms tiered to disease+symptom, `aneurysma` split out, both variants re-run | **Rejected.** Corrected concepts **0.5098** vs conflated 0.5114; all-tier variant 0.5092. 0 of 39 (and 0 of 42) clear the floor either way |
| H11 | Text adds information on top of the *full* curated baseline, not just demographics | 183 curated vars + concepts / TF-IDF / volume, matched subcohort | **Rejected.** 0.7394 → concepts **0.7397**, TF-IDF **0.7388**, volume **0.7394** |
| H13 | The free-text null means the notes lack the information (rather than that our representations fail to extract it) | Curated variables split by provenance: chart-derivable vs protocol-measured | **Rejected.** Chart-derivable curated facts alone reach **0.7310** — 87% of the demographics→full-baseline gap, with no age or sex — while every text arm realised 3%. The information is present; extraction is what failed |
| H12 | The structured result depends on `ok.OMSCHR`, whose median row is +98 days post-baseline | Structured arm rebuilt without it | **Rejected**, and the concern is moot: **0.6884** without vs 0.6890 with (2 of 534 features) |

---

## 5. Results

All values are **test** C-index at a 15-year horizon (5475 days, landmark-relative),
landmark 180, identical cohort and splits.

| arm | features | test C |
|---|---|---|
| Full curated SMART baseline | ~20 | **0.7553** |
| Curated baseline **without** age/sex | ~18 | **0.7547** |
| Events + demographics | 534 | **0.6890** |
| Events + demographics, 365-day lookback | — | **~0.6890** |
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
2. ~~**Timing heterogeneity.**~~ **Tested and ruled out.** Restricting every aggregate to
   the 365 days before the landmark — which retains 99.8% of patients, since median history
   is only 334 days — left performance unchanged at ~0.689. Heterogeneous observation
   windows are therefore not what suppresses the signal.
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
- **Unbounded aggregation is no longer a limitation**: bounding the window to 365 days
  changed nothing (§4 H7), so the remaining mechanisms are indication bias and the
  acute-versus-chronic distinction, not window width.
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

## 10. The free-text arm

Landmark 180, horizon 5475, same cohort and splits. 121,778 narrative documents,
46.4M tokens, four report columns. Because 28% of the cohort has no narrative text, the
headline arms run on the **`--require-text` subcohort** (9,644 patients; train 6,210 /
828 events; test 1,924 / 257 events) against a **cohort-identical** control.

| arm | test C |
|---|---|
| full curated baseline (183 vars), matched control | **0.7394** |
| demographics (age+sex), matched control | **0.6727** |
| TF-IDF + demographics | 0.6750 |
| concepts + demographics | 0.6749 |
| concepts, history sections | 0.5198 |
| volume only (T0 gate) | 0.5197 |
| concepts, all term tiers | 0.5092 |
| concepts (binary, disease+symptom) | 0.5098 |
| concepts (present+negated) | 0.5095 |
| TF-IDF, conclusion section | 0.5089 |
| TF-IDF char 3–5 grams | 0.4963 |
| TF-IDF word | 0.4914 |
| TF-IDF, history sections | 0.4897 |
| TF-IDF, 3 sources (no truncated one) | 0.4907 |
| TF-IDF, physician names stripped | 0.4821 |

Full cohort, for reference: full curated baseline **0.7576**, demographics 0.6883,
TF-IDF word 0.4957, volume 0.5202.

So on the identical subcohort the ladder is **0.7394 curated → 0.6750 text+demographics →
0.6727 demographics → ~0.49 text alone**: curation adds **+0.064** over text plus
demographics, while text adds **+0.0023** over demographics.

(The 0.7576 here and the 0.7553 quoted in §5 are the same arm fitted two ways — ridge
earlier, lasso once the 21 constant columns were dropped. Both are the upper reference.)

**Text adds +0.0023 over age and sex**, inside a ±0.062 noise band. Univariately, 0 of 39
concept features clear their floor; TF-IDF produces 20 of 256 above a raw 2-SE threshold
against ~12 expected from noise, and **0 survive FDR or Bonferroni**. The T0 volume gate is
inert (0 of 9, max z=1.44), so this is not a note-volume artefact.

### 10.1 The decisive comparison

**Correction (2026-08-27, raised at clinical review; resolved 2026-09-03).** The concept
term lists originally mixed three different kinds of mention. `nierfunctie` included `egfr`
and `creatinineklaring`, which fire on *"eGFR 95 ml/min"* — i.e. **normal** kidney function —
so that feature measured "renal function was reported", not "renal disease is present".
`hyperlipidemie` included `cholesterol` (fires on a normal lipid value) and `statine`;
`diabetes`, `hypertensie` and `roken` included medication or quantity terms. And
`perifeer_vaatlijden` included `aneurysma`, which is a **different disease**, not peripheral
arterial disease. Terms are now tiered (disease / symptom / measurement / medication /
procedure) with disease+symptom the default, `aneurysma` split into its own concept, and
`--concept-terms all` retained to reproduce the conflated behaviour.

The correction works and it changes nothing. Prevalences move exactly where the diagnosis
predicted — renal **21.0% → 5.2%** (33.0% when the measurement tier is re-admitted, which is
the size of the artefact), peripheral disease 14.3% → 8.4% with aneurysm now separate at
10.4%, hyperlipidaemia 36.5% → 26.2%, diabetes 28.2% → 23.9%, heart failure 10.4% → 8.7% —
and the verdict does not: corrected concepts test C **0.5098** vs 0.5114 conflated, with all
term tiers 0.5092, and **0 of 39** features clearing the floor in every variant. Per feature
the movement is in the third decimal: `nierfunctie_present` 0.4893 → 0.4900,
`diabetes_present` 0.4859 → 0.4854, `hyperlipidemie_present` 0.4873 → 0.4908,
`hypertensie_present` 0.4965 → 0.4979. The conflated lists were a real defect in what the
features *meant*; they were not what suppressed the signal.

Extraction is not the failure. Concepts are found at clinically plausible rates —
hypertension 39.8%, smoking 39.4%, stenosis 31.2%, hyperlipidaemia 26.2%, prior MI 26.2%,
diabetes 23.9%, angina 22.4%, stroke/TIA 17.2%, aneurysm 10.4%, heart failure 8.7%,
peripheral arterial disease 8.4%, atrial fibrillation 7.7%, renal disease 5.2% (disease and
symptom terms only) — and negation behaves sensibly (heart failure negated in 1,245 patients
versus asserted in 835, which is what "geen decompensatie" in a routine letter should
produce).

Yet the **same clinical concept** predicts when curated and does not when extracted from
text, on the same patients, outcome and screen (train C):

| concept | curated variable | text-extracted |
|---|---|---|
| diabetes | `vz_DM` 0.5472, `vz_t2d` 0.5480 | `diabetes_present` **0.4854** |
| smoking | `roken` 0.5654, `packyrs` 0.6066 | `roken_present` **0.5021** |
| cardiac history | `vz_hart` 0.5635, `vgt_hart` 0.5718 | `myocardinfarct_present` **0.4917** |
| renal function | `labkrea` 0.6168, `MDRD` 0.3885, `klar_coc` 0.3634 | `nierfunctie_present` **0.4900** |
| carotid stenosis | `stenACIl` 0.6420, `stenACIr` 0.6400 | `stenose_present` **0.4924** |
| hypertension | `vz_hypt` 0.5508, `bdsys` 0.5747 | `hypertensie_present` **0.4979** |
| lipids | `labtrig` 0.5303, `labhdl` 0.4657 | `hyperlipidemie_present` **0.4908** |
| peripheral disease | `pa_stolmid` 0.5935, `abivrl_n` 0.5839 | `perifeer_vaatlijden_present` **0.4916** |

(Text-extracted values are the corrected disease+symptom terms; the curated column is the
same screen on the matched subcohort.)

**106 of 183** curated features clear the floor; **0 of 39** text concepts do.

The difference is not *which facts* are recorded but *how*. A curated variable is a graded,
protocol-measured quantity (pack-years, systolic pressure, creatinine, percent stenosis);
its text counterpart is a binary mention, undated within the window, written for clinical
communication rather than measurement. Mentioning diabetes does not encode how long or how
badly; mentioning stenosis does not encode 40% versus 90%. That graded information is what
the curated variables carry and the prose does not.

### 10.2 Incremental value over the full curated baseline

The comparison a clinician actually cares about is not "text versus age and sex" but "text
*on top of everything already collected*" — those 183 variables exist in this cohort, so
text only matters if it adds to them. Each arm below is the full 183-variable curated
baseline plus one text representation, on the matched subcohort, lasso Cox tuned on
validation:

| arm | n features | test C | Δ vs curated alone |
|---|---|---|---|
| curated baseline alone | 183 | **0.7394** | — |
| + concepts (disease+symptom) | 222 | 0.7397 | **+0.0003** |
| + volume (T0 features) | 192 | 0.7394 | **+0.0000** |
| + TF-IDF word, 256 SVD | 439 | 0.7388 | **−0.0006** |

All three land inside ±0.001 of the baseline in a ±0.062 band. Text adds **+0.0023** over
demographics alone and **+0.0003** over the full curated set: the small increment it has
over age and sex is information the curated variables already carry.

This also sets the bar for any future model: a frozen-LLM or fine-tuned text arm has to
clear **0.7394**, not 0.6727, to change clinical practice here.

### 10.2b Headroom: how much of the curated skill is text-derivable in principle?

The arms above say text adds nothing. They do not say whether that is because the notes lack
the information or because TF-IDF and binary concepts fail to extract it. This check
separates the two without a model, by splitting the 183 curated variables by **provenance**
and asking what each half achieves.

The split is by exact name in `scripts/smartehr/feature_matrix.py`, reviewable with
`--list-baseline-groups`, and verified exhaustive on the real data (113 chart + 68 protocol
+ 2 demographics = 183). Age and sex sit in **neither** half — they are the floor both are
measured against.

| arm | n | test C | share of the demographics → full-baseline gap |
|---|---|---|---|
| full curated baseline | 183 | **0.7394** | 100% |
| chart-derivable + demographics | 115 | 0.7351 | **94%** |
| **chart-derivable alone** | 113 | **0.7310** | **87%** |
| protocol-measured + demographics | 70 | 0.7198 | 71% |
| protocol-measured alone | 68 | 0.7196 | 70% |
| chart-derivable, strict (no imaging findings) | 96 | 0.7024 | 44% |
| demographics only | 2 | 0.6727 | 0% |
| *best text arm (TF-IDF + demographics)* | *258* | *0.6750* | ***3%*** |

**There is substantial headroom, and this reverses the expectation.** Facts a clinical note
could plausibly state carry **87%** of the curated baseline's advantage over demographics —
without any age or sex — while the text arms realised **3%** of it. So the free-text null is
a failure of *extraction*, not an absence of information. Both halves reaching ~0.72–0.73
separately while together reaching 0.7394 also shows they are largely redundant: the same
severity is visible through history and through measurement.

What carries the chart-derivable half is specific, and it is almost all **graded or dated**:

| feature | train C | why it matters here |
|---|---|---|
| `stenACIl` / `stenACIr` | 0.6471 / 0.6468 | percent carotid stenosis — the strongest features in the half, and radiology reports **are** in our corpus |
| `KliMaYr` (onset year) | 0.3855, `C_udev` 0.6313 | dated onset, inverse: earlier first event is worse |
| `KliMaC` / `KliMaDur` / `KliMaDrD` | 0.6138 / 0.6078 / 0.5976 | type and duration of the first manifest event |
| `packyrs` | 0.6182 | **pack-years, not smoking status.** `roken` (status) reads 0.5674, and the text concept `roken_present` 0.5021 |
| `mht_alln` | 0.5732 | *count* of antihypertensive classes — treatment intensity, not presence |
| `pa_stolmid`, `pamid`, `mas01`, `mht_all`, `aspirine` | 0.5935 – 0.5587 | antiplatelet / anticoagulant / antihypertensive use |

Dropping the imaging findings costs 0.7310 → **0.7024**, so grades from radiology reports are
worth 0.029 on their own. Even the strict half still beats demographics by 0.030.

This is §10.1's "*that* versus *how much*" claim stated quantitatively, and it now cuts the
other way than a pure null would: the graded facts are prognostic, they are the kind of thing
prose can carry (a report states "70% stenose", a letter states "myocardinfarct in 2003",
"30 pakjaren", "drie antihypertensiva"), and no representation tried so far encodes grading
at all. That is a testable hypothesis rather than a closed question.

**Method note worth recording.** The provenance split was first drafted by name prefix. That
rule put the 44 medication flags, the four `KliMa*` onset variables, and `leeftijd`/`geslacht`
on the protocol side — and the table above shows those are precisely what carries the
chart-derivable half. Run as drafted, the chart half would have held ~36 features, landed
near demographics, and the conclusion would have been "no headroom, close the arm": the
opposite of the truth, reached by a rule that happened to confirm the prior. The partition is
therefore written out by name and audited for exhaustiveness rather than pattern-matched.

### 10.3 Sensitivity: `ok.OMSCHR` and post-baseline treatment

`OMSCHR` is the **operation description**, and its rows are mostly post-baseline: `datediff`
p25 = −42, **p50 = +98**, with 16,671 of 35,117 rows at or after the baseline visit. Under
the day-180 landmark it is formally admissible (available at the prediction origin; the
leakage invariant prints 0), but a model that leans on it is partly reading *treatment
delivered after enrolment*, which is not what "risk at enrolment" means.

Rebuilding the structured arm without it: **test C 0.6884** with 532 features, versus 0.6890
with 534. The two `ok.OMSCHR` occurrence codes contribute **−0.0006**. The structured result
does not depend on it, so the interpretive concern does not arise — and this is recorded
because "we checked and it did not matter" is a different claim from "we did not check".

## 11. Conclusion

Neither structured EHR events nor clinical free text carries **detectable 15-year
prognostic signal beyond age and sex** in this cohort: events add +0.0007 and text +0.0023,
and against the full curated baseline text adds **+0.0003**,
while expert-curated baseline variables reach C=0.7576 (0.7394 on the text subcohort) and
retain 0.7547 without any demographics. Sixteen text arms span 0.482–0.520. The result survives landmarking at three
origins, pivoting that recovers the full same-day panels, recovery of thresholded lab
values, tokenised diagnosis codes, a bounded 365-day feature window, permutation-calibrated
significance, multiple-testing correction over effective tests, a validated positive
control, an explicit demographics decomposition confirming the comparison is fair,
clinician-reviewed concept terms tiered to separate disease mentions from measurements and
medications, and a sensitivity arm confirming the structured result does not rest on
post-baseline operation codes.

The free-text half of that conclusion is now narrower than it looks. §10.2b shows the
chart-derivable curated variables reach **0.7310 without demographics** — 87% of the
curated advantage — so the notes plausibly contain most of what the baseline visit records.
What no representation tried so far captures is *grading*: percent stenosis, dated onset,
pack-years, count of drug classes. The negative therefore stands for TF-IDF and binary
concepts, and one further arm aimed squarely at graded extraction (T3) is justified rather
than redundant. Its bar is **0.7310**, not 0.6727.

Manual curation is therefore not redundant here, and the reason is now specific rather
than speculative: the same clinical concepts are present in the notes at plausible rates
(§10.1) and still do not predict, because prose records *that* a condition was mentioned
while the curated variable records *how much* — pack-years, systolic pressure, creatinine,
percent stenosis. What curation contributes is graded, protocol measurement, not the
presence of the fact. Both representations are now closed.
