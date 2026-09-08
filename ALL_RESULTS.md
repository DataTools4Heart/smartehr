# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (5 runs)

- **2026-09-08T13:59:01Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: sex marginals AGREE (text 0.553 vs registry 0.653) while per-patient agreement is chance: that is the signature of a MISJOIN, not a weak extractor
  - RESULT: ** JOIN CONTROL FAILS (sex_from_text rho=-0.022, age_from_text rho=-0.004) **: age and sex are stated in nearly every letter, so either the documents are joined to the WRONG PATIENTS -- which would invalidate every text arm here, T0/T1/T2 included -- or these extractors are noise. The sex marginals above say which
  - RESULT: graded vs curated (train, outcome-blind): 0 of 15 pairs reach |rho|>=0.3
  - RESULT: arm=text_graded[dates=strip] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T14:03:16Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 46 features; 2259 of 9644 patients have at least one extracted quantity
  - RESULT: sex marginals AGREE (text 0.553 vs registry 0.653) while per-patient agreement is chance: that is the signature of a MISJOIN, not a weak extractor
  - RESULT: ** JOIN CONTROL FAILS (sex_from_text rho=-0.022, age_from_text rho=-0.004) **: age and sex are stated in nearly every letter, so either the documents are joined to the WRONG PATIENTS -- which would invalidate every text arm here, T0/T1/T2 included -- or these extractors are noise. The sex marginals above say which
  - RESULT: graded vs curated (train, outcome-blind): 0 of 15 pairs reach |rho|>=0.3
  - RESULT: arm=text_graded[dates=year] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T14:07:23Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip]+baseline[leeftijd,geslacht] n_features=40 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T14:11:23Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=79 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-08T14:15:50Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip]+baseline[all] n_features=221 train=6210/914ev validation=1510/230ev test=1924/287ev

---

### RUN 2026-09-08T13:59:01Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: sex marginals AGREE (text 0.553 vs registry 0.653) while per-patient agreement is chance: that is the signature of a MISJOIN, not a weak extractor
- RESULT: ** JOIN CONTROL FAILS (sex_from_text rho=-0.022, age_from_text rho=-0.004) **: age and sex are stated in nearly every letter, so either the documents are joined to the WRONG PATIENTS -- which would invalidate every text arm here, T0/T1/T2 included -- or these extractors are noise. The sex marginals above say which
- RESULT: graded vs curated (train, outcome-blind): 0 of 15 pairs reach |rho|>=0.3
- RESULT: arm=text_graded[dates=strip] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

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
  46 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.sex_from_text                      4,036 ( 41.8%)  median=1.00 p90=2.00
    graded.age_from_text                      3,327 ( 34.5%)  median=60.00 p90=75.00
    graded.sex_agreement                      4,036 ( 41.8%)  median=1.00 p90=1.00
    graded.sex_n_docs                         4,036 ( 41.8%)  median=2.00 p90=8.00
    graded.age_spread                         3,327 ( 34.5%)  median=0.00 p90=16.00
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
RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity

  --- extracted vs curated, TRAIN, outcome never consulted ---
  `both` is the patients where BOTH are present; agreement is only defined there.
  extracted                              curated                both     rho   exact   sens   spec
  graded.sex_from_text                   geslacht              2,619  -0.022   0.506   -      -   
  graded.age_from_text                   leeftijd              2,173  -0.004     -     -      -   
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

  --- sex: the discriminating table (n=2,619) ---
  P(male) extracted from text = 0.553 | P(male) in the registry = 0.653
                   registry Man  registry Vrouw
        text Man            931             517
      text Vrouw            778             393
RESULT: sex marginals AGREE (text 0.553 vs registry 0.653) while per-patient agreement is chance: that is the signature of a MISJOIN, not a weak extractor
  -> marginals agree but the table is not diagonal: the text is being
     matched to the WRONG PATIENTS. Fix the join before anything else.
RESULT: ** JOIN CONTROL FAILS (sex_from_text rho=-0.022, age_from_text rho=-0.004) **: age and sex are stated in nearly every letter, so either the documents are joined to the WRONG PATIENTS -- which would invalidate every text arm here, T0/T1/T2 included -- or these extractors are noise. The sex marginals above say which
  ** THE JOIN CONTROL FAILED. No text result is interpretable until this is
     resolved. Read the sex table above to tell the two causes apart: equal
     marginals with an off-diagonal table means a MISJOIN; unequal marginals
     mean the EXTRACTOR is at fault and the join is still untested. Note
     that plausible concept PREVALENCES rule out neither -- a shuffled cache
     preserves prevalence exactly. **
RESULT: graded vs curated (train, outcome-blind): 0 of 15 pairs reach |rho|>=0.3
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

  raw feature matrix: 9,644 patients x 46 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  46 features tested = ~19 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 1 (~1 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<2.6e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  graded.age_spread                         0.4568  0.4568  35.0%   286  2.50    raw2SE
  graded.stenosis_n                         0.4679  0.4477  13.6%   120  1.96          
  graded.med_insuline                       0.4835  0.4835 100.0%   828  1.63          
  graded.sex_n_docs                         0.4824  0.4734  42.2%   344  1.69          
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
  graded.age_from_text                      0.4883  0.4842  35.0%   286  0.92          
  graded.onset_measured                     0.4988  0.4988 100.0%   828  0.12          
  graded.med_fibraat                        0.4992  0.4992 100.0%   828  0.08          
  graded.med_ace_remmer                     0.5008  0.5008 100.0%   828  0.08          
  graded.med_betablokker                    0.5007  0.5007 100.0%   828  0.06          
  graded.med_lmwh                           0.4995  0.4995 100.0%   828  0.05          
  graded.med_plaatjesremmer                 0.5005  0.5005 100.0%   828  0.05          
  graded.med_centraal_antihyp               0.4995  0.4995 100.0%   828  0.04          
  graded.med_galzuurbinder                  0.5004  0.5004 100.0%   828  0.04          
  graded.med_vasodilatator                  0.4997  0.4997 100.0%   828  0.03          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.

  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 168,182 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=38
  validation : 1,510 patients | events=206 (13.6%) | features=38
  test       : 1,924 patients | events=257 (13.4%) | features=38
RESULT: arm=text_graded[dates=strip] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt model=mlp model.input_size=38
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T14:03:16Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 46 features; 2259 of 9644 patients have at least one extracted quantity
- RESULT: sex marginals AGREE (text 0.553 vs registry 0.653) while per-patient agreement is chance: that is the signature of a MISJOIN, not a weak extractor
- RESULT: ** JOIN CONTROL FAILS (sex_from_text rho=-0.022, age_from_text rho=-0.004) **: age and sex are stated in nearly every letter, so either the documents are joined to the WRONG PATIENTS -- which would invalidate every text arm here, T0/T1/T2 included -- or these extractors are noise. The sex marginals above say which
- RESULT: graded vs curated (train, outcome-blind): 0 of 15 pairs reach |rho|>=0.3
- RESULT: arm=text_graded[dates=year] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

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
  46 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.sex_from_text                      4,036 ( 41.8%)  median=1.00 p90=2.00
    graded.age_from_text                      3,327 ( 34.5%)  median=60.00 p90=75.00
    graded.sex_agreement                      4,036 ( 41.8%)  median=1.00 p90=1.00
    graded.sex_n_docs                         4,036 ( 41.8%)  median=2.00 p90=8.00
    graded.age_spread                         3,327 ( 34.5%)  median=0.00 p90=16.00
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
RESULT: graded: 46 features; 2259 of 9644 patients have at least one extracted quantity

  --- extracted vs curated, TRAIN, outcome never consulted ---
  `both` is the patients where BOTH are present; agreement is only defined there.
  extracted                              curated                both     rho   exact   sens   spec
  graded.sex_from_text                   geslacht              2,619  -0.022   0.506   -      -   
  graded.age_from_text                   leeftijd              2,173  -0.004     -     -      -   
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

  --- sex: the discriminating table (n=2,619) ---
  P(male) extracted from text = 0.553 | P(male) in the registry = 0.653
                   registry Man  registry Vrouw
        text Man            931             517
      text Vrouw            778             393
RESULT: sex marginals AGREE (text 0.553 vs registry 0.653) while per-patient agreement is chance: that is the signature of a MISJOIN, not a weak extractor
  -> marginals agree but the table is not diagonal: the text is being
     matched to the WRONG PATIENTS. Fix the join before anything else.
RESULT: ** JOIN CONTROL FAILS (sex_from_text rho=-0.022, age_from_text rho=-0.004) **: age and sex are stated in nearly every letter, so either the documents are joined to the WRONG PATIENTS -- which would invalidate every text arm here, T0/T1/T2 included -- or these extractors are noise. The sex marginals above say which
  ** THE JOIN CONTROL FAILED. No text result is interpretable until this is
     resolved. Read the sex table above to tell the two causes apart: equal
     marginals with an off-diagonal table means a MISJOIN; unequal marginals
     mean the EXTRACTOR is at fault and the join is still untested. Note
     that plausible concept PREVALENCES rule out neither -- a shuffled cache
     preserves prevalence exactly. **
RESULT: graded vs curated (train, outcome-blind): 0 of 15 pairs reach |rho|>=0.3
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

  raw feature matrix: 9,644 patients x 46 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 168,166 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=38
  validation : 1,510 patients | events=206 (13.6%) | features=38
  test       : 1,924 patients | events=257 (13.4%) | features=38
RESULT: arm=text_graded[dates=year] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_year_rt model=mlp model.input_size=38
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T14:07:23Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=strip]+baseline[leeftijd,geslacht] n_features=40 train=6210/914ev validation=1510/230ev test=1924/287ev

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
  46 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.sex_from_text                      4,036 ( 41.8%)  median=1.00 p90=2.00
    graded.age_from_text                      3,327 ( 34.5%)  median=60.00 p90=75.00
    graded.sex_agreement                      4,036 ( 41.8%)  median=1.00 p90=1.00
    graded.sex_n_docs                         4,036 ( 41.8%)  median=2.00 p90=8.00
    graded.age_spread                         3,327 ( 34.5%)  median=0.00 p90=16.00
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
RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 48 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 168,182 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=40
  validation : 1,510 patients | events=206 (13.6%) | features=40
  test       : 1,924 patients | events=257 (13.4%) | features=40
RESULT: arm=text_graded[dates=strip]+baseline[leeftijd,geslacht] n_features=40 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt model=mlp model.input_size=40
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T14:11:23Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=79 train=6210/914ev validation=1510/230ev test=1924/287ev

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
  46 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.sex_from_text                      4,036 ( 41.8%)  median=1.00 p90=2.00
    graded.age_from_text                      3,327 ( 34.5%)  median=60.00 p90=75.00
    graded.sex_agreement                      4,036 ( 41.8%)  median=1.00 p90=1.00
    graded.sex_n_docs                         4,036 ( 41.8%)  median=2.00 p90=8.00
    graded.age_spread                         3,327 ( 34.5%)  median=0.00 p90=16.00
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
RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  + 39 concept features appended (binary/disease,symptom)
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 87 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 168,182 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=79
  validation : 1,510 patients | events=206 (13.6%) | features=79
  test       : 1,924 patients | events=257 (13.4%) | features=79
RESULT: arm=text_graded[dates=strip]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=79 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt model=mlp model.input_size=79
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-08T14:15:50Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=strip]+baseline[all] n_features=221 train=6210/914ev validation=1510/230ev test=1924/287ev

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
  46 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.sex_from_text                      4,036 ( 41.8%)  median=1.00 p90=2.00
    graded.age_from_text                      3,327 ( 34.5%)  median=60.00 p90=75.00
    graded.sex_agreement                      4,036 ( 41.8%)  median=1.00 p90=1.00
    graded.sex_n_docs                         4,036 ( 41.8%)  median=2.00 p90=8.00
    graded.age_spread                         3,327 ( 34.5%)  median=0.00 p90=16.00
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
RESULT: graded: 46 features; 2256 of 9644 patients have at least one extracted quantity
  appending 183 baseline columns -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 229 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 8 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 330,256 missing cells with the train median, then standardised
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
  train      : 6,210 patients | events=828 (13.3%) | features=221
  validation : 1,510 patients | events=206 (13.6%) | features=221
  test       : 1,924 patients | events=257 (13.4%) | features=221
RESULT: arm=text_graded[dates=strip]+baseline[all] n_features=221 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt model=mlp model.input_size=221
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>
