# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (43 runs)

- **2026-09-08T08:09:53Z | text arm: graded**
  - status: FAILED
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- **2026-09-08T08:10:07Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: graded vs curated (train, outcome-blind): 0 of 13 pairs reach |rho|>=0.3
  - RESULT: arm=text_graded[dates=strip] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T08:13:51Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 41 features; 2259 of 9644 patients have at least one extracted quantity
  - RESULT: graded vs curated (train, outcome-blind): 0 of 13 pairs reach |rho|>=0.3
  - RESULT: arm=text_graded[dates=year] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T08:17:21Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip]+baseline[leeftijd,geslacht] n_features=35 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T08:20:46Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=74 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T08:24:36Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip]+baseline[all] n_features=216 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T08:28:08Z | screen: CTRL_demo_full**
  - RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
- **2026-09-08T08:28:39Z | screen: CTRL_demo_rt**
  - RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:29:00Z | screen: CTRL_full_full**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-08T08:31:26Z | screen: CTRL_full_rt**
  - RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:34:00Z | screen: GRADED_all_demo_rt**
  - RESULT: univariate: 2 of 74 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:34:47Z | screen: GRADED_demo_rt**
  - RESULT: univariate: 2 of 35 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6745 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:35:20Z | screen: GRADED_full_rt**
  - RESULT: univariate: 103 of 216 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7395 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:38:45Z | screen: GRADED_rt**
  - RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.1 TEST C=0.5113 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T08:39:15Z | screen: GRADED_strip_rt**
  - RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4979 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T08:39:45Z | screen: GRADED_year_rt**
  - RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.1 TEST C=0.5113 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T08:40:16Z | screen: HR_chart_demo_rt**
  - RESULT: univariate: 59 of 115 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7351 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:41:34Z | screen: HR_chart_full**
  - RESULT: univariate: 60 of 113 features clear the 0.0192 floor; strongest smart_baseline.stenACIl C=0.6420
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7373 (2-SE band +/-0.051) -> signal
- **2026-09-08T08:43:25Z | screen: HR_chart_rt**
  - RESULT: univariate: 57 of 113 features clear the 0.0203 floor; strongest smart_baseline.stenACIl C=0.6471
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7310 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:44:41Z | screen: HR_chartstrict_rt**
  - RESULT: univariate: 43 of 96 features clear the 0.0203 floor; strongest smart_baseline.KliMaYr C=0.3855
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7024 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:45:43Z | screen: HR_protocol_demo_rt**
  - RESULT: univariate: 46 of 70 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7198 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:46:33Z | screen: HR_protocol_full**
  - RESULT: univariate: 44 of 68 features clear the 0.0192 floor; strongest smart_baseline.klar_coc C=0.3634
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7288 (2-SE band +/-0.051) -> signal
- **2026-09-08T08:47:45Z | screen: HR_protocol_rt**
  - RESULT: univariate: 44 of 68 features clear the 0.0203 floor; strongest smart_baseline.klar_coc C=0.3625
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7196 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:48:34Z | screen: INCR_concepts_full**
  - RESULT: univariate: 103 of 222 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7397 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:52:03Z | screen: INCR_tfidf_full**
  - RESULT: univariate: 123 of 439 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7388 (2-SE band +/-0.062) -> signal
- **2026-09-08T08:59:16Z | screen: INCR_volume_full**
  - RESULT: univariate: 103 of 192 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-08T09:02:04Z | screen: SENS_no_omschr**
  - RESULT: univariate: 2 of 532 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6884 (2-SE band +/-0.051) -> signal
- **2026-09-08T09:17:04Z | screen: STRUCT_ctrl**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-08T09:19:30Z | screen: T0_volume**
  - RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-08T09:20:04Z | screen: T0_volume_rt**
  - RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:20:28Z | screen: T1_tfidf_3src**
  - RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:25:21Z | screen: T1_tfidf_char**
  - RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:30:15Z | screen: T1_tfidf_conclusie**
  - RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:31:54Z | screen: T1_tfidf_demo**
  - RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-09-08T09:37:07Z | screen: T1_tfidf_history**
  - RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:38:46Z | screen: T1_tfidf_nonames**
  - RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:43:46Z | screen: T1_tfidf_word**
  - RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:48:39Z | screen: T1_tfidf_word_full**
  - RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-08T09:52:38Z | screen: T2_concepts**
  - RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5098 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:53:10Z | screen: T2_concepts_alltiers**
  - RESULT: univariate: 0 of 42 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=10 TEST C=0.5092 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:53:42Z | screen: T2_concepts_both**
  - RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5095 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-08T09:54:28Z | screen: T2_concepts_demo**
  - RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-09-08T09:55:02Z | screen: T2_concepts_history**
  - RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5198 (2-SE band +/-0.062) -> indistinguishable from chance

---

### RUN 2026-09-08T08:09:53Z | text arm: graded

- status: FAILED
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=year med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.

Traceback (most recent call last):
  File "/home/lorenzo.pratesi@mydre.org/workspace/smartehr/scripts/smartehr/results_log.py", line 74, in results_block
    yield
  File "/home/lorenzo.pratesi@mydre.org/workspace/smartehr/scripts/smartehr/prepare_text_features.py", line 1080, in <module>
    main(a)
  File "/home/lorenzo.pratesi@mydre.org/workspace/smartehr/scripts/smartehr/prepare_text_features.py", line 833, in main
    t = clean_text(txt, args.strip_dates, args.strip_names, args.strip_nameish,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lorenzo.pratesi@mydre.org/workspace/smartehr/scripts/smartehr/prepare_text_features.py", line 268, in clean_text
    return re.sub(r"\s+", " ", t).strip()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lorenzo.pratesi@mydre.org/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/re/__init__.py", line 186, in sub
    return _compile(pattern, flags).sub(repl, string, count)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
```

</details>

---

### RUN 2026-09-08T08:10:07Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: graded vs curated (train, outcome-blind): 0 of 13 pairs reach |rho|>=0.3
- RESULT: arm=text_graded[dates=strip] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=strip med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.
  after cleaning: 9,644 patients retain text (100.0%)
  NOTE: --date-mode is not 'year', so a year written as part of a full date is stripped and graded.onset_year_min will under-fire. The paired arm exists to measure the calendar-era contribution; read them together.
  reusing medication lexicon /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json (118 names, 18 classes)
  41 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,306 ( 13.5%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,306 ( 13.5%)  median=0.00 p90=4.00
    graded.stenosis_left_max                    393 (  4.1%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   380 (  3.9%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,306 ( 13.5%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            672 (  7.0%)  median=12.00 p90=44.00
    graded.packyears_stated                     581 (  6.0%)  median=13.00 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.smoking_status_max                 1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.alcohol_status_last                1,206 ( 12.5%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                       494 (  5.1%)  median=2007.00 p90=2013.00
    graded.onset_year_n                         494 (  5.1%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                         889 (  9.2%)  median=2.04 p90=4.60
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=1.00 p90=7.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity

  --- extracted vs curated, TRAIN, outcome never consulted ---
  `both` is the patients where BOTH are present; agreement is only defined there.
  extracted                              curated                both     rho   exact   sens   spec
  graded.stenosis_max                    stenACIl/stenACIr       832  +0.074   0.209   -      -   
  graded.stenosis_left_max               stenACIl                239  +0.089   0.167   -      -   
  graded.stenosis_right_max              stenACIr                234  +0.117   0.184   -      -   
  graded.stenosis_ge50                   csten_50                821  +0.038   0.627  0.417  0.648
  graded.stenosis_ge70                   csten_70                821  +0.055   0.693  0.377  0.718
  graded.packyears                       packyrs                 414  +0.056     -     -      -   
  graded.packyears_stated                packyrs                 357  +0.070     -     -      -   
  graded.smoking_status_last             roken                 1,072  +0.015   0.316   -      -   
  graded.alcohol_status_last             alcohol                 780  -0.011   0.458   -      -   
  graded.alcohol_glasses_band            AlchlGlz                413  +0.008   0.230   -      -   
  graded.onset_year_min                  KliMaYr                 202  -0.179     -     -      -   
  graded.aorta_cm_max                    aorta_hg                555  -0.006     -     -      -   
  graded.n_antihypertensive_classes      mht_alln              6,210  -0.010     -     -      -   
RESULT: graded vs curated (train, outcome-blind): 0 of 13 pairs reach |rho|>=0.3
  ** nothing reaches |rho|>=0.3: the extraction does not recover the curated
     quantities, so a null survival result would be about extraction, not text **

  extracted medication class             curated      both   sens   spec
  ace_remmer                             mht03       6,210  0.223  0.760
  alfablokker                            mht05       6,210  0.010  0.988
  at1_antagonist                         mht12       6,210  0.081  0.921
  betablokker                            mht01       6,210  0.269  0.724
  calciumantagonist                      mht04       6,210  0.337  0.656
  centraal_antihyp                       mht07       6,210  0.000  0.990
  cholesterolabsorptieremmer             mli04       5,858  0.036  0.955
  diureticum                             mht02       6,210  0.111  0.892
  doac                                   mas03       6,210  0.028  0.993
  fibraat                                mli02       5,858  0.000  0.997
  galzuurbinder                          mli03       5,858  0.000  0.999
  insuline                               mgl02       6,210  0.175  0.830
  lmwh                                   mas02c      6,210  0.500  0.688
  oraal_antidiabeticum                   mgl01       6,210  0.060  0.933
  plaatjesremmer                         mas01       6,210  0.288  0.698
  statine                                mli01       5,858  0.315  0.656
  vasodilatator                          mht41       6,210  0.000  0.999
  vka                                    mas02       6,210  0.074  0.928

  raw feature matrix: 9,644 patients x 41 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  41 features tested = ~19 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~1 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<2.6e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  graded.stenosis_n                         0.4679  0.4477  13.6%   120  1.96          
  graded.med_insuline                       0.4835  0.4835 100.0%   828  1.63          
  graded.n_med_classes                      0.4899  0.4882 100.0%   828  1.17          
  graded.med_diureticum                     0.4893  0.4893 100.0%   828  1.06          
  graded.alcohol_status_last                0.5541  0.4459  12.7%    79  1.65          
  graded.med_vka                            0.4919  0.4919 100.0%   828  0.80          
  graded.n_antihypertensive_classes         0.4929  0.4929 100.0%   828  0.70          
  graded.med_oraal_antidiabeticum           0.4932  0.4932 100.0%   828  0.67          
  graded.any_antihypertensive               0.4934  0.4934 100.0%   828  0.65          
  graded.med_calciumantagonist              0.4939  0.4939 100.0%   828  0.60          
  graded.packyears_measured                 0.4943  0.4943 100.0%   828  0.56          
  graded.med_statine                        0.4949  0.4949 100.0%   828  0.51          
  graded.med_cholesterolabsorptieremmer     0.4959  0.4959 100.0%   828  0.40          
  graded.med_at1_antagonist                 0.4959  0.4959 100.0%   828  0.40          
  graded.med_alfablokker                    0.4975  0.4975 100.0%   828  0.25          
  graded.aorta_measured                     0.4977  0.4977 100.0%   828  0.23          
  graded.stenosis_measured                  0.5018  0.5018 100.0%   828  0.18          
  graded.med_doac                           0.5016  0.5016 100.0%   828  0.16          
  graded.onset_measured                     0.4988  0.4988 100.0%   828  0.12          
  graded.med_fibraat                        0.4992  0.4992 100.0%   828  0.08          
  graded.med_ace_remmer                     0.5008  0.5008 100.0%   828  0.08          
  graded.med_betablokker                    0.5007  0.5007 100.0%   828  0.06          
  graded.med_lmwh                           0.4995  0.4995 100.0%   828  0.05          
  graded.med_plaatjesremmer                 0.5005  0.5005 100.0%   828  0.05          
  graded.med_centraal_antihyp               0.4995  0.4995 100.0%   828  0.04          
  graded.med_galzuurbinder                  0.5004  0.5004 100.0%   828  0.04          
  graded.med_vasodilatator                  0.4997  0.4997 100.0%   828  0.03          
  graded.stenosis_max                       0.4956  0.4685  13.6%   120  1.18          
  graded.alcohol_glasses_band               0.5685  0.5685   6.7%    38  1.45          
  graded.stenosis_right_max                 0.4761  0.4231   3.8%    31  1.47          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 138,724 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=33
  validation : 1,510 patients | events=206 (13.6%) | features=33
  test       : 1,924 patients | events=257 (13.4%) | features=33
RESULT: arm=text_graded[dates=strip] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt model=mlp model.input_size=33
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T08:13:51Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 41 features; 2259 of 9644 patients have at least one extracted quantity
- RESULT: graded vs curated (train, outcome-blind): 0 of 13 pairs reach |rho|>=0.3
- RESULT: arm=text_graded[dates=year] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=year med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.
  after cleaning: 9,644 patients retain text (100.0%)
  reusing medication lexicon /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json (118 names, 18 classes)
  41 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,306 ( 13.5%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,306 ( 13.5%)  median=0.00 p90=4.00
    graded.stenosis_left_max                    394 (  4.1%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   381 (  4.0%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,306 ( 13.5%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            672 (  7.0%)  median=12.00 p90=44.00
    graded.packyears_stated                     581 (  6.0%)  median=13.00 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.smoking_status_max                 1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.alcohol_status_last                1,206 ( 12.5%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                       501 (  5.2%)  median=2007.00 p90=2013.00
    graded.onset_year_n                         501 (  5.2%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                         889 (  9.2%)  median=2.04 p90=4.60
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=1.00 p90=7.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 41 features; 2259 of 9644 patients have at least one extracted quantity

  --- extracted vs curated, TRAIN, outcome never consulted ---
  `both` is the patients where BOTH are present; agreement is only defined there.
  extracted                              curated                both     rho   exact   sens   spec
  graded.stenosis_max                    stenACIl/stenACIr       832  +0.074   0.209   -      -   
  graded.stenosis_left_max               stenACIl                239  +0.089   0.167   -      -   
  graded.stenosis_right_max              stenACIr                235  +0.122   0.187   -      -   
  graded.stenosis_ge50                   csten_50                821  +0.038   0.627  0.417  0.648
  graded.stenosis_ge70                   csten_70                821  +0.055   0.693  0.377  0.718
  graded.packyears                       packyrs                 414  +0.056     -     -      -   
  graded.packyears_stated                packyrs                 357  +0.070     -     -      -   
  graded.smoking_status_last             roken                 1,072  +0.015   0.316   -      -   
  graded.alcohol_status_last             alcohol                 780  -0.011   0.458   -      -   
  graded.alcohol_glasses_band            AlchlGlz                413  +0.008   0.230   -      -   
  graded.onset_year_min                  KliMaYr                 203  -0.179     -     -      -   
  graded.aorta_cm_max                    aorta_hg                555  -0.006     -     -      -   
  graded.n_antihypertensive_classes      mht_alln              6,210  -0.010     -     -      -   
RESULT: graded vs curated (train, outcome-blind): 0 of 13 pairs reach |rho|>=0.3
  ** nothing reaches |rho|>=0.3: the extraction does not recover the curated
     quantities, so a null survival result would be about extraction, not text **

  extracted medication class             curated      both   sens   spec
  ace_remmer                             mht03       6,210  0.223  0.760
  alfablokker                            mht05       6,210  0.010  0.988
  at1_antagonist                         mht12       6,210  0.081  0.921
  betablokker                            mht01       6,210  0.269  0.724
  calciumantagonist                      mht04       6,210  0.337  0.656
  centraal_antihyp                       mht07       6,210  0.000  0.990
  cholesterolabsorptieremmer             mli04       5,858  0.036  0.955
  diureticum                             mht02       6,210  0.111  0.892
  doac                                   mas03       6,210  0.028  0.993
  fibraat                                mli02       5,858  0.000  0.997
  galzuurbinder                          mli03       5,858  0.000  0.999
  insuline                               mgl02       6,210  0.175  0.830
  lmwh                                   mas02c      6,210  0.500  0.688
  oraal_antidiabeticum                   mgl01       6,210  0.060  0.933
  plaatjesremmer                         mas01       6,210  0.288  0.698
  statine                                mli01       5,858  0.315  0.656
  vasodilatator                          mht41       6,210  0.000  0.999
  vka                                    mas02       6,210  0.074  0.928

  raw feature matrix: 9,644 patients x 41 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 138,708 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=33
  validation : 1,510 patients | events=206 (13.6%) | features=33
  test       : 1,924 patients | events=257 (13.4%) | features=33
RESULT: arm=text_graded[dates=year] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt model=mlp model.input_size=33
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T08:17:21Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=strip]+baseline[leeftijd,geslacht] n_features=35 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=strip med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.
  after cleaning: 9,644 patients retain text (100.0%)
  NOTE: --date-mode is not 'year', so a year written as part of a full date is stripped and graded.onset_year_min will under-fire. The paired arm exists to measure the calendar-era contribution; read them together.
  reusing medication lexicon /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json (118 names, 18 classes)
  41 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,306 ( 13.5%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,306 ( 13.5%)  median=0.00 p90=4.00
    graded.stenosis_left_max                    393 (  4.1%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   380 (  3.9%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,306 ( 13.5%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            672 (  7.0%)  median=12.00 p90=44.00
    graded.packyears_stated                     581 (  6.0%)  median=13.00 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.smoking_status_max                 1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.alcohol_status_last                1,206 ( 12.5%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                       494 (  5.1%)  median=2007.00 p90=2013.00
    graded.onset_year_n                         494 (  5.1%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                         889 (  9.2%)  median=2.04 p90=4.60
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=1.00 p90=7.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 43 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 138,724 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=35
  validation : 1,510 patients | events=206 (13.6%) | features=35
  test       : 1,924 patients | events=257 (13.4%) | features=35
RESULT: arm=text_graded[dates=strip]+baseline[leeftijd,geslacht] n_features=35 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt model=mlp model.input_size=35
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T08:20:46Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=74 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=strip med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.
  after cleaning: 9,644 patients retain text (100.0%)
  NOTE: --date-mode is not 'year', so a year written as part of a full date is stripped and graded.onset_year_min will under-fire. The paired arm exists to measure the calendar-era contribution; read them together.
  reusing medication lexicon /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json (118 names, 18 classes)
  41 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,306 ( 13.5%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,306 ( 13.5%)  median=0.00 p90=4.00
    graded.stenosis_left_max                    393 (  4.1%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   380 (  3.9%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,306 ( 13.5%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            672 (  7.0%)  median=12.00 p90=44.00
    graded.packyears_stated                     581 (  6.0%)  median=13.00 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.smoking_status_max                 1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.alcohol_status_last                1,206 ( 12.5%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                       494 (  5.1%)  median=2007.00 p90=2013.00
    graded.onset_year_n                         494 (  5.1%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                         889 (  9.2%)  median=2.04 p90=4.60
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=1.00 p90=7.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  + 39 concept features appended (binary/disease,symptom)
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 82 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 138,724 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=74
  validation : 1,510 patients | events=206 (13.6%) | features=74
  test       : 1,924 patients | events=257 (13.4%) | features=74
RESULT: arm=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=74 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt model=mlp model.input_size=74
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T08:24:36Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=strip]+baseline[all] n_features=216 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=strip med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='all' min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.
  after cleaning: 9,644 patients retain text (100.0%)
  NOTE: --date-mode is not 'year', so a year written as part of a full date is stripped and graded.onset_year_min will under-fire. The paired arm exists to measure the calendar-era contribution; read them together.
  reusing medication lexicon /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json (118 names, 18 classes)
  41 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,306 ( 13.5%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,306 ( 13.5%)  median=0.00 p90=4.00
    graded.stenosis_left_max                    393 (  4.1%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   380 (  3.9%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,306 ( 13.5%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,306 ( 13.5%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            672 (  7.0%)  median=12.00 p90=44.00
    graded.packyears_stated                     581 (  6.0%)  median=13.00 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.smoking_status_max                 1,655 ( 17.2%)  median=3.00 p90=3.00
    graded.alcohol_status_last                1,206 ( 12.5%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                       494 (  5.1%)  median=2007.00 p90=2013.00
    graded.onset_year_n                         494 (  5.1%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                         889 (  9.2%)  median=2.04 p90=4.60
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=1.00 p90=7.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 41 features; 2256 of 9644 patients have at least one extracted quantity
  appending 183 baseline columns -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 224 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 300,798 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
    smart_baseline.opleiding: train C=0.4764   ** suspiciously flat **
    smart_baseline.RespLand: train C=0.4962   ** suspiciously flat **
    smart_baseline.PaLand: train C=0.5000   ** suspiciously flat **
    smart_baseline.MaLand: train C=0.4979   ** suspiciously flat **
    smart_baseline.WereldDl: train C=0.4935   ** suspiciously flat **
    smart_baseline.diagnsco: train C=0.5473
    smart_baseline.vaatzkt1: train C=0.4435
    smart_baseline.DiagSide: train C=0.5053   ** suspiciously flat **
    smart_baseline.IncInt_p: train C=0.4611
    smart_baseline.IncInt_v: train C=0.4914   ** suspiciously flat **
    smart_baseline.V0405: train C=0.5132   ** suspiciously flat **
    smart_baseline.vg_0410: train C=0.5295   ** suspiciously flat **
    smart_baseline.vgok_car: train C=0.5101   ** suspiciously flat **
    smart_baseline.vgt_kop: train C=0.5357
    smart_baseline.vz_kop: train C=0.5468
    smart_baseline.vg_0321: train C=0.5584
    smart_baseline.vg_0323: train C=0.5094   ** suspiciously flat **
    smart_baseline.vgok_har: train C=0.5445
    smart_baseline.vgt_hart: train C=0.5706
    smart_baseline.vz_hart: train C=0.5646
    smart_baseline.vg_0325: train C=0.5364
    smart_baseline.vgok_aaa: train C=0.5076   ** suspiciously flat **
    smart_baseline.vgt_aaa: train C=0.5375
    smart_baseline.vz_aaa: train C=0.5393
    smart_baseline.vg_0606c: train C=0.5038   ** suspiciously flat **
    smart_baseline.vgok_nie: train C=0.5010   ** suspiciously flat **
    smart_baseline.vgt_nier: train C=0.5046   ** suspiciously flat **
    smart_baseline.vz_nier: train C=0.5085   ** suspiciously flat **
    smart_baseline.vg_0519: train C=0.5062   ** suspiciously flat **
    smart_baseline.vgok_bee: train C=0.5192   ** suspiciously flat **
    smart_baseline.vgt_been: train C=0.5192   ** suspiciously flat **
    smart_baseline.vz_been: train C=0.5411
    smart_baseline.bdsys: train C=0.5812
    smart_baseline.bddia: train C=0.4969   ** suspiciously flat **
    smart_baseline.hyptns_n: train C=0.5463
    smart_baseline.hyptns_b: train C=0.5387
    smart_baseline.vz_hypt: train C=0.5473
    smart_baseline.labgluc: train C=0.5579
    smart_baseline.hypgly_n: train C=0.5434
    smart_baseline.hypgly_b: train C=0.5012   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5441
    smart_baseline.vz_t1d: train C=0.4995   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5446
    smart_baseline.klinman: train C=0.5988
    smart_baseline.gewicht: train C=0.5100   ** suspiciously flat **
    smart_baseline.lengte: train C=0.5012   ** suspiciously flat **
    smart_baseline.bm_indx: train C=0.5132   ** suspiciously flat **
    smart_baseline.bmi_30: train C=0.5082   ** suspiciously flat **
    smart_baseline.tail_gm: train C=0.5634
    smart_baseline.heup_gm: train C=0.4993   ** suspiciously flat **
    smart_baseline.tlhp_rat: train C=0.5000   ** suspiciously flat **
    smart_baseline.vet_subc: train C=0.4559
    smart_baseline.vet_gm: train C=0.5643
    smart_baseline.plsprs: train C=0.6123
    smart_baseline.abi_lg: train C=0.4897   ** suspiciously flat **
    smart_baseline.abi_gm: train C=0.4950   ** suspiciously flat **
    smart_baseline.abivrl_n: train C=0.5839
    smart_baseline.ABiRe: train C=0.4913   ** suspiciously flat **
    smart_baseline.ABiLi: train C=0.4950   ** suspiciously flat **
    smart_baseline.imt_gm: train C=0.5234   ** suspiciously flat **
    smart_baseline.stenACIr: train C=0.6468
    smart_baseline.stenACIl: train C=0.6471
    smart_baseline.csten_50: train C=0.5609
    smart_baseline.csten_70: train C=0.5508
    smart_baseline.AortProx: train C=0.5381
    smart_baseline.AortDist: train C=0.5786
    smart_baseline.aorta_hg: train C=0.5653
    smart_baseline.aorta_gm: train C=0.5587
    smart_baseline.aaaech_n: train C=0.5376
    smart_baseline.nrlng_re: train C=0.4958   ** suspiciously flat **
    smart_baseline.nrlng_li: train C=0.4753   ** suspiciously flat **
    smart_baseline.nrlng_gm: train C=0.4829   ** suspiciously flat **
    smart_baseline.nratrof: train C=0.5195   ** suspiciously flat **
    smart_baseline.nrvol_re: train C=0.5099   ** suspiciously flat **
    smart_baseline.nrvol_li: train C=0.4909   ** suspiciously flat **
    smart_baseline.nrvol_gm: train C=0.5005   ** suspiciously flat **
    smart_baseline.labhb: train C=0.4936   ** suspiciously flat **
    smart_baseline.labht: train C=0.5040   ** suspiciously flat **
    smart_baseline.labchol: train C=0.4895   ** suspiciously flat **
    smart_baseline.labtrig: train C=0.5339
    smart_baseline.labhdl: train C=0.4614
    smart_baseline.ldlchol: train C=0.4969   ** suspiciously flat **
    smart_baseline.VgBh_HpL: train C=0.5141   ** suspiciously flat **
    smart_baseline.hyplip_n: train C=0.4975   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5233   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5138   ** suspiciously flat **
    smart_baseline.labkrea: train C=0.6233
    smart_baseline.labmalb: train C=0.5763
    smart_baseline.labkrur: train C=0.4317
    smart_baseline.mpkr_rat: train C=0.5957
    smart_baseline.albminur: train C=0.5576
    smart_baseline.nrfaln_n: train C=0.5623
    smart_baseline.klar_coc: train C=0.3625
    smart_baseline.klar_gst: train C=0.3951
    smart_baseline.MDRD: train C=0.3839
    smart_baseline.labhcyst: train C=0.5969
    smart_baseline.hyphmc_n: train C=0.5461
    smart_baseline.labins: train C=0.5408
    smart_baseline.labtsh: train C=0.5241   ** suspiciously flat **
    smart_baseline.labcrp: train C=0.5838
    smart_baseline.labhba1c: train C=0.5637
    smart_baseline.labapob: train C=0.4977   ** suspiciously flat **
    smart_baseline.roken: train C=0.5674
    smart_baseline.packyrs: train C=0.6182
    smart_baseline.alcohol: train C=0.4464
    smart_baseline.AlchlGlz: train C=0.4979   ** suspiciously flat **
    smart_baseline.V0821: train C=0.4933   ** suspiciously flat **
    smart_baseline.V082201: train C=0.5011   ** suspiciously flat **
    smart_baseline.V082202: train C=0.5006   ** suspiciously flat **
    smart_baseline.V0823: train C=0.5002   ** suspiciously flat **
    smart_baseline.MBSc: train C=0.5695
    smart_baseline.MBS: train C=0.5521
    smart_baseline.MBSc_mis: train C=0.5693
    smart_baseline.MBScgr: train C=0.5612
    smart_baseline.kl1fysfc: train C=0.4000
    smart_baseline.kl2socfc: train C=0.4403
    smart_baseline.kl3rolfy: train C=0.4522
    smart_baseline.kl4rolem: train C=0.4880   ** suspiciously flat **
    smart_baseline.kl5mengz: train C=0.4733   ** suspiciously flat **
    smart_baseline.kl6vital: train C=0.4480
    smart_baseline.kl7pijn: train C=0.4369
    smart_baseline.kl8alggz: train C=0.4233
    smart_baseline.kl9gezva: train C=0.4986   ** suspiciously flat **
    smart_baseline.mht01: train C=0.5288   ** suspiciously flat **
    smart_baseline.mht02: train C=0.5381
    smart_baseline.mht02a: train C=0.5359
    smart_baseline.mht02b: train C=0.5037   ** suspiciously flat **
    smart_baseline.mht02c: train C=0.5066   ** suspiciously flat **
    smart_baseline.mht02d: train C=0.5083   ** suspiciously flat **
    smart_baseline.mht03: train C=0.5256   ** suspiciously flat **
    smart_baseline.mht04: train C=0.5335
    smart_baseline.mht05: train C=0.5025   ** suspiciously flat **
    smart_baseline.mht06: train C=0.5025   ** suspiciously flat **
    smart_baseline.mht07: train C=0.4994   ** suspiciously flat **
    smart_baseline.mht12: train C=0.5151   ** suspiciously flat **
    smart_baseline.mht33: train C=0.5023   ** suspiciously flat **
    smart_baseline.mht41: train C=0.5000   ** suspiciously flat **
    smart_baseline.mliphoop: train C=0.5114   ** suspiciously flat **
    smart_baseline.mli01: train C=0.5183   ** suspiciously flat **
    smart_baseline.mli02: train C=0.4990   ** suspiciously flat **
    smart_baseline.mli03: train C=0.4998   ** suspiciously flat **
    smart_baseline.mli04: train C=0.4971   ** suspiciously flat **
    smart_baseline.mas01: train C=0.5657
    smart_baseline.mas01a: train C=0.5123   ** suspiciously flat **
    smart_baseline.mas01b: train C=0.5023   ** suspiciously flat **
    smart_baseline.mas01c: train C=0.5152   ** suspiciously flat **
    smart_baseline.mas01d: train C=0.5015   ** suspiciously flat **
    smart_baseline.mas02: train C=0.5366
    smart_baseline.mas02a: train C=0.5179   ** suspiciously flat **
    smart_baseline.mas02b: train C=0.5046   ** suspiciously flat **
    smart_baseline.mas02c: train C=0.5000   ** suspiciously flat **
    smart_baseline.mas03: train C=0.5002   ** suspiciously flat **
    smart_baseline.mmpr: train C=0.5334
    smart_baseline.mhmc: train C=0.5051   ** suspiciously flat **
    smart_baseline.mgl01: train C=0.5283   ** suspiciously flat **
    smart_baseline.mgl02: train C=0.5137   ** suspiciously flat **
    smart_baseline.mgl03: train C=0.4996   ** suspiciously flat **
    smart_baseline.TCA: train C=0.4986   ** suspiciously flat **
    smart_baseline.SSRI: train C=0.4970   ** suspiciously flat **
    smart_baseline.MAO: train C=0.5000   ** suspiciously flat **
    smart_baseline.OthADep: train C=0.5105   ** suspiciously flat **
    smart_baseline.Benzo: train C=0.5045   ** suspiciously flat **
    smart_baseline.BenzoDer: train C=0.5074   ** suspiciously flat **
    smart_baseline.BenzoRel: train C=0.5000   ** suspiciously flat **
    smart_baseline.Thyr: train C=0.4998   ** suspiciously flat **
    smart_baseline.Amiodar: train C=0.5013   ** suspiciously flat **
    smart_baseline.Lithium: train C=0.5005   ** suspiciously flat **
    smart_baseline.mht_alln: train C=0.5732
    smart_baseline.mht_all: train C=0.5629
    smart_baseline.lipmid: train C=0.5181   ** suspiciously flat **
    smart_baseline.statine: train C=0.5185   ** suspiciously flat **
    smart_baseline.pamid: train C=0.5657
    smart_baseline.aspirine: train C=0.5587
    smart_baseline.pa_stolmid: train C=0.5935
    smart_baseline.KliMaC: train C=0.6138
    smart_baseline.KliMaYr: train C=0.3855
    smart_baseline.KliMaDur: train C=0.6078
    smart_baseline.KliMaDrD: train C=0.5976
    smart_baseline.spMEThw: train C=0.4445
    smart_baseline.acMEThw: train C=0.4497
    smart_baseline.bwMEThw: train C=0.4353
  train      : 6,210 patients | events=828 (13.3%) | features=216
  validation : 1,510 patients | events=206 (13.6%) | features=216
  test       : 1,924 patients | events=257 (13.4%) | features=216
RESULT: arm=text_graded[dates=strip]+baseline[all] n_features=216 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt model=mlp model.input_size=216
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T08:28:08Z | screen: CTRL_demo_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
- RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_full/
  representation=matched_baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=2

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=    2 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=    2 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=    2 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 0 of 2 effectively constant (zero variance, or one value in >99% of patients); 1 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 2 of 2
RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6742   0.5139   0.6839  <-
  smart_baseline.geslacht                              0.4448   0.4448   0.4528  <-

  2 features are only ~2 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~0 times, not ~0.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6742  test C=0.6839

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.6807  val C=0.7117
  penalizer=0.1      train C=0.6811  val C=0.7115
  penalizer=1        train C=0.6806  val C=0.7099
  penalizer=10       train C=0.6806  val C=0.7099
  penalizer=100      train C=0.6806  val C=0.7099

  selected penalizer=0.01 -> TEST C=0.6883 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-09-08T08:28:39Z | screen: CTRL_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_rt/
  representation=matched_baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=2

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=    2 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=    2 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=    2 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 2 effectively constant (zero variance, or one value in >99% of patients); 1 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 2 of 2
RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.geslacht                              0.4422   0.4422   0.4587  <-

  2 features are only ~2 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~0 times, not ~0.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.6803  val C=0.7072
  penalizer=0.1      train C=0.6807  val C=0.7075
  penalizer=1        train C=0.6800  val C=0.7065
  penalizer=10       train C=0.6800  val C=0.7065
  penalizer=100      train C=0.6800  val C=0.7065

  selected penalizer=0.1 -> TEST C=0.6727 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:29:00Z | screen: CTRL_full_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
- RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_full/
  representation=matched_baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=183

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=  183 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=  183 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=  183 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 21 of 183 effectively constant (zero variance, or one value in >99% of patients); 138 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 106 of 183
RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6742   0.5139   0.6839  <-
  smart_baseline.stenACIl                              0.6420   0.4527   0.6366  <-
  smart_baseline.stenACIr                              0.6400   0.4695   0.6362  <-
  smart_baseline.klar_coc                              0.3634   0.5533   0.3635  <-
  smart_baseline.KliMaYr                               0.3911   0.6273   0.3690  <-
  smart_baseline.labkrea                               0.6168   0.5805   0.6285  <-
  smart_baseline.KliMaC                                0.6167   0.5834   0.6130  <-
  smart_baseline.MDRD                                  0.3885   0.5841   0.3685  <-
  smart_baseline.plsprs                                0.6089   0.5658   0.5976  <-
  smart_baseline.klar_gst                              0.3916   0.6084   0.3914  <-
  smart_baseline.packyrs                               0.6066   0.5515   0.6065  <-
  smart_baseline.KliMaDur                              0.6061   0.6061   0.6164  <-
  smart_baseline.klinman                               0.5993   0.4007   0.6087  <-
  smart_baseline.kl1fysfc                              0.4025   0.5132   0.4178  <-
  smart_baseline.KliMaDrD                              0.5971   0.5971   0.6097  <-
  smart_baseline.labcrp                                0.5948   0.5819   0.6062  <-
  smart_baseline.mpkr_rat                              0.5912   0.5683   0.5868  <-
  smart_baseline.labhcyst                              0.5883   0.5481   0.5994  <-
  smart_baseline.pa_stolmid                            0.5876   0.4124   0.5885  <-
  smart_baseline.AortDist                              0.5811   0.5061   0.5730  <-

  183 features are only ~119 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~6 times, not ~9.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6742  test C=0.6839

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 21 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7585  val C=0.7789
  penalizer=0.1      train C=0.7433  val C=0.7588
  penalizer=1        train C=0.7425  val C=0.7574
  penalizer=10       train C=0.7425  val C=0.7574
  penalizer=100      train C=0.7425  val C=0.7574

  selected penalizer=0.01 -> TEST C=0.7576 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-09-08T08:31:26Z | screen: CTRL_full_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_rt/
  representation=matched_baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=183

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  183 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  183 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  183 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 21 of 183 effectively constant (zero variance, or one value in >99% of patients); 138 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 103 of 183
RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-

  183 features are only ~118 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~6 times, not ~9.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 21 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7627  val C=0.7771
  penalizer=0.1      train C=0.7489  val C=0.7679
  penalizer=1        train C=0.7484  val C=0.7661
  penalizer=10       train C=0.7484  val C=0.7661
  penalizer=100      train C=0.7484  val C=0.7661

  selected penalizer=0.01 -> TEST C=0.7394 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:34:00Z | screen: GRADED_all_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 74 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt/
  representation=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=74

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   74 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   74 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   74 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 12 of 74 effectively constant (zero variance, or one value in >99% of patients); 71 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 2 of 74
RESULT: univariate: 2 of 74 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.geslacht                              0.4422   0.4422   0.4587  <-
  graded.med_insuline                                  0.4835   0.4835   0.4995
  concept.diabetes_present                             0.4854   0.4854   0.4848
  concept.aneurysma_present                            0.4881   0.4881   0.4935
  graded.n_med_classes                                 0.4899   0.4882   0.4907
  concept.hypertensie_negated                          0.4891   0.4891   0.5027
  graded.med_diureticum                                0.4893   0.4893   0.5002
  concept.nierfunctie_present                          0.4900   0.4900   0.4954
  graded.alcohol_status_last                           0.5100   0.4900   0.5085
  concept.hyperlipidemie_present                       0.4908   0.4908   0.4627
  concept.perifeer_vaatlijden_present                  0.4916   0.4916   0.4941
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  graded.med_vka                                       0.4919   0.4919   0.4947
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4931
  graded.n_antihypertensive_classes                    0.4929   0.4929   0.4985
  graded.med_oraal_antidiabeticum                      0.4932   0.4932   0.4968
  graded.any_antihypertensive                          0.4934   0.4934   0.4973

  74 features are only ~58 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~3 times, not ~4.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 12 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6809  val C=0.7070
  penalizer=0.1      train C=0.6344  val C=0.6160
  penalizer=1        train C=0.6213  val C=0.6000
  penalizer=10       train C=0.6213  val C=0.5999
  penalizer=100      train C=0.6213  val C=0.5999

  selected penalizer=0.01 -> TEST C=0.6750 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:34:47Z | screen: GRADED_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 35 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6745 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt/
  representation=text_graded[dates=strip]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=35

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   35 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   35 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   35 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 35 effectively constant (zero variance, or one value in >99% of patients); 32 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 2 of 35
RESULT: univariate: 2 of 35 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.geslacht                              0.4422   0.4422   0.4587  <-
  graded.med_insuline                                  0.4835   0.4835   0.4995
  graded.n_med_classes                                 0.4899   0.4882   0.4907
  graded.med_diureticum                                0.4893   0.4893   0.5002
  graded.alcohol_status_last                           0.5100   0.4900   0.5085
  graded.med_vka                                       0.4919   0.4919   0.4947
  graded.n_antihypertensive_classes                    0.4929   0.4929   0.4985
  graded.med_oraal_antidiabeticum                      0.4932   0.4932   0.4968
  graded.any_antihypertensive                          0.4934   0.4934   0.4973
  graded.med_calciumantagonist                         0.4939   0.4939   0.4979
  graded.stenosis_n                                    0.4942   0.4974   0.5028
  graded.packyears_measured                            0.4943   0.4943   0.5034
  graded.med_statine                                   0.4949   0.4949   0.4919
  graded.med_cholesterolabsorptieremmer                0.4959   0.4959   0.5032
  graded.med_at1_antagonist                            0.4959   0.4959   0.5102
  graded.med_alfablokker                               0.4975   0.4975   0.4999
  graded.aorta_measured                                0.4977   0.4977   0.5074
  graded.stenosis_ge70                                 0.4979   0.4979   0.4970
  graded.stenosis_last                                 0.4980   0.4980   0.5003

  35 features are only ~25 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~1 times, not ~2.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6809  val C=0.7069
  penalizer=0.1      train C=0.6587  val C=0.6476
  penalizer=1        train C=0.6480  val C=0.6307
  penalizer=10       train C=0.6479  val C=0.6305
  penalizer=100      train C=0.6479  val C=0.6305

  selected penalizer=0.01 -> TEST C=0.6745 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6745 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:35:20Z | screen: GRADED_full_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 103 of 216 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7395 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt/
  representation=text_graded[dates=strip]+baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=216

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  216 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  216 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  216 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 25 of 216 effectively constant (zero variance, or one value in >99% of patients); 169 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 103 of 216
RESULT: univariate: 103 of 216 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-

  216 features are only ~140 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~7 times, not ~11.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 25 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7630  val C=0.7768
  penalizer=0.1      train C=0.7499  val C=0.7656
  penalizer=1        train C=0.7494  val C=0.7637
  penalizer=10       train C=0.7494  val C=0.7636
  penalizer=100      train C=0.7494  val C=0.7636

  selected penalizer=0.01 -> TEST C=0.7395 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7395 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:38:45Z | screen: GRADED_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 33 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.1 TEST C=0.5113 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt/
  representation=text_graded[dates=strip] | landmark_days=180 | horizon_days=5475 | n_features=33

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   33 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   33 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   33 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 33 effectively constant (zero variance, or one value in >99% of patients); 31 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 33
RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  graded.med_insuline                                  0.4835   0.4835   0.4995
  graded.n_med_classes                                 0.4899   0.4882   0.4907
  graded.med_diureticum                                0.4893   0.4893   0.5002
  graded.alcohol_status_last                           0.5100   0.4900   0.5085
  graded.med_vka                                       0.4919   0.4919   0.4947
  graded.n_antihypertensive_classes                    0.4929   0.4929   0.4985
  graded.med_oraal_antidiabeticum                      0.4932   0.4932   0.4968
  graded.any_antihypertensive                          0.4934   0.4934   0.4973
  graded.med_calciumantagonist                         0.4939   0.4939   0.4979
  graded.stenosis_n                                    0.4942   0.4974   0.5028
  graded.packyears_measured                            0.4943   0.4943   0.5034
  graded.med_statine                                   0.4949   0.4949   0.4919
  graded.med_cholesterolabsorptieremmer                0.4959   0.4959   0.5032
  graded.med_at1_antagonist                            0.4959   0.4959   0.5102
  graded.med_alfablokker                               0.4975   0.4975   0.4999
  graded.aorta_measured                                0.4977   0.4977   0.5074
  graded.stenosis_ge70                                 0.4979   0.4979   0.4970
  graded.stenosis_last                                 0.4980   0.4980   0.5003
  graded.stenosis_measured                             0.5018   0.5018   0.4888
  graded.med_doac                                      0.5016   0.5016   0.5003

  33 features are only ~23 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~1 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5229  val C=0.4713
  penalizer=0.1      train C=0.5188  val C=0.4768
  penalizer=1        train C=0.5187  val C=0.4768
  penalizer=10       train C=0.5187  val C=0.4768
  penalizer=100      train C=0.5187  val C=0.4768

  selected penalizer=0.1 -> TEST C=0.5113 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.5113 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T08:39:15Z | screen: GRADED_strip_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_strip_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 33 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.01 TEST C=0.4979 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_strip_rt/
  representation=text_graded[dates=strip] | landmark_days=180 | horizon_days=5475 | n_features=33

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   33 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   33 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   33 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 6 of 33 effectively constant (zero variance, or one value in >99% of patients); 29 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 33
RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  graded.med_plaatjesremmer                            0.4906   0.4906   0.4964
  graded.onset_year_n                                  0.4972   0.4907   0.4804
  graded.n_med_classes                                 0.4911   0.4911   0.4933
  graded.med_at1_antagonist                            0.4918   0.4918   0.5030
  graded.med_vka                                       0.4919   0.4919   0.4947
  graded.onset_measured                                0.4921   0.4921   0.5028
  graded.smoking_status_max                            0.5077   0.5053   0.4805
  graded.alcohol_status_last                           0.5075   0.4925   0.5060
  graded.smoking_status_last                           0.5072   0.5016   0.4911
  graded.med_oraal_antidiabeticum                      0.4939   0.4939   0.5011
  graded.med_calciumantagonist                         0.4939   0.4939   0.4983
  graded.med_diureticum                                0.4945   0.4945   0.4966
  graded.packyears_measured                            0.4947   0.4947   0.5072
  graded.stenosis_n                                    0.4949   0.4989   0.5027
  graded.n_antihypertensive_classes                    0.4951   0.4951   0.4940
  graded.med_ace_remmer                                0.5048   0.5048   0.4942
  graded.onset_year_min                                0.4981   0.4956   0.5067
  graded.stenosis_measured                             0.5035   0.5035   0.4881
  graded.any_antihypertensive                          0.4967   0.4967   0.4952
  graded.stenosis_max                                  0.5027   0.5005   0.5014

  33 features are only ~24 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~1 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 6 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5206  val C=0.4731
  penalizer=0.1      train C=0.5214  val C=0.4691
  penalizer=1        train C=0.5214  val C=0.4691
  penalizer=10       train C=0.5214  val C=0.4691
  penalizer=100      train C=0.5214  val C=0.4691

  selected penalizer=0.01 -> TEST C=0.4979 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4979 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T08:39:45Z | screen: GRADED_year_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 33 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.1 TEST C=0.5113 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt/
  representation=text_graded[dates=year] | landmark_days=180 | horizon_days=5475 | n_features=33

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   33 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   33 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   33 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 33 effectively constant (zero variance, or one value in >99% of patients); 31 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 33
RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  graded.med_insuline                                  0.4835   0.4835   0.4995
  graded.n_med_classes                                 0.4899   0.4882   0.4907
  graded.med_diureticum                                0.4893   0.4893   0.5002
  graded.alcohol_status_last                           0.5100   0.4900   0.5085
  graded.med_vka                                       0.4919   0.4919   0.4947
  graded.n_antihypertensive_classes                    0.4929   0.4929   0.4985
  graded.med_oraal_antidiabeticum                      0.4932   0.4932   0.4968
  graded.any_antihypertensive                          0.4934   0.4934   0.4973
  graded.med_calciumantagonist                         0.4939   0.4939   0.4979
  graded.stenosis_n                                    0.4942   0.4974   0.5028
  graded.packyears_measured                            0.4943   0.4943   0.5034
  graded.med_statine                                   0.4949   0.4949   0.4919
  graded.med_cholesterolabsorptieremmer                0.4959   0.4959   0.5032
  graded.med_at1_antagonist                            0.4959   0.4959   0.5102
  graded.med_alfablokker                               0.4975   0.4975   0.4999
  graded.aorta_measured                                0.4977   0.4977   0.5074
  graded.stenosis_ge70                                 0.4979   0.4979   0.4970
  graded.stenosis_last                                 0.4980   0.4980   0.5003
  graded.stenosis_measured                             0.5018   0.5018   0.4888
  graded.med_doac                                      0.5016   0.5016   0.5003

  33 features are only ~23 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~1 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5230  val C=0.4713
  penalizer=0.1      train C=0.5188  val C=0.4767
  penalizer=1        train C=0.5188  val C=0.4767
  penalizer=10       train C=0.5188  val C=0.4767
  penalizer=100      train C=0.5188  val C=0.4767

  selected penalizer=0.1 -> TEST C=0.5113 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.5113 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T08:40:16Z | screen: HR_chart_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 59 of 115 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7351 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_demo_rt/
  representation=matched_baseline[group:chart,leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=115

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  115 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  115 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  115 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 17 of 115 effectively constant (zero variance, or one value in >99% of patients); 105 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 59 of 115
RESULT: univariate: 59 of 115 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.AortDist                              0.5786   0.5111   0.5704  <-
  smart_baseline.mht_alln                              0.5732   0.4869   0.5718  <-
  smart_baseline.vgt_hart                              0.5706   0.5706   0.5668  <-
  smart_baseline.roken                                 0.5674   0.4963   0.5393  <-
  smart_baseline.pamid                                 0.5657   0.4343   0.5542  <-
  smart_baseline.mas01                                 0.5657   0.4343   0.5542  <-
  smart_baseline.aorta_hg                              0.5653   0.5516   0.5586  <-
  smart_baseline.vz_hart                               0.5646   0.5646   0.5697  <-
  smart_baseline.mht_all                               0.5629   0.4371   0.5520  <-
  smart_baseline.nrfaln_n                              0.5623   0.5623   0.5562  <-

  115 features are only ~73 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~4 times, not ~6.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 17 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7464  val C=0.7694
  penalizer=0.1      train C=0.7251  val C=0.7507
  penalizer=1        train C=0.7237  val C=0.7479
  penalizer=10       train C=0.7237  val C=0.7479
  penalizer=100      train C=0.7237  val C=0.7479

  selected penalizer=0.01 -> TEST C=0.7351 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7351 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:41:34Z | screen: HR_chart_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 60 of 113 features clear the 0.0192 floor; strongest smart_baseline.stenACIl C=0.6420
- RESULT: COX lasso penalizer=0.01 TEST C=0.7373 (2-SE band +/-0.051) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_full/
  representation=matched_baseline[group:chart] | landmark_days=180 | horizon_days=5475 | n_features=113

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=  113 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=  113 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=  113 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 17 of 113 effectively constant (zero variance, or one value in >99% of patients); 104 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 60 of 113
RESULT: univariate: 60 of 113 features clear the 0.0192 floor; strongest smart_baseline.stenACIl C=0.6420
  feature                                              C_mono   C_udev   C_test
  smart_baseline.stenACIl                              0.6420   0.4527   0.6366  <-
  smart_baseline.stenACIr                              0.6400   0.4695   0.6362  <-
  smart_baseline.KliMaYr                               0.3911   0.6273   0.3690  <-
  smart_baseline.KliMaC                                0.6167   0.5834   0.6130  <-
  smart_baseline.packyrs                               0.6066   0.5515   0.6065  <-
  smart_baseline.KliMaDur                              0.6061   0.6061   0.6164  <-
  smart_baseline.klinman                               0.5993   0.4007   0.6087  <-
  smart_baseline.KliMaDrD                              0.5971   0.5971   0.6097  <-
  smart_baseline.pa_stolmid                            0.5876   0.4124   0.5885  <-
  smart_baseline.AortDist                              0.5811   0.5061   0.5730  <-
  smart_baseline.mht_alln                              0.5736   0.5356   0.5767  <-
  smart_baseline.vgt_hart                              0.5718   0.5718   0.5763  <-
  smart_baseline.roken                                 0.5654   0.4970   0.5565  <-
  smart_baseline.aorta_hg                              0.5648   0.5528   0.5563  <-
  smart_baseline.nrfaln_n                              0.5638   0.5638   0.5600  <-
  smart_baseline.vz_hart                               0.5635   0.5635   0.5794  <-
  smart_baseline.vaatzkt1                              0.4456   0.5622   0.4616  <-
  smart_baseline.pamid                                 0.5612   0.4388   0.5547  <-
  smart_baseline.mas01                                 0.5612   0.4388   0.5547  <-
  smart_baseline.aorta_gm                              0.5612   0.5385   0.5473  <-

  113 features are only ~73 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~4 times, not ~6.

--- best feature train vs test: smart_baseline.stenACIl ---
  train C=0.6420  test C=0.6366

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 17 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7345  val C=0.7452
  penalizer=0.1      train C=0.7142  val C=0.7314
  penalizer=1        train C=0.7135  val C=0.7298
  penalizer=10       train C=0.7135  val C=0.7298
  penalizer=100      train C=0.7135  val C=0.7298

  selected penalizer=0.01 -> TEST C=0.7373 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7373 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-09-08T08:43:25Z | screen: HR_chart_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 57 of 113 features clear the 0.0203 floor; strongest smart_baseline.stenACIl C=0.6471
- RESULT: COX lasso penalizer=0.01 TEST C=0.7310 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_rt/
  representation=matched_baseline[group:chart] | landmark_days=180 | horizon_days=5475 | n_features=113

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  113 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  113 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  113 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 17 of 113 effectively constant (zero variance, or one value in >99% of patients); 104 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 57 of 113
RESULT: univariate: 57 of 113 features clear the 0.0203 floor; strongest smart_baseline.stenACIl C=0.6471
  feature                                              C_mono   C_udev   C_test
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.AortDist                              0.5786   0.5111   0.5704  <-
  smart_baseline.mht_alln                              0.5732   0.4869   0.5718  <-
  smart_baseline.vgt_hart                              0.5706   0.5706   0.5668  <-
  smart_baseline.roken                                 0.5674   0.4963   0.5393  <-
  smart_baseline.pamid                                 0.5657   0.4343   0.5542  <-
  smart_baseline.mas01                                 0.5657   0.4343   0.5542  <-
  smart_baseline.aorta_hg                              0.5653   0.5516   0.5586  <-
  smart_baseline.vz_hart                               0.5646   0.5646   0.5697  <-
  smart_baseline.mht_all                               0.5629   0.4371   0.5520  <-
  smart_baseline.nrfaln_n                              0.5623   0.5623   0.5562  <-
  smart_baseline.csten_50                              0.5609   0.5609   0.5716  <-

  113 features are only ~72 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~4 times, not ~6.

--- best feature train vs test: smart_baseline.stenACIl ---
  train C=0.6471  test C=0.6440

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 17 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7388  val C=0.7543
  penalizer=0.1      train C=0.7181  val C=0.7431
  penalizer=1        train C=0.7174  val C=0.7410
  penalizer=10       train C=0.7174  val C=0.7410
  penalizer=100      train C=0.7174  val C=0.7410

  selected penalizer=0.01 -> TEST C=0.7310 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7310 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:44:41Z | screen: HR_chartstrict_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chartstrict_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 43 of 96 features clear the 0.0203 floor; strongest smart_baseline.KliMaYr C=0.3855
- RESULT: COX lasso penalizer=0.01 TEST C=0.7024 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chartstrict_rt/
  representation=matched_baseline[group:chart_strict] | landmark_days=180 | horizon_days=5475 | n_features=96

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   96 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   96 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   96 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 17 of 96 effectively constant (zero variance, or one value in >99% of patients); 90 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 43 of 96
RESULT: univariate: 43 of 96 features clear the 0.0203 floor; strongest smart_baseline.KliMaYr C=0.3855
  feature                                              C_mono   C_udev   C_test
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.mht_alln                              0.5732   0.4869   0.5718  <-
  smart_baseline.vgt_hart                              0.5706   0.5706   0.5668  <-
  smart_baseline.roken                                 0.5674   0.4963   0.5393  <-
  smart_baseline.pamid                                 0.5657   0.4343   0.5542  <-
  smart_baseline.mas01                                 0.5657   0.4343   0.5542  <-
  smart_baseline.vz_hart                               0.5646   0.5646   0.5697  <-
  smart_baseline.mht_all                               0.5629   0.4371   0.5520  <-
  smart_baseline.aspirine                              0.5587   0.4413   0.5550  <-
  smart_baseline.vg_0321                               0.5584   0.5584   0.5667  <-
  smart_baseline.vaatzkt1                              0.4435   0.5573   0.4621  <-
  smart_baseline.alcohol                               0.4464   0.5536   0.4218  <-
  smart_baseline.vz_hypt                               0.5473   0.4527   0.5463  <-
  smart_baseline.diagnsco                              0.5473   0.4763   0.5553  <-

  96 features are only ~62 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~3 times, not ~5.

--- best feature train vs test: smart_baseline.KliMaYr ---
  train C=0.3855  test C=0.3741

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 17 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7179  val C=0.7149
  penalizer=0.1      train C=0.6899  val C=0.6886
  penalizer=1        train C=0.6896  val C=0.6880
  penalizer=10       train C=0.6896  val C=0.6880
  penalizer=100      train C=0.6896  val C=0.6880

  selected penalizer=0.01 -> TEST C=0.7024 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7024 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:45:43Z | screen: HR_protocol_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 46 of 70 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7198 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_demo_rt/
  representation=matched_baseline[group:protocol,leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=70

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   70 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   70 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   70 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 70 effectively constant (zero variance, or one value in >99% of patients); 34 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 46 of 70
RESULT: univariate: 46 of 70 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-
  smart_baseline.bdsys                                 0.5812   0.5331   0.5546  <-
  smart_baseline.kl8alggz                              0.4233   0.4794   0.4609  <-
  smart_baseline.labmalb                               0.5763   0.5687   0.5890  <-
  smart_baseline.MBSc                                  0.5695   0.5356   0.5828  <-
  smart_baseline.MBSc_mis                              0.5693   0.5176   0.5814  <-
  smart_baseline.labkrur                               0.4317   0.4826   0.4505  <-
  smart_baseline.bwMEThw                               0.4353   0.5232   0.3907  <-
  smart_baseline.vet_gm                                0.5643   0.4895   0.5807  <-
  smart_baseline.labhba1c                              0.5637   0.4858   0.5502  <-

  70 features are only ~49 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~4.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7399  val C=0.7589
  penalizer=0.1      train C=0.7229  val C=0.7322
  penalizer=1        train C=0.7218  val C=0.7296
  penalizer=10       train C=0.7218  val C=0.7296
  penalizer=100      train C=0.7218  val C=0.7296

  selected penalizer=0.01 -> TEST C=0.7198 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7198 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:46:33Z | screen: HR_protocol_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 44 of 68 features clear the 0.0192 floor; strongest smart_baseline.klar_coc C=0.3634
- RESULT: COX lasso penalizer=0.01 TEST C=0.7288 (2-SE band +/-0.051) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_full/
  representation=matched_baseline[group:protocol] | landmark_days=180 | horizon_days=5475 | n_features=68

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=   68 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=   68 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=   68 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 4 of 68 effectively constant (zero variance, or one value in >99% of patients); 33 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 44 of 68
RESULT: univariate: 44 of 68 features clear the 0.0192 floor; strongest smart_baseline.klar_coc C=0.3634
  feature                                              C_mono   C_udev   C_test
  smart_baseline.klar_coc                              0.3634   0.5533   0.3635  <-
  smart_baseline.labkrea                               0.6168   0.5805   0.6285  <-
  smart_baseline.MDRD                                  0.3885   0.5841   0.3685  <-
  smart_baseline.plsprs                                0.6089   0.5658   0.5976  <-
  smart_baseline.klar_gst                              0.3916   0.6084   0.3914  <-
  smart_baseline.kl1fysfc                              0.4025   0.5132   0.4178  <-
  smart_baseline.labcrp                                0.5948   0.5819   0.6062  <-
  smart_baseline.mpkr_rat                              0.5912   0.5683   0.5868  <-
  smart_baseline.labhcyst                              0.5883   0.5481   0.5994  <-
  smart_baseline.kl8alggz                              0.4231   0.4845   0.4595  <-
  smart_baseline.abivrl_n                              0.5766   0.5766   0.5900  <-
  smart_baseline.bdsys                                 0.5747   0.5297   0.5646  <-
  smart_baseline.labmalb                               0.5691   0.5667   0.5870  <-
  smart_baseline.MBSc                                  0.5672   0.5231   0.5799  <-
  smart_baseline.MBSc_mis                              0.5666   0.5404   0.5793  <-
  smart_baseline.tail_gm                               0.5625   0.4797   0.5798  <-
  smart_baseline.vet_gm                                0.5619   0.4892   0.5760  <-
  smart_baseline.labgluc                               0.5614   0.5346   0.5854  <-
  smart_baseline.labkrur                               0.4393   0.4823   0.4429  <-
  smart_baseline.kl7pijn                               0.4411   0.4917   0.4884  <-

  68 features are only ~48 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~3.

--- best feature train vs test: smart_baseline.klar_coc ---
  train C=0.3634  test C=0.3635

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7195  val C=0.7360
  penalizer=0.1      train C=0.7036  val C=0.7170
  penalizer=1        train C=0.7030  val C=0.7158
  penalizer=10       train C=0.7030  val C=0.7158
  penalizer=100      train C=0.7030  val C=0.7158

  selected penalizer=0.01 -> TEST C=0.7288 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7288 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-09-08T08:47:45Z | screen: HR_protocol_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 44 of 68 features clear the 0.0203 floor; strongest smart_baseline.klar_coc C=0.3625
- RESULT: COX lasso penalizer=0.01 TEST C=0.7196 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_rt/
  representation=matched_baseline[group:protocol] | landmark_days=180 | horizon_days=5475 | n_features=68

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   68 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   68 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   68 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 68 effectively constant (zero variance, or one value in >99% of patients); 33 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 44 of 68
RESULT: univariate: 44 of 68 features clear the 0.0203 floor; strongest smart_baseline.klar_coc C=0.3625
  feature                                              C_mono   C_udev   C_test
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-
  smart_baseline.bdsys                                 0.5812   0.5331   0.5546  <-
  smart_baseline.kl8alggz                              0.4233   0.4794   0.4609  <-
  smart_baseline.labmalb                               0.5763   0.5687   0.5890  <-
  smart_baseline.MBSc                                  0.5695   0.5356   0.5828  <-
  smart_baseline.MBSc_mis                              0.5693   0.5176   0.5814  <-
  smart_baseline.labkrur                               0.4317   0.4826   0.4505  <-
  smart_baseline.bwMEThw                               0.4353   0.5232   0.3907  <-
  smart_baseline.vet_gm                                0.5643   0.4895   0.5807  <-
  smart_baseline.labhba1c                              0.5637   0.4858   0.5502  <-
  smart_baseline.tail_gm                               0.5634   0.4783   0.5792  <-

  68 features are only ~48 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~3.

--- best feature train vs test: smart_baseline.klar_coc ---
  train C=0.3625  test C=0.3636

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7244  val C=0.7366
  penalizer=0.1      train C=0.7111  val C=0.7182
  penalizer=1        train C=0.7104  val C=0.7163
  penalizer=10       train C=0.7104  val C=0.7163
  penalizer=100      train C=0.7104  val C=0.7163

  selected penalizer=0.01 -> TEST C=0.7196 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7196 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:48:34Z | screen: INCR_concepts_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_concepts_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 103 of 222 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7397 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_concepts_full/
  representation=text_concepts[binary/disease,symptom]+baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=222

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  222 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  222 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  222 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 29 of 222 effectively constant (zero variance, or one value in >99% of patients); 177 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 103 of 222
RESULT: univariate: 103 of 222 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-

  222 features are only ~152 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~8 times, not ~11.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 29 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7631  val C=0.7772
  penalizer=0.1      train C=0.7504  val C=0.7672
  penalizer=1        train C=0.7499  val C=0.7653
  penalizer=10       train C=0.7499  val C=0.7653
  penalizer=100      train C=0.7499  val C=0.7653

  selected penalizer=0.01 -> TEST C=0.7397 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7397 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:52:03Z | screen: INCR_tfidf_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_tfidf_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 123 of 439 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7388 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_tfidf_full/
  representation=text_tfidf[word]+baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=439

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  439 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  439 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  439 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 21 of 439 effectively constant (zero variance, or one value in >99% of patients); 138 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 123 of 439
RESULT: univariate: 123 of 439 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-

  439 features are only ~345 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~17 times, not ~22.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 21 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7655  val C=0.7754
  penalizer=0.1      train C=0.7561  val C=0.7674
  penalizer=1        train C=0.7560  val C=0.7659
  penalizer=10       train C=0.7560  val C=0.7659
  penalizer=100      train C=0.7560  val C=0.7659

  selected penalizer=0.01 -> TEST C=0.7388 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7388 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T08:59:16Z | screen: INCR_volume_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_volume_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 103 of 192 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_volume_full/
  representation=text_volume+baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=192

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  192 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  192 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  192 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 21 of 192 effectively constant (zero variance, or one value in >99% of patients); 140 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 103 of 192
RESULT: univariate: 103 of 192 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.stenACIl                              0.6471   0.4491   0.6440  <-
  smart_baseline.stenACIr                              0.6468   0.4587   0.6293  <-
  smart_baseline.klar_coc                              0.3625   0.5487   0.3636  <-
  smart_baseline.KliMaYr                               0.3855   0.6313   0.3741  <-
  smart_baseline.labkrea                               0.6233   0.5751   0.6288  <-
  smart_baseline.packyrs                               0.6182   0.5666   0.5803  <-
  smart_baseline.MDRD                                  0.3839   0.5847   0.3614  <-
  smart_baseline.KliMaC                                0.6138   0.5788   0.6026  <-
  smart_baseline.plsprs                                0.6123   0.5453   0.5835  <-
  smart_baseline.KliMaDur                              0.6078   0.6078   0.6128  <-
  smart_baseline.klar_gst                              0.3951   0.6049   0.3981  <-
  smart_baseline.kl1fysfc                              0.4000   0.5048   0.4253  <-
  smart_baseline.klinman                               0.5988   0.4012   0.6088  <-
  smart_baseline.KliMaDrD                              0.5976   0.5976   0.6075  <-
  smart_baseline.labhcyst                              0.5969   0.5594   0.6063  <-
  smart_baseline.mpkr_rat                              0.5957   0.5619   0.5807  <-
  smart_baseline.pa_stolmid                            0.5935   0.4065   0.5840  <-
  smart_baseline.labcrp                                0.5838   0.5858   0.6028  <-
  smart_baseline.abivrl_n                              0.5839   0.5839   0.5878  <-

  192 features are only ~124 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~6 times, not ~10.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 21 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7629  val C=0.7770
  penalizer=0.1      train C=0.7493  val C=0.7672
  penalizer=1        train C=0.7488  val C=0.7653
  penalizer=10       train C=0.7488  val C=0.7653
  penalizer=100      train C=0.7488  val C=0.7653

  selected penalizer=0.01 -> TEST C=0.7394 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T09:02:04Z | screen: SENS_no_omschr

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/SENS_no_omschr/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 532 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
- RESULT: COX lasso penalizer=0.01 TEST C=0.6884 (2-SE band +/-0.051) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/SENS_no_omschr/
  representation=pivoted_events+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | aggregators=['last', 'mean', 'slope', 'count'] | min_patients=860 | n_features=532

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=  532 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=  532 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=  532 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 12 of 532 effectively constant (zero variance, or one value in >99% of patients); 89 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 2 of 532
RESULT: univariate: 2 of 532 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6742   0.5139   0.6839  <-
  smart_baseline.geslacht                              0.4448   0.4448   0.4528  <-
  meting_20251203.label.gewicht_mean                   0.4925   0.5175   0.5034
  ecg_measmatrix_20251208.wide.T_Offset_slope          0.4833   0.5052   0.5063
  meting_20251203.label.gewicht_last                   0.4934   0.5162   0.5024
  hos_mut_20251209.specialisme_omschrijving.cardiolo   0.4838   0.4838   0.4921
  meting_20251203.label.gewicht_slope                  0.5028   0.5158   0.4871
  meting_20251203.label.hr_last                        0.4865   0.4983   0.5126
  echo_20250626.MeasName_ECHO.lv_mass(c)di_last        0.5132   0.4993   0.4891
  ecg_measmatrix_20251208.wide.P_Onset_last            0.4992   0.4869   0.5006
  lab_ezis_20250709.lab_testcode.creat-bl_mean         0.5130   0.5015   0.4947
  ecg_measmatrix_20251208.wide.QT_Interval_mean        0.5130   0.5102   0.5007
  hos_mut_20251209.wide.hos_duur_mean                  0.5031   0.4873   0.4983
  lab_ezis_20250709.lab_testcode.creat-up_last         0.4902   0.5124   0.4978
  meting_20251203.label.gewicht_count                  0.5122   0.4940   0.5075
  meting_20251203.eenheid.kg_count                     0.5122   0.4940   0.5075
  meting_20251203.Omschrijving.gewicht_count           0.5122   0.4940   0.5075
  lab_ezis_20250709.lab_testcode.kalium-bl_last        0.5120   0.4988   0.4845
  meting_20251203.SOURCETYPE.k_count                   0.5120   0.4982   0.5083
  lab_ezis_20250709.lab_testcode.asat-bl_last          0.4883   0.5019   0.5050

  532 features are only ~183 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~9 times, not ~27.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6742  test C=0.6839

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 12 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6820  val C=0.7112
  penalizer=0.1      train C=0.6401  val C=0.5963
  penalizer=1        train C=0.6302  val C=0.5835
  penalizer=10       train C=0.6302  val C=0.5834
  penalizer=100      train C=0.6302  val C=0.5834

  selected penalizer=0.01 -> TEST C=0.6884 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6884 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-09-08T09:17:04Z | screen: STRUCT_ctrl

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/STRUCT_ctrl/ cox=True l1_ratio=1.0
- RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
- RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/STRUCT_ctrl/
  representation=smart_baseline[all] | landmark_days=180 | horizon_days=5475 | aggregators=[] | min_patients=860 | n_features=183

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=  183 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=  183 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=  183 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 21 of 183 effectively constant (zero variance, or one value in >99% of patients); 138 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 106 of 183
RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6742   0.5139   0.6839  <-
  smart_baseline.stenACIl                              0.6420   0.4527   0.6366  <-
  smart_baseline.stenACIr                              0.6400   0.4695   0.6362  <-
  smart_baseline.klar_coc                              0.3634   0.5533   0.3635  <-
  smart_baseline.KliMaYr                               0.3911   0.6273   0.3690  <-
  smart_baseline.labkrea                               0.6168   0.5805   0.6285  <-
  smart_baseline.KliMaC                                0.6167   0.5834   0.6130  <-
  smart_baseline.MDRD                                  0.3885   0.5841   0.3685  <-
  smart_baseline.plsprs                                0.6089   0.5658   0.5976  <-
  smart_baseline.klar_gst                              0.3916   0.6084   0.3914  <-
  smart_baseline.packyrs                               0.6066   0.5515   0.6065  <-
  smart_baseline.KliMaDur                              0.6061   0.6061   0.6164  <-
  smart_baseline.klinman                               0.5993   0.4007   0.6087  <-
  smart_baseline.kl1fysfc                              0.4025   0.5132   0.4178  <-
  smart_baseline.KliMaDrD                              0.5971   0.5971   0.6097  <-
  smart_baseline.labcrp                                0.5948   0.5819   0.6062  <-
  smart_baseline.mpkr_rat                              0.5912   0.5683   0.5868  <-
  smart_baseline.labhcyst                              0.5883   0.5481   0.5994  <-
  smart_baseline.pa_stolmid                            0.5876   0.4124   0.5885  <-
  smart_baseline.AortDist                              0.5811   0.5061   0.5730  <-

  183 features are only ~119 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~6 times, not ~9.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6742  test C=0.6839

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 21 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7585  val C=0.7789
  penalizer=0.1      train C=0.7433  val C=0.7588
  penalizer=1        train C=0.7425  val C=0.7574
  penalizer=10       train C=0.7425  val C=0.7574
  penalizer=100      train C=0.7425  val C=0.7574

  selected penalizer=0.01 -> TEST C=0.7576 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-09-08T09:19:30Z | screen: T0_volume

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 9 features clear the 0.0192 floor
- RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume/
  representation=text_volume | landmark_days=180 | horizon_days=5475 | n_features=9

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=    9 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=    9 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=    9 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 0 of 9 effectively constant (zero variance, or one value in >99% of patients); 2 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 9
RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  feature                                              C_mono   C_udev   C_test
  text.recency                                         0.4894   0.4955   0.4756
  text.n_chars                                         0.4995   0.4952   0.4839
  text.n_docs[mri_verslag_20250626]                    0.4954   0.4954   0.4958
  text.n_docs[radiologie_verslag_20251208]             0.5039   0.4957   0.4866
  text.history_span                                    0.4958   0.4975   0.5010
  text.n_documents                                     0.5004   0.5037   0.4831
  text.n_sources                                       0.5036   0.5009   0.4830
  text.n_docs[uitgaandebrief_20251208]                 0.5007   0.5007   0.4804
  text.n_docs[consult_20251208]                        0.4997   0.4997   0.4852

  9 features are only ~6 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~0 times, not ~0.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.4993  val C=0.5108
  penalizer=0.1      train C=0.4995  val C=0.5106
  penalizer=1        train C=0.4995  val C=0.5106
  penalizer=10       train C=0.4995  val C=0.5106
  penalizer=100      train C=0.4995  val C=0.5106

  selected penalizer=0.01 -> TEST C=0.5202 (test 2-SE band around 0.5 is +/-0.051)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:20:04Z | screen: T0_volume_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 9 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume_rt/
  representation=text_volume | landmark_days=180 | horizon_days=5475 | n_features=9

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=    9 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=    9 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=    9 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 9 effectively constant (zero variance, or one value in >99% of patients); 2 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 9
RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  text.recency                                         0.4881   0.4854   0.4734
  text.history_span                                    0.4985   0.4895   0.4985
  text.n_docs[radiologie_verslag_20251208]             0.5005   0.4929   0.4894
  text.n_documents                                     0.4953   0.4930   0.4827
  text.n_docs[mri_verslag_20250626]                    0.4934   0.4934   0.4945
  text.n_chars                                         0.4935   0.4971   0.4842
  text.n_docs[consult_20251208]                        0.4955   0.4953   0.4816
  text.n_sources                                       0.5013   0.5013   0.4825
  text.n_docs[uitgaandebrief_20251208]                 0.4996   0.4996   0.4742

  9 features are only ~6 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~0 times, not ~0.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5058  val C=0.4875
  penalizer=0.1      train C=0.5043  val C=0.4853
  penalizer=1        train C=0.5043  val C=0.4852
  penalizer=10       train C=0.5043  val C=0.4852
  penalizer=100      train C=0.5043  val C=0.4852

  selected penalizer=0.01 -> TEST C=0.5197 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:20:28Z | screen: T1_tfidf_3src

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_3src/ cox=True l1_ratio=1.0
- RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
- RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_3src/
  representation=text_tfidf[word] | landmark_days=180 | horizon_days=5475 | n_features=256

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  256 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  256 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  256 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 256 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 27 of 256
RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_123                                        0.4640   0.5048   0.5093  <-
  tfidf.svd_65                                         0.4681   0.5127   0.5034  <-
  tfidf.svd_237                                        0.5293   0.4915   0.5051  <-
  tfidf.svd_106                                        0.5058   0.5282   0.5070  <-
  tfidf.svd_187                                        0.4926   0.4732   0.4638  <-
  tfidf.svd_61                                         0.5111   0.5268   0.4685  <-
  tfidf.svd_174                                        0.5104   0.5255   0.4863  <-
  tfidf.svd_159                                        0.5253   0.5106   0.4812  <-
  tfidf.svd_141                                        0.5059   0.5250   0.4813  <-
  tfidf.svd_87                                         0.4755   0.4959   0.5215  <-
  tfidf.svd_148                                        0.4849   0.5244   0.5044  <-
  tfidf.svd_60                                         0.5062   0.5239   0.4892  <-
  tfidf.svd_98                                         0.5238   0.5041   0.5134  <-
  tfidf.svd_191                                        0.5050   0.4767   0.4922  <-
  tfidf.svd_52                                         0.5060   0.5233   0.5063  <-
  tfidf.svd_251                                        0.4768   0.5009   0.4767  <-
  tfidf.svd_128                                        0.4773   0.5174   0.4913  <-
  tfidf.svd_92                                         0.4997   0.5226   0.4924  <-
  tfidf.svd_183                                        0.5221   0.4824   0.4975  <-
  tfidf.svd_188                                        0.5056   0.4781   0.4714  <-

  256 features are only ~242 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~12 times, not ~13.

--- best feature train vs test: tfidf.svd_123 ---
  train C=0.4640  test C=0.5093

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5727  val C=0.4758
  penalizer=0.1      train C=0.6556  val C=0.5019
  penalizer=1        train C=0.6556  val C=0.5019
  penalizer=10       train C=0.6556  val C=0.5019
  penalizer=100      train C=0.6556  val C=0.5019

  selected penalizer=0.1 -> TEST C=0.4907 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:25:21Z | screen: T1_tfidf_char

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_char/ cox=True l1_ratio=1.0
- RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
- RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_char/
  representation=text_tfidf[char] | landmark_days=180 | horizon_days=5475 | n_features=256

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  256 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  256 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  256 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 256 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 30 of 256
RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_153                                        0.5076   0.5319   0.5003  <-
  tfidf.svd_228                                        0.4686   0.5190   0.5100  <-
  tfidf.svd_71                                         0.5004   0.4692   0.5022  <-
  tfidf.svd_60                                         0.4891   0.5305   0.4788  <-
  tfidf.svd_131                                        0.4701   0.5017   0.5149  <-
  tfidf.svd_123                                        0.5049   0.4703   0.5199  <-
  tfidf.svd_144                                        0.5165   0.5295   0.5002  <-
  tfidf.svd_109                                        0.5276   0.4882   0.5039  <-
  tfidf.svd_73                                         0.5249   0.5143   0.4898  <-
  tfidf.svd_61                                         0.5083   0.4752   0.5133  <-
  tfidf.svd_193                                        0.5173   0.5247   0.5019  <-
  tfidf.svd_189                                        0.4758   0.5051   0.5289  <-
  tfidf.svd_167                                        0.5240   0.5018   0.4850  <-
  tfidf.svd_180                                        0.5237   0.4889   0.4732  <-
  tfidf.svd_233                                        0.5118   0.5235   0.4921  <-
  tfidf.svd_66                                         0.4766   0.5052   0.5017  <-
  tfidf.svd_214                                        0.5053   0.4766   0.5270  <-
  tfidf.svd_101                                        0.4773   0.4825   0.4863  <-
  tfidf.svd_67                                         0.5226   0.5124   0.4797  <-
  tfidf.svd_40                                         0.5223   0.5065   0.5136  <-

  256 features are only ~242 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~12 times, not ~13.

--- best feature train vs test: tfidf.svd_153 ---
  train C=0.5076  test C=0.5003

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5707  val C=0.5396
  penalizer=0.1      train C=0.6653  val C=0.5205
  penalizer=1        train C=0.6653  val C=0.5205
  penalizer=10       train C=0.6653  val C=0.5205
  penalizer=100      train C=0.6653  val C=0.5205

  selected penalizer=0.01 -> TEST C=0.4963 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:30:15Z | screen: T1_tfidf_conclusie

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_conclusie/ cox=True l1_ratio=1.0
- RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
- RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_conclusie/
  representation=text_tfidf[word]+section:conclusie | landmark_days=180 | horizon_days=5475 | n_features=128

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  128 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  128 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  128 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 128 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 6 of 128
RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_31                                         0.4720   0.5030   0.4920  <-
  tfidf.svd_65                                         0.5243   0.5062   0.5198  <-
  tfidf.svd_15                                         0.4766   0.5011   0.5064  <-
  tfidf.svd_112                                        0.4773   0.5045   0.4865  <-
  tfidf.svd_26                                         0.5210   0.5029   0.5106  <-
  tfidf.svd_120                                        0.4794   0.4996   0.4903  <-
  tfidf.svd_124                                        0.5200   0.5008   0.5018
  tfidf.svd_126                                        0.4804   0.5009   0.5018
  tfidf.svd_3                                          0.5180   0.4988   0.4791
  tfidf.svd_62                                         0.5179   0.4929   0.5160
  tfidf.svd_50                                         0.4828   0.4993   0.4983
  tfidf.svd_24                                         0.4828   0.5037   0.5099
  tfidf.svd_71                                         0.5169   0.4970   0.4982
  tfidf.svd_38                                         0.5169   0.5008   0.5002
  tfidf.svd_1                                          0.5052   0.4835   0.5167
  tfidf.svd_109                                        0.4838   0.5036   0.4902
  tfidf.svd_52                                         0.5162   0.4979   0.4690
  tfidf.svd_119                                        0.4840   0.4956   0.4910
  tfidf.svd_85                                         0.4844   0.5022   0.5095
  tfidf.svd_64                                         0.4844   0.4993   0.5043

  128 features are only ~121 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~6 times, not ~6.

--- best feature train vs test: tfidf.svd_31 ---
  train C=0.4720  test C=0.4920

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5388  val C=0.5082
  penalizer=0.1      train C=0.5948  val C=0.5051
  penalizer=1        train C=0.5948  val C=0.5052
  penalizer=10       train C=0.5948  val C=0.5052
  penalizer=100      train C=0.5948  val C=0.5052

  selected penalizer=0.01 -> TEST C=0.5089 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:31:54Z | screen: T1_tfidf_demo

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_demo/ cox=True l1_ratio=1.0
- RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_demo/
  representation=text_tfidf[word]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=258

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  258 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  258 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  258 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 258 effectively constant (zero variance, or one value in >99% of patients); 1 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 22 of 258
RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.geslacht                              0.4422   0.4422   0.4587  <-
  tfidf.svd_123                                        0.4680   0.4891   0.5186  <-
  tfidf.svd_65                                         0.4706   0.5084   0.5159  <-
  tfidf.svd_93                                         0.5032   0.5287   0.5025  <-
  tfidf.svd_251                                        0.4721   0.5091   0.4794  <-
  tfidf.svd_84                                         0.4834   0.5253   0.5068  <-
  tfidf.svd_177                                        0.5251   0.5014   0.4960  <-
  tfidf.svd_237                                        0.5245   0.4806   0.4802  <-
  tfidf.svd_87                                         0.4759   0.4956   0.5244  <-
  tfidf.svd_55                                         0.4926   0.5240   0.4896  <-
  tfidf.svd_106                                        0.4925   0.5232   0.5053  <-
  tfidf.svd_35                                         0.4965   0.5231   0.5149  <-
  tfidf.svd_61                                         0.4995   0.5228   0.4755  <-
  tfidf.svd_241                                        0.5220   0.5043   0.5279  <-
  tfidf.svd_222                                        0.5103   0.4782   0.5098  <-
  tfidf.svd_114                                        0.5211   0.5021   0.5248  <-
  tfidf.svd_26                                         0.5211   0.4900   0.4933  <-
  tfidf.svd_212                                        0.5210   0.4918   0.5270  <-
  tfidf.svd_139                                        0.5208   0.5059   0.5205  <-

  258 features are only ~243 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~12 times, not ~13.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.6839  val C=0.7058
  penalizer=0.1      train C=0.7299  val C=0.6658
  penalizer=1        train C=0.7292  val C=0.6521
  penalizer=10       train C=0.7292  val C=0.6520
  penalizer=100      train C=0.7292  val C=0.6520

  selected penalizer=0.01 -> TEST C=0.6750 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T09:37:07Z | screen: T1_tfidf_history

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_history/ cox=True l1_ratio=1.0
- RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
- RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_history/
  representation=text_tfidf[word]+section:voorgeschiedenis,anamnese | landmark_days=180 | horizon_days=5475 | n_features=128

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  128 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  128 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  128 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 128 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 7 of 128
RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_53                                         0.4708   0.4895   0.5294  <-
  tfidf.svd_3                                          0.5265   0.4872   0.5230  <-
  tfidf.svd_45                                         0.4737   0.4945   0.5242  <-
  tfidf.svd_117                                        0.5248   0.4923   0.5044  <-
  tfidf.svd_109                                        0.4788   0.4891   0.4891  <-
  tfidf.svd_119                                        0.5208   0.4951   0.4734  <-
  tfidf.svd_125                                        0.4793   0.4937   0.5150  <-
  tfidf.svd_21                                         0.5191   0.4897   0.4871
  tfidf.svd_29                                         0.4916   0.4815   0.5146
  tfidf.svd_69                                         0.5182   0.4877   0.4959
  tfidf.svd_28                                         0.5020   0.4820   0.5290
  tfidf.svd_23                                         0.5178   0.4977   0.4918
  tfidf.svd_118                                        0.5175   0.4976   0.4630
  tfidf.svd_126                                        0.4826   0.5012   0.4827
  tfidf.svd_5                                          0.4827   0.4969   0.4830
  tfidf.svd_78                                         0.5168   0.4957   0.5091
  tfidf.svd_39                                         0.4832   0.4921   0.5016
  tfidf.svd_64                                         0.4837   0.4897   0.5102
  tfidf.svd_14                                         0.5160   0.4958   0.5014
  tfidf.svd_67                                         0.4932   0.4848   0.5120

  128 features are only ~121 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~6 times, not ~6.

--- best feature train vs test: tfidf.svd_53 ---
  train C=0.4708  test C=0.5294

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5300  val C=0.4855
  penalizer=0.1      train C=0.5931  val C=0.4756
  penalizer=1        train C=0.5932  val C=0.4756
  penalizer=10       train C=0.5932  val C=0.4756
  penalizer=100      train C=0.5932  val C=0.4756

  selected penalizer=0.01 -> TEST C=0.4897 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:38:46Z | screen: T1_tfidf_nonames

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_nonames/ cox=True l1_ratio=1.0
- RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
- RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_nonames/
  representation=text_tfidf[word] | landmark_days=180 | horizon_days=5475 | n_features=256

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  256 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  256 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  256 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 256 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 24 of 256
RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_28                                         0.4675   0.4968   0.5039  <-
  tfidf.svd_129                                        0.5306   0.5041   0.4624  <-
  tfidf.svd_176                                        0.5288   0.4994   0.4773  <-
  tfidf.svd_163                                        0.5285   0.5043   0.4885  <-
  tfidf.svd_119                                        0.4719   0.5189   0.5155  <-
  tfidf.svd_115                                        0.5045   0.5263   0.4953  <-
  tfidf.svd_95                                         0.5252   0.5019   0.5089  <-
  tfidf.svd_70                                         0.5239   0.5074   0.5179  <-
  tfidf.svd_255                                        0.5237   0.4823   0.5131  <-
  tfidf.svd_250                                        0.5229   0.5074   0.5236  <-
  tfidf.svd_100                                        0.5104   0.5228   0.4905  <-
  tfidf.svd_55                                         0.4910   0.5226   0.4746  <-
  tfidf.svd_56                                         0.5223   0.4935   0.4669  <-
  tfidf.svd_156                                        0.5220   0.5065   0.5250  <-
  tfidf.svd_248                                        0.5216   0.4780   0.4993  <-
  tfidf.svd_17                                         0.4855   0.4782   0.4828  <-
  tfidf.svd_103                                        0.5217   0.5088   0.4854  <-
  tfidf.svd_235                                        0.4972   0.5216   0.4986  <-
  tfidf.svd_209                                        0.5103   0.4785   0.5184  <-
  tfidf.svd_135                                        0.4789   0.5057   0.4778  <-

  256 features are only ~242 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~12 times, not ~13.

--- best feature train vs test: tfidf.svd_28 ---
  train C=0.4675  test C=0.5039

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5605  val C=0.5430
  penalizer=0.1      train C=0.6573  val C=0.5009
  penalizer=1        train C=0.6573  val C=0.5009
  penalizer=10       train C=0.6573  val C=0.5009
  penalizer=100      train C=0.6573  val C=0.5009

  selected penalizer=0.01 -> TEST C=0.4821 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:43:46Z | screen: T1_tfidf_word

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word/ cox=True l1_ratio=1.0
- RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
- RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word/
  representation=text_tfidf[word] | landmark_days=180 | horizon_days=5475 | n_features=256

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  256 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  256 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  256 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 0 of 256 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 20 of 256
RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_123                                        0.4680   0.4891   0.5186  <-
  tfidf.svd_65                                         0.4706   0.5084   0.5159  <-
  tfidf.svd_93                                         0.5032   0.5287   0.5025  <-
  tfidf.svd_251                                        0.4721   0.5091   0.4794  <-
  tfidf.svd_84                                         0.4834   0.5253   0.5068  <-
  tfidf.svd_177                                        0.5251   0.5014   0.4960  <-
  tfidf.svd_237                                        0.5245   0.4806   0.4802  <-
  tfidf.svd_87                                         0.4759   0.4956   0.5244  <-
  tfidf.svd_55                                         0.4926   0.5240   0.4896  <-
  tfidf.svd_106                                        0.4925   0.5232   0.5053  <-
  tfidf.svd_35                                         0.4965   0.5231   0.5149  <-
  tfidf.svd_61                                         0.4995   0.5228   0.4755  <-
  tfidf.svd_241                                        0.5220   0.5043   0.5279  <-
  tfidf.svd_222                                        0.5103   0.4782   0.5098  <-
  tfidf.svd_114                                        0.5211   0.5021   0.5248  <-
  tfidf.svd_26                                         0.5211   0.4900   0.4933  <-
  tfidf.svd_212                                        0.5210   0.4918   0.5270  <-
  tfidf.svd_139                                        0.5208   0.5059   0.5205  <-
  tfidf.svd_210                                        0.5054   0.4794   0.4848  <-
  tfidf.svd_137                                        0.4881   0.5203   0.4832  <-

  256 features are only ~242 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~12 times, not ~13.

--- best feature train vs test: tfidf.svd_123 ---
  train C=0.4680  test C=0.5186

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5746  val C=0.5042
  penalizer=0.1      train C=0.6557  val C=0.5043
  penalizer=1        train C=0.6557  val C=0.5043
  penalizer=10       train C=0.6557  val C=0.5043
  penalizer=100      train C=0.6557  val C=0.5043

  selected penalizer=0.1 -> TEST C=0.4914 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:48:39Z | screen: T1_tfidf_word_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
- RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word_full/
  representation=text_tfidf[word] | landmark_days=180 | horizon_days=5475 | n_features=256

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 8,599 features=  256 events=1,136 (13.2%) duration p0/p50/p100 = 1/2999/5475
  validation  n= 2,141 features=  256 events=  310 (14.5%) duration p0/p50/p100 = 4/3096/5475
  test        n= 2,694 features=  256 events=  381 (14.1%) duration p0/p50/p100 = 3/2986/5475

  feature spread: 0 of 256 effectively constant (zero variance, or one value in >99% of patients); 0 take <=10 distinct values (normal for counts)

  permutation-calibrated null: SE(C) = 0.323/sqrt(events); 2-SE floor on train (1,136 events) = 0.0192
  (the analytic 0.5/sqrt(events) would give 0.0297 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 8 of 256
RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  feature                                              C_mono   C_udev   C_test
  tfidf.svd_209                                        0.5252   0.4965   0.5045  <-
  tfidf.svd_114                                        0.5248   0.4990   0.5256  <-
  tfidf.svd_238                                        0.5224   0.5044   0.4899  <-
  tfidf.svd_123                                        0.5223   0.5022   0.4924  <-
  tfidf.svd_60                                         0.5020   0.5222   0.5060  <-
  tfidf.svd_65                                         0.4783   0.5051   0.4769  <-
  tfidf.svd_177                                        0.5208   0.5030   0.5152  <-
  tfidf.svd_67                                         0.4797   0.5097   0.4759  <-
  tfidf.svd_87                                         0.4811   0.5003   0.5129
  tfidf.svd_159                                        0.4896   0.5181   0.5188
  tfidf.svd_132                                        0.4825   0.4945   0.4870
  tfidf.svd_255                                        0.4827   0.5102   0.4766
  tfidf.svd_250                                        0.4827   0.5041   0.5228
  tfidf.svd_125                                        0.5172   0.5010   0.5017
  tfidf.svd_3                                          0.4829   0.5023   0.4920
  tfidf.svd_234                                        0.5170   0.4964   0.5121
  tfidf.svd_12                                         0.5170   0.5057   0.5166
  tfidf.svd_83                                         0.5167   0.5052   0.5107
  tfidf.svd_131                                        0.4834   0.5128   0.4783
  tfidf.svd_231                                        0.4984   0.5162   0.5213

  256 features are only ~242 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~12 times, not ~13.

--- best feature train vs test: tfidf.svd_209 ---
  train C=0.5252  test C=0.5045

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5383  val C=0.5159
  penalizer=0.1      train C=0.6260  val C=0.5018
  penalizer=1        train C=0.6260  val C=0.5019
  penalizer=10       train C=0.6260  val C=0.5019
  penalizer=100      train C=0.6260  val C=0.5019

  selected penalizer=0.01 -> TEST C=0.4957 (test 2-SE band around 0.5 is +/-0.051)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:52:38Z | screen: T2_concepts

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 39 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=1 TEST C=0.5098 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts/
  representation=text_concepts[binary/disease,symptom] | landmark_days=180 | horizon_days=5475 | n_features=39

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   39 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   39 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   39 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 8 of 39 effectively constant (zero variance, or one value in >99% of patients); 39 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 39
RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  concept.diabetes_present                             0.4854   0.4854   0.4848
  concept.aneurysma_present                            0.4881   0.4881   0.4935
  concept.hypertensie_negated                          0.4891   0.4891   0.5027
  concept.nierfunctie_present                          0.4900   0.4900   0.4954
  concept.hyperlipidemie_present                       0.4908   0.4908   0.4627
  concept.perifeer_vaatlijden_present                  0.4916   0.4916   0.4941
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4931
  concept.angina_uncertain                             0.5062   0.5062   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.perifeer_vaatlijden_negated                  0.4949   0.4949   0.4978
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4961   0.4961   0.4942
  concept.angina_negated                               0.4963   0.4963   0.4875
  concept.aneurysma_negated                            0.5035   0.5035   0.4926
  concept.cva_tia_uncertain                            0.5034   0.5034   0.4933
  concept.nierfunctie_negated                          0.4967   0.4967   0.5029

  39 features are only ~35 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 8 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5352  val C=0.4879
  penalizer=0.1      train C=0.5323  val C=0.4982
  penalizer=1        train C=0.5323  val C=0.4982
  penalizer=10       train C=0.5323  val C=0.4982
  penalizer=100      train C=0.5323  val C=0.4982

  selected penalizer=1 -> TEST C=0.5098 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=1 TEST C=0.5098 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:53:10Z | screen: T2_concepts_alltiers

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_alltiers/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 42 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=10 TEST C=0.5092 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_alltiers/
  representation=text_concepts[binary/disease,symptom,measurement,medication,procedure] | landmark_days=180 | horizon_days=5475 | n_features=42

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   42 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   42 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   42 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 7 of 42 effectively constant (zero variance, or one value in >99% of patients); 42 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 42
RESULT: univariate: 0 of 42 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  concept.diabetes_present                             0.4858   0.4858   0.4831
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.aneurysma_present                            0.4881   0.4881   0.4935
  concept.hyperlipidemie_present                       0.4887   0.4887   0.4638
  concept.perifeer_vaatlijden_present                  0.4916   0.4916   0.4941
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4931
  concept.angina_uncertain                             0.5062   0.5062   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.perifeer_vaatlijden_negated                  0.4949   0.4949   0.4978
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4959   0.4959   0.4938
  concept.nierfunctie_present                          0.4961   0.4961   0.4983
  concept.angina_negated                               0.4963   0.4963   0.4875
  concept.hypertensie_present                          0.4965   0.4965   0.4988
  concept.aneurysma_negated                            0.5035   0.5035   0.4926
  concept.cva_tia_uncertain                            0.5034   0.5034   0.4933

  42 features are only ~37 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 7 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5336  val C=0.4934
  penalizer=0.1      train C=0.5267  val C=0.4983
  penalizer=1        train C=0.5267  val C=0.4983
  penalizer=10       train C=0.5267  val C=0.4983
  penalizer=100      train C=0.5267  val C=0.4983

  selected penalizer=10 -> TEST C=0.5092 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=10 TEST C=0.5092 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:53:42Z | screen: T2_concepts_both

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 78 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=1 TEST C=0.5095 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both/
  representation=text_concepts[both/disease,symptom] | landmark_days=180 | horizon_days=5475 | n_features=78

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   78 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   78 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   78 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 16 of 78 effectively constant (zero variance, or one value in >99% of patients); 57 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 78
RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  concept.diabetes_present_n                           0.4820   0.4820   0.4857
  concept.diabetes_present                             0.4854   0.4854   0.4848
  concept.aneurysma_present                            0.4881   0.4881   0.4935
  concept.aneurysma_present_n                          0.4884   0.4884   0.4927
  concept.hypertensie_negated                          0.4891   0.4891   0.5027
  concept.hypertensie_negated_n                        0.4892   0.4892   0.5020
  concept.nierfunctie_present_n                        0.4899   0.4899   0.4953
  concept.nierfunctie_present                          0.4900   0.4900   0.4954
  concept.hyperlipidemie_present_n                     0.4906   0.4906   0.4662
  concept.hyperlipidemie_present                       0.4908   0.4908   0.4627
  concept.perifeer_vaatlijden_present                  0.4916   0.4916   0.4941
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.perifeer_vaatlijden_present_n                0.4918   0.4918   0.4939
  concept.atriumfibrilleren_present_n                  0.4919   0.4919   0.4962
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4931
  concept.myocardinfarct_present_n                     0.4929   0.4929   0.5042
  concept.stenose_present_n                            0.4931   0.4931   0.4762
  concept.angina_uncertain_n                           0.5062   0.5062   0.4951

  78 features are only ~52 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~3 times, not ~4.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 16 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5386  val C=0.4823
  penalizer=0.1      train C=0.5326  val C=0.4955
  penalizer=1        train C=0.5326  val C=0.4955
  penalizer=10       train C=0.5326  val C=0.4955
  penalizer=100      train C=0.5326  val C=0.4955

  selected penalizer=1 -> TEST C=0.5095 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=1 TEST C=0.5095 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-08T09:54:28Z | screen: T2_concepts_demo

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo/
  representation=text_concepts[binary/disease,symptom]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=41

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   41 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   41 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   41 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 8 of 41 effectively constant (zero variance, or one value in >99% of patients); 40 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 2 of 41
RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  feature                                              C_mono   C_udev   C_test
  smart_baseline.leeftijd                              0.6731   0.5165   0.6716  <-
  smart_baseline.geslacht                              0.4422   0.4422   0.4587  <-
  concept.diabetes_present                             0.4854   0.4854   0.4848
  concept.aneurysma_present                            0.4881   0.4881   0.4935
  concept.hypertensie_negated                          0.4891   0.4891   0.5027
  concept.nierfunctie_present                          0.4900   0.4900   0.4954
  concept.hyperlipidemie_present                       0.4908   0.4908   0.4627
  concept.perifeer_vaatlijden_present                  0.4916   0.4916   0.4941
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4931
  concept.angina_uncertain                             0.5062   0.5062   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.perifeer_vaatlijden_negated                  0.4949   0.4949   0.4978
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4961   0.4961   0.4942
  concept.angina_negated                               0.4963   0.4963   0.4875
  concept.aneurysma_negated                            0.5035   0.5035   0.4926

  41 features are only ~37 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 8 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6809  val C=0.7073
  penalizer=0.1      train C=0.6722  val C=0.6781
  penalizer=1        train C=0.6646  val C=0.6652
  penalizer=10       train C=0.6645  val C=0.6651
  penalizer=100      train C=0.6645  val C=0.6651

  selected penalizer=0.01 -> TEST C=0.6749 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-08T09:55:02Z | screen: T2_concepts_history

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 38 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=1 TEST C=0.5198 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history/
  representation=text_concepts[binary/disease,symptom] | landmark_days=180 | horizon_days=5475 | n_features=38

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   38 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   38 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   38 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 8 of 38 effectively constant (zero variance, or one value in >99% of patients); 38 take <=10 distinct values (normal for counts)
     The effectively-constant ones carry nothing and dilute a penalised model:
     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.

  permutation-calibrated null: SE(C) = 0.292/sqrt(events); 2-SE floor on train (828 events) = 0.0203
  (the analytic 0.5/sqrt(events) would give 0.0348 — too wide under heavy censoring, which discards real signal)

--- univariate Harrell C per feature, TRAIN ---
  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped
  risk (both extremes harmful) that a monotone C-index reads as 0.50
  features clearing the floor (either form): 0 of 38
RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  feature                                              C_mono   C_udev   C_test
  concept.diabetes_present                             0.4860   0.4860   0.4872
  concept.nierfunctie_present                          0.4924   0.4924   0.4935
  concept.angina_present                               0.4926   0.4926   0.4890
  concept.hypertensie_present                          0.4928   0.4928   0.4884
  concept.hypertensie_negated                          0.4930   0.4930   0.5033
  concept.atriumfibrilleren_present                    0.4932   0.4932   0.4978
  concept.angina_negated                               0.4937   0.4937   0.4881
  concept.stenose_present                              0.4944   0.4944   0.4653
  concept.hyperlipidemie_present                       0.4944   0.4944   0.4635
  concept.diabetes_negated                             0.4950   0.4950   0.4970
  concept.cva_tia_present                              0.4950   0.4950   0.4997
  concept.perifeer_vaatlijden_negated                  0.4955   0.4955   0.5009
  concept.roken_negated                                0.5040   0.5040   0.4905
  concept.aneurysma_present                            0.4963   0.4963   0.4971
  concept.cva_tia_negated                              0.4965   0.4965   0.4993
  concept.perifeer_vaatlijden_present                  0.4966   0.4966   0.4967
  concept.myocardinfarct_uncertain                     0.4967   0.4967   0.5037
  concept.nierfunctie_negated                          0.4970   0.4970   0.5036
  concept.hartfalen_negated                            0.4974   0.4974   0.4994
  concept.myocardinfarct_negated                       0.4975   0.4975   0.4936

  38 features are only ~34 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 8 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5179  val C=0.4903
  penalizer=0.1      train C=0.5179  val C=0.4986
  penalizer=1        train C=0.5179  val C=0.4986
  penalizer=10       train C=0.5179  val C=0.4986
  penalizer=100      train C=0.5179  val C=0.4986

  selected penalizer=1 -> TEST C=0.5198 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=1 TEST C=0.5198 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>
