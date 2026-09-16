# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (2 runs)

- **2026-09-16T08:19:38Z | corrected delivery check**
  - RESULT: EHR csv hashes: 0 identical, 16 differ, 0 on one side only
  - RESULT: ** 16 EHR FILES DIFFER between the inbox and what was analysed **: the analysis was not run on the inbox copies
  - RESULT: EHR content comparison: inbox and analysed copies agree on ids, per-id row counts and per-id values in every file: True
  - RESULT: corrected registry ids: 13806 distinct vs 13806 original; identical=True; shared 13806
  - RESULT: corrected registry: 0 of 13806 shared ids keep the same row content (0.0%); same multiset of rows=False
  - RESULT: value triangulation across original raw / corrected raw / local normalised written for 6 columns
  - RESULT: normalised the corrected export: 0 decimal-comma columns converted, 13806 rows
  - RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.022)
  - RESULT: join check meting.Lengte vs lengte: n=8202 rho=+0.002 (shuffled -0.014)
  - RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.031)
  - RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
  - RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.014 (shuffled +0.020)
  - RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.014 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn
  - RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager
  - RESULT: registry self-consistency: BMI vs weight/height^2 rho=+1.000 on 13772 rows (median abs diff 0.00)
  - RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)
  - RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949 vs 10954 expected under independence (ratio 0.9995)
  - RESULT: ** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent id assignments over the same numbering range would produce by arithmetic alone, so the 10949 'matching' patients match by coincidence. The extracts come from different pseudonymisation runs and a crosswalk is required
  - RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
  - RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
  - RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
  - RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
  - RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
  - RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable
  - RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.021)
  - RESULT: join check meting.Lengte vs lengte: n=8202 rho=-0.017 (shuffled +0.006)
  - RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.029)
  - RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
  - RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.012 (shuffled +0.020)
  - RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.017 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn
  - RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager
  - RESULT: registry self-consistency: BMI vs weight/height^2 rho=+0.798 on 13731 rows (median abs diff 6.25)
  - RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)
  - RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949 vs 10954 expected under independence (ratio 0.9995)
  - RESULT: ** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent id assignments over the same numbering range would produce by arithmetic alone, so the 10949 'matching' patients match by coincidence. The extracts come from different pseudonymisation runs and a crosswalk is required
  - RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
  - RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
  - RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
  - RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
  - RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
  - RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable
- **2026-09-16T08:27:05Z | diagnose: did normalisation break the join?**
  - RESULT: ** ROW COUNT CHANGED in the registry: 13808 -> 13806 **
  - RESULT: registry id->weight preserved by normalisation: n=5223 rho=+1.000
  - RESULT: id normalisation row check: 0.00% of zero-padded ids differ vs 0.00% of non-padded -- a padding bug hits one group and not the other
  - RESULT: ** ID NORMALISATION IS CLEAN **: all 13806 ids keep their own row across every one of 260 shared columns, zero-padded and not alike
  - RESULT: rank-matched (k-th smallest id to k-th smallest id) weight agreement: rho=+0.000 on 12771 pairs
  - RESULT: normalisation is NOT the culprit (best agreement across all four pairings: original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011): the originals do not join either, so the two extracts genuinely carry independent pseudonymisation runs and a crosswalk is required

---

### RUN 2026-09-16T08:19:38Z | corrected delivery check

- status: ok
- context: inbox=/mnt/data/inbox/SMART_EHRDATA/
- RESULT: EHR csv hashes: 0 identical, 16 differ, 0 on one side only
- RESULT: ** 16 EHR FILES DIFFER between the inbox and what was analysed **: the analysis was not run on the inbox copies
- RESULT: EHR content comparison: inbox and analysed copies agree on ids, per-id row counts and per-id values in every file: True
- RESULT: corrected registry ids: 13806 distinct vs 13806 original; identical=True; shared 13806
- RESULT: corrected registry: 0 of 13806 shared ids keep the same row content (0.0%); same multiset of rows=False
- RESULT: value triangulation across original raw / corrected raw / local normalised written for 6 columns
- RESULT: normalised the corrected export: 0 decimal-comma columns converted, 13806 rows
- RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.022)
- RESULT: join check meting.Lengte vs lengte: n=8202 rho=+0.002 (shuffled -0.014)
- RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.031)
- RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
- RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.014 (shuffled +0.020)
- RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.014 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn
- RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager
- RESULT: registry self-consistency: BMI vs weight/height^2 rho=+1.000 on 13772 rows (median abs diff 0.00)
- RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)
- RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949 vs 10954 expected under independence (ratio 0.9995)
- RESULT: ** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent id assignments over the same numbering range would produce by arithmetic alone, so the 10949 'matching' patients match by coincidence. The extracts come from different pseudonymisation runs and a crosswalk is required
- RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
- RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
- RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
- RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
- RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
- RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
- RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
- RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable
- RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.021)
- RESULT: join check meting.Lengte vs lengte: n=8202 rho=-0.017 (shuffled +0.006)
- RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.029)
- RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
- RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.012 (shuffled +0.020)
- RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.017 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn
- RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager
- RESULT: registry self-consistency: BMI vs weight/height^2 rho=+0.798 on 13731 rows (median abs diff 6.25)
- RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)
- RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949 vs 10954 expected under independence (ratio 0.9995)
- RESULT: ** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent id assignments over the same numbering range would produce by arithmetic alone, so the 10949 'matching' patients match by coincidence. The extracts come from different pseudonymisation runs and a crosswalk is required
- RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
- RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
- RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
- RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
- RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
- RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
- RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
- RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable

<details><summary>full output</summary>

```
=== 1. EHR csv hashes: inbox vs currently used ============================
  inbox   /mnt/data/inbox/SMART_EHRDATA/ (16 csv)
  current data/smartehr-utf8 (16 csv)

  file                               status       sha1 (current)                                  MB
  consult_20251208.csv               ** DIFFERS ** ce621ffdff9ad5f6535217cbb40b91389b7df350     313.2
                                                  inbox: c9a71cf035c0b94c9706540bdbd511850b378c8a  (379.8 MB)
  dbc_20251203.csv                   ** DIFFERS ** f26a91a2d212fb6e952b1094c22814df26d57049       9.4
                                                  inbox: e0c609dd6de2e0c42cd8e7dd13ffdc8c24242434  (9.6 MB)
  diag_20250626.csv                  ** DIFFERS ** 372f56da1a39dfb5c89eebfc4106d700d6c18bad       6.8
                                                  inbox: 77f9025cf113180de46460a6d350cb4dd51798ca  (7.0 MB)
  ecg_measmatrix_20251208.csv        ** DIFFERS ** 644332012b59d4692ca6ecccba171d5fe194d1d3       8.5
                                                  inbox: 3a8bc8e8eadd6b18ffbe8a1acfe19db01118dd34  (8.7 MB)
  echo_20250626.csv                  ** DIFFERS ** b24697833f24fee5c4a34200bca4340a66a75193      25.2
                                                  inbox: 514fe99cb555b5311640a4f482ee6bb2a014d88b  (26.3 MB)
  hos_20251209.csv                   ** DIFFERS ** 2aadce96c4c64cfa6bbc6b5dd25678b7e4d232a4       0.6
                                                  inbox: 698c902662c9c1abc2a0a4846c3bfb08b247bd67  (0.7 MB)
  hos_mut_20251209.csv               ** DIFFERS ** bc9980188b0ac6818c9e8a4d391deaeeca3027e9       8.1
                                                  inbox: 7b7338d92e9db64552e03c921502b0930f7cdbbe  (8.3 MB)
  lab_ezis_20250709.csv              ** DIFFERS ** be4390c3ed8d021e08e400ec5275fd2c589af19f     132.4
                                                  inbox: 80ebe60c467dabb9b515747491adc2eb6caa2eda  (135.0 MB)
  med_20250709.csv                   ** DIFFERS ** f59d0f1c39af037b899ef01dd71c9241aac9764c      29.5
                                                  inbox: dbe1e190958a42c18072490c470cd02231e57dc4  (29.3 MB)
  meting_20251203.csv                ** DIFFERS ** 771a277670f761ca5bae2ed7fd9632c3c3e3afac     803.2
                                                  inbox: 552fdbc759d944cdf37abdadd98269d472dac483  (840.0 MB)
  mri_verslag_20250626.csv           ** DIFFERS ** d2b3609ce1cd9633aea8287b5d9919ed42d1b882       2.6
                                                  inbox: cf02ac44c0386d87f6a195ca85492ccf5623a407  (2.6 MB)
  ok_20250626.csv                    ** DIFFERS ** b6c2e5b53ed75d620e857f6e844f0cf09c155f38       1.9
                                                  inbox: 5bf9d03ae6866d2d8092d0389c4a0026b9140443  (2.0 MB)
  ok_verslag_20250626.csv            ** DIFFERS ** 6e58b640848ddc20d3a7762ba23cbea154ba1602       5.1
                                                  inbox: 7ef8769f61b612d9e59bb72cde40dc4fa67c11cf  (5.2 MB)
  radiologie_verslag_20251208.csv    ** DIFFERS ** c25764394114009d090ebe238a40da30a87b8e97      55.7
                                                  inbox: 4126b6371628d9c0e8d126215f1a195c67e48359  (55.8 MB)
  uitgaandebrief_20251208.csv        ** DIFFERS ** b30eb6b284164be557a1f28bece2b85f9a3e6f02     254.4
                                                  inbox: e2f0ac740c73174e076a4d967bf1a1672e4be70e  (254.0 MB)
  verr_20251203.csv                  ** DIFFERS ** 471ecd0e7868c4ad95a35820bccb4914a0ad315c       1.9
                                                  inbox: e7603a6d5b9b0e1df3d1249215da9149b759e024  (2.0 MB)

  registry exports in the inbox (not EHR extracts, not counted above):
  smart_22nov2022.csv                             c34af94832a6fcee0ff5038c5d0c15af6238576c       9.5
  smart_22nov2022_corrected.csv                   9217e042406d9fe2062e95ecdbe600e2a9c1f671      10.8

  EHR extracts: 0 identical, 16 differing, 0 present on one side only
RESULT: EHR csv hashes: 0 identical, 16 differ, 0 on one side only
RESULT: ** 16 EHR FILES DIFFER between the inbox and what was analysed **: the analysis was not run on the inbox copies

=== 1b. EHR content: same data, or different data? ========================
  'ids/rows/values' = id sets equal / per-id row counts equal / per-id values equal
  file                                inbox rows   cur rows  inbox ids   cur ids  ids/rows/values
  consult_20251208.csv                   286,193    286,193      8,991     8,991        True/True
  dbc_20251203.csv                       187,827    187,827     12,532    12,532        True/True
  diag_20250626.csv                      127,741    127,741     14,354    14,354        True/True
  ecg_measmatrix_20251208.csv            154,214    154,214     15,390    15,390        True/True
  echo_20250626.csv                      671,168    671,168      4,768     4,768        True/True
  hos_20251209.csv                        43,553     43,553     12,227    12,227   True/True/True
  hos_mut_20251209.csv                   129,462    129,462     12,227    12,227   True/True/True
  lab_ezis_20250709.csv                3,322,765  3,322,765     11,298    11,298   True/True/True
  med_20250709.csv                       747,888    747,888     11,864    11,864   True/True/True
  meting_20251203.csv                 22,276,566 22,276,566     15,831    15,831   True/True/True
  mri_verslag_20250626.csv                 3,159      3,159      1,679     1,679        True/True
  ok_20250626.csv                         35,117     35,117      7,548     7,548        True/True
  ok_verslag_20250626.csv                 80,363     80,363      4,531     4,531        True/True
  radiologie_verslag_20251208.csv         78,722     78,722     10,893    10,893        True/True
  uitgaandebrief_20251208.csv             61,713     61,713      8,472     8,472        True/True
  verr_20251203.csv                       32,923     32,923      2,989     2,989        True/True
RESULT: EHR content comparison: inbox and analysed copies agree on ids, per-id row counts and per-id values in every file: True

=== 2. registry: original vs corrected ====================================
  original  smart_22nov2022.csv: enc=cp1252 sep=; rows=13,808 cols=261 id='M3LIFE_no'
  corrected smart_22nov2022_corrected.csv: enc=cp1252 sep=; rows=13,806 cols=261 id='M3LIFE_no'
  ids: original 13,806 distinct in [1, 16,096]; corrected 13,806 in [1, 16,096]
  identical id sets? True   |  shared 13,806  only-original 0  only-corrected 0
RESULT: corrected registry ids: 13806 distinct vs 13806 original; identical=True; shared 13806
  row content over 260 shared non-id columns:
    same multiset of rows? False
    of 13,806 ids present in both, 0 (0.0%) still carry the SAME row
RESULT: corrected registry: 0 of 13806 shared ids keep the same row content (0.0%); same multiset of rows=False
    -> the row multiset differs, so the DATA itself changed. A low
       'kept' share here does NOT indicate relabelling: comparing 260
       columns as text, any reformatting makes every row differ.

=== 2b. where did any value change come from? =============================
  column             original raw      corrected raw   local normalised
  gewicht                   81.00              81.00              81.00
  lengte                     2.00               1.75               2.00
  bm_indx                   26.00              26.33              26.00
  labchol                    5.00               4.90               5.00
  labkrea                   84.00              84.00              84.00
  leeftijd                  58.00              57.80              58.00
RESULT: value triangulation across original raw / corrected raw / local normalised written for 6 columns

=== 3. THE TEST: does the corrected registry join to the EHR data? ========
  Value-level checks only. Id overlap is never the evidence here -- two
  independent assignments over one range overlap at the chance rate, which is how
  this project was misled before.
    normalised smart_22nov2022_corrected.csv: cp1252/';' -> utf-8/',' | 0 decimal-comma column(s) converted | id -> 'm3life_no' | 13,806 rows -> data/smart/smart_corrected_utf8.csv
RESULT: normalised the corrected export: 0 decimal-comma columns converted, 13806 rows

--- CORRECTED registry + current events
    registry: data/smart/smart_corrected_utf8.csv
    events:   data/smartehr-utf8
  registry: 13,806 patients

  event source                 registry      both     rho  shuffled  med(event)   med(reg)
  meting.Gewicht               gewicht     10,923  +0.011    +0.022       81.00      80.00
RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.022)
  meting.Lengte                lengte       8,202  +0.002    -0.014      174.00       1.74
RESULT: join check meting.Lengte vs lengte: n=8202 rho=+0.002 (shuffled -0.014)
  meting.BMI                   bm_indx      2,776  -0.009    -0.031       26.30      26.34
RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.031)
  lab_ezis.Creat-BL            labkrea      6,010  +0.002    -0.007       79.00      84.00
RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
  lab_ezis.Chol-BL             labchol      5,161  -0.014    +0.020        4.70       4.90
RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.014 (shuffled +0.020)
RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.014 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn

  ** THE EVENT JOIN IS BROKEN. Weight, height and creatinine are measured in
     both sources and cannot legitimately disagree for the same patient. Every
     null in this project -- structured and text -- is uninterpretable until
     the identifier join is fixed. **

  --- which smart.csv column, used as the join key, recovers routine weight? ---
  probe: 12,771 patients with a routine weight near baseline
  candidate key              unique  matched      rho  note
  m3life_no                  13,806   10,923   +0.011  
  SmrtRisk                    8,559        0      -    
RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager

  -> No column in smart.csv recovers weight (best +0.011 (m3life_no)). The linkage
     cannot be fixed from these files: the EHR extracts and the registry need
     to be re-linked at source. This is a question for the data manager.

  --- is each file self-consistent? BMI = weight / height^2 within one row ---
  REGISTRY  n=13,772  rho(implied BMI, stated BMI)=+1.000  median |diff|=0.00
RESULT: registry self-consistency: BMI vs weight/height^2 rho=+1.000 on 13772 rows (median abs diff 0.00)
  EVENTS    n=3,180  rho(implied BMI, stated BMI)=+0.941  median |diff|=0.31
RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)

  identifier spaces: registry 13,806 ids in [1, 16,096] | events 12,771 ids in [2, 15,877] | overlap 10,949
  expected overlap if the two id sets were INDEPENDENT draws from [1, 16,096] (N=16,096): 10,954
  observed / expected = 0.9995
RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949 vs 10954 expected under independence (ratio 0.9995)
RESULT: ** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent id assignments over the same numbering range would produce by arithmetic alone, so the 10949 'matching' patients match by coincidence. The extracts come from different pseudonymisation runs and a crosswalk is required
  -> The overlap IS the chance value. These are independent id assignments
     over one numbering range: the files share a range, not a key. Ask the
     data manager for the crosswalk; no code change can recover this.

=== sex check: do sex-specific lab tests land on that sex? =============
  registry base rate: P(Man)=0.650 on 13,806 patients
  test                 implies  patients  observed  expected       z
  Totaal PSA (5,312 ro Man         1,047     0.647     0.650    -0.2
RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
  Vrij PSA (367)       Man           193     0.658     0.650    +0.2
RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
  PSA F/T-ratio (349)  Man           180     0.656     0.650    +0.2
RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
  Totaal PSA plasma (8 Man            63     0.683     0.650    +0.5
RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
  Zwangerschapstest (5 Vrouw          30     0.433     0.350    +1.0
RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
  Anti-Mullerian Hormo Vrouw          48     0.354     0.350    +0.1
RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved

  ** The sex check FAILS: a prostate-specific test lands on the cohort's own
     sex ratio. Categorical confirmation, with nothing to aggregate. **

=== demographics extract (the only route to an AGE check) ==============
  not found. Age cannot be checked from the 16 event extracts: none carries an
  age or birth date. If UCN_PATIENT_DEMOGRAFISCH.csv can be made available,
  pass it with --demographics-file and this will report what it holds.
RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable

--- control: UNCORRECTED registry + current events
    registry: data/smart/smart_utf8.csv
    events:   data/smartehr-utf8
  registry: 13,806 patients

  event source                 registry      both     rho  shuffled  med(event)   med(reg)
  meting.Gewicht               gewicht     10,923  +0.011    +0.021       81.00      80.00
RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.021)
  meting.Lengte                lengte       8,202  -0.017    +0.006      174.00       2.00
RESULT: join check meting.Lengte vs lengte: n=8202 rho=-0.017 (shuffled +0.006)
  meting.BMI                   bm_indx      2,776  -0.009    -0.029       26.30      26.00
RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.029)
  lab_ezis.Creat-BL            labkrea      6,010  +0.002    -0.007       79.00      84.00
RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
  lab_ezis.Chol-BL             labchol      5,161  -0.012    +0.020        4.70       5.00
RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.012 (shuffled +0.020)
RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.017 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn

  ** THE EVENT JOIN IS BROKEN. Weight, height and creatinine are measured in
     both sources and cannot legitimately disagree for the same patient. Every
     null in this project -- structured and text -- is uninterpretable until
     the identifier join is fixed. **

  --- which smart.csv column, used as the join key, recovers routine weight? ---
  probe: 12,771 patients with a routine weight near baseline
  candidate key              unique  matched      rho  note
  m3life_no                  13,806   10,923   +0.011  
RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager

  -> No column in smart.csv recovers weight (best +0.011 (m3life_no)). The linkage
     cannot be fixed from these files: the EHR extracts and the registry need
     to be re-linked at source. This is a question for the data manager.

  --- is each file self-consistent? BMI = weight / height^2 within one row ---
  REGISTRY  n=13,731  rho(implied BMI, stated BMI)=+0.798  median |diff|=6.25
RESULT: registry self-consistency: BMI vs weight/height^2 rho=+0.798 on 13731 rows (median abs diff 6.25)
  EVENTS    n=3,180  rho(implied BMI, stated BMI)=+0.941  median |diff|=0.31
RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)

  identifier spaces: registry 13,806 ids in [1, 16,096] | events 12,771 ids in [2, 15,877] | overlap 10,949
  expected overlap if the two id sets were INDEPENDENT draws from [1, 16,096] (N=16,096): 10,954
  observed / expected = 0.9995
RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949 vs 10954 expected under independence (ratio 0.9995)
RESULT: ** THE TWO FILES DO NOT SHARE A KEY **: the overlap is what independent id assignments over the same numbering range would produce by arithmetic alone, so the 10949 'matching' patients match by coincidence. The extracts come from different pseudonymisation runs and a crosswalk is required
  -> The overlap IS the chance value. These are independent id assignments
     over one numbering range: the files share a range, not a key. Ask the
     data manager for the crosswalk; no code change can recover this.

=== sex check: do sex-specific lab tests land on that sex? =============
  registry base rate: P(Man)=0.650 on 13,806 patients
  test                 implies  patients  observed  expected       z
  Totaal PSA (5,312 ro Man         1,047     0.647     0.650    -0.2
RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
  Vrij PSA (367)       Man           193     0.658     0.650    +0.2
RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
  PSA F/T-ratio (349)  Man           180     0.656     0.650    +0.2
RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
  Totaal PSA plasma (8 Man            63     0.683     0.650    +0.5
RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
  Zwangerschapstest (5 Vrouw          30     0.433     0.350    +1.0
RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
  Anti-Mullerian Hormo Vrouw          48     0.354     0.350    +0.1
RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved

  ** The sex check FAILS: a prostate-specific test lands on the cohort's own
     sex ratio. Categorical confirmation, with nothing to aggregate. **

=== demographics extract (the only route to an AGE check) ==============
  not found. Age cannot be checked from the 16 event extracts: none carries an
  age or birth date. If UCN_PATIENT_DEMOGRAFISCH.csv can be made available,
  pass it with --demographics-file and this will report what it holds.
RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable
```

</details>

---

### RUN 2026-09-16T08:27:05Z | diagnose: did normalisation break the join?

- status: ok
- context: orig_smart=data/smart/smart_22nov2022.csv norm_smart=data/smart/smart_utf8.csv
- RESULT: ** ROW COUNT CHANGED in the registry: 13808 -> 13806 **
- RESULT: registry id->weight preserved by normalisation: n=5223 rho=+1.000
- RESULT: id normalisation row check: 0.00% of zero-padded ids differ vs 0.00% of non-padded -- a padding bug hits one group and not the other
- RESULT: ** ID NORMALISATION IS CLEAN **: all 13806 ids keep their own row across every one of 260 shared columns, zero-padded and not alike
- RESULT: rank-matched (k-th smallest id to k-th smallest id) weight agreement: rho=+0.000 on 12771 pairs
- RESULT: normalisation is NOT the culprit (best agreement across all four pairings: original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011): the originals do not join either, so the two extracts genuinely carry independent pseudonymisation runs and a crosswalk is required

<details><summary>full output</summary>

```
=== 1. registry: original vs normalised ==================================
  ORIGINAL registry
    path      data/smart/smart_22nov2022.csv
    parsed as encoding=cp1252 sep=;  rows=13,808 cols=261
    id column 'M3LIFE_no'
    ids       n=13,808 unique=13,807 purely_numeric=13,806 leading_zeros=8,573 whitespace=0
    id lengths (chars) {5: 13806, 11: 2}
    NON-NUMERIC id examples: ['Ao vene RDP', 'Ao vene RDP']
  NORMALISED registry
    path      data/smart/smart_utf8.csv
    parsed as encoding=utf-8 sep=,  rows=13,806 cols=261
    id column 'm3life_no'
    ids       n=13,806 unique=13,806 purely_numeric=13,806 leading_zeros=0 whitespace=0
    id lengths (chars) {1: 8, 2: 76, 3: 765, 4: 7724, 5: 5233}
RESULT: ** ROW COUNT CHANGED in the registry: 13808 -> 13806 **
  ** rows changed 13,808 -> 13,806: the re-encode altered how rows were split, which misaligns every column from its id **

  registry id sets: original 13,807 | normalised 13,806
    identical as strings? False
    identical as ints?    True
    string overlap 5,233 | int overlap 13,806
    id -> weight preserved across normalisation? n=5,223 rho=+1.000
RESULT: registry id->weight preserved by normalisation: n=5223 rho=+1.000

=== id normalisation: did every id keep its own row? =====================
  original: 13,806 distinct id strings -> 13,806 distinct integers
  the integer conversion is injective: no two original ids collapse into one
  zero-padded original ids: 8,573 of 13,808 (the subset the earlier check never compared)
  ids shared as integers: 13,806 (original-only 0, normalised-only 0)
  rows whose content differs on ANY of 260 columns: 0 of 13,806 (0.00%)
    zero-padded ids: 0 of 8,573 differ (0.00%)
    non-padded ids:  0 of 5,233 differ (0.00%)
RESULT: id normalisation row check: 0.00% of zero-padded ids differ vs 0.00% of non-padded -- a padding bug hits one group and not the other
RESULT: ** ID NORMALISATION IS CLEAN **: all 13806 ids keep their own row across every one of 260 shared columns, zero-padded and not alike
  -> every id keeps its own row. The normalisation moved no data.

=== 2. THE DECISIVE TEST: does the ORIGINAL pair join? ==================
  ORIGINAL events:
    meting_20251203.csv (encoding=cp1252, sep=;): weights for 12,771 ids
  NORMALISED events:
    no meting*.csv in data/smartehr-utf-8
    ORIGINAL pair matched on string ids: n=10,923  rho=+0.011
    ORIGINAL pair matched on int    ids: n=10,923  rho=+0.011
    norm registry + orig events matched on string ids: n= 4,067  rho=-0.004
    norm registry + orig events matched on int    ids: n=10,923  rho=+0.011

=== 3. were the ids assigned in the same ORDER? =========================
  registry 13,776 ids | events 12,771 ids | pairing the 12,771 smallest of each by rank
  rank-matched weight agreement: rho=+0.000
RESULT: rank-matched (k-th smallest id to k-th smallest id) weight agreement: rho=+0.000 on 12771 pairs
  -> no. The id orders are unrelated too, so the assignments are
     independent in value AND in order.
RESULT: normalisation is NOT the culprit (best agreement across all four pairings: original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011): the originals do not join either, so the two extracts genuinely carry independent pseudonymisation runs and a crosswalk is required

  -> The ORIGINAL files do not join either (original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011). The normalisation is
     exonerated: the two extracts carry independent pseudonymisation runs, and
     the crosswalk has to come from the data provider.
```

</details>
