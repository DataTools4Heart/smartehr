# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (170 runs)

- **2026-08-26T11:33:40Z | phase0 text EDA**
  - RESULT: narrative text coverage 9644/13434 (71.8%); no text for 3790
  - RESULT: T0 volume control: 0 of 9 features clear the 0.0149 floor -> INERT, content gains are attributable to content
- **2026-08-26T11:35:55Z | text arm: volume**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_volume n_features=9 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-08-26T11:36:15Z | text arm: volume**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_volume n_features=9 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:36:29Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:38:41Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word] n_features=256 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-08-26T11:40:26Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[char] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:46:10Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word]+section:voorgeschiedenis,anamnese n_features=128 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:47:08Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word]+section:conclusie n_features=128 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:47:54Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:49:43Z | text arm: tfidf**
  - RESULT: documents=120776 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:51:44Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word]+baseline[leeftijd,geslacht] n_features=258 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:53:37Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
  - RESULT: arm=text_concepts[binary] n_features=39 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:54:43Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
  - RESULT: arm=text_concepts[both] n_features=78 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:55:37Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
  - RESULT: arm=text_concepts[binary]+baseline[leeftijd,geslacht] n_features=41 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:56:44Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 5085 patients with text): roken=3302, hypertensie=3212, hyperlipidemie=2489, revascularisatie=2343
  - RESULT: arm=text_concepts[binary] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:57:27Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[leeftijd,geslacht] n_features=2 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:57:33Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[all] n_features=183 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-08-26T11:57:46Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[leeftijd,geslacht] n_features=2 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-08-26T11:57:52Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[all] n_features=183 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-08-26T11:58:11Z | structured arm**
  - RESULT: arm=smart_baseline[all] n_features=183 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-08-26T11:58:30Z | screen: CTRL_demo_full**
  - RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
- **2026-08-26T11:58:59Z | screen: CTRL_demo_rt**
  - RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
- **2026-08-26T11:59:18Z | screen: CTRL_full_full**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
- **2026-08-26T12:00:06Z | screen: CTRL_full_rt**
  - RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- **2026-08-26T12:00:37Z | screen: STRUCT_ctrl**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
- **2026-08-26T12:01:24Z | screen: T0_volume**
  - RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-08-26T12:01:57Z | screen: T0_volume_rt**
  - RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:02:19Z | screen: T1_tfidf_3src**
  - RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:06:41Z | screen: T1_tfidf_char**
  - RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:11:09Z | screen: T1_tfidf_conclusie**
  - RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:12:39Z | screen: T1_tfidf_demo**
  - RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-08-26T12:17:16Z | screen: T1_tfidf_history**
  - RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:18:45Z | screen: T1_tfidf_nonames**
  - RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:23:11Z | screen: T1_tfidf_word**
  - RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:27:33Z | screen: T1_tfidf_word_full**
  - RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-08-26T12:31:12Z | screen: T2_concepts**
  - RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.1 TEST C=0.5114 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:31:43Z | screen: T2_concepts_both**
  - RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.1 TEST C=0.5097 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-26T12:32:34Z | screen: T2_concepts_demo**
  - RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-08-26T12:33:06Z | screen: T2_concepts_history**
  - RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5212 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T07:54:30Z | screen: CTRL_demo_full**
  - RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
- **2026-08-27T07:55:01Z | screen: CTRL_demo_rt**
  - RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
- **2026-08-27T07:55:23Z | screen: CTRL_full_full**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-08-27T07:57:49Z | screen: CTRL_full_rt**
  - RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-08-27T08:00:24Z | screen: STRUCT_ctrl**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-08-27T08:02:51Z | screen: T0_volume**
  - RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-08-27T08:03:25Z | screen: T0_volume_rt**
  - RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:03:49Z | screen: T1_tfidf_3src**
  - RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:08:45Z | screen: T1_tfidf_char**
  - RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:13:44Z | screen: T1_tfidf_conclusie**
  - RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:15:24Z | screen: T1_tfidf_demo**
  - RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-08-27T08:20:36Z | screen: T1_tfidf_history**
  - RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:22:16Z | screen: T1_tfidf_nonames**
  - RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:27:14Z | screen: T1_tfidf_word**
  - RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:32:13Z | screen: T1_tfidf_word_full**
  - RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-08-27T08:36:15Z | screen: T2_concepts**
  - RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.1 TEST C=0.5120 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:36:47Z | screen: T2_concepts_both**
  - RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.1 TEST C=0.5101 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-08-27T08:37:37Z | screen: T2_concepts_demo**
  - RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-08-27T08:38:12Z | screen: T2_concepts_history**
  - RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5209 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T08:53:27Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  - RESULT: arm=text_concepts[binary/disease,symptom] n_features=39 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T08:54:39Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  - RESULT: arm=text_concepts[both/disease,symptom] n_features=78 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T08:55:34Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  - RESULT: arm=text_concepts[binary/disease,symptom]+baseline[leeftijd,geslacht] n_features=41 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T08:56:38Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 5085 patients with text): roken=3300, hypertensie=3197, diabetes=1960, myocardinfarct=1865
  - RESULT: arm=text_concepts[binary/disease,symptom] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T08:57:20Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4527, hyperlipidemie=4176, hypertensie=3860, roken=3802
  - RESULT: arm=text_concepts[binary/disease,symptom,measurement,medication,procedure] n_features=42 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T08:58:31Z | text arm: concepts**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  - RESULT: arm=text_concepts[binary/disease,symptom]+baseline[all] n_features=222 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T08:59:58Z | text arm: tfidf**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_tfidf[word]+baseline[all] n_features=439 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T09:01:47Z | text arm: volume**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=text_volume+baseline[all] n_features=192 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-03T09:02:00Z | structured arm**
  - RESULT: arm=pivoted_events+baseline[leeftijd,geslacht] n_features=532 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-09-03T09:04:22Z | screen: CTRL_demo_full**
  - RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
- **2026-09-03T09:04:54Z | screen: CTRL_demo_rt**
  - RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
- **2026-09-03T09:05:15Z | screen: CTRL_full_full**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-03T09:07:41Z | screen: CTRL_full_rt**
  - RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-03T09:10:15Z | screen: INCR_concepts_full**
  - RESULT: univariate: 103 of 222 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7397 (2-SE band +/-0.062) -> signal
- **2026-09-03T09:13:46Z | screen: INCR_tfidf_full**
  - RESULT: univariate: 123 of 439 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7388 (2-SE band +/-0.062) -> signal
- **2026-09-03T09:20:58Z | screen: INCR_volume_full**
  - RESULT: univariate: 103 of 192 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-03T09:23:46Z | screen: SENS_no_omschr**
  - RESULT: univariate: 2 of 532 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6884 (2-SE band +/-0.051) -> signal
- **2026-09-03T09:38:32Z | screen: STRUCT_ctrl**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-03T09:40:58Z | screen: T0_volume**
  - RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-03T09:41:32Z | screen: T0_volume_rt**
  - RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T09:41:56Z | screen: T1_tfidf_3src**
  - RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T09:46:49Z | screen: T1_tfidf_char**
  - RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T09:51:44Z | screen: T1_tfidf_conclusie**
  - RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T09:53:24Z | screen: T1_tfidf_demo**
  - RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-09-03T09:58:34Z | screen: T1_tfidf_history**
  - RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T10:00:13Z | screen: T1_tfidf_nonames**
  - RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T10:05:10Z | screen: T1_tfidf_word**
  - RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T10:10:06Z | screen: T1_tfidf_word_full**
  - RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-03T10:14:05Z | screen: T2_concepts**
  - RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5098 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T10:14:37Z | screen: T2_concepts_alltiers**
  - RESULT: univariate: 0 of 42 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=10 TEST C=0.5092 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T10:15:10Z | screen: T2_concepts_both**
  - RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5095 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-03T10:15:56Z | screen: T2_concepts_demo**
  - RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-09-03T10:16:29Z | screen: T2_concepts_history**
  - RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5198 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T17:24:15Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:chart] n_features=113 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T17:24:25Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:chart,leeftijd,geslacht] n_features=115 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T17:24:35Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:chart_strict] n_features=96 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T17:24:44Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:protocol] n_features=68 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T17:24:52Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:protocol,leeftijd,geslacht] n_features=70 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T17:25:00Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:chart] n_features=113 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-09-07T17:25:13Z | text arm: baseline**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: arm=matched_baseline[group:protocol] n_features=68 train=8599/1253ev validation=2141/341ev test=2694/422ev
- **2026-09-07T17:25:23Z | screen: CTRL_demo_full**
  - RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
- **2026-09-07T17:25:55Z | screen: CTRL_demo_rt**
  - RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:26:16Z | screen: CTRL_full_full**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-07T17:28:40Z | screen: CTRL_full_rt**
  - RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:31:14Z | screen: HR_chart_demo_rt**
  - RESULT: univariate: 59 of 115 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7351 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:32:33Z | screen: HR_chart_full**
  - RESULT: univariate: 60 of 113 features clear the 0.0192 floor; strongest smart_baseline.stenACIl C=0.6420
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7373 (2-SE band +/-0.051) -> signal
- **2026-09-07T17:34:23Z | screen: HR_chart_rt**
  - RESULT: univariate: 57 of 113 features clear the 0.0203 floor; strongest smart_baseline.stenACIl C=0.6471
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7310 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:35:39Z | screen: HR_chartstrict_rt**
  - RESULT: univariate: 43 of 96 features clear the 0.0203 floor; strongest smart_baseline.KliMaYr C=0.3855
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7024 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:36:40Z | screen: HR_protocol_demo_rt**
  - RESULT: univariate: 46 of 70 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7198 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:37:31Z | screen: HR_protocol_full**
  - RESULT: univariate: 44 of 68 features clear the 0.0192 floor; strongest smart_baseline.klar_coc C=0.3634
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7288 (2-SE band +/-0.051) -> signal
- **2026-09-07T17:38:43Z | screen: HR_protocol_rt**
  - RESULT: univariate: 44 of 68 features clear the 0.0203 floor; strongest smart_baseline.klar_coc C=0.3625
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7196 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:39:32Z | screen: INCR_concepts_full**
  - RESULT: univariate: 103 of 222 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7397 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:42:59Z | screen: INCR_tfidf_full**
  - RESULT: univariate: 123 of 439 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7388 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:50:01Z | screen: INCR_volume_full**
  - RESULT: univariate: 103 of 192 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-07T17:52:47Z | screen: SENS_no_omschr**
  - RESULT: univariate: 2 of 532 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6884 (2-SE band +/-0.051) -> signal
- **2026-09-07T18:06:56Z | screen: STRUCT_ctrl**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-07T18:09:22Z | screen: T0_volume**
  - RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-07T18:09:56Z | screen: T0_volume_rt**
  - RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:10:20Z | screen: T1_tfidf_3src**
  - RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:15:14Z | screen: T1_tfidf_char**
  - RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:20:10Z | screen: T1_tfidf_conclusie**
  - RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:21:49Z | screen: T1_tfidf_demo**
  - RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-09-07T18:27:02Z | screen: T1_tfidf_history**
  - RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:28:41Z | screen: T1_tfidf_nonames**
  - RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:33:34Z | screen: T1_tfidf_word**
  - RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:38:25Z | screen: T1_tfidf_word_full**
  - RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-07T18:42:23Z | screen: T2_concepts**
  - RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5098 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:42:55Z | screen: T2_concepts_alltiers**
  - RESULT: univariate: 0 of 42 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=10 TEST C=0.5092 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:43:28Z | screen: T2_concepts_both**
  - RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5095 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T18:44:14Z | screen: T2_concepts_demo**
  - RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-09-07T18:44:47Z | screen: T2_concepts_history**
  - RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5198 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T20:29:56Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  - RESULT: graded vs curated (train, outcome-blind): 0 of 12 pairs reach |rho|>=0.3
  - RESULT: arm=text_graded[dates=year] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T20:33:24Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 40 features; 4218 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=strip] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T20:36:32Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=year]+baseline[leeftijd,geslacht] n_features=35 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T20:39:49Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=year]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=74 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T20:43:27Z | text arm: graded**
  - RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  - RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  - RESULT: arm=text_graded[dates=year]+baseline[all] n_features=216 train=6210/914ev validation=1510/230ev test=1924/287ev
- **2026-09-07T20:46:51Z | screen: CTRL_demo_full**
  - RESULT: univariate: 2 of 2 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
- **2026-09-07T20:47:22Z | screen: CTRL_demo_rt**
  - RESULT: univariate: 2 of 2 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
- **2026-09-07T20:47:43Z | screen: CTRL_full_full**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-07T20:50:08Z | screen: CTRL_full_rt**
  - RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-07T20:52:42Z | screen: GRADED_all_demo_rt**
  - RESULT: univariate: 2 of 74 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-09-07T20:53:28Z | screen: GRADED_demo_rt**
  - RESULT: univariate: 2 of 35 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6746 (2-SE band +/-0.062) -> signal
- **2026-09-07T20:54:00Z | screen: GRADED_full_rt**
  - RESULT: univariate: 103 of 216 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7396 (2-SE band +/-0.062) -> signal
- **2026-09-07T20:57:19Z | screen: GRADED_rt**
  - RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4920 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T20:57:49Z | screen: GRADED_strip_rt**
  - RESULT: univariate: 0 of 33 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4979 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T20:58:19Z | screen: HR_chart_demo_rt**
  - RESULT: univariate: 59 of 115 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7351 (2-SE band +/-0.062) -> signal
- **2026-09-07T20:59:36Z | screen: HR_chart_full**
  - RESULT: univariate: 60 of 113 features clear the 0.0192 floor; strongest smart_baseline.stenACIl C=0.6420
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7373 (2-SE band +/-0.051) -> signal
- **2026-09-07T21:01:27Z | screen: HR_chart_rt**
  - RESULT: univariate: 57 of 113 features clear the 0.0203 floor; strongest smart_baseline.stenACIl C=0.6471
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7310 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:02:43Z | screen: HR_chartstrict_rt**
  - RESULT: univariate: 43 of 96 features clear the 0.0203 floor; strongest smart_baseline.KliMaYr C=0.3855
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7024 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:03:44Z | screen: HR_protocol_demo_rt**
  - RESULT: univariate: 46 of 70 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7198 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:04:34Z | screen: HR_protocol_full**
  - RESULT: univariate: 44 of 68 features clear the 0.0192 floor; strongest smart_baseline.klar_coc C=0.3634
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7288 (2-SE band +/-0.051) -> signal
- **2026-09-07T21:05:46Z | screen: HR_protocol_rt**
  - RESULT: univariate: 44 of 68 features clear the 0.0203 floor; strongest smart_baseline.klar_coc C=0.3625
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7196 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:06:34Z | screen: INCR_concepts_full**
  - RESULT: univariate: 103 of 222 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7397 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:10:01Z | screen: INCR_tfidf_full**
  - RESULT: univariate: 123 of 439 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7388 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:17:04Z | screen: INCR_volume_full**
  - RESULT: univariate: 103 of 192 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7394 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:19:50Z | screen: SENS_no_omschr**
  - RESULT: univariate: 2 of 532 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6884 (2-SE band +/-0.051) -> signal
- **2026-09-07T21:33:23Z | screen: STRUCT_ctrl**
  - RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742
  - RESULT: COX lasso penalizer=0.01 TEST C=0.7576 (2-SE band +/-0.051) -> signal
- **2026-09-07T21:35:47Z | screen: T0_volume**
  - RESULT: univariate: 0 of 9 features clear the 0.0192 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-07T21:36:21Z | screen: T0_volume_rt**
  - RESULT: univariate: 0 of 9 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T21:36:45Z | screen: T1_tfidf_3src**
  - RESULT: univariate: 27 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4640
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T21:41:40Z | screen: T1_tfidf_char**
  - RESULT: univariate: 30 of 256 features clear the 0.0203 floor; strongest tfidf.svd_153 C=0.5076
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T21:46:32Z | screen: T1_tfidf_conclusie**
  - RESULT: univariate: 6 of 128 features clear the 0.0203 floor; strongest tfidf.svd_31 C=0.4720
  - RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T21:48:11Z | screen: T1_tfidf_demo**
  - RESULT: univariate: 22 of 258 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
- **2026-09-07T21:53:20Z | screen: T1_tfidf_history**
  - RESULT: univariate: 7 of 128 features clear the 0.0203 floor; strongest tfidf.svd_53 C=0.4708
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T21:54:59Z | screen: T1_tfidf_nonames**
  - RESULT: univariate: 24 of 256 features clear the 0.0203 floor; strongest tfidf.svd_28 C=0.4675
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T21:59:52Z | screen: T1_tfidf_word**
  - RESULT: univariate: 20 of 256 features clear the 0.0203 floor; strongest tfidf.svd_123 C=0.4680
  - RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T22:04:46Z | screen: T1_tfidf_word_full**
  - RESULT: univariate: 8 of 256 features clear the 0.0192 floor; strongest tfidf.svd_209 C=0.5252
  - RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
- **2026-09-07T22:08:44Z | screen: T2_concepts**
  - RESULT: univariate: 0 of 39 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5098 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T22:09:16Z | screen: T2_concepts_alltiers**
  - RESULT: univariate: 0 of 42 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=10 TEST C=0.5092 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T22:09:49Z | screen: T2_concepts_both**
  - RESULT: univariate: 0 of 78 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5095 (2-SE band +/-0.062) -> indistinguishable from chance
- **2026-09-07T22:10:35Z | screen: T2_concepts_demo**
  - RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
  - RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
- **2026-09-07T22:11:08Z | screen: T2_concepts_history**
  - RESULT: univariate: 0 of 38 features clear the 0.0203 floor
  - RESULT: COX lasso penalizer=1 TEST C=0.5198 (2-SE band +/-0.062) -> indistinguishable from chance

---

### RUN 2026-08-26T11:33:40Z | phase0 text EDA

- status: ok
- context: landmark=180 horizon=5475 out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/eda_text
- RESULT: narrative text coverage 9644/13434 (71.8%); no text for 3790
- RESULT: T0 volume control: 0 of 9 features clear the 0.0149 floor -> INERT, content gains are attributable to content

<details><summary>full output</summary>

```
tokenizer: Qwen/Qwen3-Embedding-0.6B
scanning consult_20251208.csv.consult_tekst ...
scanning mri_verslag_20250626.csv.rad_report ...
scanning radiologie_verslag_20251208.csv.verslagtekst ...
scanning uitgaandebrief_20251208.csv.inhoud ...
RESULT: narrative text coverage 9644/13434 (71.8%); no text for 3790
RESULT: T0 volume control: 0 of 9 features clear the 0.0149 floor -> INERT, content gains are attributable to content
# EDA — clinical free text for baseline-free survival

- landmark: **180 days**; lookback: unbounded; horizon: 5475 days from the landmark
- privacy: no raw clinical text is written; terms/values shown only at >= 20 occurrences

## §1 Cohort

- legacy: dropped 1 rows with a missing SMART outcome column
- legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
- 13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
- landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
- **13,434 patients, 1,827 events (13.6%)** at the 5475-day horizon
- splits: train=8,599, test=2,694, validation=2,141

## §2 Coverage — is the empty-text confound still present?

- patients with >= 1 narrative document: **9,644 / 13,434 (71.8%)**
- patients with NO narrative text: **3,790** <- these get an all-zero text vector and are unrankable from text alone
  - train: 6,210 with text, **2,389 without** (27.8%)
  - test: 1,924 with text, **770 without** (28.6%)
  - validation: 1,510 with text, **631 without** (29.5%)
- documents per patient (text-bearing only): {'p50': 5.0, 'p95': 50.0, 'p100': 589.0}
- chars per patient: {'p5': 583.0, 'p50': 5196.5, 'p95': 52706.1, 'p100': 550223.0}
- **total corpus: 46,440,123 tokens** (~4,815/patient, real tokenizer)

| source | docs | patients | pre-bl docs | post-bl docs in window | chars/doc p50 | words/doc p50 |
|---|---|---|---|---|---|---|
| consult_20251208.consult_tekst | 75,445 | 4,957 | 47,716 | 27,729 | 418.0 | 53.0 |
| mri_verslag_20250626.rad_report | 1,002 | 461 | 632 | 370 | 1024.0 | 122.0 |
| radiologie_verslag_20251208.verslagtekst | 33,087 | 7,478 | 26,608 | 6,479 | 691.0 | 47.0 |
| uitgaandebrief_20251208.inhoud | 12,244 | 4,164 | 7,286 | 4,958 | 3570.5 | 421.0 |

## §3 Text shape — boilerplate, truncation, structure, de-identification risk

### consult_20251208.consult_tekst

- documents in window: 75,445 across 4,957 patients; docs/patient {'p50': 9.0, 'p95': 46.0, 'p100': 517.0}
- chars/doc {'p5': 81.0, 'p50': 418.0, 'p95': 2664.0, 'p100': 12603.0} | words/doc {'p5': 9.0, 'p50': 53.0, 'p95': 329.0, 'p100': 1596.0}
- tokens/doc {'p5': 29.0, 'p50': 154.0, 'p95': 980.0, 'p100': 4534.0} | tokens/patient {'p5': 280.6, 'p50': 2565.0, 'p95': 13176.6, 'p100': 154250.0} | total 20,848,942
- `datediff` of documents: {'p0': -4758.0, 'p5': -1367.8, 'p50': -60.0, 'p95': 122.0, 'p100': 179.0}
- modal document length: 88 chars in 0.2% of documents
- **72,556 distinct documents** of 75,445 (96.2% distinct); 3,861 share their text with another document
- **boilerplate: 0% of a median document's 8-grams are shared with >=30% of documents** (0 common n-grams, 4,000 sampled)
- de-id risk: ISO dates in 0.0% of docs, NL dates 42.5%, clinician tokens 24.7%, name-like tokens/doc {'p50': 10.0, 'p95': 55.0}
- section headers (share of docs): {'anamnese': 0.523, 'conclusie': 0.293, 'beleid': 0.208, 'voorgeschiedenis': 0.134, 'lichamelijk onderzoek': 0.095, 'samenvatting': 0.054, 'indicatie': 0.036, 'advies': 0.035, 'bevindingen': 0.015}

### mri_verslag_20250626.rad_report

- documents in window: 1,002 across 461 patients; docs/patient {'p50': 2.0, 'p95': 4.0, 'p100': 12.0}
- chars/doc {'p5': 238.0, 'p50': 1024.0, 'p95': 1024.0, 'p100': 1024.0} | words/doc {'p5': 32.05, 'p50': 122.0, 'p95': 142.0, 'p100': 163.0}
- tokens/doc {'p5': 77.0, 'p50': 352.0, 'p95': 444.0, 'p100': 578.0} | tokens/patient {'p5': 27.0, 'p50': 706.0, 'p95': 1610.0, 'p100': 3672.0} | total 334,230
- `datediff` of documents: {'p0': -7384.0, 'p5': -2253.85, 'p50': -52.5, 'p95': 119.95, 'p100': 178.0}
- modal document length: 1024 chars in 59.3% of documents  **<- TRUNCATION SUSPECTED**
- **538 distinct documents** of 1,002 (53.7% distinct); 900 share their text with another document
- **boilerplate: 0% of a median document's 8-grams are shared with >=30% of documents** (0 common n-grams, 1,002 sampled)
- de-id risk: ISO dates in 0.0% of docs, NL dates 14.8%, clinician tokens 11.6%, name-like tokens/doc {'p50': 7.0, 'p95': 13.0}
- section headers (share of docs): {'klinische gegevens': 0.537, 'indicatie': 0.324, 'conclusie': 0.254, 'voorgeschiedenis': 0.031}

### radiologie_verslag_20251208.verslagtekst

- documents in window: 33,087 across 7,478 patients; docs/patient {'p50': 2.0, 'p95': 14.0, 'p100': 129.0}
- chars/doc {'p5': 231.0, 'p50': 691.0, 'p95': 1186.0, 'p100': 4558.0} | words/doc {'p5': 24.0, 'p50': 47.0, 'p95': 122.0, 'p100': 583.0}
- tokens/doc {'p5': 81.0, 'p50': 182.0, 'p95': 358.0, 'p100': 1484.0} | tokens/patient {'p5': 112.0, 'p50': 396.0, 'p95': 2860.2, 'p100': 26571.0} | total 6,447,936
- `datediff` of documents: {'p0': -9598.0, 'p5': -4707.0, 'p50': -184.0, 'p95': 96.7, 'p100': 179.0}
- modal document length: 752 chars in 0.3% of documents
- **32,352 distinct documents** of 33,087 (97.8% distinct); 1,123 share their text with another document
- **boilerplate: 0% of a median document's 8-grams are shared with >=30% of documents** (0 common n-grams, 4,000 sampled)
- de-id risk: ISO dates in 0.0% of docs, NL dates 78.0%, clinician tokens 64.7%, name-like tokens/doc {'p50': 6.0, 'p95': 11.0}
- section headers (share of docs): {'klinische gegevens': 0.378, 'conclusie': 0.176, 'indicatie': 0.104, 'bevindingen': 0.022, 'voorgeschiedenis': 0.009, 'advies': 0.008}

### uitgaandebrief_20251208.inhoud

- documents in window: 12,244 across 4,164 patients; docs/patient {'p50': 2.0, 'p95': 7.0, 'p100': 24.0}
- chars/doc {'p5': 854.0, 'p50': 3570.5, 'p95': 8301.4, 'p100': 19106.0} | words/doc {'p5': 101.0, 'p50': 421.0, 'p95': 930.0, 'p100': 2292.0}
- tokens/doc {'p5': 313.0, 'p50': 1349.5, 'p95': 3455.0, 'p100': 7235.0} | tokens/patient {'p5': 935.15, 'p50': 3347.0, 'p95': 11881.35, 'p100': 41913.0} | total 18,809,015
- `datediff` of documents: {'p0': -3031.0, 'p5': -976.85, 'p50': -34.0, 'p95': 137.0, 'p100': 179.0}
- modal document length: 2814 chars in 0.1% of documents
- **12,189 distinct documents** of 12,244 (99.6% distinct); 79 share their text with another document
- **boilerplate: 0% of a median document's 8-grams are shared with >=30% of documents** (0 common n-grams, 4,000 sampled)
- de-id risk: ISO dates in 0.3% of docs, NL dates 94.1%, clinician tokens 99.5%, name-like tokens/doc {'p50': 50.0, 'p95': 117.0}
- section headers (share of docs): {'voorgeschiedenis': 0.799, 'anamnese': 0.691, 'conclusie': 0.642, 'beleid': 0.548, 'lichamelijk onderzoek': 0.521, 'indicatie': 0.212, 'samenvatting': 0.193, 'advies': 0.165, 'bevindingen': 0.114, 'klinische gegevens': 0.026}

## §4 T0 control — how much signal is in text VOLUME alone (no content)?

Permutation-calibrated null: SE(C) = 0.319/sqrt(events); with 1,827 events the 2-SE floor is **0.0149**.

**Every content arm must be shown to beat these numbers.** Otherwise a text 'signal' is only saying that sicker patients accumulate more notes — the same artefact as the `gfr_count` C=0.851 that turned out to be pure missingness.

| volume feature | C | clears 2-SE floor? |
|---|---|---|
| n_tokens_total | 0.4931 | no |
| n_chars_total | 0.4935 | no |
| n_documents_total | 0.4939 | no |
| n_docs[radiologie_verslag_20251208] | 0.4948 | no |
| n_sources_with_text | 0.4953 | no |
| n_docs[consult_20251208] | 0.4958 | no |
| has_any_text | 0.4961 | no |
| n_docs[mri_verslag_20250626] | 0.4966 | no |
| n_docs[uitgaandebrief_20251208] | 0.4973 | no |

> No volume feature clears the floor. A later content gain can therefore be attributed to content rather than to note-taking intensity.


=== wrote /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/eda_text/eda_text_report.md and eda_text_report.json ===
Paste eda_text_report.md back into the chat.
```

</details>

---

### RUN 2026-08-26T11:35:55Z | text arm: volume

- status: ok
- context: mode=volume landmark=180 horizon=5475 analyzer=word require_text=False strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_volume n_features=9 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: mode=volume landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=False strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  raw feature matrix: 13,434 patients x 9 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  1,136 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.323/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  9 features tested = ~4 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~0 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<1.3e-02): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  text.recency                              0.4881  0.4854  72.2%   828  1.30          
  text.history_span                         0.4985  0.4895  72.2%   828  0.94          
  text.n_docs[radiologie_verslag_20251208]  0.5039  0.4945 100.0% 1,136  0.58          
  text.n_chars                              0.4995  0.4952 100.0% 1,136  0.50          
  text.n_docs[mri_verslag_20250626]         0.4954  0.4954 100.0% 1,136  0.48          
  text.n_sources                            0.5036  0.5009 100.0% 1,136  0.38          
  text.n_documents                          0.5004  0.5031 100.0% 1,136  0.32          
  text.n_docs[uitgaandebrief_20251208]      0.5007  0.5007 100.0% 1,136  0.07          
  text.n_docs[consult_20251208]             0.4997  0.4997 100.0% 1,136  0.03          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  imputed 7,580 missing cells with the train median, then standardised
  train      : 8,599 patients | events=1,136 (13.2%) | features=9
  validation : 2,141 patients | events=310 (14.5%) | features=9
  test       : 2,694 patients | events=381 (14.1%) | features=9
RESULT: arm=text_volume n_features=9 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume model=mlp model.input_size=9
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:36:15Z | text arm: volume

- status: ok
- context: mode=volume landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_volume n_features=9 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=volume landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  raw feature matrix: 9,644 patients x 9 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  9 features tested = ~6 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~0 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<8.3e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  text.recency                              0.4881  0.4854 100.0%   828  1.44          
  text.history_span                         0.4985  0.4895 100.0%   828  1.04          
  text.n_docs[radiologie_verslag_20251208]  0.5005  0.4922 100.0%   828  0.77          
  text.n_documents                          0.4953  0.4927 100.0%   828  0.72          
  text.n_docs[mri_verslag_20250626]         0.4934  0.4934 100.0%   828  0.65          
  text.n_chars                              0.4935  0.4971 100.0%   828  0.64          
  text.n_docs[consult_20251208]             0.4955  0.4937 100.0%   828  0.62          
  text.n_sources                            0.5013  0.5013 100.0%   828  0.13          
  text.n_docs[uitgaandebrief_20251208]      0.4996  0.4996 100.0%   828  0.04          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=9
  validation : 1,510 patients | events=206 (13.6%) | features=9
  test       : 1,924 patients | events=257 (13.4%) | features=9
RESULT: arm=text_volume n_features=9 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T0_volume_rt model=mlp model.input_size=9
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:36:29Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.42; a low share is normal for text LSA)
  raw feature matrix: 9,644 patients x 256 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  256 features tested = ~243 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 20 (~12 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<2.1e-04): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  tfidf.svd_123                             0.4680  0.4891 100.0%   828  3.16    raw2SE
  tfidf.svd_65                              0.4706  0.5084 100.0%   828  2.90    raw2SE
  tfidf.svd_93                              0.5032  0.5287 100.0%   828  2.84    raw2SE
  tfidf.svd_251                             0.4721  0.5091 100.0%   828  2.75    raw2SE
  tfidf.svd_84                              0.4834  0.5253 100.0%   828  2.50    raw2SE
  tfidf.svd_177                             0.5251  0.5014 100.0%   828  2.47    raw2SE
  tfidf.svd_237                             0.5245  0.4806 100.0%   828  2.41    raw2SE
  tfidf.svd_87                              0.4759  0.4956 100.0%   828  2.38    raw2SE
  tfidf.svd_55                              0.4926  0.5240 100.0%   828  2.37    raw2SE
  tfidf.svd_106                             0.4925  0.5232 100.0%   828  2.29    raw2SE
  tfidf.svd_35                              0.4965  0.5231 100.0%   828  2.28    raw2SE
  tfidf.svd_61                              0.4995  0.5228 100.0%   828  2.25    raw2SE
  tfidf.svd_241                             0.5220  0.5043 100.0%   828  2.17    raw2SE
  tfidf.svd_222                             0.5103  0.4782 100.0%   828  2.15    raw2SE
  tfidf.svd_114                             0.5211  0.5021 100.0%   828  2.08    raw2SE
  tfidf.svd_26                              0.5211  0.4900 100.0%   828  2.08    raw2SE
  tfidf.svd_212                             0.5210  0.4918 100.0%   828  2.07    raw2SE
  tfidf.svd_139                             0.5208  0.5059 100.0%   828  2.05    raw2SE
  tfidf.svd_210                             0.5054  0.4794 100.0%   828  2.04    raw2SE
  tfidf.svd_137                             0.4881  0.5203 100.0%   828  2.00    raw2SE
  tfidf.svd_75                              0.4885  0.5201 100.0%   828  1.98          
  tfidf.svd_132                             0.4799  0.5005 100.0%   828  1.98          
  tfidf.svd_60                              0.5093  0.5201 100.0%   828  1.98          
  tfidf.svd_22                              0.5039  0.5200 100.0%   828  1.98          
  tfidf.svd_191                             0.5040  0.4800 100.0%   828  1.98          
  tfidf.svd_99                              0.5199  0.5032 100.0%   828  1.97          
  tfidf.svd_7                               0.5135  0.5199 100.0%   828  1.96          
  tfidf.svd_173                             0.4872  0.4801 100.0%   828  1.96          
  tfidf.svd_159                             0.5199  0.5049 100.0%   828  1.96          
  tfidf.svd_183                             0.5166  0.4801 100.0%   828  1.96          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=256
  validation : 1,510 patients | events=206 (13.6%) | features=256
  test       : 1,924 patients | events=257 (13.4%) | features=256
RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word model=mlp model.input_size=256
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:38:41Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=word require_text=False strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word] n_features=256 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=False strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  after cleaning: 9,644 patients retain text (71.8%)
  3,790 patients have no text after cleaning and get an all-zero vector
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.45; a low share is normal for text LSA)
  raw feature matrix: 13,434 patients x 256 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 8,599 patients | events=1,136 (13.2%) | features=256
  validation : 2,141 patients | events=310 (14.5%) | features=256
  test       : 2,694 patients | events=381 (14.1%) | features=256
RESULT: arm=text_tfidf[word] n_features=256 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_word_full model=mlp model.input_size=256
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:40:26Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=char require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_char
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[char] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=char svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  TF-IDF analyzer=char vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.59; a low share is normal for text LSA)
  raw feature matrix: 9,644 patients x 256 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=256
  validation : 1,510 patients | events=206 (13.6%) | features=256
  test       : 1,924 patients | events=257 (13.4%) | features=256
RESULT: arm=text_tfidf[char] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_char
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_char model=mlp model.input_size=256
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:46:10Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 section=voorgeschiedenis,anamnese analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_history
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word]+section:voorgeschiedenis,anamnese n_features=128 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=voorgeschiedenis,anamnese analyzer=word svd=128 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  after cleaning + section=voorgeschiedenis,anamnese: 5,085 patients retain text (52.7%)
  4,559 patients have no text after cleaning/section and get an all-zero vector
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=128 (explained var=0.24; a low share is normal for text LSA)
  raw feature matrix: 9,644 patients x 128 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=128
  validation : 1,510 patients | events=206 (13.6%) | features=128
  test       : 1,924 patients | events=257 (13.4%) | features=128
RESULT: arm=text_tfidf[word]+section:voorgeschiedenis,anamnese n_features=128 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_history
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_history model=mlp model.input_size=128
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:47:08Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 section=conclusie analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_conclusie
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word]+section:conclusie n_features=128 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=conclusie analyzer=word svd=128 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  after cleaning + section=conclusie: 5,730 patients retain text (59.4%)
  3,914 patients have no text after cleaning/section and get an all-zero vector
  TF-IDF analyzer=word vocab=34,647 (max_df=0.8 drops boilerplate)
  SVD dim=128 (explained var=0.33; a low share is normal for text LSA)
  raw feature matrix: 9,644 patients x 128 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=128
  validation : 1,510 patients | events=206 (13.6%) | features=128
  test       : 1,924 patients | events=257 (13.4%) | features=128
RESULT: arm=text_tfidf[word]+section:conclusie n_features=128 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_conclusie
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_conclusie model=mlp model.input_size=128
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:47:54Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=True concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_nonames
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=True concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.39; a low share is normal for text LSA)
  raw feature matrix: 9,644 patients x 256 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=256
  validation : 1,510 patients | events=206 (13.6%) | features=256
  test       : 1,924 patients | events=257 (13.4%) | features=256
RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_nonames
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_nonames model=mlp model.input_size=256
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:49:43Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_3src
- RESULT: documents=120776 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  cached 75,445 documents from consult_20251208.consult_tekst
  cached 33,087 documents from radiologie_verslag_20251208.verslagtekst
  cached 12,244 documents from uitgaandebrief_20251208.inhoud
  document cache: 120,776 documents -> /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents_3src.parquet
RESULT: documents=120776 patients_with_text=9644/13434 (71.8%)
  120,776 documents, 9,644/13,434 patients have text (71.8%)
  --require-text: cohort restricted to 9,644 patients with text (1,431 events) | train=6,210 val=1,510 test=1,924
  NOTE: benchmarks measured on the FULL cohort do not apply to this subcohort. Build the matched control with --mode baseline --require-text.
  after cleaning: 9,644 patients retain text (100.0%)
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.42; a low share is normal for text LSA)
  raw feature matrix: 9,644 patients x 256 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=256
  validation : 1,510 patients | events=206 (13.6%) | features=256
  test       : 1,924 patients | events=257 (13.4%) | features=256
RESULT: arm=text_tfidf[word] n_features=256 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_3src
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_3src model=mlp model.input_size=256
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:51:44Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_demo
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word]+baseline[leeftijd,geslacht] n_features=258 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
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
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.42; a low share is normal for text LSA)
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 258 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=258
  validation : 1,510 patients | events=206 (13.6%) | features=258
  test       : 1,924 patients | events=257 (13.4%) | features=258
RESULT: arm=text_tfidf[word]+baseline[leeftijd,geslacht] n_features=258 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_demo
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T1_tfidf_demo model=mlp model.input_size=258
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:53:37Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
- RESULT: arm=text_concepts[binary] n_features=39 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  angina                         2,132     1,610       155   (22.1% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,724       947        74   (28.2% asserted)
  hartfalen                      1,004     1,678        97   (10.4% asserted)
  hyperlipidemie                 3,516       874       119   (36.5% asserted)
  hypertensie                    3,860     1,186       249   (40.0% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                    2,024       367        61   (21.0% asserted)
  perifeer_vaatlijden            1,381       455        97   (14.3% asserted)
  revascularisatie               4,477     1,297       216   (46.4% asserted)
  roken                          3,796     1,155        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
  raw feature matrix: 9,644 patients x 39 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  39 features tested = ~35 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~2 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<1.4e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  concept.perifeer_vaatlijden_present       0.4857  0.4857 100.0%   828  1.41          
  concept.diabetes_present                  0.4859  0.4859 100.0%   828  1.39          
  concept.hyperlipidemie_present            0.4873  0.4873 100.0%   828  1.26          
  concept.hypertensie_negated               0.4874  0.4874 100.0%   828  1.24          
  concept.nierfunctie_present               0.4893  0.4893 100.0%   828  1.05          
  concept.myocardinfarct_present            0.4917  0.4917 100.0%   828  0.82          
  concept.atriumfibrilleren_present         0.4918  0.4918 100.0%   828  0.81          
  concept.stenose_present                   0.4924  0.4924 100.0%   828  0.75          
  concept.angina_present                    0.4928  0.4928 100.0%   828  0.71          
  concept.angina_uncertain                  0.5058  0.5058 100.0%   828  0.57          
  concept.myocardinfarct_uncertain          0.4943  0.4943 100.0%   828  0.57          
  concept.hartfalen_negated                 0.5051  0.5051 100.0%   828  0.50          
  concept.myocardinfarct_negated            0.4953  0.4953 100.0%   828  0.46          
  concept.cva_tia_present                   0.4956  0.4956 100.0%   828  0.43          
  concept.diabetes_negated                  0.4959  0.4959 100.0%   828  0.41          
  concept.perifeer_vaatlijden_negated       0.4961  0.4961 100.0%   828  0.39          
  concept.hypertensie_present               0.4965  0.4965 100.0%   828  0.35          
  concept.cva_tia_uncertain                 0.5034  0.5034 100.0%   828  0.34          
  concept.revascularisatie_present          0.4969  0.4969 100.0%   828  0.31          
  concept.angina_negated                    0.4969  0.4969 100.0%   828  0.31          
  concept.revascularisatie_negated          0.5029  0.5029 100.0%   828  0.29          
  concept.hartfalen_present                 0.4972  0.4972 100.0%   828  0.27          
  concept.atriumfibrilleren_negated         0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_uncertain                 0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_negated                   0.5021  0.5021 100.0%   828  0.21          
  concept.hyperlipidemie_uncertain          0.5018  0.5018 100.0%   828  0.18          
  concept.roken_negated                     0.5017  0.5017 100.0%   828  0.16          
  concept.nierfunctie_negated               0.4985  0.4985 100.0%   828  0.15          
  concept.cva_tia_negated                   0.4986  0.4986 100.0%   828  0.14          
  concept.hartfalen_uncertain               0.4987  0.4987 100.0%   828  0.13          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=39
  validation : 1,510 patients | events=206 (13.6%) | features=39
  test       : 1,924 patients | events=257 (13.4%) | features=39
RESULT: arm=text_concepts[binary] n_features=39 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts model=mlp model.input_size=39
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:54:43Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=both out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
- RESULT: arm=text_concepts[both] n_features=78 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=both expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  78 concept features (encoding=both) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  angina                         2,132     1,610       155   (22.1% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,724       947        74   (28.2% asserted)
  hartfalen                      1,004     1,678        97   (10.4% asserted)
  hyperlipidemie                 3,516       874       119   (36.5% asserted)
  hypertensie                    3,860     1,186       249   (40.0% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                    2,024       367        61   (21.0% asserted)
  perifeer_vaatlijden            1,381       455        97   (14.3% asserted)
  revascularisatie               4,477     1,297       216   (46.4% asserted)
  roken                          3,796     1,155        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
  raw feature matrix: 9,644 patients x 78 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=78
  validation : 1,510 patients | events=206 (13.6%) | features=78
  test       : 1,924 patients | events=257 (13.4%) | features=78
RESULT: arm=text_concepts[both] n_features=78 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both model=mlp model.input_size=78
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:55:37Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
- RESULT: arm=text_concepts[binary]+baseline[leeftijd,geslacht] n_features=41 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
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
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  angina                         2,132     1,610       155   (22.1% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,724       947        74   (28.2% asserted)
  hartfalen                      1,004     1,678        97   (10.4% asserted)
  hyperlipidemie                 3,516       874       119   (36.5% asserted)
  hypertensie                    3,860     1,186       249   (40.0% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                    2,024       367        61   (21.0% asserted)
  perifeer_vaatlijden            1,381       455        97   (14.3% asserted)
  revascularisatie               4,477     1,297       216   (46.4% asserted)
  roken                          3,796     1,155        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4477, hypertensie=3860, roken=3796, hyperlipidemie=3516
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 41 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  41 features tested = ~36 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 2 (~2 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 2 | surviving Bonferroni (p<1.4e-03): 2  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  smart_baseline.leeftijd                   0.6731  0.5170 100.0%   828 17.08      BONF
  smart_baseline.geslacht                   0.4422  0.4422 100.0%   828  5.71      BONF
  concept.perifeer_vaatlijden_present       0.4857  0.4857 100.0%   828  1.41          
  concept.diabetes_present                  0.4859  0.4859 100.0%   828  1.39          
  concept.hyperlipidemie_present            0.4873  0.4873 100.0%   828  1.26          
  concept.hypertensie_negated               0.4874  0.4874 100.0%   828  1.24          
  concept.nierfunctie_present               0.4893  0.4893 100.0%   828  1.05          
  concept.myocardinfarct_present            0.4917  0.4917 100.0%   828  0.82          
  concept.atriumfibrilleren_present         0.4918  0.4918 100.0%   828  0.81          
  concept.stenose_present                   0.4924  0.4924 100.0%   828  0.75          
  concept.angina_present                    0.4928  0.4928 100.0%   828  0.71          
  concept.angina_uncertain                  0.5058  0.5058 100.0%   828  0.57          
  concept.myocardinfarct_uncertain          0.4943  0.4943 100.0%   828  0.57          
  concept.hartfalen_negated                 0.5051  0.5051 100.0%   828  0.50          
  concept.myocardinfarct_negated            0.4953  0.4953 100.0%   828  0.46          
  concept.cva_tia_present                   0.4956  0.4956 100.0%   828  0.43          
  concept.diabetes_negated                  0.4959  0.4959 100.0%   828  0.41          
  concept.perifeer_vaatlijden_negated       0.4961  0.4961 100.0%   828  0.39          
  concept.hypertensie_present               0.4965  0.4965 100.0%   828  0.35          
  concept.cva_tia_uncertain                 0.5034  0.5034 100.0%   828  0.34          
  concept.revascularisatie_present          0.4969  0.4969 100.0%   828  0.31          
  concept.angina_negated                    0.4969  0.4969 100.0%   828  0.31          
  concept.revascularisatie_negated          0.5029  0.5029 100.0%   828  0.29          
  concept.hartfalen_present                 0.4972  0.4972 100.0%   828  0.27          
  concept.atriumfibrilleren_negated         0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_uncertain                 0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_negated                   0.5021  0.5021 100.0%   828  0.21          
  concept.hyperlipidemie_uncertain          0.5018  0.5018 100.0%   828  0.18          
  concept.roken_negated                     0.5017  0.5017 100.0%   828  0.16          
  concept.nierfunctie_negated               0.4985  0.4985 100.0%   828  0.15          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=41
  validation : 1,510 patients | events=206 (13.6%) | features=41
  test       : 1,924 patients | events=257 (13.4%) | features=41
RESULT: arm=text_concepts[binary]+baseline[leeftijd,geslacht] n_features=41 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo model=mlp model.input_size=41
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:56:44Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 section=voorgeschiedenis,anamnese analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 5085 patients with text): roken=3302, hypertensie=3212, hyperlipidemie=2489, revascularisatie=2343
- RESULT: arm=text_concepts[binary] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=voorgeschiedenis,anamnese analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  after cleaning + section=voorgeschiedenis,anamnese: 5,085 patients retain text (52.7%)
  4,559 patients have no text after cleaning/section and get an all-zero vector
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  angina                         1,583     1,441        71   (31.1% asserted)
  atriumfibrilleren                588       103        37   (11.6% asserted)
  cva_tia                        1,305       298       179   (25.7% asserted)
  diabetes                       2,231       706        33   (43.9% asserted)
  hartfalen                        419       193        31   (8.2% asserted)
  hyperlipidemie                 2,489       668        45   (48.9% asserted)
  hypertensie                    3,212       905       101   (63.2% asserted)
  myocardinfarct                 1,865       319       130   (36.7% asserted)
  nierfunctie                      895       322         7   (17.6% asserted)
  perifeer_vaatlijden            1,082       295        40   (21.3% asserted)
  revascularisatie               2,343       390        56   (46.1% asserted)
  roken                          3,302       763        22   (64.9% asserted)
  stenose                        1,509       488        89   (29.7% asserted)
RESULT: concept prevalence (asserted, of 5085 patients with text): roken=3302, hypertensie=3212, hyperlipidemie=2489, revascularisatie=2343
  raw feature matrix: 9,644 patients x 39 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 1 features constant or all-missing on train
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=38
  validation : 1,510 patients | events=206 (13.6%) | features=38
  test       : 1,924 patients | events=257 (13.4%) | features=38
RESULT: arm=text_concepts[binary] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history model=mlp model.input_size=38
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:57:27Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[leeftijd,geslacht] n_features=2 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  MATCHED CONTROL (leeftijd,geslacht): 2 baseline features -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 2 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=2
  validation : 1,510 patients | events=206 (13.6%) | features=2
  test       : 1,924 patients | events=257 (13.4%) | features=2
RESULT: arm=matched_baseline[leeftijd,geslacht] n_features=2 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_rt model=mlp model.input_size=2
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:57:33Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[all] n_features=183 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  MATCHED CONTROL (all): 183 baseline features -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 183 features
  winsorised at train quantiles [0.001, 0.999]
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 162,074 missing cells with the train median, then standardised
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
  train      : 6,210 patients | events=828 (13.3%) | features=183
  validation : 1,510 patients | events=206 (13.6%) | features=183
  test       : 1,924 patients | events=257 (13.4%) | features=183
RESULT: arm=matched_baseline[all] n_features=183 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_rt model=mlp model.input_size=183
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:57:46Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=False strip_nameish=False concept_encoding=binary baseline_cols=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[leeftijd,geslacht] n_features=2 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=False strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  MATCHED CONTROL (leeftijd,geslacht): 2 baseline features -> ['geslacht', 'leeftijd']
  raw feature matrix: 13,434 patients x 2 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4448
    smart_baseline.leeftijd: train C=0.6742
  train      : 8,599 patients | events=1,136 (13.2%) | features=2
  validation : 2,141 patients | events=310 (14.5%) | features=2
  test       : 2,694 patients | events=381 (14.1%) | features=2
RESULT: arm=matched_baseline[leeftijd,geslacht] n_features=2 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_demo_full model=mlp model.input_size=2
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:57:52Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=False strip_nameish=False concept_encoding=binary baseline_cols=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[all] n_features=183 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=False strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  MATCHED CONTROL (all): 183 baseline features -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 13,434 patients x 183 features
  winsorised at train quantiles [0.001, 0.999]
  3 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 226,844 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4448
    smart_baseline.leeftijd: train C=0.6742
    smart_baseline.opleiding: train C=0.4711   ** suspiciously flat **
    smart_baseline.RespLand: train C=0.4994   ** suspiciously flat **
    smart_baseline.PaLand: train C=0.5046   ** suspiciously flat **
    smart_baseline.MaLand: train C=0.5035   ** suspiciously flat **
    smart_baseline.WereldDl: train C=0.4958   ** suspiciously flat **
    smart_baseline.diagnsco: train C=0.5511
    smart_baseline.vaatzkt1: train C=0.4456
    smart_baseline.DiagSide: train C=0.5053   ** suspiciously flat **
    smart_baseline.IncInt_p: train C=0.4683
    smart_baseline.IncInt_v: train C=0.4912   ** suspiciously flat **
    smart_baseline.V0405: train C=0.5127   ** suspiciously flat **
    smart_baseline.vg_0410: train C=0.5298   ** suspiciously flat **
    smart_baseline.vgok_car: train C=0.5093   ** suspiciously flat **
    smart_baseline.vgt_kop: train C=0.5354
    smart_baseline.vz_kop: train C=0.5461
    smart_baseline.vg_0321: train C=0.5604
    smart_baseline.vg_0323: train C=0.5115   ** suspiciously flat **
    smart_baseline.vgok_har: train C=0.5448
    smart_baseline.vgt_hart: train C=0.5718
    smart_baseline.vz_hart: train C=0.5635
    smart_baseline.vg_0325: train C=0.5388
    smart_baseline.vgok_aaa: train C=0.5058   ** suspiciously flat **
    smart_baseline.vgt_aaa: train C=0.5395
    smart_baseline.vz_aaa: train C=0.5413
    smart_baseline.vg_0606c: train C=0.5040   ** suspiciously flat **
    smart_baseline.vgok_nie: train C=0.5005   ** suspiciously flat **
    smart_baseline.vgt_nier: train C=0.5044   ** suspiciously flat **
    smart_baseline.vz_nier: train C=0.5092   ** suspiciously flat **
    smart_baseline.vg_0519: train C=0.5062   ** suspiciously flat **
    smart_baseline.vgok_bee: train C=0.5168   ** suspiciously flat **
    smart_baseline.vgt_been: train C=0.5173   ** suspiciously flat **
    smart_baseline.vz_been: train C=0.5399
    smart_baseline.bdsys: train C=0.5747
    smart_baseline.bddia: train C=0.4890   ** suspiciously flat **
    smart_baseline.hyptns_n: train C=0.5378
    smart_baseline.hyptns_b: train C=0.5439
    smart_baseline.vz_hypt: train C=0.5508
    smart_baseline.labgluc: train C=0.5614
    smart_baseline.hypgly_n: train C=0.5439
    smart_baseline.hypgly_b: train C=0.5024   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5472
    smart_baseline.vz_t1d: train C=0.4992   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5480
    smart_baseline.klinman: train C=0.5993
    smart_baseline.gewicht: train C=0.5037   ** suspiciously flat **
    smart_baseline.lengte: train C=0.5009   ** suspiciously flat **
    smart_baseline.bm_indx: train C=0.5101   ** suspiciously flat **
    smart_baseline.bmi_30: train C=0.5021   ** suspiciously flat **
    smart_baseline.tail_gm: train C=0.5625
    smart_baseline.heup_gm: train C=0.4969   ** suspiciously flat **
    smart_baseline.tlhp_rat: train C=0.5000   ** suspiciously flat **
    smart_baseline.vet_subc: train C=0.4561
    smart_baseline.vet_gm: train C=0.5619
    smart_baseline.plsprs: train C=0.6089
    smart_baseline.abi_lg: train C=0.4912   ** suspiciously flat **
    smart_baseline.abi_gm: train C=0.4968   ** suspiciously flat **
    smart_baseline.abivrl_n: train C=0.5766
    smart_baseline.ABiRe: train C=0.4917   ** suspiciously flat **
    smart_baseline.ABiLi: train C=0.4969   ** suspiciously flat **
    smart_baseline.imt_gm: train C=0.5210   ** suspiciously flat **
    smart_baseline.stenACIr: train C=0.6400
    smart_baseline.stenACIl: train C=0.6420
    smart_baseline.csten_50: train C=0.5565
    smart_baseline.csten_70: train C=0.5479
    smart_baseline.AortProx: train C=0.5363
    smart_baseline.AortDist: train C=0.5811
    smart_baseline.aorta_hg: train C=0.5648
    smart_baseline.aorta_gm: train C=0.5612
    smart_baseline.aaaech_n: train C=0.5364
    smart_baseline.nrlng_re: train C=0.4931   ** suspiciously flat **
    smart_baseline.nrlng_li: train C=0.4763   ** suspiciously flat **
    smart_baseline.nrlng_gm: train C=0.4815   ** suspiciously flat **
    smart_baseline.nratrof: train C=0.5147   ** suspiciously flat **
    smart_baseline.nrvol_re: train C=0.5044   ** suspiciously flat **
    smart_baseline.nrvol_li: train C=0.4869   ** suspiciously flat **
    smart_baseline.nrvol_gm: train C=0.4964   ** suspiciously flat **
    smart_baseline.labhb: train C=0.4905   ** suspiciously flat **
    smart_baseline.labht: train C=0.5038   ** suspiciously flat **
    smart_baseline.labchol: train C=0.4818   ** suspiciously flat **
    smart_baseline.labtrig: train C=0.5303
    smart_baseline.labhdl: train C=0.4657
    smart_baseline.ldlchol: train C=0.4895   ** suspiciously flat **
    smart_baseline.VgBh_HpL: train C=0.5102   ** suspiciously flat **
    smart_baseline.hyplip_n: train C=0.4908   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5239   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5101   ** suspiciously flat **
    smart_baseline.labkrea: train C=0.6168
    smart_baseline.labmalb: train C=0.5691
    smart_baseline.labkrur: train C=0.4393
    smart_baseline.mpkr_rat: train C=0.5912
    smart_baseline.albminur: train C=0.5568
    smart_baseline.nrfaln_n: train C=0.5638
    smart_baseline.klar_coc: train C=0.3634
    smart_baseline.klar_gst: train C=0.3916
    smart_baseline.MDRD: train C=0.3885
    smart_baseline.labhcyst: train C=0.5883
    smart_baseline.hyphmc_n: train C=0.5391
    smart_baseline.labins: train C=0.5272   ** suspiciously flat **
    smart_baseline.labtsh: train C=0.5193   ** suspiciously flat **
    smart_baseline.labcrp: train C=0.5948
    smart_baseline.labhba1c: train C=0.5581
    smart_baseline.labapob: train C=0.4959   ** suspiciously flat **
    smart_baseline.roken: train C=0.5654
    smart_baseline.packyrs: train C=0.6066
    smart_baseline.alcohol: train C=0.4519
    smart_baseline.AlchlGlz: train C=0.4987   ** suspiciously flat **
    smart_baseline.V0821: train C=0.4939   ** suspiciously flat **
    smart_baseline.V082201: train C=0.5021   ** suspiciously flat **
    smart_baseline.V082202: train C=0.5018   ** suspiciously flat **
    smart_baseline.V0823: train C=0.4999   ** suspiciously flat **
    smart_baseline.MBSc: train C=0.5672
    smart_baseline.MBS: train C=0.5530
    smart_baseline.MBSc_mis: train C=0.5666
    smart_baseline.MBScgr: train C=0.5567
    smart_baseline.kl1fysfc: train C=0.4025
    smart_baseline.kl2socfc: train C=0.4499
    smart_baseline.kl3rolfy: train C=0.4555
    smart_baseline.kl4rolem: train C=0.4915   ** suspiciously flat **
    smart_baseline.kl5mengz: train C=0.4859   ** suspiciously flat **
    smart_baseline.kl6vital: train C=0.4582
    smart_baseline.kl7pijn: train C=0.4411
    smart_baseline.kl8alggz: train C=0.4231
    smart_baseline.kl9gezva: train C=0.4968   ** suspiciously flat **
    smart_baseline.mht01: train C=0.5309
    smart_baseline.mht02: train C=0.5387
    smart_baseline.mht02a: train C=0.5374
    smart_baseline.mht02b: train C=0.5015   ** suspiciously flat **
    smart_baseline.mht02c: train C=0.5048   ** suspiciously flat **
    smart_baseline.mht02d: train C=0.5094   ** suspiciously flat **
    smart_baseline.mht03: train C=0.5232   ** suspiciously flat **
    smart_baseline.mht04: train C=0.5322
    smart_baseline.mht05: train C=0.5018   ** suspiciously flat **
    smart_baseline.mht06: train C=0.5036   ** suspiciously flat **
    smart_baseline.mht07: train C=0.4996   ** suspiciously flat **
    smart_baseline.mht12: train C=0.5164   ** suspiciously flat **
    smart_baseline.mht33: train C=0.5017   ** suspiciously flat **
    smart_baseline.mht41: train C=0.5000   ** suspiciously flat **
    smart_baseline.mliphoop: train C=0.5107   ** suspiciously flat **
    smart_baseline.mli01: train C=0.5099   ** suspiciously flat **
    smart_baseline.mli02: train C=0.4990   ** suspiciously flat **
    smart_baseline.mli03: train C=0.5004   ** suspiciously flat **
    smart_baseline.mli04: train C=0.5008   ** suspiciously flat **
    smart_baseline.mas01: train C=0.5612
    smart_baseline.mas01a: train C=0.5138   ** suspiciously flat **
    smart_baseline.mas01b: train C=0.5061   ** suspiciously flat **
    smart_baseline.mas01c: train C=0.5098   ** suspiciously flat **
    smart_baseline.mas01d: train C=0.5028   ** suspiciously flat **
    smart_baseline.mas02: train C=0.5355
    smart_baseline.mas02a: train C=0.5179   ** suspiciously flat **
    smart_baseline.mas02b: train C=0.5054   ** suspiciously flat **
    smart_baseline.mas02c: train C=0.4997   ** suspiciously flat **
    smart_baseline.mas03: train C=0.5001   ** suspiciously flat **
    smart_baseline.mmpr: train C=0.5330
    smart_baseline.mhmc: train C=0.5059   ** suspiciously flat **
    smart_baseline.mgl01: train C=0.5297   ** suspiciously flat **
    smart_baseline.mgl02: train C=0.5155   ** suspiciously flat **
    smart_baseline.mgl03: train C=0.5004   ** suspiciously flat **
    smart_baseline.TCA: train C=0.4984   ** suspiciously flat **
    smart_baseline.SSRI: train C=0.4980   ** suspiciously flat **
    smart_baseline.MAO: train C=0.5000   ** suspiciously flat **
    smart_baseline.OthADep: train C=0.5097   ** suspiciously flat **
    smart_baseline.Benzo: train C=0.5036   ** suspiciously flat **
    smart_baseline.BenzoDer: train C=0.5063   ** suspiciously flat **
    smart_baseline.BenzoRel: train C=0.4999   ** suspiciously flat **
    smart_baseline.Thyr: train C=0.4987   ** suspiciously flat **
    smart_baseline.Amiodar: train C=0.5013   ** suspiciously flat **
    smart_baseline.Lithium: train C=0.5001   ** suspiciously flat **
    smart_baseline.mht_alln: train C=0.5736
    smart_baseline.mht_all: train C=0.5586
    smart_baseline.lipmid: train C=0.5224   ** suspiciously flat **
    smart_baseline.statine: train C=0.5210   ** suspiciously flat **
    smart_baseline.pamid: train C=0.5612
    smart_baseline.aspirine: train C=0.5567
    smart_baseline.pa_stolmid: train C=0.5876
    smart_baseline.KliMaC: train C=0.6167
    smart_baseline.KliMaYr: train C=0.3911
    smart_baseline.KliMaDur: train C=0.6061
    smart_baseline.KliMaDrD: train C=0.5971
    smart_baseline.spMEThw: train C=0.4418
    smart_baseline.acMEThw: train C=0.4631
    smart_baseline.bwMEThw: train C=0.4470
  train      : 8,599 patients | events=1,136 (13.2%) | features=183
  validation : 2,141 patients | events=310 (14.5%) | features=183
  test       : 2,694 patients | events=381 (14.1%) | features=183
RESULT: arm=matched_baseline[all] n_features=183 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_full model=mlp model.input_size=183
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:58:11Z | structured arm

- status: ok
- context: landmark=180 horizon=5475 positive_control=True baseline_cols=all auto_occurrence=False out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/STRUCT_ctrl
- RESULT: arm=smart_baseline[all] n_features=183 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: landmark=180/lookback=None horizon=5475 auto_occurrence=False add_baseline_cols=None baseline_cols='all' positive_control=True min_coverage_frac=0.1 aggregators=last,mean,slope,count
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events); survival now measured from day 180
  effective coverage floor: 860 train patients (= max(--min-patients, 10% of 8,599))
  cohort 13,434 patients | train=8,599 val=2,141 test=2,694
  BASELINE ARM (all): 183 numeric SMART baseline features -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 13,434 patients x 183 features
  winsorised at train quantiles [0.001, 0.999]
  3 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 226,844 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4448
    smart_baseline.leeftijd: train C=0.6742
    smart_baseline.opleiding: train C=0.4711   ** suspiciously flat **
    smart_baseline.RespLand: train C=0.4994   ** suspiciously flat **
    smart_baseline.PaLand: train C=0.5046   ** suspiciously flat **
    smart_baseline.MaLand: train C=0.5035   ** suspiciously flat **
    smart_baseline.WereldDl: train C=0.4958   ** suspiciously flat **
    smart_baseline.diagnsco: train C=0.5511
    smart_baseline.vaatzkt1: train C=0.4456
    smart_baseline.DiagSide: train C=0.5053   ** suspiciously flat **
    smart_baseline.IncInt_p: train C=0.4683
    smart_baseline.IncInt_v: train C=0.4912   ** suspiciously flat **
    smart_baseline.V0405: train C=0.5127   ** suspiciously flat **
    smart_baseline.vg_0410: train C=0.5298   ** suspiciously flat **
    smart_baseline.vgok_car: train C=0.5093   ** suspiciously flat **
    smart_baseline.vgt_kop: train C=0.5354
    smart_baseline.vz_kop: train C=0.5461
    smart_baseline.vg_0321: train C=0.5604
    smart_baseline.vg_0323: train C=0.5115   ** suspiciously flat **
    smart_baseline.vgok_har: train C=0.5448
    smart_baseline.vgt_hart: train C=0.5718
    smart_baseline.vz_hart: train C=0.5635
    smart_baseline.vg_0325: train C=0.5388
    smart_baseline.vgok_aaa: train C=0.5058   ** suspiciously flat **
    smart_baseline.vgt_aaa: train C=0.5395
    smart_baseline.vz_aaa: train C=0.5413
    smart_baseline.vg_0606c: train C=0.5040   ** suspiciously flat **
    smart_baseline.vgok_nie: train C=0.5005   ** suspiciously flat **
    smart_baseline.vgt_nier: train C=0.5044   ** suspiciously flat **
    smart_baseline.vz_nier: train C=0.5092   ** suspiciously flat **
    smart_baseline.vg_0519: train C=0.5062   ** suspiciously flat **
    smart_baseline.vgok_bee: train C=0.5168   ** suspiciously flat **
    smart_baseline.vgt_been: train C=0.5173   ** suspiciously flat **
    smart_baseline.vz_been: train C=0.5399
    smart_baseline.bdsys: train C=0.5747
    smart_baseline.bddia: train C=0.4890   ** suspiciously flat **
    smart_baseline.hyptns_n: train C=0.5378
    smart_baseline.hyptns_b: train C=0.5439
    smart_baseline.vz_hypt: train C=0.5508
    smart_baseline.labgluc: train C=0.5614
    smart_baseline.hypgly_n: train C=0.5439
    smart_baseline.hypgly_b: train C=0.5024   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5472
    smart_baseline.vz_t1d: train C=0.4992   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5480
    smart_baseline.klinman: train C=0.5993
    smart_baseline.gewicht: train C=0.5037   ** suspiciously flat **
    smart_baseline.lengte: train C=0.5009   ** suspiciously flat **
    smart_baseline.bm_indx: train C=0.5101   ** suspiciously flat **
    smart_baseline.bmi_30: train C=0.5021   ** suspiciously flat **
    smart_baseline.tail_gm: train C=0.5625
    smart_baseline.heup_gm: train C=0.4969   ** suspiciously flat **
    smart_baseline.tlhp_rat: train C=0.5000   ** suspiciously flat **
    smart_baseline.vet_subc: train C=0.4561
    smart_baseline.vet_gm: train C=0.5619
    smart_baseline.plsprs: train C=0.6089
    smart_baseline.abi_lg: train C=0.4912   ** suspiciously flat **
    smart_baseline.abi_gm: train C=0.4968   ** suspiciously flat **
    smart_baseline.abivrl_n: train C=0.5766
    smart_baseline.ABiRe: train C=0.4917   ** suspiciously flat **
    smart_baseline.ABiLi: train C=0.4969   ** suspiciously flat **
    smart_baseline.imt_gm: train C=0.5210   ** suspiciously flat **
    smart_baseline.stenACIr: train C=0.6400
    smart_baseline.stenACIl: train C=0.6420
    smart_baseline.csten_50: train C=0.5565
    smart_baseline.csten_70: train C=0.5479
    smart_baseline.AortProx: train C=0.5363
    smart_baseline.AortDist: train C=0.5811
    smart_baseline.aorta_hg: train C=0.5648
    smart_baseline.aorta_gm: train C=0.5612
    smart_baseline.aaaech_n: train C=0.5364
    smart_baseline.nrlng_re: train C=0.4931   ** suspiciously flat **
    smart_baseline.nrlng_li: train C=0.4763   ** suspiciously flat **
    smart_baseline.nrlng_gm: train C=0.4815   ** suspiciously flat **
    smart_baseline.nratrof: train C=0.5147   ** suspiciously flat **
    smart_baseline.nrvol_re: train C=0.5044   ** suspiciously flat **
    smart_baseline.nrvol_li: train C=0.4869   ** suspiciously flat **
    smart_baseline.nrvol_gm: train C=0.4964   ** suspiciously flat **
    smart_baseline.labhb: train C=0.4905   ** suspiciously flat **
    smart_baseline.labht: train C=0.5038   ** suspiciously flat **
    smart_baseline.labchol: train C=0.4818   ** suspiciously flat **
    smart_baseline.labtrig: train C=0.5303
    smart_baseline.labhdl: train C=0.4657
    smart_baseline.ldlchol: train C=0.4895   ** suspiciously flat **
    smart_baseline.VgBh_HpL: train C=0.5102   ** suspiciously flat **
    smart_baseline.hyplip_n: train C=0.4908   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5239   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5101   ** suspiciously flat **
    smart_baseline.labkrea: train C=0.6168
    smart_baseline.labmalb: train C=0.5691
    smart_baseline.labkrur: train C=0.4393
    smart_baseline.mpkr_rat: train C=0.5912
    smart_baseline.albminur: train C=0.5568
    smart_baseline.nrfaln_n: train C=0.5638
    smart_baseline.klar_coc: train C=0.3634
    smart_baseline.klar_gst: train C=0.3916
    smart_baseline.MDRD: train C=0.3885
    smart_baseline.labhcyst: train C=0.5883
    smart_baseline.hyphmc_n: train C=0.5391
    smart_baseline.labins: train C=0.5272   ** suspiciously flat **
    smart_baseline.labtsh: train C=0.5193   ** suspiciously flat **
    smart_baseline.labcrp: train C=0.5948
    smart_baseline.labhba1c: train C=0.5581
    smart_baseline.labapob: train C=0.4959   ** suspiciously flat **
    smart_baseline.roken: train C=0.5654
    smart_baseline.packyrs: train C=0.6066
    smart_baseline.alcohol: train C=0.4519
    smart_baseline.AlchlGlz: train C=0.4987   ** suspiciously flat **
    smart_baseline.V0821: train C=0.4939   ** suspiciously flat **
    smart_baseline.V082201: train C=0.5021   ** suspiciously flat **
    smart_baseline.V082202: train C=0.5018   ** suspiciously flat **
    smart_baseline.V0823: train C=0.4999   ** suspiciously flat **
    smart_baseline.MBSc: train C=0.5672
    smart_baseline.MBS: train C=0.5530
    smart_baseline.MBSc_mis: train C=0.5666
    smart_baseline.MBScgr: train C=0.5567
    smart_baseline.kl1fysfc: train C=0.4025
    smart_baseline.kl2socfc: train C=0.4499
    smart_baseline.kl3rolfy: train C=0.4555
    smart_baseline.kl4rolem: train C=0.4915   ** suspiciously flat **
    smart_baseline.kl5mengz: train C=0.4859   ** suspiciously flat **
    smart_baseline.kl6vital: train C=0.4582
    smart_baseline.kl7pijn: train C=0.4411
    smart_baseline.kl8alggz: train C=0.4231
    smart_baseline.kl9gezva: train C=0.4968   ** suspiciously flat **
    smart_baseline.mht01: train C=0.5309
    smart_baseline.mht02: train C=0.5387
    smart_baseline.mht02a: train C=0.5374
    smart_baseline.mht02b: train C=0.5015   ** suspiciously flat **
    smart_baseline.mht02c: train C=0.5048   ** suspiciously flat **
    smart_baseline.mht02d: train C=0.5094   ** suspiciously flat **
    smart_baseline.mht03: train C=0.5232   ** suspiciously flat **
    smart_baseline.mht04: train C=0.5322
    smart_baseline.mht05: train C=0.5018   ** suspiciously flat **
    smart_baseline.mht06: train C=0.5036   ** suspiciously flat **
    smart_baseline.mht07: train C=0.4996   ** suspiciously flat **
    smart_baseline.mht12: train C=0.5164   ** suspiciously flat **
    smart_baseline.mht33: train C=0.5017   ** suspiciously flat **
    smart_baseline.mht41: train C=0.5000   ** suspiciously flat **
    smart_baseline.mliphoop: train C=0.5107   ** suspiciously flat **
    smart_baseline.mli01: train C=0.5099   ** suspiciously flat **
    smart_baseline.mli02: train C=0.4990   ** suspiciously flat **
    smart_baseline.mli03: train C=0.5004   ** suspiciously flat **
    smart_baseline.mli04: train C=0.5008   ** suspiciously flat **
    smart_baseline.mas01: train C=0.5612
    smart_baseline.mas01a: train C=0.5138   ** suspiciously flat **
    smart_baseline.mas01b: train C=0.5061   ** suspiciously flat **
    smart_baseline.mas01c: train C=0.5098   ** suspiciously flat **
    smart_baseline.mas01d: train C=0.5028   ** suspiciously flat **
    smart_baseline.mas02: train C=0.5355
    smart_baseline.mas02a: train C=0.5179   ** suspiciously flat **
    smart_baseline.mas02b: train C=0.5054   ** suspiciously flat **
    smart_baseline.mas02c: train C=0.4997   ** suspiciously flat **
    smart_baseline.mas03: train C=0.5001   ** suspiciously flat **
    smart_baseline.mmpr: train C=0.5330
    smart_baseline.mhmc: train C=0.5059   ** suspiciously flat **
    smart_baseline.mgl01: train C=0.5297   ** suspiciously flat **
    smart_baseline.mgl02: train C=0.5155   ** suspiciously flat **
    smart_baseline.mgl03: train C=0.5004   ** suspiciously flat **
    smart_baseline.TCA: train C=0.4984   ** suspiciously flat **
    smart_baseline.SSRI: train C=0.4980   ** suspiciously flat **
    smart_baseline.MAO: train C=0.5000   ** suspiciously flat **
    smart_baseline.OthADep: train C=0.5097   ** suspiciously flat **
    smart_baseline.Benzo: train C=0.5036   ** suspiciously flat **
    smart_baseline.BenzoDer: train C=0.5063   ** suspiciously flat **
    smart_baseline.BenzoRel: train C=0.4999   ** suspiciously flat **
    smart_baseline.Thyr: train C=0.4987   ** suspiciously flat **
    smart_baseline.Amiodar: train C=0.5013   ** suspiciously flat **
    smart_baseline.Lithium: train C=0.5001   ** suspiciously flat **
    smart_baseline.mht_alln: train C=0.5736
    smart_baseline.mht_all: train C=0.5586
    smart_baseline.lipmid: train C=0.5224   ** suspiciously flat **
    smart_baseline.statine: train C=0.5210   ** suspiciously flat **
    smart_baseline.pamid: train C=0.5612
    smart_baseline.aspirine: train C=0.5567
    smart_baseline.pa_stolmid: train C=0.5876
    smart_baseline.KliMaC: train C=0.6167
    smart_baseline.KliMaYr: train C=0.3911
    smart_baseline.KliMaDur: train C=0.6061
    smart_baseline.KliMaDrD: train C=0.5971
    smart_baseline.spMEThw: train C=0.4418
    smart_baseline.acMEThw: train C=0.4631
    smart_baseline.bwMEThw: train C=0.4470
  train      : 8,599 patients | events=1,136 (13.2%) | features=183
  validation : 2,141 patients | events=310 (14.5%) | features=183
  test       : 2,694 patients | events=381 (14.1%) | features=183
RESULT: arm=smart_baseline[all] n_features=183 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/STRUCT_ctrl
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/STRUCT_ctrl model=mlp model.input_size=183
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-08-26T11:58:30Z | screen: CTRL_demo_full

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

  selected penalizer=0.01 -> TEST C=0.6883 (test 2-SE band around 0.5 is +/-0.051)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6883 (2-SE band +/-0.051) -> signal
```

</details>

---

### RUN 2026-08-26T11:58:59Z | screen: CTRL_demo_rt

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

  selected penalizer=0.1 -> TEST C=0.6727 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.1 TEST C=0.6727 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-08-26T11:59:18Z | screen: CTRL_full_full

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_full/ cox=True l1_ratio=1.0
- RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742

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
  penalizer=0.01     fit failed: ConvergenceError
  penalizer=0.1      fit failed: ConvergenceError
  penalizer=1        fit failed: ConvergenceError
  penalizer=10       fit failed: ConvergenceError
```

</details>

---

### RUN 2026-08-26T12:00:06Z | screen: CTRL_full_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/CTRL_full_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 103 of 183 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731

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
  penalizer=0.01     fit failed: ConvergenceError
  penalizer=0.1      fit failed: ConvergenceError
  penalizer=1        fit failed: ConvergenceError
  penalizer=10       fit failed: ConvergenceError
```

</details>

---

### RUN 2026-08-26T12:00:37Z | screen: STRUCT_ctrl

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/STRUCT_ctrl/ cox=True l1_ratio=1.0
- RESULT: univariate: 106 of 183 features clear the 0.0192 floor; strongest smart_baseline.leeftijd C=0.6742

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
  penalizer=0.01     fit failed: ConvergenceError
  penalizer=0.1      fit failed: ConvergenceError
  penalizer=1        fit failed: ConvergenceError
  penalizer=10       fit failed: ConvergenceError
```

</details>

---

### RUN 2026-08-26T12:01:24Z | screen: T0_volume

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

  selected penalizer=0.01 -> TEST C=0.5202 (test 2-SE band around 0.5 is +/-0.051)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.5202 (2-SE band +/-0.051) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:01:57Z | screen: T0_volume_rt

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

  selected penalizer=0.01 -> TEST C=0.5197 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.5197 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:02:19Z | screen: T1_tfidf_3src

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

  selected penalizer=0.1 -> TEST C=0.4907 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.4907 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:06:41Z | screen: T1_tfidf_char

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

  selected penalizer=0.01 -> TEST C=0.4963 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4963 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:11:09Z | screen: T1_tfidf_conclusie

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

  selected penalizer=0.01 -> TEST C=0.5089 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.5089 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:12:39Z | screen: T1_tfidf_demo

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

  selected penalizer=0.01 -> TEST C=0.6750 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6750 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-08-26T12:17:16Z | screen: T1_tfidf_history

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

  selected penalizer=0.01 -> TEST C=0.4897 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4897 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:18:45Z | screen: T1_tfidf_nonames

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

  selected penalizer=0.01 -> TEST C=0.4821 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4821 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:23:11Z | screen: T1_tfidf_word

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

  selected penalizer=0.1 -> TEST C=0.4914 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.4914 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:27:33Z | screen: T1_tfidf_word_full

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

  selected penalizer=0.01 -> TEST C=0.4957 (test 2-SE band around 0.5 is +/-0.051)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4957 (2-SE band +/-0.051) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:31:12Z | screen: T2_concepts

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 39 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.1 TEST C=0.5114 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts/
  representation=text_concepts[binary] | landmark_days=180 | horizon_days=5475 | n_features=39

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   39 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   39 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   39 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 39 effectively constant (zero variance, or one value in >99% of patients); 39 take <=10 distinct values (normal for counts)
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
  concept.perifeer_vaatlijden_present                  0.4857   0.4857   0.4941
  concept.diabetes_present                             0.4859   0.4859   0.4832
  concept.hyperlipidemie_present                       0.4873   0.4873   0.4602
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.nierfunctie_present                          0.4893   0.4893   0.5004
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4930
  concept.angina_uncertain                             0.5058   0.5058   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.hartfalen_negated                            0.5051   0.5051   0.4954
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4959   0.4959   0.4938
  concept.perifeer_vaatlijden_negated                  0.4961   0.4961   0.4985
  concept.hypertensie_present                          0.4965   0.4965   0.4988
  concept.cva_tia_uncertain                            0.5034   0.5034   0.4933
  concept.revascularisatie_present                     0.4969   0.4969   0.5094
  concept.angina_negated                               0.4969   0.4969   0.4877

  39 features are only ~35 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5327  val C=0.4831
  penalizer=0.1      train C=0.5255  val C=0.4941
  penalizer=1        train C=0.5255  val C=0.4941
  penalizer=10       train C=0.5255  val C=0.4941

  selected penalizer=0.1 -> TEST C=0.5114 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.5114 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:31:43Z | screen: T2_concepts_both

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 78 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.1 TEST C=0.5097 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both/
  representation=text_concepts[both] | landmark_days=180 | horizon_days=5475 | n_features=78

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   78 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   78 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   78 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 8 of 78 effectively constant (zero variance, or one value in >99% of patients); 56 take <=10 distinct values (normal for counts)
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
  concept.diabetes_present_n                           0.4823   0.4823   0.4858
  concept.perifeer_vaatlijden_present                  0.4857   0.4857   0.4941
  concept.diabetes_present                             0.4859   0.4859   0.4832
  concept.perifeer_vaatlijden_present_n                0.4865   0.4865   0.4936
  concept.hyperlipidemie_present                       0.4873   0.4873   0.4602
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.hyperlipidemie_present_n                     0.4875   0.4875   0.4686
  concept.hypertensie_negated_n                        0.4877   0.4877   0.5043
  concept.nierfunctie_present_n                        0.4891   0.4891   0.5011
  concept.nierfunctie_present                          0.4893   0.4893   0.5004
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.atriumfibrilleren_present_n                  0.4919   0.4919   0.4962
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4930
  concept.myocardinfarct_present_n                     0.4929   0.4929   0.5042
  concept.stenose_present_n                            0.4931   0.4931   0.4762
  concept.hypertensie_present_n                        0.4938   0.4938   0.4985
  concept.angina_present_n                             0.4940   0.4940   0.4915
  concept.revascularisatie_present_n                   0.4942   0.4942   0.5098

  78 features are only ~53 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~3 times, not ~4.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5328  val C=0.4846
  penalizer=0.1      train C=0.5253  val C=0.4939
  penalizer=1        train C=0.5253  val C=0.4939
  penalizer=10       train C=0.5253  val C=0.4939

  selected penalizer=0.1 -> TEST C=0.5097 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.5097 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-26T12:32:34Z | screen: T2_concepts_demo

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo/
  representation=text_concepts[binary]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=41

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   41 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   41 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   41 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 41 effectively constant (zero variance, or one value in >99% of patients); 40 take <=10 distinct values (normal for counts)
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
  concept.perifeer_vaatlijden_present                  0.4857   0.4857   0.4941
  concept.diabetes_present                             0.4859   0.4859   0.4832
  concept.hyperlipidemie_present                       0.4873   0.4873   0.4602
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.nierfunctie_present                          0.4893   0.4893   0.5004
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4930
  concept.angina_uncertain                             0.5058   0.5058   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.hartfalen_negated                            0.5051   0.5051   0.4954
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4959   0.4959   0.4938
  concept.perifeer_vaatlijden_negated                  0.4961   0.4961   0.4985
  concept.hypertensie_present                          0.4965   0.4965   0.4988
  concept.cva_tia_uncertain                            0.5034   0.5034   0.4933

  41 features are only ~36 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.6807  val C=0.7070
  penalizer=0.1      train C=0.6678  val C=0.6673
  penalizer=1        train C=0.6586  val C=0.6527
  penalizer=10       train C=0.6586  val C=0.6526

  selected penalizer=0.01 -> TEST C=0.6749 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-08-26T12:33:06Z | screen: T2_concepts_history

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 38 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=1 TEST C=0.5212 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history/
  representation=text_concepts[binary] | landmark_days=180 | horizon_days=5475 | n_features=38

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
  concept.diabetes_present                             0.4858   0.4858   0.4815
  concept.hyperlipidemie_present                       0.4909   0.4909   0.4666
  concept.angina_present                               0.4914   0.4914   0.4883
  concept.hypertensie_present                          0.4916   0.4916   0.4881
  concept.hypertensie_negated                          0.4923   0.4923   0.5068
  concept.perifeer_vaatlijden_present                  0.4925   0.4925   0.4950
  concept.atriumfibrilleren_present                    0.4932   0.4932   0.4978
  concept.angina_negated                               0.4939   0.4939   0.4881
  concept.perifeer_vaatlijden_negated                  0.4941   0.4941   0.5016
  concept.stenose_present                              0.4944   0.4944   0.4653
  concept.revascularisatie_negated                     0.5056   0.5056   0.4912
  concept.cva_tia_present                              0.4950   0.4950   0.4997
  concept.roken_negated                                0.5040   0.5040   0.4905
  concept.diabetes_negated                             0.4960   0.4960   0.4977
  concept.cva_tia_negated                              0.4965   0.4965   0.4993
  concept.myocardinfarct_uncertain                     0.4967   0.4967   0.5037
  concept.nierfunctie_present                          0.4967   0.4967   0.5031
  concept.revascularisatie_present                     0.4967   0.4967   0.4856
  concept.hartfalen_present                            0.4973   0.4973   0.4889
  concept.myocardinfarct_negated                       0.4975   0.4975   0.4936

  38 features are only ~34 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  penalizer=0.01     train C=0.5184  val C=0.4893
  penalizer=0.1      train C=0.5189  val C=0.4982
  penalizer=1        train C=0.5189  val C=0.4982
  penalizer=10       train C=0.5189  val C=0.4982

  selected penalizer=1 -> TEST C=0.5212 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=1 TEST C=0.5212 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-27T07:54:30Z | screen: CTRL_demo_full

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

### RUN 2026-08-27T07:55:01Z | screen: CTRL_demo_rt

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

### RUN 2026-08-27T07:55:23Z | screen: CTRL_full_full

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

### RUN 2026-08-27T07:57:49Z | screen: CTRL_full_rt

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

### RUN 2026-08-27T08:00:24Z | screen: STRUCT_ctrl

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

### RUN 2026-08-27T08:02:51Z | screen: T0_volume

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

### RUN 2026-08-27T08:03:25Z | screen: T0_volume_rt

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

### RUN 2026-08-27T08:03:49Z | screen: T1_tfidf_3src

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

### RUN 2026-08-27T08:08:45Z | screen: T1_tfidf_char

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

### RUN 2026-08-27T08:13:44Z | screen: T1_tfidf_conclusie

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

### RUN 2026-08-27T08:15:24Z | screen: T1_tfidf_demo

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

### RUN 2026-08-27T08:20:36Z | screen: T1_tfidf_history

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

### RUN 2026-08-27T08:22:16Z | screen: T1_tfidf_nonames

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

### RUN 2026-08-27T08:27:14Z | screen: T1_tfidf_word

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

### RUN 2026-08-27T08:32:13Z | screen: T1_tfidf_word_full

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

### RUN 2026-08-27T08:36:15Z | screen: T2_concepts

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 39 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.1 TEST C=0.5120 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts/
  representation=text_concepts[binary] | landmark_days=180 | horizon_days=5475 | n_features=39

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   39 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   39 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   39 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 39 effectively constant (zero variance, or one value in >99% of patients); 39 take <=10 distinct values (normal for counts)
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
  concept.perifeer_vaatlijden_present                  0.4857   0.4857   0.4941
  concept.diabetes_present                             0.4859   0.4859   0.4832
  concept.hyperlipidemie_present                       0.4873   0.4873   0.4602
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.nierfunctie_present                          0.4893   0.4893   0.5004
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4930
  concept.angina_uncertain                             0.5058   0.5058   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.hartfalen_negated                            0.5051   0.5051   0.4954
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4959   0.4959   0.4938
  concept.perifeer_vaatlijden_negated                  0.4961   0.4961   0.4985
  concept.hypertensie_present                          0.4965   0.4965   0.4988
  concept.cva_tia_uncertain                            0.5034   0.5034   0.4933
  concept.revascularisatie_present                     0.4969   0.4969   0.5094
  concept.angina_negated                               0.4969   0.4969   0.4877

  39 features are only ~35 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5326  val C=0.4830
  penalizer=0.1      train C=0.5253  val C=0.4942
  penalizer=1        train C=0.5253  val C=0.4942
  penalizer=10       train C=0.5253  val C=0.4942
  penalizer=100      train C=0.5253  val C=0.4942

  selected penalizer=0.1 -> TEST C=0.5120 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.5120 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-27T08:36:47Z | screen: T2_concepts_both

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 78 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.1 TEST C=0.5101 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both/
  representation=text_concepts[both] | landmark_days=180 | horizon_days=5475 | n_features=78

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   78 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   78 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   78 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 8 of 78 effectively constant (zero variance, or one value in >99% of patients); 56 take <=10 distinct values (normal for counts)
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
  concept.diabetes_present_n                           0.4823   0.4823   0.4858
  concept.perifeer_vaatlijden_present                  0.4857   0.4857   0.4941
  concept.diabetes_present                             0.4859   0.4859   0.4832
  concept.perifeer_vaatlijden_present_n                0.4865   0.4865   0.4936
  concept.hyperlipidemie_present                       0.4873   0.4873   0.4602
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.hyperlipidemie_present_n                     0.4875   0.4875   0.4686
  concept.hypertensie_negated_n                        0.4877   0.4877   0.5043
  concept.nierfunctie_present_n                        0.4891   0.4891   0.5011
  concept.nierfunctie_present                          0.4893   0.4893   0.5004
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.atriumfibrilleren_present_n                  0.4919   0.4919   0.4962
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4930
  concept.myocardinfarct_present_n                     0.4929   0.4929   0.5042
  concept.stenose_present_n                            0.4931   0.4931   0.4762
  concept.hypertensie_present_n                        0.4938   0.4938   0.4985
  concept.angina_present_n                             0.4940   0.4940   0.4915
  concept.revascularisatie_present_n                   0.4942   0.4942   0.5098

  78 features are only ~53 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~3 times, not ~4.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 8 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5328  val C=0.4846
  penalizer=0.1      train C=0.5256  val C=0.4943
  penalizer=1        train C=0.5256  val C=0.4943
  penalizer=10       train C=0.5256  val C=0.4943
  penalizer=100      train C=0.5256  val C=0.4943

  selected penalizer=0.1 -> TEST C=0.5101 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.1 TEST C=0.5101 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-08-27T08:37:37Z | screen: T2_concepts_demo

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 41 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo/
  representation=text_concepts[binary]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=41

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   41 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   41 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   41 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 4 of 41 effectively constant (zero variance, or one value in >99% of patients); 40 take <=10 distinct values (normal for counts)
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
  concept.perifeer_vaatlijden_present                  0.4857   0.4857   0.4941
  concept.diabetes_present                             0.4859   0.4859   0.4832
  concept.hyperlipidemie_present                       0.4873   0.4873   0.4602
  concept.hypertensie_negated                          0.4874   0.4874   0.5049
  concept.nierfunctie_present                          0.4893   0.4893   0.5004
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  concept.stenose_present                              0.4924   0.4924   0.4742
  concept.angina_present                               0.4928   0.4928   0.4930
  concept.angina_uncertain                             0.5058   0.5058   0.4951
  concept.myocardinfarct_uncertain                     0.4943   0.4943   0.5034
  concept.hartfalen_negated                            0.5051   0.5051   0.4954
  concept.myocardinfarct_negated                       0.4953   0.4953   0.4969
  concept.cva_tia_present                              0.4956   0.4956   0.5036
  concept.diabetes_negated                             0.4959   0.4959   0.4938
  concept.perifeer_vaatlijden_negated                  0.4961   0.4961   0.4985
  concept.hypertensie_present                          0.4965   0.4965   0.4988
  concept.cva_tia_uncertain                            0.5034   0.5034   0.4933

  41 features are only ~36 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 4 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6807  val C=0.7070
  penalizer=0.1      train C=0.6676  val C=0.6677
  penalizer=1        train C=0.6585  val C=0.6531
  penalizer=10       train C=0.6584  val C=0.6530
  penalizer=100      train C=0.6584  val C=0.6530

  selected penalizer=0.01 -> TEST C=0.6749 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-08-27T08:38:12Z | screen: T2_concepts_history

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 38 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=1 TEST C=0.5209 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history/
  representation=text_concepts[binary] | landmark_days=180 | horizon_days=5475 | n_features=38

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
  concept.diabetes_present                             0.4858   0.4858   0.4815
  concept.hyperlipidemie_present                       0.4909   0.4909   0.4666
  concept.angina_present                               0.4914   0.4914   0.4883
  concept.hypertensie_present                          0.4916   0.4916   0.4881
  concept.hypertensie_negated                          0.4923   0.4923   0.5068
  concept.perifeer_vaatlijden_present                  0.4925   0.4925   0.4950
  concept.atriumfibrilleren_present                    0.4932   0.4932   0.4978
  concept.angina_negated                               0.4939   0.4939   0.4881
  concept.perifeer_vaatlijden_negated                  0.4941   0.4941   0.5016
  concept.stenose_present                              0.4944   0.4944   0.4653
  concept.revascularisatie_negated                     0.5056   0.5056   0.4912
  concept.cva_tia_present                              0.4950   0.4950   0.4997
  concept.roken_negated                                0.5040   0.5040   0.4905
  concept.diabetes_negated                             0.4960   0.4960   0.4977
  concept.cva_tia_negated                              0.4965   0.4965   0.4993
  concept.myocardinfarct_uncertain                     0.4967   0.4967   0.5037
  concept.nierfunctie_present                          0.4967   0.4967   0.5031
  concept.revascularisatie_present                     0.4967   0.4967   0.4856
  concept.hartfalen_present                            0.4973   0.4973   0.4889
  concept.myocardinfarct_negated                       0.4975   0.4975   0.4936

  38 features are only ~34 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~2 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 8 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5178  val C=0.4894
  penalizer=0.1      train C=0.5179  val C=0.4985
  penalizer=1        train C=0.5179  val C=0.4985
  penalizer=10       train C=0.5179  val C=0.4985
  penalizer=100      train C=0.5179  val C=0.4985

  selected penalizer=1 -> TEST C=0.5209 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=1 TEST C=0.5209 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-03T08:53:27Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
- RESULT: arm=text_concepts[binary/disease,symptom] n_features=39 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  aneurysma                      1,006       269        70   (10.4% asserted)
  angina                         2,162     1,617       157   (22.4% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,307       862        49   (23.9% asserted)
  hartfalen                        835     1,245        76   (8.7% asserted)
  hyperlipidemie                 2,531       716        72   (26.2% asserted)
  hypertensie                    3,842     1,140       240   (39.8% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                      503       318        66   (5.2% asserted)
  perifeer_vaatlijden              811       305        49   (8.4% asserted)
  roken                          3,795     1,149        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  raw feature matrix: 9,644 patients x 39 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  39 features tested = ~35 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~2 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<1.4e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  concept.diabetes_present                  0.4854  0.4854 100.0%   828  1.44          
  concept.aneurysma_present                 0.4881  0.4881 100.0%   828  1.18          
  concept.hypertensie_negated               0.4891  0.4891 100.0%   828  1.08          
  concept.nierfunctie_present               0.4900  0.4900 100.0%   828  0.99          
  concept.hyperlipidemie_present            0.4908  0.4908 100.0%   828  0.91          
  concept.perifeer_vaatlijden_present       0.4916  0.4916 100.0%   828  0.83          
  concept.myocardinfarct_present            0.4917  0.4917 100.0%   828  0.82          
  concept.atriumfibrilleren_present         0.4918  0.4918 100.0%   828  0.81          
  concept.stenose_present                   0.4924  0.4924 100.0%   828  0.75          
  concept.angina_present                    0.4928  0.4928 100.0%   828  0.71          
  concept.angina_uncertain                  0.5062  0.5062 100.0%   828  0.61          
  concept.myocardinfarct_uncertain          0.4943  0.4943 100.0%   828  0.57          
  concept.perifeer_vaatlijden_negated       0.4949  0.4949 100.0%   828  0.50          
  concept.myocardinfarct_negated            0.4953  0.4953 100.0%   828  0.46          
  concept.cva_tia_present                   0.4956  0.4956 100.0%   828  0.43          
  concept.diabetes_negated                  0.4961  0.4961 100.0%   828  0.39          
  concept.angina_negated                    0.4963  0.4963 100.0%   828  0.36          
  concept.aneurysma_negated                 0.5035  0.5035 100.0%   828  0.35          
  concept.cva_tia_uncertain                 0.5034  0.5034 100.0%   828  0.34          
  concept.nierfunctie_negated               0.4967  0.4967 100.0%   828  0.32          
  concept.hartfalen_present                 0.4977  0.4977 100.0%   828  0.22          
  concept.atriumfibrilleren_negated         0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_uncertain                 0.4978  0.4978 100.0%   828  0.22          
  concept.roken_negated                     0.5021  0.5021 100.0%   828  0.21          
  concept.stenose_negated                   0.5021  0.5021 100.0%   828  0.21          
  concept.hypertensie_present               0.4979  0.4979 100.0%   828  0.20          
  concept.hyperlipidemie_negated            0.4984  0.4984 100.0%   828  0.15          
  concept.cva_tia_negated                   0.4986  0.4986 100.0%   828  0.14          
  concept.hartfalen_negated                 0.5008  0.5008 100.0%   828  0.08          
  concept.atriumfibrilleren_uncertain       0.5008  0.5008 100.0%   828  0.08          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=39
  validation : 1,510 patients | events=206 (13.6%) | features=39
  test       : 1,924 patients | events=257 (13.4%) | features=39
RESULT: arm=text_concepts[binary/disease,symptom] n_features=39 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts model=mlp model.input_size=39
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T08:54:39Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=both out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
- RESULT: arm=text_concepts[both/disease,symptom] n_features=78 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=both concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  78 concept features (encoding=both) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  aneurysma                      1,006       269        70   (10.4% asserted)
  angina                         2,162     1,617       157   (22.4% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,307       862        49   (23.9% asserted)
  hartfalen                        835     1,245        76   (8.7% asserted)
  hyperlipidemie                 2,531       716        72   (26.2% asserted)
  hypertensie                    3,842     1,140       240   (39.8% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                      503       318        66   (5.2% asserted)
  perifeer_vaatlijden              811       305        49   (8.4% asserted)
  roken                          3,795     1,149        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  raw feature matrix: 9,644 patients x 78 features
  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=78
  validation : 1,510 patients | events=206 (13.6%) | features=78
  test       : 1,924 patients | events=257 (13.4%) | features=78
RESULT: arm=text_concepts[both/disease,symptom] n_features=78 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_both model=mlp model.input_size=78
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T08:55:34Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
- RESULT: arm=text_concepts[binary/disease,symptom]+baseline[leeftijd,geslacht] n_features=41 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
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
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  aneurysma                      1,006       269        70   (10.4% asserted)
  angina                         2,162     1,617       157   (22.4% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,307       862        49   (23.9% asserted)
  hartfalen                        835     1,245        76   (8.7% asserted)
  hyperlipidemie                 2,531       716        72   (26.2% asserted)
  hypertensie                    3,842     1,140       240   (39.8% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                      503       318        66   (5.2% asserted)
  perifeer_vaatlijden              811       305        49   (8.4% asserted)
  roken                          3,795     1,149        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 41 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  41 features tested = ~37 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 2 (~2 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 2 | surviving Bonferroni (p<1.4e-03): 2  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  smart_baseline.leeftijd                   0.6731  0.5170 100.0%   828 17.08      BONF
  smart_baseline.geslacht                   0.4422  0.4422 100.0%   828  5.71      BONF
  concept.diabetes_present                  0.4854  0.4854 100.0%   828  1.44          
  concept.aneurysma_present                 0.4881  0.4881 100.0%   828  1.18          
  concept.hypertensie_negated               0.4891  0.4891 100.0%   828  1.08          
  concept.nierfunctie_present               0.4900  0.4900 100.0%   828  0.99          
  concept.hyperlipidemie_present            0.4908  0.4908 100.0%   828  0.91          
  concept.perifeer_vaatlijden_present       0.4916  0.4916 100.0%   828  0.83          
  concept.myocardinfarct_present            0.4917  0.4917 100.0%   828  0.82          
  concept.atriumfibrilleren_present         0.4918  0.4918 100.0%   828  0.81          
  concept.stenose_present                   0.4924  0.4924 100.0%   828  0.75          
  concept.angina_present                    0.4928  0.4928 100.0%   828  0.71          
  concept.angina_uncertain                  0.5062  0.5062 100.0%   828  0.61          
  concept.myocardinfarct_uncertain          0.4943  0.4943 100.0%   828  0.57          
  concept.perifeer_vaatlijden_negated       0.4949  0.4949 100.0%   828  0.50          
  concept.myocardinfarct_negated            0.4953  0.4953 100.0%   828  0.46          
  concept.cva_tia_present                   0.4956  0.4956 100.0%   828  0.43          
  concept.diabetes_negated                  0.4961  0.4961 100.0%   828  0.39          
  concept.angina_negated                    0.4963  0.4963 100.0%   828  0.36          
  concept.aneurysma_negated                 0.5035  0.5035 100.0%   828  0.35          
  concept.cva_tia_uncertain                 0.5034  0.5034 100.0%   828  0.34          
  concept.nierfunctie_negated               0.4967  0.4967 100.0%   828  0.32          
  concept.hartfalen_present                 0.4977  0.4977 100.0%   828  0.22          
  concept.atriumfibrilleren_negated         0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_uncertain                 0.4978  0.4978 100.0%   828  0.22          
  concept.roken_negated                     0.5021  0.5021 100.0%   828  0.21          
  concept.stenose_negated                   0.5021  0.5021 100.0%   828  0.21          
  concept.hypertensie_present               0.4979  0.4979 100.0%   828  0.20          
  concept.hyperlipidemie_negated            0.4984  0.4984 100.0%   828  0.15          
  concept.cva_tia_negated                   0.4986  0.4986 100.0%   828  0.14          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=41
  validation : 1,510 patients | events=206 (13.6%) | features=41
  test       : 1,924 patients | events=257 (13.4%) | features=41
RESULT: arm=text_concepts[binary/disease,symptom]+baseline[leeftijd,geslacht] n_features=41 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_demo model=mlp model.input_size=41
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T08:56:38Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 section=voorgeschiedenis,anamnese analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 5085 patients with text): roken=3300, hypertensie=3197, diabetes=1960, myocardinfarct=1865
- RESULT: arm=text_concepts[binary/disease,symptom] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=voorgeschiedenis,anamnese analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  after cleaning + section=voorgeschiedenis,anamnese: 5,085 patients retain text (52.7%)
  4,559 patients have no text after cleaning/section and get an all-zero vector
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  aneurysma                        705       128        32   (13.9% asserted)
  angina                         1,602     1,443        72   (31.5% asserted)
  atriumfibrilleren                588       103        37   (11.6% asserted)
  cva_tia                        1,305       298       179   (25.7% asserted)
  diabetes                       1,960       649        24   (38.5% asserted)
  hartfalen                        397       163        31   (7.8% asserted)
  hyperlipidemie                 1,847       593        25   (36.3% asserted)
  hypertensie                    3,197       876        98   (62.9% asserted)
  myocardinfarct                 1,865       319       130   (36.7% asserted)
  nierfunctie                      252       305         9   (5.0% asserted)
  perifeer_vaatlijden              662       238        14   (13.0% asserted)
  roken                          3,300       763        22   (64.9% asserted)
  stenose                        1,509       488        89   (29.7% asserted)
RESULT: concept prevalence (asserted, of 5085 patients with text): roken=3300, hypertensie=3197, diabetes=1960, myocardinfarct=1865
  raw feature matrix: 9,644 patients x 39 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 1 features constant or all-missing on train
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=38
  validation : 1,510 patients | events=206 (13.6%) | features=38
  test       : 1,924 patients | events=257 (13.4%) | features=38
RESULT: arm=text_concepts[binary/disease,symptom] n_features=38 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_history model=mlp model.input_size=38
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T08:57:20Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_alltiers
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4527, hyperlipidemie=4176, hypertensie=3860, roken=3802
- RESULT: arm=text_concepts[binary/disease,symptom,measurement,medication,procedure] n_features=42 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom,measurement,medication,procedure expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  concept tiers in use: disease,symptom,measurement,medication,procedure
  42 concept features (encoding=binary) from 14 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  aneurysma                      1,006       269        70   (10.4% asserted)
  angina                         2,162     1,617       157   (22.4% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,726       948        76   (28.3% asserted)
  hartfalen                      1,135     1,258        78   (11.8% asserted)
  hyperlipidemie                 4,176     1,122       139   (43.3% asserted)
  hypertensie                    3,860     1,186       249   (40.0% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                    3,178       405        67   (33.0% asserted)
  perifeer_vaatlijden              811       305        49   (8.4% asserted)
  revascularisatie               4,527     1,306       217   (46.9% asserted)
  roken                          3,802     1,170        89   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): revascularisatie=4527, hyperlipidemie=4176, hypertensie=3860, roken=3802
  raw feature matrix: 9,644 patients x 42 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  42 features tested = ~37 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~2 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<1.4e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  concept.diabetes_present                  0.4858  0.4858 100.0%   828  1.41          
  concept.hypertensie_negated               0.4874  0.4874 100.0%   828  1.24          
  concept.aneurysma_present                 0.4881  0.4881 100.0%   828  1.18          
  concept.hyperlipidemie_present            0.4887  0.4887 100.0%   828  1.12          
  concept.perifeer_vaatlijden_present       0.4916  0.4916 100.0%   828  0.83          
  concept.myocardinfarct_present            0.4917  0.4917 100.0%   828  0.82          
  concept.atriumfibrilleren_present         0.4918  0.4918 100.0%   828  0.81          
  concept.stenose_present                   0.4924  0.4924 100.0%   828  0.75          
  concept.angina_present                    0.4928  0.4928 100.0%   828  0.71          
  concept.angina_uncertain                  0.5062  0.5062 100.0%   828  0.61          
  concept.myocardinfarct_uncertain          0.4943  0.4943 100.0%   828  0.57          
  concept.perifeer_vaatlijden_negated       0.4949  0.4949 100.0%   828  0.50          
  concept.myocardinfarct_negated            0.4953  0.4953 100.0%   828  0.46          
  concept.cva_tia_present                   0.4956  0.4956 100.0%   828  0.43          
  concept.diabetes_negated                  0.4959  0.4959 100.0%   828  0.41          
  concept.nierfunctie_present               0.4961  0.4961 100.0%   828  0.39          
  concept.angina_negated                    0.4963  0.4963 100.0%   828  0.36          
  concept.hypertensie_present               0.4965  0.4965 100.0%   828  0.35          
  concept.aneurysma_negated                 0.5035  0.5035 100.0%   828  0.35          
  concept.cva_tia_uncertain                 0.5034  0.5034 100.0%   828  0.34          
  concept.hartfalen_present                 0.4967  0.4967 100.0%   828  0.33          
  concept.revascularisatie_present          0.4970  0.4970 100.0%   828  0.30          
  concept.revascularisatie_negated          0.5026  0.5026 100.0%   828  0.26          
  concept.atriumfibrilleren_negated         0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_uncertain                 0.4978  0.4978 100.0%   828  0.22          
  concept.stenose_negated                   0.5021  0.5021 100.0%   828  0.21          
  concept.roken_negated                     0.5018  0.5018 100.0%   828  0.17          
  concept.hyperlipidemie_negated            0.4985  0.4985 100.0%   828  0.15          
  concept.cva_tia_negated                   0.4986  0.4986 100.0%   828  0.14          
  concept.diabetes_uncertain                0.4987  0.4987 100.0%   828  0.13          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  imputed 0 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=42
  validation : 1,510 patients | events=206 (13.6%) | features=42
  test       : 1,924 patients | events=257 (13.4%) | features=42
RESULT: arm=text_concepts[binary/disease,symptom,measurement,medication,procedure] n_features=42 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_alltiers
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/T2_concepts_alltiers model=mlp model.input_size=42
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T08:58:31Z | text arm: concepts

- status: ok
- context: mode=concepts landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_concepts_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
- RESULT: arm=text_concepts[binary/disease,symptom]+baseline[all] n_features=222 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=concepts landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='all' min_coverage_frac=0.1
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
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  39 concept features (encoding=binary) from 13 concepts x present/negated/uncertain
  concept                     asserted   negated uncertain   (patients, % of those with text)
  aneurysma                      1,006       269        70   (10.4% asserted)
  angina                         2,162     1,617       157   (22.4% asserted)
  atriumfibrilleren                747       187        76   (7.7% asserted)
  cva_tia                        1,660       453       304   (17.2% asserted)
  diabetes                       2,307       862        49   (23.9% asserted)
  hartfalen                        835     1,245        76   (8.7% asserted)
  hyperlipidemie                 2,531       716        72   (26.2% asserted)
  hypertensie                    3,842     1,140       240   (39.8% asserted)
  myocardinfarct                 2,530       604       259   (26.2% asserted)
  nierfunctie                      503       318        66   (5.2% asserted)
  perifeer_vaatlijden              811       305        49   (8.4% asserted)
  roken                          3,795     1,149        88   (39.4% asserted)
  stenose                        3,009     1,584       275   (31.2% asserted)
RESULT: concept prevalence (asserted, of 9644 patients with text): hypertensie=3842, roken=3795, stenose=3009, hyperlipidemie=2531
  appending 183 baseline columns -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 222 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  222 features tested = ~72 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 103 (~4 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 101 | surviving Bonferroni (p<6.9e-04): 83  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  smart_baseline.leeftijd                   0.6731  0.5170 100.0%   828 17.08      BONF
  smart_baseline.stenACIl                   0.6489  0.4585  98.3%   806 14.49      BONF
  smart_baseline.stenACIr                   0.6485  0.4591  98.5%   813 14.52      BONF
  smart_baseline.kl1fysfc                   0.3559  0.6014  78.5%   504 11.09      BONF
  smart_baseline.klar_coc                   0.3625  0.5470  99.4%   827 13.56      BONF
  smart_baseline.labkrea                    0.6233  0.5736  99.6%   827 12.16      BONF
  smart_baseline.mpkr_rat                   0.6259  0.5764  53.2%   512  9.77      BONF
  smart_baseline.packyrs                    0.6186  0.5675  99.4%   822 11.66      BONF
  smart_baseline.MDRD                       0.3839  0.5825  99.6%   827 11.44      BONF
  smart_baseline.KliMaC                     0.6138  0.5788 100.0%   828 11.23      BONF
  smart_baseline.plsprs                     0.6125  0.5458  99.6%   826 11.09      BONF
  smart_baseline.KliMaYr                    0.3861  0.5687  63.7%   690 10.26      BONF
  smart_baseline.labhcyst                   0.6105  0.5802  61.0%   659  9.73      BONF
  smart_baseline.kl8alggz                   0.3900  0.5452  78.2%   502  8.45      BONF
  smart_baseline.klar_gst                   0.3959  0.6041  99.4%   827 10.26      BONF
  smart_baseline.klinman                    0.5988  0.4012 100.0%   828  9.75      BONF
  smart_baseline.labmalb                    0.5996  0.5603  53.4%   513  7.74      BONF
  smart_baseline.pa_stolmid                 0.5935  0.4065 100.0%   828  9.22      BONF
  smart_baseline.labhba1c                   0.5994  0.5060  69.4%   413  6.93      BONF
  smart_baseline.KliMaDur                   0.5899  0.5899  63.7%   690  8.10      BONF
  smart_baseline.vet_gm                     0.5897  0.5335  85.0%   595  7.50      BONF
  smart_baseline.labcrp                     0.5863  0.5618  87.4%   755  8.13      BONF
  smart_baseline.abivrl_n                   0.5849  0.5849  99.4%   821  8.34      BONF
  smart_baseline.bdsys                      0.5813  0.5326  99.9%   827  8.01      BONF
  smart_baseline.AortDist                   0.5791  0.5067  99.0%   818  7.76      BONF
  smart_baseline.kl2socfc                   0.4169  0.5203  78.5%   506  6.41      BONF
  smart_baseline.kl7pijn                    0.4176  0.5382  78.5%   506  6.35      BONF
  smart_baseline.mht_alln                   0.5732  0.5067 100.0%   828  7.22      BONF
  smart_baseline.vgt_hart                   0.5706  0.5706 100.0%   828  6.97      BONF
  smart_baseline.tail_gm                    0.5724  0.5081  90.0%   675  6.45      BONF
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.

  winsorised at train quantiles [0.001, 0.999]
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 162,074 missing cells with the train median, then standardised
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
  train      : 6,210 patients | events=828 (13.3%) | features=222
  validation : 1,510 patients | events=206 (13.6%) | features=222
  test       : 1,924 patients | events=257 (13.4%) | features=222
RESULT: arm=text_concepts[binary/disease,symptom]+baseline[all] n_features=222 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_concepts_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_concepts_full model=mlp model.input_size=222
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T08:59:58Z | text arm: tfidf

- status: ok
- context: mode=tfidf landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_tfidf_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_tfidf[word]+baseline[all] n_features=439 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=tfidf landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='all' min_coverage_frac=0.1
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
  TF-IDF analyzer=word vocab=50,000 (max_df=0.8 drops boilerplate)
  SVD dim=256 (explained var=0.42; a low share is normal for text LSA)
  appending 183 baseline columns -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 439 features
  winsorised at train quantiles [0.001, 0.999]
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 162,074 missing cells with the train median, then standardised
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
  train      : 6,210 patients | events=828 (13.3%) | features=439
  validation : 1,510 patients | events=206 (13.6%) | features=439
  test       : 1,924 patients | events=257 (13.4%) | features=439
RESULT: arm=text_tfidf[word]+baseline[all] n_features=439 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_tfidf_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_tfidf_full model=mlp model.input_size=439
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T09:01:47Z | text arm: volume

- status: ok
- context: mode=volume landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_volume_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=text_volume+baseline[all] n_features=192 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=volume landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='all' min_coverage_frac=0.1
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
  appending 183 baseline columns -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 192 features
  winsorised at train quantiles [0.001, 0.999]
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 162,074 missing cells with the train median, then standardised
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
  train      : 6,210 patients | events=828 (13.3%) | features=192
  validation : 1,510 patients | events=206 (13.6%) | features=192
  test       : 1,924 patients | events=257 (13.4%) | features=192
RESULT: arm=text_volume+baseline[all] n_features=192 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_volume_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/INCR_volume_full model=mlp model.input_size=192
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T09:02:00Z | structured arm

- status: ok
- context: landmark=180 horizon=5475 positive_control=False add_baseline=leeftijd,geslacht auto_occurrence=True out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/SENS_no_omschr
- RESULT: arm=pivoted_events+baseline[leeftijd,geslacht] n_features=532 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: landmark=180/lookback=None horizon=5475 auto_occurrence=True add_baseline_cols='leeftijd,geslacht' baseline_cols=None positive_control=False min_coverage_frac=0.1 aggregators=last,mean,slope,count
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events); survival now measured from day 180
  effective coverage floor: 860 train patients (= max(--min-patients, 10% of 8,599))
  cohort 13,434 patients | train=8,599 val=2,141 test=2,694
  consult_20251208.SpecialismeNaam [occurrence]: 7 distinct codes -> kept 3 (>= 860 train patients; 4 below the floor)
  consult_20251208.title [occurrence]: 14 distinct codes -> kept 8 (>= 860 train patients; 6 below the floor)
  dbc_20251203.Diagnose [occurrence/tokenised]: 441 distinct codes -> kept 10 (>= 860 train patients; 431 below the floor)
  dbc_20251203.Behandeling [occurrence]: 162 distinct codes -> kept 1 (>= 860 train patients; 161 below the floor)
  dbc_20251203.Zorgvraag [occurrence]: 25 distinct codes -> kept 0 (>= 860 train patients; 25 below the floor)
  diag_20250626.diag_omschrijving [occurrence/tokenised]: 6,722 distinct codes -> kept 26 (>= 860 train patients; 6,696 below the floor)
  ecg_measmatrix_20251208 [wide]: 12 numeric columns aggregated directly
  echo_20250626: unit check over 330 codes -> 0 report a SECOND unit in >1% of rows; pass --split-by-unit to separate them
  echo_20250626.MeasName_ECHO [numeric]: 322 distinct codes -> kept 34 (>= 860 train patients; 288 below the floor)
  echo_20250626.UnitName_ECHO [occurrence]: 23 distinct codes -> kept 15 (>= 860 train patients; 8 below the floor)
  hos_20251209 [wide]: 2 numeric columns aggregated directly
  hos_mut_20251209.specialisme_omschrijving [occurrence]: 45 distinct codes -> kept 4 (>= 860 train patients; 41 below the floor)
  hos_mut_20251209.locatie [occurrence]: 169 distinct codes -> kept 6 (>= 860 train patients; 163 below the floor)
  hos_mut_20251209 [wide]: 2 numeric columns aggregated directly
  lab_ezis_20250709: unit check over 682 codes -> 0 report a SECOND unit in >1% of rows; pass --split-by-unit to separate them
  lab_ezis_20250709.lab_testcode [numeric]: 661 distinct codes -> kept 60 (>= 860 train patients; 601 below the floor)
  lab_ezis_20250709.lab_testunit [occurrence]: 76 distinct codes -> kept 23 (>= 860 train patients; 53 below the floor)
  lab_ezis_20250709.material [occurrence]: 4 distinct codes -> kept 3 (>= 860 train patients; 1 below the floor)
  med_20250709.med_ZIatc [occurrence/tokenised]: 658 distinct codes -> kept 17 (>= 860 train patients; 641 below the floor)
  med_20250709.med_genNaam [occurrence/tokenised]: 604 distinct codes -> kept 25 (>= 860 train patients; 579 below the floor)
  med_20250709 [wide]: 2 numeric columns aggregated directly
  meting_20251203: unit check over 33 codes -> 0 report a SECOND unit in >1% of rows; pass --split-by-unit to separate them
  meting_20251203.label [numeric]: 33 distinct codes -> kept 8 (>= 860 train patients; 25 below the floor)
  meting_20251203.eenheid [occurrence]: 9 distinct codes -> kept 8 (>= 860 train patients; 1 below the floor)
  meting_20251203.Omschrijving [occurrence]: 38 distinct codes -> kept 10 (>= 860 train patients; 28 below the floor)
  meting_20251203.SOURCETYPE [occurrence]: 6 distinct codes -> kept 3 (>= 860 train patients; 3 below the floor)
  meting_20251203 [wide]: 2 numeric columns aggregated directly
  mri_verslag_20250626.verrichting_oms [occurrence]: 5 distinct codes -> kept 0 (>= 860 train patients; 5 below the floor)
  ok_20250626: no usable columns, skipped
  ok_verslag_20250626.STELLING [occurrence]: 156 distinct codes -> kept 3 (>= 860 train patients; 153 below the floor)
  radiologie_verslag_20251208.verr_oms [occurrence]: 54 distinct codes -> kept 3 (>= 860 train patients; 51 below the floor)
  radiologie_verslag_20251208.status [occurrence]: 5 distinct codes -> kept 1 (>= 860 train patients; 4 below the floor)
  uitgaandebrief_20251208.afdeling [occurrence]: 33 distinct codes -> kept 2 (>= 860 train patients; 31 below the floor)
  uitgaandebrief_20251208.type_brief [occurrence]: 2 distinct codes -> kept 2 (>= 860 train patients; 0 below the floor)
  verr_20251203: no usable columns, skipped
  accumulating consult_20251208.SpecialismeNaam ...
  accumulating consult_20251208.title ...
  accumulating dbc_20251203.Diagnose ...
  accumulating dbc_20251203.Behandeling ...
  accumulating diag_20250626.diag_omschrijving ...
  accumulating ecg_measmatrix_20251208.wide ...
  accumulating echo_20250626.MeasName_ECHO ...
  accumulating echo_20250626.UnitName_ECHO ...
  accumulating hos_20251209.wide ...
  accumulating hos_mut_20251209.specialisme_omschrijving ...
  accumulating hos_mut_20251209.locatie ...
  accumulating hos_mut_20251209.wide ...
  accumulating lab_ezis_20250709.lab_testcode ...
    rescued 47,094 values from the text column (thresholds like '>90', and neg/pos)
  accumulating lab_ezis_20250709.lab_testunit ...
  accumulating lab_ezis_20250709.material ...
  accumulating med_20250709.med_ZIatc ...
  accumulating med_20250709.med_genNaam ...
  accumulating med_20250709.wide ...
  accumulating meting_20251203.label ...
  accumulating meting_20251203.eenheid ...
  accumulating meting_20251203.Omschrijving ...
  accumulating meting_20251203.SOURCETYPE ...
  accumulating meting_20251203.wide ...
  accumulating ok_verslag_20250626.STELLING ...
  accumulating radiologie_verslag_20251208.verr_oms ...
  accumulating radiologie_verslag_20251208.status ...
  accumulating uitgaandebrief_20251208.afdeling ...
  accumulating uitgaandebrief_20251208.type_brief ...
  coverage floor removed 61 codes across all blocks (applies to wide columns too, not just pivoted codes)
  appending 2 baseline columns to the event features -> ['geslacht', 'leeftijd']
  (age and sex need no chart review, so events+demographics is still a baseline-free model in the sense that matters)
  raw feature matrix: 13,434 patients x 602 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 3 features constant or all-missing on train
  dropped 67 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 3,630,254 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4448
    smart_baseline.leeftijd: train C=0.6742
  train      : 8,599 patients | events=1,136 (13.2%) | features=532
  validation : 2,141 patients | events=310 (14.5%) | features=532
  test       : 2,694 patients | events=381 (14.1%) | features=532
RESULT: arm=pivoted_events+baseline[leeftijd,geslacht] n_features=532 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/SENS_no_omschr
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/SENS_no_omschr model=mlp model.input_size=532
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-03T09:04:22Z | screen: CTRL_demo_full

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

### RUN 2026-09-03T09:04:54Z | screen: CTRL_demo_rt

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

### RUN 2026-09-03T09:05:15Z | screen: CTRL_full_full

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

### RUN 2026-09-03T09:07:41Z | screen: CTRL_full_rt

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

### RUN 2026-09-03T09:10:15Z | screen: INCR_concepts_full

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

### RUN 2026-09-03T09:13:46Z | screen: INCR_tfidf_full

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

### RUN 2026-09-03T09:20:58Z | screen: INCR_volume_full

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

### RUN 2026-09-03T09:23:46Z | screen: SENS_no_omschr

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

### RUN 2026-09-03T09:38:32Z | screen: STRUCT_ctrl

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

### RUN 2026-09-03T09:40:58Z | screen: T0_volume

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

### RUN 2026-09-03T09:41:32Z | screen: T0_volume_rt

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

### RUN 2026-09-03T09:41:56Z | screen: T1_tfidf_3src

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

### RUN 2026-09-03T09:46:49Z | screen: T1_tfidf_char

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

### RUN 2026-09-03T09:51:44Z | screen: T1_tfidf_conclusie

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

### RUN 2026-09-03T09:53:24Z | screen: T1_tfidf_demo

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

### RUN 2026-09-03T09:58:34Z | screen: T1_tfidf_history

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

### RUN 2026-09-03T10:00:13Z | screen: T1_tfidf_nonames

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

### RUN 2026-09-03T10:05:10Z | screen: T1_tfidf_word

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

### RUN 2026-09-03T10:10:06Z | screen: T1_tfidf_word_full

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

### RUN 2026-09-03T10:14:05Z | screen: T2_concepts

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

### RUN 2026-09-03T10:14:37Z | screen: T2_concepts_alltiers

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

### RUN 2026-09-03T10:15:10Z | screen: T2_concepts_both

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

### RUN 2026-09-03T10:15:56Z | screen: T2_concepts_demo

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

### RUN 2026-09-03T10:16:29Z | screen: T2_concepts_history

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

---

### RUN 2026-09-07T17:24:15Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=group:chart out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:chart] n_features=113 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  baseline group chart: 113 of 183 numeric baseline columns
  members: ['diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'nrfaln_n', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  age/sex and admin columns are in NEITHER half by design (2: ['geslacht', 'leeftijd']) — leaving them in one half would hand it ~0.673 for free
  MATCHED CONTROL (group:chart): 113 baseline features -> ['diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'nrfaln_n', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  raw feature matrix: 9,644 patients x 113 features
  winsorised at train quantiles [0.001, 0.999]
  3 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 59,878 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
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
    smart_baseline.hyptns_b: train C=0.5387
    smart_baseline.vz_hypt: train C=0.5473
    smart_baseline.hypgly_b: train C=0.5012   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5441
    smart_baseline.vz_t1d: train C=0.4995   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5446
    smart_baseline.klinman: train C=0.5988
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
    smart_baseline.VgBh_HpL: train C=0.5141   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5233   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5138   ** suspiciously flat **
    smart_baseline.nrfaln_n: train C=0.5623
    smart_baseline.roken: train C=0.5674
    smart_baseline.packyrs: train C=0.6182
    smart_baseline.alcohol: train C=0.4464
    smart_baseline.AlchlGlz: train C=0.4979   ** suspiciously flat **
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
  train      : 6,210 patients | events=828 (13.3%) | features=113
  validation : 1,510 patients | events=206 (13.6%) | features=113
  test       : 1,924 patients | events=257 (13.4%) | features=113
RESULT: arm=matched_baseline[group:chart] n_features=113 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_rt model=mlp model.input_size=113
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:24:25Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=group:chart,leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:chart,leeftijd,geslacht] n_features=115 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  baseline group chart+leeftijd,geslacht: 115 of 183 numeric baseline columns
  members: ['geslacht', 'leeftijd', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'nrfaln_n', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  MATCHED CONTROL (group:chart,leeftijd,geslacht): 115 baseline features -> ['geslacht', 'leeftijd', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'nrfaln_n', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  raw feature matrix: 9,644 patients x 115 features
  winsorised at train quantiles [0.001, 0.999]
  3 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 59,878 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
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
    smart_baseline.hyptns_b: train C=0.5387
    smart_baseline.vz_hypt: train C=0.5473
    smart_baseline.hypgly_b: train C=0.5012   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5441
    smart_baseline.vz_t1d: train C=0.4995   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5446
    smart_baseline.klinman: train C=0.5988
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
    smart_baseline.VgBh_HpL: train C=0.5141   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5233   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5138   ** suspiciously flat **
    smart_baseline.nrfaln_n: train C=0.5623
    smart_baseline.roken: train C=0.5674
    smart_baseline.packyrs: train C=0.6182
    smart_baseline.alcohol: train C=0.4464
    smart_baseline.AlchlGlz: train C=0.4979   ** suspiciously flat **
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
  train      : 6,210 patients | events=828 (13.3%) | features=115
  validation : 1,510 patients | events=206 (13.6%) | features=115
  test       : 1,924 patients | events=257 (13.4%) | features=115
RESULT: arm=matched_baseline[group:chart,leeftijd,geslacht] n_features=115 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_demo_rt model=mlp model.input_size=115
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:24:35Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=group:chart_strict out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chartstrict_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:chart_strict] n_features=96 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  baseline group chart_strict: 96 of 183 numeric baseline columns
  members: ['diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  age/sex and admin columns are in NEITHER half by design (2: ['geslacht', 'leeftijd']) — leaving them in one half would hand it ~0.673 for free
  MATCHED CONTROL (group:chart_strict): 96 baseline features -> ['diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  raw feature matrix: 9,644 patients x 96 features
  winsorised at train quantiles [0.001, 0.999]
  3 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 57,780 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
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
    smart_baseline.hyptns_b: train C=0.5387
    smart_baseline.vz_hypt: train C=0.5473
    smart_baseline.hypgly_b: train C=0.5012   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5441
    smart_baseline.vz_t1d: train C=0.4995   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5446
    smart_baseline.klinman: train C=0.5988
    smart_baseline.VgBh_HpL: train C=0.5141   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5233   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5138   ** suspiciously flat **
    smart_baseline.roken: train C=0.5674
    smart_baseline.packyrs: train C=0.6182
    smart_baseline.alcohol: train C=0.4464
    smart_baseline.AlchlGlz: train C=0.4979   ** suspiciously flat **
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
  train      : 6,210 patients | events=828 (13.3%) | features=96
  validation : 1,510 patients | events=206 (13.6%) | features=96
  test       : 1,924 patients | events=257 (13.4%) | features=96
RESULT: arm=matched_baseline[group:chart_strict] n_features=96 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chartstrict_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chartstrict_rt model=mlp model.input_size=96
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:24:44Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=group:protocol out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:protocol] n_features=68 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  baseline group protocol: 68 of 183 numeric baseline columns
  members: ['opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'bdsys', 'bddia', 'hyptns_n', 'labgluc', 'hypgly_n', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'hyplip_n', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'spMEThw', 'acMEThw', 'bwMEThw']
  age/sex and admin columns are in NEITHER half by design (2: ['geslacht', 'leeftijd']) — leaving them in one half would hand it ~0.673 for free
  MATCHED CONTROL (group:protocol): 68 baseline features -> ['opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'bdsys', 'bddia', 'hyptns_n', 'labgluc', 'hypgly_n', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'hyplip_n', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 68 features
  winsorised at train quantiles [0.001, 0.999]
  1 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 102,196 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.opleiding: train C=0.4764   ** suspiciously flat **
    smart_baseline.RespLand: train C=0.4962   ** suspiciously flat **
    smart_baseline.PaLand: train C=0.5000   ** suspiciously flat **
    smart_baseline.MaLand: train C=0.4979   ** suspiciously flat **
    smart_baseline.WereldDl: train C=0.4935   ** suspiciously flat **
    smart_baseline.bdsys: train C=0.5812
    smart_baseline.bddia: train C=0.4969   ** suspiciously flat **
    smart_baseline.hyptns_n: train C=0.5463
    smart_baseline.labgluc: train C=0.5579
    smart_baseline.hypgly_n: train C=0.5434
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
    smart_baseline.labhb: train C=0.4936   ** suspiciously flat **
    smart_baseline.labht: train C=0.5040   ** suspiciously flat **
    smart_baseline.labchol: train C=0.4895   ** suspiciously flat **
    smart_baseline.labtrig: train C=0.5339
    smart_baseline.labhdl: train C=0.4614
    smart_baseline.ldlchol: train C=0.4969   ** suspiciously flat **
    smart_baseline.hyplip_n: train C=0.4975   ** suspiciously flat **
    smart_baseline.labkrea: train C=0.6233
    smart_baseline.labmalb: train C=0.5763
    smart_baseline.labkrur: train C=0.4317
    smart_baseline.mpkr_rat: train C=0.5957
    smart_baseline.albminur: train C=0.5576
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
    smart_baseline.spMEThw: train C=0.4445
    smart_baseline.acMEThw: train C=0.4497
    smart_baseline.bwMEThw: train C=0.4353
  train      : 6,210 patients | events=828 (13.3%) | features=68
  validation : 1,510 patients | events=206 (13.6%) | features=68
  test       : 1,924 patients | events=257 (13.4%) | features=68
RESULT: arm=matched_baseline[group:protocol] n_features=68 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_rt model=mlp model.input_size=68
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:24:52Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary baseline_cols=group:protocol,leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:protocol,leeftijd,geslacht] n_features=70 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
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
  baseline group protocol+leeftijd,geslacht: 70 of 183 numeric baseline columns
  members: ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'bdsys', 'bddia', 'hyptns_n', 'labgluc', 'hypgly_n', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'hyplip_n', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'spMEThw', 'acMEThw', 'bwMEThw']
  MATCHED CONTROL (group:protocol,leeftijd,geslacht): 70 baseline features -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'bdsys', 'bddia', 'hyptns_n', 'labgluc', 'hypgly_n', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'hyplip_n', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 70 features
  winsorised at train quantiles [0.001, 0.999]
  1 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 102,196 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
    smart_baseline.opleiding: train C=0.4764   ** suspiciously flat **
    smart_baseline.RespLand: train C=0.4962   ** suspiciously flat **
    smart_baseline.PaLand: train C=0.5000   ** suspiciously flat **
    smart_baseline.MaLand: train C=0.4979   ** suspiciously flat **
    smart_baseline.WereldDl: train C=0.4935   ** suspiciously flat **
    smart_baseline.bdsys: train C=0.5812
    smart_baseline.bddia: train C=0.4969   ** suspiciously flat **
    smart_baseline.hyptns_n: train C=0.5463
    smart_baseline.labgluc: train C=0.5579
    smart_baseline.hypgly_n: train C=0.5434
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
    smart_baseline.labhb: train C=0.4936   ** suspiciously flat **
    smart_baseline.labht: train C=0.5040   ** suspiciously flat **
    smart_baseline.labchol: train C=0.4895   ** suspiciously flat **
    smart_baseline.labtrig: train C=0.5339
    smart_baseline.labhdl: train C=0.4614
    smart_baseline.ldlchol: train C=0.4969   ** suspiciously flat **
    smart_baseline.hyplip_n: train C=0.4975   ** suspiciously flat **
    smart_baseline.labkrea: train C=0.6233
    smart_baseline.labmalb: train C=0.5763
    smart_baseline.labkrur: train C=0.4317
    smart_baseline.mpkr_rat: train C=0.5957
    smart_baseline.albminur: train C=0.5576
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
    smart_baseline.spMEThw: train C=0.4445
    smart_baseline.acMEThw: train C=0.4497
    smart_baseline.bwMEThw: train C=0.4353
  train      : 6,210 patients | events=828 (13.3%) | features=70
  validation : 1,510 patients | events=206 (13.6%) | features=70
  test       : 1,924 patients | events=257 (13.4%) | features=70
RESULT: arm=matched_baseline[group:protocol,leeftijd,geslacht] n_features=70 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_demo_rt model=mlp model.input_size=70
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:25:00Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=False strip_nameish=False concept_encoding=binary baseline_cols=group:chart out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:chart] n_features=113 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=False strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  baseline group chart: 113 of 183 numeric baseline columns
  members: ['diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'nrfaln_n', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  age/sex and admin columns are in NEITHER half by design (2: ['geslacht', 'leeftijd']) — leaving them in one half would hand it ~0.673 for free
  MATCHED CONTROL (group:chart): 113 baseline features -> ['diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'hyptns_b', 'vz_hypt', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'VgBh_HpL', 'hyplip_b', 'vz_HypLp', 'nrfaln_n', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD']
  raw feature matrix: 13,434 patients x 113 features
  winsorised at train quantiles [0.001, 0.999]
  2 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 83,630 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.diagnsco: train C=0.5511
    smart_baseline.vaatzkt1: train C=0.4456
    smart_baseline.DiagSide: train C=0.5053   ** suspiciously flat **
    smart_baseline.IncInt_p: train C=0.4683
    smart_baseline.IncInt_v: train C=0.4912   ** suspiciously flat **
    smart_baseline.V0405: train C=0.5127   ** suspiciously flat **
    smart_baseline.vg_0410: train C=0.5298   ** suspiciously flat **
    smart_baseline.vgok_car: train C=0.5093   ** suspiciously flat **
    smart_baseline.vgt_kop: train C=0.5354
    smart_baseline.vz_kop: train C=0.5461
    smart_baseline.vg_0321: train C=0.5604
    smart_baseline.vg_0323: train C=0.5115   ** suspiciously flat **
    smart_baseline.vgok_har: train C=0.5448
    smart_baseline.vgt_hart: train C=0.5718
    smart_baseline.vz_hart: train C=0.5635
    smart_baseline.vg_0325: train C=0.5388
    smart_baseline.vgok_aaa: train C=0.5058   ** suspiciously flat **
    smart_baseline.vgt_aaa: train C=0.5395
    smart_baseline.vz_aaa: train C=0.5413
    smart_baseline.vg_0606c: train C=0.5040   ** suspiciously flat **
    smart_baseline.vgok_nie: train C=0.5005   ** suspiciously flat **
    smart_baseline.vgt_nier: train C=0.5044   ** suspiciously flat **
    smart_baseline.vz_nier: train C=0.5092   ** suspiciously flat **
    smart_baseline.vg_0519: train C=0.5062   ** suspiciously flat **
    smart_baseline.vgok_bee: train C=0.5168   ** suspiciously flat **
    smart_baseline.vgt_been: train C=0.5173   ** suspiciously flat **
    smart_baseline.vz_been: train C=0.5399
    smart_baseline.hyptns_b: train C=0.5439
    smart_baseline.vz_hypt: train C=0.5508
    smart_baseline.hypgly_b: train C=0.5024   ** suspiciously flat **
    smart_baseline.vz_DM: train C=0.5472
    smart_baseline.vz_t1d: train C=0.4992   ** suspiciously flat **
    smart_baseline.vz_t2d: train C=0.5480
    smart_baseline.klinman: train C=0.5993
    smart_baseline.stenACIr: train C=0.6400
    smart_baseline.stenACIl: train C=0.6420
    smart_baseline.csten_50: train C=0.5565
    smart_baseline.csten_70: train C=0.5479
    smart_baseline.AortProx: train C=0.5363
    smart_baseline.AortDist: train C=0.5811
    smart_baseline.aorta_hg: train C=0.5648
    smart_baseline.aorta_gm: train C=0.5612
    smart_baseline.aaaech_n: train C=0.5364
    smart_baseline.nrlng_re: train C=0.4931   ** suspiciously flat **
    smart_baseline.nrlng_li: train C=0.4763   ** suspiciously flat **
    smart_baseline.nrlng_gm: train C=0.4815   ** suspiciously flat **
    smart_baseline.nratrof: train C=0.5147   ** suspiciously flat **
    smart_baseline.nrvol_re: train C=0.5044   ** suspiciously flat **
    smart_baseline.nrvol_li: train C=0.4869   ** suspiciously flat **
    smart_baseline.nrvol_gm: train C=0.4964   ** suspiciously flat **
    smart_baseline.VgBh_HpL: train C=0.5102   ** suspiciously flat **
    smart_baseline.hyplip_b: train C=0.5239   ** suspiciously flat **
    smart_baseline.vz_HypLp: train C=0.5101   ** suspiciously flat **
    smart_baseline.nrfaln_n: train C=0.5638
    smart_baseline.roken: train C=0.5654
    smart_baseline.packyrs: train C=0.6066
    smart_baseline.alcohol: train C=0.4519
    smart_baseline.AlchlGlz: train C=0.4987   ** suspiciously flat **
    smart_baseline.mht01: train C=0.5309
    smart_baseline.mht02: train C=0.5387
    smart_baseline.mht02a: train C=0.5374
    smart_baseline.mht02b: train C=0.5015   ** suspiciously flat **
    smart_baseline.mht02c: train C=0.5048   ** suspiciously flat **
    smart_baseline.mht02d: train C=0.5094   ** suspiciously flat **
    smart_baseline.mht03: train C=0.5232   ** suspiciously flat **
    smart_baseline.mht04: train C=0.5322
    smart_baseline.mht05: train C=0.5018   ** suspiciously flat **
    smart_baseline.mht06: train C=0.5036   ** suspiciously flat **
    smart_baseline.mht07: train C=0.4996   ** suspiciously flat **
    smart_baseline.mht12: train C=0.5164   ** suspiciously flat **
    smart_baseline.mht33: train C=0.5017   ** suspiciously flat **
    smart_baseline.mht41: train C=0.5000   ** suspiciously flat **
    smart_baseline.mliphoop: train C=0.5107   ** suspiciously flat **
    smart_baseline.mli01: train C=0.5099   ** suspiciously flat **
    smart_baseline.mli02: train C=0.4990   ** suspiciously flat **
    smart_baseline.mli03: train C=0.5004   ** suspiciously flat **
    smart_baseline.mli04: train C=0.5008   ** suspiciously flat **
    smart_baseline.mas01: train C=0.5612
    smart_baseline.mas01a: train C=0.5138   ** suspiciously flat **
    smart_baseline.mas01b: train C=0.5061   ** suspiciously flat **
    smart_baseline.mas01c: train C=0.5098   ** suspiciously flat **
    smart_baseline.mas01d: train C=0.5028   ** suspiciously flat **
    smart_baseline.mas02: train C=0.5355
    smart_baseline.mas02a: train C=0.5179   ** suspiciously flat **
    smart_baseline.mas02b: train C=0.5054   ** suspiciously flat **
    smart_baseline.mas02c: train C=0.4997   ** suspiciously flat **
    smart_baseline.mas03: train C=0.5001   ** suspiciously flat **
    smart_baseline.mmpr: train C=0.5330
    smart_baseline.mhmc: train C=0.5059   ** suspiciously flat **
    smart_baseline.mgl01: train C=0.5297   ** suspiciously flat **
    smart_baseline.mgl02: train C=0.5155   ** suspiciously flat **
    smart_baseline.mgl03: train C=0.5004   ** suspiciously flat **
    smart_baseline.TCA: train C=0.4984   ** suspiciously flat **
    smart_baseline.SSRI: train C=0.4980   ** suspiciously flat **
    smart_baseline.MAO: train C=0.5000   ** suspiciously flat **
    smart_baseline.OthADep: train C=0.5097   ** suspiciously flat **
    smart_baseline.Benzo: train C=0.5036   ** suspiciously flat **
    smart_baseline.BenzoDer: train C=0.5063   ** suspiciously flat **
    smart_baseline.BenzoRel: train C=0.4999   ** suspiciously flat **
    smart_baseline.Thyr: train C=0.4987   ** suspiciously flat **
    smart_baseline.Amiodar: train C=0.5013   ** suspiciously flat **
    smart_baseline.Lithium: train C=0.5001   ** suspiciously flat **
    smart_baseline.mht_alln: train C=0.5736
    smart_baseline.mht_all: train C=0.5586
    smart_baseline.lipmid: train C=0.5224   ** suspiciously flat **
    smart_baseline.statine: train C=0.5210   ** suspiciously flat **
    smart_baseline.pamid: train C=0.5612
    smart_baseline.aspirine: train C=0.5567
    smart_baseline.pa_stolmid: train C=0.5876
    smart_baseline.KliMaC: train C=0.6167
    smart_baseline.KliMaYr: train C=0.3911
    smart_baseline.KliMaDur: train C=0.6061
    smart_baseline.KliMaDrD: train C=0.5971
  train      : 8,599 patients | events=1,136 (13.2%) | features=113
  validation : 2,141 patients | events=310 (14.5%) | features=113
  test       : 2,694 patients | events=381 (14.1%) | features=113
RESULT: arm=matched_baseline[group:chart] n_features=113 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_chart_full model=mlp model.input_size=113
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:25:13Z | text arm: baseline

- status: ok
- context: mode=baseline landmark=180 horizon=5475 analyzer=word require_text=False strip_nameish=False concept_encoding=binary baseline_cols=group:protocol out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_full
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: arm=matched_baseline[group:protocol] n_features=68 train=8599/1253ev validation=2141/341ev test=2694/422ev

<details><summary>full output</summary>

```
  ARGS: mode=baseline landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=False strip_dates=True strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols=None min_coverage_frac=0.1
  legacy: dropped 1 rows with a missing SMART outcome column
  legacy: 1,252 patients flagged lost-to-follow-up (indicator==2)
  13,806 raw rows -> 13,805 unique patients (deduplicated 0 extra rows)
  landmark 180d: dropped 371 patients whose outcome was at/before the landmark (130 events)
  cohort 13,434 | train=8,599 val=2,141 test=2,694
  reusing document cache /home/lorenzo.pratesi@mydre.org/workspace/smartehr/text_cache/documents.parquet (121,778 documents)
RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
  121,778 documents, 9,644/13,434 patients have text (71.8%)
  baseline group protocol: 68 of 183 numeric baseline columns
  members: ['opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'bdsys', 'bddia', 'hyptns_n', 'labgluc', 'hypgly_n', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'hyplip_n', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'spMEThw', 'acMEThw', 'bwMEThw']
  age/sex and admin columns are in NEITHER half by design (2: ['geslacht', 'leeftijd']) — leaving them in one half would hand it ~0.673 for free
  MATCHED CONTROL (group:protocol): 68 baseline features -> ['opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'bdsys', 'bddia', 'hyptns_n', 'labgluc', 'hypgly_n', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'hyplip_n', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 13,434 patients x 68 features
  winsorised at train quantiles [0.001, 0.999]
  1 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 143,214 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.opleiding: train C=0.4711   ** suspiciously flat **
    smart_baseline.RespLand: train C=0.4994   ** suspiciously flat **
    smart_baseline.PaLand: train C=0.5046   ** suspiciously flat **
    smart_baseline.MaLand: train C=0.5035   ** suspiciously flat **
    smart_baseline.WereldDl: train C=0.4958   ** suspiciously flat **
    smart_baseline.bdsys: train C=0.5747
    smart_baseline.bddia: train C=0.4890   ** suspiciously flat **
    smart_baseline.hyptns_n: train C=0.5378
    smart_baseline.labgluc: train C=0.5614
    smart_baseline.hypgly_n: train C=0.5439
    smart_baseline.gewicht: train C=0.5037   ** suspiciously flat **
    smart_baseline.lengte: train C=0.5009   ** suspiciously flat **
    smart_baseline.bm_indx: train C=0.5101   ** suspiciously flat **
    smart_baseline.bmi_30: train C=0.5021   ** suspiciously flat **
    smart_baseline.tail_gm: train C=0.5625
    smart_baseline.heup_gm: train C=0.4969   ** suspiciously flat **
    smart_baseline.tlhp_rat: train C=0.5000   ** suspiciously flat **
    smart_baseline.vet_subc: train C=0.4561
    smart_baseline.vet_gm: train C=0.5619
    smart_baseline.plsprs: train C=0.6089
    smart_baseline.abi_lg: train C=0.4912   ** suspiciously flat **
    smart_baseline.abi_gm: train C=0.4968   ** suspiciously flat **
    smart_baseline.abivrl_n: train C=0.5766
    smart_baseline.ABiRe: train C=0.4917   ** suspiciously flat **
    smart_baseline.ABiLi: train C=0.4969   ** suspiciously flat **
    smart_baseline.imt_gm: train C=0.5210   ** suspiciously flat **
    smart_baseline.labhb: train C=0.4905   ** suspiciously flat **
    smart_baseline.labht: train C=0.5038   ** suspiciously flat **
    smart_baseline.labchol: train C=0.4818   ** suspiciously flat **
    smart_baseline.labtrig: train C=0.5303
    smart_baseline.labhdl: train C=0.4657
    smart_baseline.ldlchol: train C=0.4895   ** suspiciously flat **
    smart_baseline.hyplip_n: train C=0.4908   ** suspiciously flat **
    smart_baseline.labkrea: train C=0.6168
    smart_baseline.labmalb: train C=0.5691
    smart_baseline.labkrur: train C=0.4393
    smart_baseline.mpkr_rat: train C=0.5912
    smart_baseline.albminur: train C=0.5568
    smart_baseline.klar_coc: train C=0.3634
    smart_baseline.klar_gst: train C=0.3916
    smart_baseline.MDRD: train C=0.3885
    smart_baseline.labhcyst: train C=0.5883
    smart_baseline.hyphmc_n: train C=0.5391
    smart_baseline.labins: train C=0.5272   ** suspiciously flat **
    smart_baseline.labtsh: train C=0.5193   ** suspiciously flat **
    smart_baseline.labcrp: train C=0.5948
    smart_baseline.labhba1c: train C=0.5581
    smart_baseline.labapob: train C=0.4959   ** suspiciously flat **
    smart_baseline.V0821: train C=0.4939   ** suspiciously flat **
    smart_baseline.V082201: train C=0.5021   ** suspiciously flat **
    smart_baseline.V082202: train C=0.5018   ** suspiciously flat **
    smart_baseline.V0823: train C=0.4999   ** suspiciously flat **
    smart_baseline.MBSc: train C=0.5672
    smart_baseline.MBS: train C=0.5530
    smart_baseline.MBSc_mis: train C=0.5666
    smart_baseline.MBScgr: train C=0.5567
    smart_baseline.kl1fysfc: train C=0.4025
    smart_baseline.kl2socfc: train C=0.4499
    smart_baseline.kl3rolfy: train C=0.4555
    smart_baseline.kl4rolem: train C=0.4915   ** suspiciously flat **
    smart_baseline.kl5mengz: train C=0.4859   ** suspiciously flat **
    smart_baseline.kl6vital: train C=0.4582
    smart_baseline.kl7pijn: train C=0.4411
    smart_baseline.kl8alggz: train C=0.4231
    smart_baseline.kl9gezva: train C=0.4968   ** suspiciously flat **
    smart_baseline.spMEThw: train C=0.4418
    smart_baseline.acMEThw: train C=0.4631
    smart_baseline.bwMEThw: train C=0.4470
  train      : 8,599 patients | events=1,136 (13.2%) | features=68
  validation : 2,141 patients | events=310 (14.5%) | features=68
  test       : 2,694 patients | events=381 (14.1%) | features=68
RESULT: arm=matched_baseline[group:protocol] n_features=68 train=8599/1253ev validation=2141/341ev test=2694/422ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_full
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/HR_protocol_full model=mlp model.input_size=68
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T17:25:23Z | screen: CTRL_demo_full

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

### RUN 2026-09-07T17:25:55Z | screen: CTRL_demo_rt

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

### RUN 2026-09-07T17:26:16Z | screen: CTRL_full_full

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

### RUN 2026-09-07T17:28:40Z | screen: CTRL_full_rt

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

### RUN 2026-09-07T17:31:14Z | screen: HR_chart_demo_rt

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

### RUN 2026-09-07T17:32:33Z | screen: HR_chart_full

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

### RUN 2026-09-07T17:34:23Z | screen: HR_chart_rt

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

### RUN 2026-09-07T17:35:39Z | screen: HR_chartstrict_rt

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

### RUN 2026-09-07T17:36:40Z | screen: HR_protocol_demo_rt

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

### RUN 2026-09-07T17:37:31Z | screen: HR_protocol_full

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

### RUN 2026-09-07T17:38:43Z | screen: HR_protocol_rt

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

### RUN 2026-09-07T17:39:32Z | screen: INCR_concepts_full

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

### RUN 2026-09-07T17:42:59Z | screen: INCR_tfidf_full

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

### RUN 2026-09-07T17:50:01Z | screen: INCR_volume_full

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

### RUN 2026-09-07T17:52:47Z | screen: SENS_no_omschr

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

### RUN 2026-09-07T18:06:56Z | screen: STRUCT_ctrl

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

### RUN 2026-09-07T18:09:22Z | screen: T0_volume

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

### RUN 2026-09-07T18:09:56Z | screen: T0_volume_rt

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

### RUN 2026-09-07T18:10:20Z | screen: T1_tfidf_3src

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

### RUN 2026-09-07T18:15:14Z | screen: T1_tfidf_char

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

### RUN 2026-09-07T18:20:10Z | screen: T1_tfidf_conclusie

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

### RUN 2026-09-07T18:21:49Z | screen: T1_tfidf_demo

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

### RUN 2026-09-07T18:27:02Z | screen: T1_tfidf_history

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

### RUN 2026-09-07T18:28:41Z | screen: T1_tfidf_nonames

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

### RUN 2026-09-07T18:33:34Z | screen: T1_tfidf_word

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

### RUN 2026-09-07T18:38:25Z | screen: T1_tfidf_word_full

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

### RUN 2026-09-07T18:42:23Z | screen: T2_concepts

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

### RUN 2026-09-07T18:42:55Z | screen: T2_concepts_alltiers

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

### RUN 2026-09-07T18:43:28Z | screen: T2_concepts_both

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

### RUN 2026-09-07T18:44:14Z | screen: T2_concepts_demo

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

### RUN 2026-09-07T18:44:47Z | screen: T2_concepts_history

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

---

### RUN 2026-09-07T20:29:56Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
- RESULT: graded vs curated (train, outcome-blind): 0 of 12 pairs reach |rho|>=0.3
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
  medication lexicon derived from med_20250709.csv (353,610 train rows): 18 of 18 classes have names in this cohort
    ace_remmer                   mht03   C09A/C09B       15 names: CAPTOPRIL, ENALAPRIL, ENALAPRIL AND DIURETICS, FOSINOPRIL, FOSINOPRIL AND DIURETICS, LISINOPRIL ...
    alfablokker                  mht05   C02CA            1 names: DOXAZOSIN
    at1_antagonist               mht12   C09C/C09D       18 names: CANDESARTAN, CANDESARTAN AND DIURETICS, EPROSARTAN, IRBESARTAN, IRBESARTAN AND DIURETICS, LOSARTAN ...
    betablokker                  mht01   C07              8 names: ATENOLOL, BISOPROLOL, CARVEDILOL, LABETALOL, METOPROLOL, NEBIVOLOL ...
    calciumantagonist            mht04   C08              9 names: AMLODIPINE, BARNIDIPINE, DILTIAZEM, FELODIPINE, LERCANIDIPINE, NICARDIPINE ...
    centraal_antihyp             mht07   C02A             3 names: CLONIDINE, METHYLDOPA (LEVOROTATORY), MOXONIDINE
    cholesterolabsorptieremmer   mli04   C10AX09          1 names: EZETIMIBE
    diureticum                   mht02   C03             10 names: BUMETANIDE, CHLORTALIDONE, EPITIZIDE AND POTASSIUM-SPARING AGENTS, EPLERENONE, FUROSEMIDE, HYDROCHLOROTHIAZIDE ...
    doac                         mas03   B01AE/B01AF      4 names: APIXABAN, DABIGATRAN ETEXILATE, EDOXABAN, RIVAROXABAN
    fibraat                      mli02   C10AB            3 names: BEZAFIBRATE, CIPROFIBRATE, GEMFIBROZIL
    galzuurbinder                mli03   C10AC            2 names: COLESEVELAM, COLESTYRAMINE
    insuline                     mgl02   A10A             8 names: INSULIN (HUMAN), INSULIN ASPART, INSULIN DEGLUDEC, INSULIN DEGLUDEC AND LIRAGLUTIDE, INSULIN DETEMIR, INSULIN GLARGINE ...
    lmwh                         mas02c  B01AB            3 names: DALTEPARIN, HEPARIN, NADROPARIN
    oraal_antidiabeticum         mgl01   A10B            17 names: ACARBOSE, DAPAGLIFLOZIN, EMPAGLIFLOZIN, GLIBENCLAMIDE, GLICLAZIDE, GLIMEPIRIDE ...
    plaatjesremmer               mas01   B01AC            8 names: ACETYLSALICYLIC ACID, CARBASALATE CALCIUM, CLOPIDOGREL, DIPYRIDAMOLE, ILOPROST, PRASUGREL ...
    statine                      mli01   C10AA            5 names: ATORVASTATIN, FLUVASTATIN, PRAVASTATIN, ROSUVASTATIN, SIMVASTATIN
    vasodilatator                mht41   C02DB/C02DD      1 names: HYDRALAZINE
    vka                          mas02   B01AA            2 names: ACENOCOUMAROL, PHENPROCOUMON
  lexicon written to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json
  40 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,322 ( 13.7%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,322 ( 13.7%)  median=0.00 p90=5.00
    graded.stenosis_left_max                    401 (  4.2%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   383 (  4.0%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,322 ( 13.7%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            830 (  8.6%)  median=16.75 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.smoking_status_max                 2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.alcohol_status_last                2,864 ( 29.7%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                     4,621 ( 47.9%)  median=2009.00 p90=2015.00
    graded.onset_year_n                       4,621 ( 47.9%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                       1,353 ( 14.0%)  median=2.70 p90=7.00
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=0.00 p90=4.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity

  --- extracted vs curated, TRAIN, outcome never consulted ---
  `both` is the patients where BOTH are present; agreement is only defined there.
  extracted                              curated                both     rho   exact   sens   spec
  graded.stenosis_max                    stenACIl/stenACIr       840  +0.072   0.206   -      -   
  graded.stenosis_left_max               stenACIl                241  +0.094   0.162   -      -   
  graded.stenosis_right_max              stenACIr                237  +0.125   0.186   -      -   
  graded.stenosis_ge50                   csten_50                829  +0.030   0.615  0.417  0.634
  graded.stenosis_ge70                   csten_70                829  +0.046   0.680  0.377  0.704
  graded.packyears                       packyrs                 513  +0.052     -     -      -   
  graded.smoking_status_last             roken                 1,778  -0.008   0.376   -      -   
  graded.alcohol_status_last             alcohol               1,823  -0.009   0.528   -      -   
  graded.alcohol_glasses_band            AlchlGlz                413  +0.008   0.230   -      -   
  graded.onset_year_min                  KliMaYr               1,918  -0.028     -     -      -   
  graded.aorta_cm_max                    aorta_hg                860  +0.002     -     -      -   
  graded.n_antihypertensive_classes      mht_alln              6,210  -0.011     -     -      -   
RESULT: graded vs curated (train, outcome-blind): 0 of 12 pairs reach |rho|>=0.3
  ** nothing reaches |rho|>=0.3: the extraction does not recover the curated
     quantities, so a null survival result would be about extraction, not text **

  extracted medication class             curated      both   sens   spec
  ace_remmer                             mht03       6,210  0.210  0.777
  alfablokker                            mht05       6,210  0.000  1.000
  at1_antagonist                         mht12       6,210  0.070  0.931
  betablokker                            mht01       6,210  0.265  0.727
  calciumantagonist                      mht04       6,210  0.337  0.656
  centraal_antihyp                       mht07       6,210  0.000  0.993
  cholesterolabsorptieremmer             mli04       5,858  0.014  0.976
  diureticum                             mht02       6,210  0.088  0.917
  doac                                   mas03       6,210  0.028  0.994
  fibraat                                mli02       5,858  0.000  0.997
  galzuurbinder                          mli03       5,858  0.000  0.999
  insuline                               mgl02       6,210  0.000  1.000
  lmwh                                   mas02c      6,210  0.000  0.999
  oraal_antidiabeticum                   mgl01       6,210  0.018  0.974
  plaatjesremmer                         mas01       6,210  0.216  0.774
  statine                                mli01       5,858  0.001  0.998
  vasodilatator                          mht41       6,210  0.000  0.999
  vka                                    mas02       6,210  0.074  0.928

  raw feature matrix: 9,644 patients x 40 features

  --- univariate screen on RAW (un-imputed) features, train, horizon 5475d ---
  828 events; each feature scored only on the patients who HAVE it
  permutation-calibrated null: SE(C) = 0.292/sqrt(events) (the analytic 0.5/sqrt(events) is ~1.6x too wide under this censoring)
  C_mono = raw value; C_udev = |value - median|, which catches U-shaped risk that
  a monotone C-index cannot see (a true 0.62 U-shape reads as 0.50 monotone)
  40 features tested = ~18 independent tests (correlated aggregators of the same code) | clearing raw 2-SE: 0 (~1 expected from noise)
  surviving Benjamini-Hochberg FDR 5%: 0 | surviving Bonferroni (p<2.8e-03): 0  <- believe these, not the raw count
  feature                                   C_mono  C_udev   trn%    ev     z       sig
  graded.stenosis_n                         0.4716  0.4501  13.7%   123  1.90          
  graded.smoking_status_max                 0.5336  0.5302  28.7%   223  1.72          
  graded.med_plaatjesremmer                 0.4906  0.4906 100.0%   828  0.93          
  graded.smoking_status_last                0.5279  0.5155  28.7%   223  1.43          
  graded.n_med_classes                      0.4911  0.4911 100.0%   828  0.88          
  graded.med_at1_antagonist                 0.4918  0.4918 100.0%   828  0.81          
  graded.med_vka                            0.4919  0.4919 100.0%   828  0.80          
  graded.alcohol_status_last                0.5239  0.4761  29.6%   234  1.26          
  graded.med_oraal_antidiabeticum           0.4939  0.4939 100.0%   828  0.60          
  graded.med_calciumantagonist              0.4939  0.4939 100.0%   828  0.60          
  graded.med_diureticum                     0.4945  0.4945 100.0%   828  0.54          
  graded.packyears_measured                 0.4947  0.4947 100.0%   828  0.52          
  graded.n_antihypertensive_classes         0.4951  0.4951 100.0%   828  0.48          
  graded.med_ace_remmer                     0.5048  0.5048 100.0%   828  0.47          
  graded.onset_year_n                       0.4860  0.4921  48.3%   385  0.94          
  graded.onset_measured                     0.4956  0.4956 100.0%   828  0.43          
  graded.stenosis_measured                  0.5035  0.5035 100.0%   828  0.35          
  graded.any_antihypertensive               0.4967  0.4967 100.0%   828  0.33          
  graded.onset_year_min                     0.5048  0.5117  48.3%   385  0.79          
  graded.med_betablokker                    0.4984  0.4984 100.0%   828  0.16          
  graded.med_cholesterolabsorptieremmer     0.5012  0.5012 100.0%   828  0.12          
  graded.med_fibraat                        0.4992  0.4992 100.0%   828  0.08          
  graded.med_statine                        0.4995  0.4995 100.0%   828  0.05          
  graded.med_galzuurbinder                  0.5004  0.5004 100.0%   828  0.04          
  graded.med_doac                           0.5004  0.5004 100.0%   828  0.04          
  graded.aorta_measured                     0.5004  0.5004 100.0%   828  0.03          
  graded.med_vasodilatator                  0.4997  0.4997 100.0%   828  0.03          
  graded.med_lmwh                           0.4997  0.4997 100.0%   828  0.03          
  graded.med_centraal_antihyp               0.4998  0.4998 100.0%   828  0.02          
  graded.med_insuline                       0.5000  0.5000 100.0%   828  0.00          
  trn% is the share of the TRAIN split carrying a value (the screen is train-only);
  a feature covering a few percent cannot drive a cohort-level model, however real
  its subcohort signal. Count/indicator features are never missing, so they read 100%.
  ** nothing clears its floor even before imputation: not an imputation artefact **

  winsorised at train quantiles [0.001, 0.999]
  dropped 3 features constant or all-missing on train
  dropped 4 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 116,816 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=33
  validation : 1,510 patients | events=206 (13.6%) | features=33
  test       : 1,924 patients | events=257 (13.4%) | features=33
RESULT: arm=text_graded[dates=year] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt model=mlp model.input_size=33
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T20:33:24Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_strip_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 40 features; 4218 of 9644 patients have at least one extracted quantity
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
  40 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,322 ( 13.7%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,322 ( 13.7%)  median=0.00 p90=5.00
    graded.stenosis_left_max                    400 (  4.1%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   382 (  4.0%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,322 ( 13.7%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            830 (  8.6%)  median=16.75 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.smoking_status_max                 2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.alcohol_status_last                2,864 ( 29.7%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                     3,125 ( 32.4%)  median=2007.00 p90=2014.00
    graded.onset_year_n                       3,125 ( 32.4%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                       1,353 ( 14.0%)  median=2.70 p90=7.00
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=0.00 p90=4.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 40 features; 4218 of 9644 patients have at least one extracted quantity
  raw feature matrix: 9,644 patients x 40 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 3 features constant or all-missing on train
  dropped 4 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 119,810 missing cells with the train median, then standardised
  train      : 6,210 patients | events=828 (13.3%) | features=33
  validation : 1,510 patients | events=206 (13.6%) | features=33
  test       : 1,924 patients | events=257 (13.4%) | features=33
RESULT: arm=text_graded[dates=strip] n_features=33 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_strip_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_strip_rt model=mlp model.input_size=33
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T20:36:32Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=year]+baseline[leeftijd,geslacht] n_features=35 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=year med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
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
  40 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,322 ( 13.7%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,322 ( 13.7%)  median=0.00 p90=5.00
    graded.stenosis_left_max                    401 (  4.2%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   383 (  4.0%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,322 ( 13.7%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            830 (  8.6%)  median=16.75 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.smoking_status_max                 2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.alcohol_status_last                2,864 ( 29.7%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                     4,621 ( 47.9%)  median=2009.00 p90=2015.00
    graded.onset_year_n                       4,621 ( 47.9%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                       1,353 ( 14.0%)  median=2.70 p90=7.00
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=0.00 p90=4.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 42 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 3 features constant or all-missing on train
  dropped 4 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 116,816 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=35
  validation : 1,510 patients | events=206 (13.6%) | features=35
  test       : 1,924 patients | events=257 (13.4%) | features=35
RESULT: arm=text_graded[dates=year]+baseline[leeftijd,geslacht] n_features=35 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt model=mlp model.input_size=35
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T20:39:49Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=leeftijd,geslacht out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=year]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=74 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=year med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='leeftijd,geslacht' min_coverage_frac=0.1
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
  40 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,322 ( 13.7%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,322 ( 13.7%)  median=0.00 p90=5.00
    graded.stenosis_left_max                    401 (  4.2%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   383 (  4.0%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,322 ( 13.7%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            830 (  8.6%)  median=16.75 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.smoking_status_max                 2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.alcohol_status_last                2,864 ( 29.7%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                     4,621 ( 47.9%)  median=2009.00 p90=2015.00
    graded.onset_year_n                       4,621 ( 47.9%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                       1,353 ( 14.0%)  median=2.70 p90=7.00
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=0.00 p90=4.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  concept tiers in use: disease,symptom
  concepts with no terms in these tiers, skipped: revascularisatie
  + 39 concept features appended (binary/disease,symptom)
  appending 2 baseline columns -> ['geslacht', 'leeftijd']
  raw feature matrix: 9,644 patients x 81 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 3 features constant or all-missing on train
  dropped 4 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  imputed 116,816 missing cells with the train median, then standardised
  self-check on the appended baseline columns (each should be clearly off 0.5;
  if one is missing or ~0.5 the arm is broken, not null):
    smart_baseline.geslacht: train C=0.4422
    smart_baseline.leeftijd: train C=0.6731
  train      : 6,210 patients | events=828 (13.3%) | features=74
  validation : 1,510 patients | events=206 (13.6%) | features=74
  test       : 1,924 patients | events=257 (13.4%) | features=74
RESULT: arm=text_graded[dates=year]+concepts[disease,symptom]+baseline[leeftijd,geslacht] n_features=74 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt model=mlp model.input_size=74
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T20:43:27Z | text arm: graded

- status: ok
- context: mode=graded landmark=180 horizon=5475 analyzer=word require_text=True strip_nameish=False concept_encoding=binary add_baseline=all out=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt
- RESULT: documents=121778 patients_with_text=9644/13434 (71.8%)
- RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
- RESULT: arm=text_graded[dates=year]+baseline[all] n_features=216 train=6210/914ev validation=1510/230ev test=1924/287ev

<details><summary>full output</summary>

```
  ARGS: mode=graded landmark=180 lookback=None horizon=5475 section=None analyzer=word svd=256 require_text=True strip_dates=True date_mode=year med_lexicon=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/med_lexicon.json strip_names=True strip_nameish=False concept_encoding=binary concept_terms=disease,symptom expand_terms=0 add_baseline_cols='all' min_coverage_frac=0.1
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
  40 graded features; coverage over 9,644 patients (NaN = not stated, which the pre-imputation screen scores separately):
    graded.stenosis_max                       1,322 ( 13.7%)  median=2.00 p90=6.00
    graded.stenosis_last                      1,322 ( 13.7%)  median=0.00 p90=5.00
    graded.stenosis_left_max                    401 (  4.2%)  median=3.00 p90=6.00
    graded.stenosis_right_max                   383 (  4.0%)  median=2.00 p90=6.00
    graded.stenosis_ge50                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_ge70                      1,322 ( 13.7%)  median=0.00 p90=1.00
    graded.stenosis_n                         1,322 ( 13.7%)
    graded.stenosis_measured                  9,644 (100.0%)
    graded.packyears                            830 (  8.6%)  median=16.75 p90=45.00
    graded.packyears_measured                 9,644 (100.0%)
    graded.smoking_status_last                2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.smoking_status_max                 2,765 ( 28.7%)  median=1.00 p90=3.00
    graded.alcohol_status_last                2,864 ( 29.7%)  median=3.00 p90=3.00
    graded.alcohol_glasses_band                 631 (  6.5%)  median=0.00 p90=3.00
    graded.onset_year_min                     4,621 ( 47.9%)  median=2009.00 p90=2015.00
    graded.onset_year_n                       4,621 ( 47.9%)
    graded.onset_measured                     9,644 (100.0%)
    graded.aorta_cm_max                       1,353 ( 14.0%)  median=2.70 p90=7.00
    graded.aorta_measured                     9,644 (100.0%)
    graded.n_antihypertensive_classes         9,644 (100.0%)  median=0.00 p90=3.00
    graded.any_antihypertensive               9,644 (100.0%)  median=0.00 p90=1.00
    graded.n_med_classes                      9,644 (100.0%)  median=0.00 p90=4.00
    graded.med_ace_remmer                     9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_alfablokker                    9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_at1_antagonist                 9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_betablokker                    9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_calciumantagonist              9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_centraal_antihyp               9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_cholesterolabsorptieremmer     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_diureticum                     9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_doac                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_fibraat                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_galzuurbinder                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_insuline                       9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_lmwh                           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_oraal_antidiabeticum           9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_plaatjesremmer                 9,644 (100.0%)  median=0.00 p90=1.00
    graded.med_statine                        9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vasodilatator                  9,644 (100.0%)  median=0.00 p90=0.00
    graded.med_vka                            9,644 (100.0%)  median=0.00 p90=0.00
RESULT: graded: 40 features; 5424 of 9644 patients have at least one extracted quantity
  appending 183 baseline columns -> ['geslacht', 'leeftijd', 'opleiding', 'RespLand', 'PaLand', 'MaLand', 'WereldDl', 'diagnsco', 'vaatzkt1', 'DiagSide', 'IncInt_p', 'IncInt_v', 'V0405', 'vg_0410', 'vgok_car', 'vgt_kop', 'vz_kop', 'vg_0321', 'vg_0323', 'vgok_har', 'vgt_hart', 'vz_hart', 'vg_0325', 'vgok_aaa', 'vgt_aaa', 'vz_aaa', 'vg_0606c', 'vgok_nie', 'vgt_nier', 'vz_nier', 'vg_0519', 'vgok_bee', 'vgt_been', 'vz_been', 'bdsys', 'bddia', 'hyptns_n', 'hyptns_b', 'vz_hypt', 'labgluc', 'hypgly_n', 'hypgly_b', 'vz_DM', 'vz_t1d', 'vz_t2d', 'klinman', 'gewicht', 'lengte', 'bm_indx', 'bmi_30', 'tail_gm', 'heup_gm', 'tlhp_rat', 'vet_subc', 'vet_gm', 'plsprs', 'abi_lg', 'abi_gm', 'abivrl_n', 'ABiRe', 'ABiLi', 'imt_gm', 'stenACIr', 'stenACIl', 'csten_50', 'csten_70', 'AortProx', 'AortDist', 'aorta_hg', 'aorta_gm', 'aaaech_n', 'nrlng_re', 'nrlng_li', 'nrlng_gm', 'nratrof', 'nrvol_re', 'nrvol_li', 'nrvol_gm', 'labhb', 'labht', 'labchol', 'labtrig', 'labhdl', 'ldlchol', 'VgBh_HpL', 'hyplip_n', 'hyplip_b', 'vz_HypLp', 'labkrea', 'labmalb', 'labkrur', 'mpkr_rat', 'albminur', 'nrfaln_n', 'klar_coc', 'klar_gst', 'MDRD', 'labhcyst', 'hyphmc_n', 'labins', 'labtsh', 'labcrp', 'labhba1c', 'labapob', 'roken', 'packyrs', 'alcohol', 'AlchlGlz', 'V0821', 'V082201', 'V082202', 'V0823', 'MBSc', 'MBS', 'MBSc_mis', 'MBScgr', 'kl1fysfc', 'kl2socfc', 'kl3rolfy', 'kl4rolem', 'kl5mengz', 'kl6vital', 'kl7pijn', 'kl8alggz', 'kl9gezva', 'mht01', 'mht02', 'mht02a', 'mht02b', 'mht02c', 'mht02d', 'mht03', 'mht04', 'mht05', 'mht06', 'mht07', 'mht12', 'mht33', 'mht41', 'mliphoop', 'mli01', 'mli02', 'mli03', 'mli04', 'mas01', 'mas01a', 'mas01b', 'mas01c', 'mas01d', 'mas02', 'mas02a', 'mas02b', 'mas02c', 'mas03', 'mmpr', 'mhmc', 'mgl01', 'mgl02', 'mgl03', 'TCA', 'SSRI', 'MAO', 'OthADep', 'Benzo', 'BenzoDer', 'BenzoRel', 'Thyr', 'Amiodar', 'Lithium', 'mht_alln', 'mht_all', 'lipmid', 'statine', 'pamid', 'aspirine', 'pa_stolmid', 'KliMaC', 'KliMaYr', 'KliMaDur', 'KliMaDrD', 'spMEThw', 'acMEThw', 'bwMEThw']
  raw feature matrix: 9,644 patients x 223 features
  winsorised at train quantiles [0.001, 0.999]
  dropped 3 features constant or all-missing on train
  dropped 4 features covered in <10% of train (post-imputation they are near-constant and only add noise)
  4 features had ~zero train variance; left unscaled instead of divided by ~0 (that would swamp a penalised model)
  imputed 278,890 missing cells with the train median, then standardised
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
RESULT: arm=text_graded[dates=year]+baseline[all] n_features=216 train=6210/914ev validation=1510/230ev test=1924/287ev

Saved to /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt
Train with:  dataset=smartehr_embeddings dataset.root_path=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt model=mlp model.input_size=216
(feature_names in metadata.json — use them to interpret the fitted model)
```

</details>

---

### RUN 2026-09-07T20:46:51Z | screen: CTRL_demo_full

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

### RUN 2026-09-07T20:47:22Z | screen: CTRL_demo_rt

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

### RUN 2026-09-07T20:47:43Z | screen: CTRL_full_full

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

### RUN 2026-09-07T20:50:08Z | screen: CTRL_full_rt

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

### RUN 2026-09-07T20:52:42Z | screen: GRADED_all_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 74 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_all_demo_rt/
  representation=text_graded[dates=year]+concepts[disease,symptom]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=74

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   74 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   74 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   74 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 14 of 74 effectively constant (zero variance, or one value in >99% of patients); 69 take <=10 distinct values (normal for counts)
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
  concept.diabetes_present                             0.4854   0.4854   0.4848
  concept.aneurysma_present                            0.4881   0.4881   0.4935
  concept.hypertensie_negated                          0.4892   0.4892   0.5027
  concept.nierfunctie_present                          0.4900   0.4900   0.4954
  graded.med_plaatjesremmer                            0.4906   0.4906   0.4964
  concept.hyperlipidemie_present                       0.4908   0.4908   0.4627
  graded.onset_year_n                                  0.4924   0.4909   0.4634
  graded.n_med_classes                                 0.4911   0.4911   0.4933
  concept.perifeer_vaatlijden_present                  0.4916   0.4916   0.4941
  concept.myocardinfarct_present                       0.4917   0.4917   0.5048
  concept.atriumfibrilleren_present                    0.4918   0.4918   0.4968
  graded.med_at1_antagonist                            0.4918   0.4918   0.5030
  graded.med_vka                                       0.4919   0.4919   0.4947
  graded.smoking_status_max                            0.5077   0.5053   0.4805
  concept.stenose_present                              0.4924   0.4924   0.4742
  graded.alcohol_status_last                           0.5075   0.4925   0.5060
  concept.angina_present                               0.4928   0.4928   0.4931
  graded.smoking_status_last                           0.5072   0.5016   0.4911

  74 features are only ~59 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~3 times, not ~4.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 14 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6809  val C=0.7072
  penalizer=0.1      train C=0.6486  val C=0.6280
  penalizer=1        train C=0.6367  val C=0.6111
  penalizer=10       train C=0.6366  val C=0.6109
  penalizer=100      train C=0.6366  val C=0.6109

  selected penalizer=0.01 -> TEST C=0.6749 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6749 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-07T20:53:28Z | screen: GRADED_demo_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 2 of 35 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.6746 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_demo_rt/
  representation=text_graded[dates=year]+baseline[leeftijd,geslacht] | landmark_days=180 | horizon_days=5475 | n_features=35

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=   35 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=   35 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=   35 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 6 of 35 effectively constant (zero variance, or one value in >99% of patients); 30 take <=10 distinct values (normal for counts)
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
  graded.med_plaatjesremmer                            0.4906   0.4906   0.4964
  graded.onset_year_n                                  0.4924   0.4909   0.4634
  graded.n_med_classes                                 0.4911   0.4911   0.4933
  graded.med_at1_antagonist                            0.4918   0.4918   0.5030
  graded.med_vka                                       0.4919   0.4919   0.4947
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
  graded.onset_measured                                0.4956   0.4956   0.5139
  graded.stenosis_measured                             0.5035   0.5035   0.4881
  graded.any_antihypertensive                          0.4967   0.4967   0.4952

  35 features are only ~26 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~1 times, not ~2.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 6 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.6805  val C=0.7067
  penalizer=0.1      train C=0.6718  val C=0.6599
  penalizer=1        train C=0.6644  val C=0.6449
  penalizer=10       train C=0.6643  val C=0.6448
  penalizer=100      train C=0.6643  val C=0.6448

  selected penalizer=0.01 -> TEST C=0.6746 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.6746 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-07T20:54:00Z | screen: GRADED_full_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 103 of 216 features clear the 0.0203 floor; strongest smart_baseline.leeftijd C=0.6731
- RESULT: COX lasso penalizer=0.01 TEST C=0.7396 (2-SE band +/-0.062) -> signal

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_full_rt/
  representation=text_graded[dates=year]+baseline[all] | landmark_days=180 | horizon_days=5475 | n_features=216

--- label sanity (a broken target shows up here, not in the model) ---
  train       n= 6,210 features=  216 events=  828 (13.3%) duration p0/p50/p100 = 1/2985/5475
  validation  n= 1,510 features=  216 events=  206 (13.6%) duration p0/p50/p100 = 4/3130/5475
  test        n= 1,924 features=  216 events=  257 (13.4%) duration p0/p50/p100 = 3/2939/5475

  feature spread: 27 of 216 effectively constant (zero variance, or one value in >99% of patients); 167 take <=10 distinct values (normal for counts)
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

  216 features are only ~141 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~7 times, not ~11.

--- best feature train vs test: smart_baseline.leeftijd ---
  train C=0.6731  test C=0.6716

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 27 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.7631  val C=0.7763
  penalizer=0.1      train C=0.7499  val C=0.7658
  penalizer=1        train C=0.7495  val C=0.7638
  penalizer=10       train C=0.7495  val C=0.7638
  penalizer=100      train C=0.7495  val C=0.7638

  selected penalizer=0.01 -> TEST C=0.7396 (test 2-SE band around 0.5 is +/-0.062)
  verdict: signal
RESULT: COX lasso penalizer=0.01 TEST C=0.7396 (2-SE band +/-0.062) -> signal
```

</details>

---

### RUN 2026-09-07T20:57:19Z | screen: GRADED_rt

- status: ok
- context: parquet_dir=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt/ cox=True l1_ratio=1.0
- RESULT: univariate: 0 of 33 features clear the 0.0203 floor
- RESULT: COX lasso penalizer=0.01 TEST C=0.4920 (2-SE band +/-0.062) -> indistinguishable from chance

<details><summary>full output</summary>

```
=== /home/lorenzo.pratesi@mydre.org/workspace/smartehr/arms/GRADED_rt/
  representation=text_graded[dates=year] | landmark_days=180 | horizon_days=5475 | n_features=33

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
  graded.onset_year_n                                  0.4924   0.4909   0.4634
  graded.n_med_classes                                 0.4911   0.4911   0.4933
  graded.med_at1_antagonist                            0.4918   0.4918   0.5030
  graded.med_vka                                       0.4919   0.4919   0.4947
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
  graded.onset_measured                                0.4956   0.4956   0.5139
  graded.stenosis_measured                             0.5035   0.5035   0.4881
  graded.any_antihypertensive                          0.4967   0.4967   0.4952
  graded.stenosis_max                                  0.5027   0.5005   0.5014
  graded.stenosis_ge50                                 0.5017   0.5017   0.4943

  33 features are only ~24 INDEPENDENT tests (PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.
  Pure noise would therefore clear the floor ~1 times, not ~2.
  ** No feature clears the floor, and with this few independent tests that is
     consistent with a genuine absence of univariate signal. **

--- penalised Cox (lasso, l1_ratio=1.0): tuned on validation, reported on test ---
  dropped 6 effectively-constant columns before fitting (they make the design singular)
  penalizer=0.01     train C=0.5198  val C=0.4755
  penalizer=0.1      train C=0.5210  val C=0.4725
  penalizer=1        train C=0.5210  val C=0.4725
  penalizer=10       train C=0.5210  val C=0.4725
  penalizer=100      train C=0.5210  val C=0.4725

  selected penalizer=0.01 -> TEST C=0.4920 (test 2-SE band around 0.5 is +/-0.062)
  verdict: indistinguishable from chance
RESULT: COX lasso penalizer=0.01 TEST C=0.4920 (2-SE band +/-0.062) -> indistinguishable from chance
```

</details>

---

### RUN 2026-09-07T20:57:49Z | screen: GRADED_strip_rt

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

### RUN 2026-09-07T20:58:19Z | screen: HR_chart_demo_rt

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

### RUN 2026-09-07T20:59:36Z | screen: HR_chart_full

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

### RUN 2026-09-07T21:01:27Z | screen: HR_chart_rt

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

### RUN 2026-09-07T21:02:43Z | screen: HR_chartstrict_rt

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

### RUN 2026-09-07T21:03:44Z | screen: HR_protocol_demo_rt

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

### RUN 2026-09-07T21:04:34Z | screen: HR_protocol_full

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

### RUN 2026-09-07T21:05:46Z | screen: HR_protocol_rt

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

### RUN 2026-09-07T21:06:34Z | screen: INCR_concepts_full

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

### RUN 2026-09-07T21:10:01Z | screen: INCR_tfidf_full

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

### RUN 2026-09-07T21:17:04Z | screen: INCR_volume_full

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

### RUN 2026-09-07T21:19:50Z | screen: SENS_no_omschr

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

### RUN 2026-09-07T21:33:23Z | screen: STRUCT_ctrl

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

### RUN 2026-09-07T21:35:47Z | screen: T0_volume

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

### RUN 2026-09-07T21:36:21Z | screen: T0_volume_rt

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

### RUN 2026-09-07T21:36:45Z | screen: T1_tfidf_3src

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

### RUN 2026-09-07T21:41:40Z | screen: T1_tfidf_char

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

### RUN 2026-09-07T21:46:32Z | screen: T1_tfidf_conclusie

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

### RUN 2026-09-07T21:48:11Z | screen: T1_tfidf_demo

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

### RUN 2026-09-07T21:53:20Z | screen: T1_tfidf_history

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

### RUN 2026-09-07T21:54:59Z | screen: T1_tfidf_nonames

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

### RUN 2026-09-07T21:59:52Z | screen: T1_tfidf_word

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

### RUN 2026-09-07T22:04:46Z | screen: T1_tfidf_word_full

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

### RUN 2026-09-07T22:08:44Z | screen: T2_concepts

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

### RUN 2026-09-07T22:09:16Z | screen: T2_concepts_alltiers

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

### RUN 2026-09-07T22:09:49Z | screen: T2_concepts_both

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

### RUN 2026-09-07T22:10:35Z | screen: T2_concepts_demo

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

### RUN 2026-09-07T22:11:08Z | screen: T2_concepts_history

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
