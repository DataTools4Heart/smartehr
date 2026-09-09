# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (3 runs)

- **2026-09-09T11:41:04Z | join check: events vs registry**
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
  - RESULT: whole-timeline meting.Gewicht vs gewicht: n=10923 readings=39249 rho(median)=+0.011 | best-case closest match median 13.00 vs 13.00 permuted
  - RESULT: whole-timeline meting.Lengte vs lengte: n=8202 readings=24179 rho(median)=-0.013 | best-case closest match median 171.00 vs 171.00 permuted
  - RESULT: whole-timeline meting.BMI vs bm_indx: n=2776 readings=4623 rho(median)=-0.007 | best-case closest match median 3.68 vs 3.64 permuted
  - RESULT: whole-timeline lab_ezis.Creat-BL vs labkrea: n=6010 readings=36778 rho(median)=+0.001 | best-case closest match median 11.00 vs 11.00 permuted
  - RESULT: whole-timeline lab_ezis.Chol-BL vs labchol: n=5161 readings=11461 rho(median)=-0.010 | best-case closest match median 0.90 vs 0.90 permuted
  - RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
  - RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
  - RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
  - RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
  - RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
  - RESULT: demographics extract not found: age is not checkable from the event files, which carry no age or birth date; UCN_PATIENT_DEMOGRAFISCH.csv is the only candidate and was not reachable
- **2026-09-09T11:44:15Z | join check: events vs registry**
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
  - RESULT: whole-timeline meting.Gewicht vs gewicht: n=10923 readings=39249 rho(median)=+0.011 | best-case closest match median 13.00 vs 13.00 permuted
  - RESULT: whole-timeline meting.Lengte vs lengte: n=8202 readings=24179 rho(median)=-0.013 | best-case closest match median 171.00 vs 171.00 permuted
  - RESULT: whole-timeline meting.BMI vs bm_indx: n=2776 readings=4623 rho(median)=-0.007 | best-case closest match median 3.68 vs 3.64 permuted
  - RESULT: whole-timeline lab_ezis.Creat-BL vs labkrea: n=6010 readings=36778 rho(median)=+0.001 | best-case closest match median 11.00 vs 11.00 permuted
  - RESULT: whole-timeline lab_ezis.Chol-BL vs labchol: n=5161 readings=11461 rho(median)=-0.010 | best-case closest match median 0.90 vs 0.90 permuted
  - RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
  - RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
  - RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
  - RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
  - RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
  - RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
  - RESULT: demographics extract UCN_PATIENT_DEMOGRAFISCH.csv: id=M3LIFE_no sex=Geslacht birth=Geboortejaar
  - RESULT: demographics sex agreement with registry: 1.000 on 658 patients (chance is ~0.55 at this cohort's sex ratio)
  - RESULT: demographics birth-year vs registry age: rho=-0.891 on 658 patients (negative is correct: older patients were born earlier)
- **2026-09-09T12:16:39Z | UCN crosswalk test**
  - RESULT: UCN inventory UCN_ALG_1000008241_UCORBIOFORM.csv: 205 cols, id=M3LIFE_no, 4287 sampled rows
  - RESULT: UCN inventory UCN_ALG_CS00005657_HEARTTEAM.csv: 102 cols, id=M3LIFE_no, 2212 sampled rows
  - RESULT: UCN inventory UCN_CAR_1000010899_XPERIM.csv: 201 cols, id=M3LIFE_no, 2818 sampled rows
  - RESULT: UCN UCN_CAR_1000011395_UCORBIOFU.csv: 16 of 6768 rows have a non-numeric id (malformed rows)
  - RESULT: UCN inventory UCN_CAR_1000011395_UCORBIOFU.csv: 119 cols, id=M3LIFE_no, 6768 sampled rows
  - RESULT: UCN UCN_ECG_DETAILS.csv: 21412 of 50000 rows have a non-numeric id (malformed rows)
  - RESULT: UCN inventory UCN_ECG_DETAILS.csv: 56 cols, id=QRS_Area_ECG, 50000 sampled rows
  - RESULT: UCN inventory UCN_ECG_TEST.csv: 34 cols, id=M3LIFE_no, 50000 sampled rows
  - RESULT: UCN inventory UCN_ECG_TEST_EXAMINATION.csv: 24 cols, id=ECG_TestID, 50000 sampled rows
  - RESULT: UCN inventory UCN_ECHO_FINDING.csv: 9 cols, id=M3LIFE_no, 50000 sampled rows
  - RESULT: UCN inventory UCN_ECHO_GROUP.csv: 7 cols, id=M3LIFE_no, 4489 sampled rows
  - RESULT: UCN inventory UCN_ECHO_MEASUREMENT.csv: 7 cols, id=M3LIFE_no, 50000 sampled rows
  - RESULT: UCN inventory UCN_ECHO_STUDY.csv: 4 cols, id=M3LIFE_no, 7960 sampled rows
  - RESULT: UCN inventory UCN_LAB_BEPALING_KLINCHEM.csv: 14 cols, id=M3LIFE_no, 50000 sampled rows
  - RESULT: UCN inventory UCN_OKVCAR_1000009333_CAGOK.csv: 136 cols, id=M3LIFE_no, 250 sampled rows
  - RESULT: UCN inventory UCN_OK_1000004189_OKNAZORG1.csv: 31 cols, id=M3LIFE_no, 1177 sampled rows
  - RESULT: UCN UCN_OK_1000007347_PCI_DETAILS.csv: 1 of 4016 rows have a non-numeric id (malformed rows)
  - RESULT: UCN inventory UCN_OK_1000007347_PCI_DETAILS.csv: 260 cols, id=M3LIFE_no, 4016 sampled rows
  - RESULT: UCN inventory UCN_OK_1000007347_PCI_DETAILS_R.csv: 19 cols, id=M3LIFE_no, 50000 sampled rows
  - RESULT: UCN inventory UCN_OK_1000007350_PCI_L_EN_P.csv: 142 cols, id=M3LIFE_no, 19481 sampled rows
  - RESULT: UCN inventory UCN_OK_1000007371_OKNAZORG2.csv: 16 cols, id=M3LIFE_no, 15 sampled rows
  - RESULT: UCN inventory UCN_OK_1000007373_OKNAZORG3.csv: 9 cols, id=M3LIFE_no, 643 sampled rows
  - RESULT: UCN inventory UCN_PATIENT_DEMOGRAFISCH.csv: 6 cols, id=M3LIFE_no, 2948 sampled rows
  - RESULT: UCN value check QRS_Duration_ECG vs ecg.QRS_Duration: n=2291 rho=-0.006 best-case 4.00 vs 4.00 permuted
  - RESULT: UCN value check Q_TInterval_ECG vs ecg.QT_Interval: n=2291 rho=+0.041 best-case 5.00 vs 4.00 permuted
  - RESULT: UCN value check POnset_ECG vs ecg.P_Onset: n=2241 rho=-0.022 best-case 6.00 vs 6.00 permuted
  - RESULT: UCN value check POffset_ECG vs ecg.P_Offset: n=2241 rho=-0.022 best-case 6.00 vs 6.00 permuted
  - RESULT: UCN value check T_Onset_ECG vs ecg.T_Onset: n=2291 rho=-0.006 best-case 3.00 vs 3.00 permuted
  - RESULT: UCN value check T_Offset_ECG vs ecg.T_Offset: n=2291 rho=+0.020 best-case 3.00 vs 3.00 permuted
  - RESULT: UCN value check QRS_Onset_ECG vs ecg.QRS_Onset: n=2291 rho=+0.010 best-case 2.00 vs 2.00 permuted
  - RESULT: UCN value check QRS_Offset_ECG vs ecg.QRS_Offset: n=2291 rho=+0.008 best-case 2.00 vs 2.00 permuted
  - RESULT: UCN demographics sex agreement with registry: 1.000 on 658 patients (chance 0.545)
  - RESULT: UCN demographics birth-year vs registry age: rho=-0.891 on 658 patients (negative is correct)
  - RESULT: ** UCN SHARES THE REGISTRY ID SPACE ** (sex 1.000 vs chance 0.545, birth-year vs age rho -0.891; EHR 0.041): UCN's own clinical content -- echo, ECG, heart-team, biobank -- is therefore usable against the registry, so the research question is answerable from UCN data even without repairing the EHR link

---

### RUN 2026-09-09T11:41:04Z | join check: events vs registry

- status: ok
- context: landmark=180 probe_keys=False
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
- RESULT: whole-timeline meting.Gewicht vs gewicht: n=10923 readings=39249 rho(median)=+0.011 | best-case closest match median 13.00 vs 13.00 permuted
- RESULT: whole-timeline meting.Lengte vs lengte: n=8202 readings=24179 rho(median)=-0.013 | best-case closest match median 171.00 vs 171.00 permuted
- RESULT: whole-timeline meting.BMI vs bm_indx: n=2776 readings=4623 rho(median)=-0.007 | best-case closest match median 3.68 vs 3.64 permuted
- RESULT: whole-timeline lab_ezis.Creat-BL vs labkrea: n=6010 readings=36778 rho(median)=+0.001 | best-case closest match median 11.00 vs 11.00 permuted
- RESULT: whole-timeline lab_ezis.Chol-BL vs labchol: n=5161 readings=11461 rho(median)=-0.010 | best-case closest match median 0.90 vs 0.90 permuted
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

=== whole-timeline check: every reading, not just the nearest ===========

  meting.Gewicht vs gewicht  (10,923 patients)
    readings per patient: median 2, p90 7, max 127, total 39,249
    value range p1/p50/p99: 47.4 / 81.0 / 126.1
    rho(first reading ) = +0.014
    rho(median of all ) = +0.011
    BEST CASE |closest reading - registry|: median 13.00, under permutation 13.00
RESULT: whole-timeline meting.Gewicht vs gewicht: n=10923 readings=39249 rho(median)=+0.011 | best-case closest match median 13.00 vs 13.00 permuted

  meting.Lengte vs lengte  (8,202 patients)
    readings per patient: median 2, p90 6, max 50, total 24,179
    value range p1/p50/p99: 0.0 / 175.0 / 196.0
    rho(first reading ) = -0.009
    rho(median of all ) = -0.013
    BEST CASE |closest reading - registry|: median 171.00, under permutation 171.00
RESULT: whole-timeline meting.Lengte vs lengte: n=8202 readings=24179 rho(median)=-0.013 | best-case closest match median 171.00 vs 171.00 permuted

  meting.BMI vs bm_indx  (2,776 patients)
    readings per patient: median 1, p90 3, max 20, total 4,623
    value range p1/p50/p99: 18.2 / 26.1 / 44.0
    rho(first reading ) = -0.009
    rho(median of all ) = -0.007
    BEST CASE |closest reading - registry|: median 3.68, under permutation 3.64
RESULT: whole-timeline meting.BMI vs bm_indx: n=2776 readings=4623 rho(median)=-0.007 | best-case closest match median 3.68 vs 3.64 permuted

  lab_ezis.Creat-BL vs labkrea  (6,010 patients)
    readings per patient: median 3, p90 13, max 270, total 36,778
    value range p1/p50/p99: 43.0 / 84.0 / 655.0
    rho(first reading ) = +0.001
    rho(median of all ) = +0.001
    BEST CASE |closest reading - registry|: median 11.00, under permutation 11.00
RESULT: whole-timeline lab_ezis.Creat-BL vs labkrea: n=6010 readings=36778 rho(median)=+0.001 | best-case closest match median 11.00 vs 11.00 permuted

  lab_ezis.Chol-BL vs labchol  (5,161 patients)
    readings per patient: median 2, p90 4, max 31, total 11,461
    value range p1/p50/p99: 2.5 / 4.7 / 8.8
    rho(first reading ) = -0.018
    rho(median of all ) = -0.010
    BEST CASE |closest reading - registry|: median 0.90, under permutation 0.90
RESULT: whole-timeline lab_ezis.Chol-BL vs labchol: n=5161 readings=11461 rho(median)=-0.010 | best-case closest match median 0.90 vs 0.90 permuted

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

### RUN 2026-09-09T11:44:15Z | join check: events vs registry

- status: ok
- context: landmark=180 probe_keys=False
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
- RESULT: whole-timeline meting.Gewicht vs gewicht: n=10923 readings=39249 rho(median)=+0.011 | best-case closest match median 13.00 vs 13.00 permuted
- RESULT: whole-timeline meting.Lengte vs lengte: n=8202 readings=24179 rho(median)=-0.013 | best-case closest match median 171.00 vs 171.00 permuted
- RESULT: whole-timeline meting.BMI vs bm_indx: n=2776 readings=4623 rho(median)=-0.007 | best-case closest match median 3.68 vs 3.64 permuted
- RESULT: whole-timeline lab_ezis.Creat-BL vs labkrea: n=6010 readings=36778 rho(median)=+0.001 | best-case closest match median 11.00 vs 11.00 permuted
- RESULT: whole-timeline lab_ezis.Chol-BL vs labchol: n=5161 readings=11461 rho(median)=-0.010 | best-case closest match median 0.90 vs 0.90 permuted
- RESULT: sex check psatot-bl (implies Man): 1047 patients, observed 0.647 vs base rate 0.650 (z=-0.2)
- RESULT: sex check psavrij-bl (implies Man): 193 patients, observed 0.658 vs base rate 0.650 (z=+0.2)
- RESULT: sex check psaratio-bl (implies Man): 180 patients, observed 0.656 vs base rate 0.650 (z=+0.2)
- RESULT: sex check psatot_plasma-bl (implies Man): 63 patients, observed 0.683 vs base rate 0.650 (z=+0.5)
- RESULT: sex check zwanger-up (implies Vrouw): 30 patients, observed 0.433 vs base rate 0.350 (z=+1.0)
- RESULT: sex check amh-bl (implies Vrouw): 48 patients, observed 0.354 vs base rate 0.350 (z=+0.1)
- RESULT: ** SEX CHECK FAILS **: only 64.7% of 1047 patients given psatot-bl are recorded Man, against a base rate of 65.0% (z=-0.2) -- a prostate-specific test lands on the cohort's sex ratio, which is what an arbitrary sample of patients gives. Categorical confirmation of the broken join, with no units, no aggregation and no outliers involved
- RESULT: demographics extract UCN_PATIENT_DEMOGRAFISCH.csv: id=M3LIFE_no sex=Geslacht birth=Geboortejaar
- RESULT: demographics sex agreement with registry: 1.000 on 658 patients (chance is ~0.55 at this cohort's sex ratio)
- RESULT: demographics birth-year vs registry age: rho=-0.891 on 658 patients (negative is correct: older patients were born earlier)

<details><summary>full output</summary>

```
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

=== whole-timeline check: every reading, not just the nearest ===========

  meting.Gewicht vs gewicht  (10,923 patients)
    readings per patient: median 2, p90 7, max 127, total 39,249
    value range p1/p50/p99: 47.4 / 81.0 / 126.1
    rho(first reading ) = +0.014
    rho(median of all ) = +0.011
    BEST CASE |closest reading - registry|: median 13.00, under permutation 13.00
RESULT: whole-timeline meting.Gewicht vs gewicht: n=10923 readings=39249 rho(median)=+0.011 | best-case closest match median 13.00 vs 13.00 permuted

  meting.Lengte vs lengte  (8,202 patients)
    readings per patient: median 2, p90 6, max 50, total 24,179
    value range p1/p50/p99: 0.0 / 175.0 / 196.0
    rho(first reading ) = -0.009
    rho(median of all ) = -0.013
    BEST CASE |closest reading - registry|: median 171.00, under permutation 171.00
RESULT: whole-timeline meting.Lengte vs lengte: n=8202 readings=24179 rho(median)=-0.013 | best-case closest match median 171.00 vs 171.00 permuted

  meting.BMI vs bm_indx  (2,776 patients)
    readings per patient: median 1, p90 3, max 20, total 4,623
    value range p1/p50/p99: 18.2 / 26.1 / 44.0
    rho(first reading ) = -0.009
    rho(median of all ) = -0.007
    BEST CASE |closest reading - registry|: median 3.68, under permutation 3.64
RESULT: whole-timeline meting.BMI vs bm_indx: n=2776 readings=4623 rho(median)=-0.007 | best-case closest match median 3.68 vs 3.64 permuted

  lab_ezis.Creat-BL vs labkrea  (6,010 patients)
    readings per patient: median 3, p90 13, max 270, total 36,778
    value range p1/p50/p99: 43.0 / 84.0 / 655.0
    rho(first reading ) = +0.001
    rho(median of all ) = +0.001
    BEST CASE |closest reading - registry|: median 11.00, under permutation 11.00
RESULT: whole-timeline lab_ezis.Creat-BL vs labkrea: n=6010 readings=36778 rho(median)=+0.001 | best-case closest match median 11.00 vs 11.00 permuted

  lab_ezis.Chol-BL vs labchol  (5,161 patients)
    readings per patient: median 2, p90 4, max 31, total 11,461
    value range p1/p50/p99: 2.5 / 4.7 / 8.8
    rho(first reading ) = -0.018
    rho(median of all ) = -0.010
    BEST CASE |closest reading - registry|: median 0.90, under permutation 0.90
RESULT: whole-timeline lab_ezis.Chol-BL vs labchol: n=5161 readings=11461 rho(median)=-0.010 | best-case closest match median 0.90 vs 0.90 permuted

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
  UCN_PATIENT_DEMOGRAFISCH.csv: encoding=utf-8 sep=; rows(sampled)=2,948 cols=6
  columns: ['M3LIFE_no', 'Land', 'Geslacht', 'Geboortejaar', 'Overleden', 'Overledenjaar']
  detected: id='M3LIFE_no' sex='Geslacht' birth-year-like='Geboortejaar'
RESULT: demographics extract UCN_PATIENT_DEMOGRAFISCH.csv: id=M3LIFE_no sex=Geslacht birth=Geboortejaar
  sex agreement with the registry: 1.000 on 658 patients
RESULT: demographics sex agreement with registry: 1.000 on 658 patients (chance is ~0.55 at this cohort's sex ratio)
  birth-year vs registry age: rho=-0.891 on 658 patients (a working join gives a strong NEGATIVE rho)
RESULT: demographics birth-year vs registry age: rho=-0.891 on 658 patients (negative is correct: older patients were born earlier)
```

</details>

---

### RUN 2026-09-09T12:16:39Z | UCN crosswalk test

- status: ok
- context: ucn_folder=/home/lorenzo.pratesi@mydre.org/workspace/smartehr/data/ucn/
- RESULT: UCN inventory UCN_ALG_1000008241_UCORBIOFORM.csv: 205 cols, id=M3LIFE_no, 4287 sampled rows
- RESULT: UCN inventory UCN_ALG_CS00005657_HEARTTEAM.csv: 102 cols, id=M3LIFE_no, 2212 sampled rows
- RESULT: UCN inventory UCN_CAR_1000010899_XPERIM.csv: 201 cols, id=M3LIFE_no, 2818 sampled rows
- RESULT: UCN UCN_CAR_1000011395_UCORBIOFU.csv: 16 of 6768 rows have a non-numeric id (malformed rows)
- RESULT: UCN inventory UCN_CAR_1000011395_UCORBIOFU.csv: 119 cols, id=M3LIFE_no, 6768 sampled rows
- RESULT: UCN UCN_ECG_DETAILS.csv: 21412 of 50000 rows have a non-numeric id (malformed rows)
- RESULT: UCN inventory UCN_ECG_DETAILS.csv: 56 cols, id=QRS_Area_ECG, 50000 sampled rows
- RESULT: UCN inventory UCN_ECG_TEST.csv: 34 cols, id=M3LIFE_no, 50000 sampled rows
- RESULT: UCN inventory UCN_ECG_TEST_EXAMINATION.csv: 24 cols, id=ECG_TestID, 50000 sampled rows
- RESULT: UCN inventory UCN_ECHO_FINDING.csv: 9 cols, id=M3LIFE_no, 50000 sampled rows
- RESULT: UCN inventory UCN_ECHO_GROUP.csv: 7 cols, id=M3LIFE_no, 4489 sampled rows
- RESULT: UCN inventory UCN_ECHO_MEASUREMENT.csv: 7 cols, id=M3LIFE_no, 50000 sampled rows
- RESULT: UCN inventory UCN_ECHO_STUDY.csv: 4 cols, id=M3LIFE_no, 7960 sampled rows
- RESULT: UCN inventory UCN_LAB_BEPALING_KLINCHEM.csv: 14 cols, id=M3LIFE_no, 50000 sampled rows
- RESULT: UCN inventory UCN_OKVCAR_1000009333_CAGOK.csv: 136 cols, id=M3LIFE_no, 250 sampled rows
- RESULT: UCN inventory UCN_OK_1000004189_OKNAZORG1.csv: 31 cols, id=M3LIFE_no, 1177 sampled rows
- RESULT: UCN UCN_OK_1000007347_PCI_DETAILS.csv: 1 of 4016 rows have a non-numeric id (malformed rows)
- RESULT: UCN inventory UCN_OK_1000007347_PCI_DETAILS.csv: 260 cols, id=M3LIFE_no, 4016 sampled rows
- RESULT: UCN inventory UCN_OK_1000007347_PCI_DETAILS_R.csv: 19 cols, id=M3LIFE_no, 50000 sampled rows
- RESULT: UCN inventory UCN_OK_1000007350_PCI_L_EN_P.csv: 142 cols, id=M3LIFE_no, 19481 sampled rows
- RESULT: UCN inventory UCN_OK_1000007371_OKNAZORG2.csv: 16 cols, id=M3LIFE_no, 15 sampled rows
- RESULT: UCN inventory UCN_OK_1000007373_OKNAZORG3.csv: 9 cols, id=M3LIFE_no, 643 sampled rows
- RESULT: UCN inventory UCN_PATIENT_DEMOGRAFISCH.csv: 6 cols, id=M3LIFE_no, 2948 sampled rows
- RESULT: UCN value check QRS_Duration_ECG vs ecg.QRS_Duration: n=2291 rho=-0.006 best-case 4.00 vs 4.00 permuted
- RESULT: UCN value check Q_TInterval_ECG vs ecg.QT_Interval: n=2291 rho=+0.041 best-case 5.00 vs 4.00 permuted
- RESULT: UCN value check POnset_ECG vs ecg.P_Onset: n=2241 rho=-0.022 best-case 6.00 vs 6.00 permuted
- RESULT: UCN value check POffset_ECG vs ecg.P_Offset: n=2241 rho=-0.022 best-case 6.00 vs 6.00 permuted
- RESULT: UCN value check T_Onset_ECG vs ecg.T_Onset: n=2291 rho=-0.006 best-case 3.00 vs 3.00 permuted
- RESULT: UCN value check T_Offset_ECG vs ecg.T_Offset: n=2291 rho=+0.020 best-case 3.00 vs 3.00 permuted
- RESULT: UCN value check QRS_Onset_ECG vs ecg.QRS_Onset: n=2291 rho=+0.010 best-case 2.00 vs 2.00 permuted
- RESULT: UCN value check QRS_Offset_ECG vs ecg.QRS_Offset: n=2291 rho=+0.008 best-case 2.00 vs 2.00 permuted
- RESULT: UCN demographics sex agreement with registry: 1.000 on 658 patients (chance 0.545)
- RESULT: UCN demographics birth-year vs registry age: rho=-0.891 on 658 patients (negative is correct)
- RESULT: ** UCN SHARES THE REGISTRY ID SPACE ** (sex 1.000 vs chance 0.545, birth-year vs age rho -0.891; EHR 0.041): UCN's own clinical content -- echo, ECG, heart-team, biobank -- is therefore usable against the registry, so the research question is answerable from UCN data even without repairing the EHR link

<details><summary>full output</summary>

```
=== 1. inventory of 20 files in /home/lorenzo.pratesi@mydre.org/workspace/smartehr/data/ucn/ ====================
  UCN_ALG_1000008241_UCORBIOFORM.csv
    encoding=cp1252 sep=';' rows(sampled)=4,287 cols=205
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00002', 'v00014', 'v00015', 'v00017', 'v00021', 'v00022', 'v00024', 'v00026', 'v00027', 'v00028', 'v00031', 'v00033', 'v00035', 'v00037', 'v00038', 'v00040', 'v00041'] ... (+185 more)
    detected id column: 'M3LIFE_no' (2,708 distinct)
RESULT: UCN inventory UCN_ALG_1000008241_UCORBIOFORM.csv: 205 cols, id=M3LIFE_no, 4287 sampled rows
  UCN_ALG_CS00005657_HEARTTEAM.csv
    encoding=cp1252 sep=';' rows(sampled)=2,212 cols=102
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00003', 'v00004', 'v00009', 'v00013', 'v00014', 'v00015', 'v00017', 'v00018', 'v00019', 'v00020', 'v00021', 'v00022', 'v00023', 'v00024', 'v00025', 'v00026', 'v00027'] ... (+82 more)
    detected id column: 'M3LIFE_no' (1,610 distinct)
RESULT: UCN inventory UCN_ALG_CS00005657_HEARTTEAM.csv: 102 cols, id=M3LIFE_no, 2212 sampled rows
  UCN_CAR_1000010899_XPERIM.csv
    encoding=cp1252 sep=';' rows(sampled)=2,818 cols=201
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00004', 'v00005', 'v00006', 'v00007', 'v00008', 'v00009', 'v00010', 'v00011', 'v00012', 'v00016', 'v00017', 'v00018', 'v00019', 'v00020', 'v00021', 'v00022', 'v00023'] ... (+181 more)
    detected id column: 'M3LIFE_no' (869 distinct)
RESULT: UCN inventory UCN_CAR_1000010899_XPERIM.csv: 201 cols, id=M3LIFE_no, 2818 sampled rows
  UCN_CAR_1000011395_UCORBIOFU.csv
    encoding=cp1252 sep=';' rows(sampled)=6,768 cols=119
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00007', 'v00008', 'v00009', 'v00010', 'v00013', 'v00015', 'v00018', 'v00020', 'v00023', 'v00025', 'v00026', 'v00027', 'v00028', 'v00029', 'v00030', 'v00031', 'v00032', 'v00033'] ... (+99 more)
    detected id column: 'M3LIFE_no' (2,505 distinct)
    UCN_CAR_1000011395_UCORBIOFU.csv: note 16 of 6,768 rows have a non-numeric id (fragment rows from embedded newlines); examples ['']
RESULT: UCN UCN_CAR_1000011395_UCORBIOFU.csv: 16 of 6768 rows have a non-numeric id (malformed rows)
RESULT: UCN inventory UCN_CAR_1000011395_UCORBIOFU.csv: 119 cols, id=M3LIFE_no, 6768 sampled rows
  UCN_ECG_DETAILS.csv
    encoding=utf-8 sep=';' rows(sampled)=50,000 cols=56
    columns: ['ECG_TestID', 'LeadIDText_ECG', 'ECG_LeadID', 'P_OnsetAmpl_ECG', 'P_PeakAmpl_ECG', 'P_Duration_ECG', 'P_Area_ECG', 'P_PeakTime_ECG', 'PP_PeakAmpl_ECG', 'PP_Duration_ECG', 'PP_Area_ECG', 'PP_PeakTime_ECG', 'Q_PeakAmpl_ECG', 'Q_Duration_ECG', 'Q_Area_ECG', 'Q_PeakTime_ECG', 'R_PeakAmpl_ECG', 'R_Duration_ECG', 'R_Area_ECG', 'R_PeakTime_ECG'] ... (+36 more)
    detected id column: 'QRS_Area_ECG' (10,010 distinct)
    UCN_ECG_DETAILS.csv: WARNING 21,412 of 50,000 rows have a non-numeric id (fragment rows from embedded newlines); examples ['-5277', '-5505', '-2137']
RESULT: UCN UCN_ECG_DETAILS.csv: 21412 of 50000 rows have a non-numeric id (malformed rows)
RESULT: UCN inventory UCN_ECG_DETAILS.csv: 56 cols, id=QRS_Area_ECG, 50000 sampled rows
  UCN_ECG_TEST.csv
    encoding=cp1252 sep=';' rows(sampled)=50,000 cols=34
    columns: ['M3LIFE_no', 'ECG_TestID', 'TestTypeCode_ECG', 'TestTypeOmschrijving_ECG', 'TestStatus_ECG', 'TestReason_ECG', 'SystolicBP_ECG', 'DiastolicBP_ECG', 'VentricularRate_ECG', 'AtrialRate_ECG', 'P_RInterval_ECG', 'QRS_Duration_ECG', 'Q_TInterval_ECG', 'QTCCalculation_ECG', 'PAxis_ECG', 'RAxis_ECG', 'TAxis_ECG', 'QRSCount_ECG', 'QOnset_ECG', 'QOffset_ECG'] ... (+14 more)
    detected id column: 'M3LIFE_no' (1,995 distinct)
RESULT: UCN inventory UCN_ECG_TEST.csv: 34 cols, id=M3LIFE_no, 50000 sampled rows
  UCN_ECG_TEST_EXAMINATION.csv
    encoding=cp1252 sep=';' rows(sampled)=50,000 cols=24
    columns: ['ECG_TestID', 'NthOccur_ECG', 'UserEntered_ECG', 'StatementText_ECG', 'Acronym_ECG', 'FullText_ECG', 'InjuryClass_ECG', 'StatementsInjuryDegree_ECG', 'ECG_DiagnosisOrderID', 'DiagnosisOrderName_ECG', 'GroupName_ECG', 'EnumString_ECG', 'InjClsRepolarization_ECG', 'InjClsConduction_ECG', 'InjClsInfarction_ECG', 'InjClsHypertrophy_ECG', 'InjClsRhythm_ECG', 'InjClsWallMotion_ECG', 'InjClsValve_ECG', 'InjClsMass_ECG'] ... (+4 more)
    detected id column: 'ECG_TestID' (43,881 distinct)
RESULT: UCN inventory UCN_ECG_TEST_EXAMINATION.csv: 24 cols, id=ECG_TestID, 50000 sampled rows
  UCN_ECHO_FINDING.csv
    encoding=cp1252 sep=';' rows(sampled)=50,000 cols=9
    columns: ['M3LIFE_no', 'ECHO_StudyID', 'ReportVersion_ECHO', 'GroupCode_ECHO', 'FindingCode_ECHO', 'FindingCodeText_ECHO', 'MenuText_ECHO', 'QualifierIDk_ECHO', 'AuxiliaryText_ECHO']
    detected id column: 'M3LIFE_no' (1,480 distinct)
RESULT: UCN inventory UCN_ECHO_FINDING.csv: 9 cols, id=M3LIFE_no, 50000 sampled rows
  UCN_ECHO_GROUP.csv
    encoding=cp1252 sep=';' rows(sampled)=4,489 cols=7
    columns: ['M3LIFE_no', 'ECHO_StudyID', 'ReportVersion_ECHO', 'GroupCode_ECHO', 'GroupDescription_ECHO', 'ReportHeading_ECHO', 'Comment_ECHO']
    detected id column: 'M3LIFE_no' (1,080 distinct)
RESULT: UCN inventory UCN_ECHO_GROUP.csv: 7 cols, id=M3LIFE_no, 4489 sampled rows
  UCN_ECHO_MEASUREMENT.csv
    encoding=utf-8 sep=';' rows(sampled)=50,000 cols=7
    columns: ['M3LIFE_no', 'ECHO_StudyID', 'ReportVersion_ECHO', 'MeasName_ECHO', 'MeasAbstractNumber_ECHO', 'Value_ECHO', 'UnitName_ECHO']
    detected id column: 'M3LIFE_no' (283 distinct)
RESULT: UCN inventory UCN_ECHO_MEASUREMENT.csv: 7 cols, id=M3LIFE_no, 50000 sampled rows
  UCN_ECHO_STUDY.csv
    encoding=cp1252 sep=';' rows(sampled)=7,960 cols=4
    columns: ['M3LIFE_no', 'ECHO_StudyID', 'ReportVersion_ECHO', 'Conclusions_ECHO']
    detected id column: 'M3LIFE_no' (1,860 distinct)
RESULT: UCN inventory UCN_ECHO_STUDY.csv: 4 cols, id=M3LIFE_no, 7960 sampled rows
  UCN_LAB_BEPALING_KLINCHEM.csv
    encoding=cp1252 sep=';' rows(sampled)=50,000 cols=14
    columns: ['M3LIFE_no', 'Broncode_LAB', 'LabgroepNaam_LAB', 'LabgroepCode_LAB', 'Bepaling_LAB', 'BepalingOmschrijving_LAB', 'BepalingMateriaal_LAB', 'UitslagWaarde_LAB', 'UitslagEenheid_LAB', 'UitslagGrenswaardeOnder_LAB', 'UitslagGrenswaardeBoven_LAB', 'UitslagGrenswaardeVlag_LAB', 'UitslagStatus_LAB', 'afname_datediff']
    detected id column: 'M3LIFE_no' (86 distinct)
RESULT: UCN inventory UCN_LAB_BEPALING_KLINCHEM.csv: 14 cols, id=M3LIFE_no, 50000 sampled rows
  UCN_OKVCAR_1000009333_CAGOK.csv
    encoding=cp1252 sep=';' rows(sampled)=250 cols=136
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00018', 'v00019', 'v00020', 'v00021', 'v00022', 'v00023', 'v00024', 'v00025', 'v00029', 'v00030', 'v00031', 'v00033', 'v00034', 'v00035', 'v00036', 'v00037', 'v00038', 'v00039'] ... (+116 more)
    detected id column: 'M3LIFE_no' (96 distinct)
RESULT: UCN inventory UCN_OKVCAR_1000009333_CAGOK.csv: 136 cols, id=M3LIFE_no, 250 sampled rows
  UCN_OK_1000004189_OKNAZORG1.csv
    encoding=cp1252 sep=';' rows(sampled)=1,177 cols=31
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00002', 'v00003', 'v00004', 'v00005', 'v00006', 'v00007', 'v00008', 'v00009', 'v00010', 'v00011', 'v00012', 'v00013', 'v00014', 'v00015', 'v00016', 'v00017', 'v00018'] ... (+11 more)
    detected id column: 'M3LIFE_no' (720 distinct)
RESULT: UCN inventory UCN_OK_1000004189_OKNAZORG1.csv: 31 cols, id=M3LIFE_no, 1177 sampled rows
  UCN_OK_1000007347_PCI_DETAILS.csv
    encoding=cp1252 sep=';' rows(sampled)=4,016 cols=260
    columns: ['M3LIFE_no', 'groept', 'obs', 'v00001', 'v00004', 'v00005', 'v00006', 'v00007', 'v00008', 'v00010', 'v00012', 'v00013', 'v00014', 'v00015', 'v00016', 'v00017', 'v00018', 'v00019', 'v00022', 'v00024'] ... (+240 more)
    detected id column: 'M3LIFE_no' (2,020 distinct)
    UCN_OK_1000007347_PCI_DETAILS.csv: note 1 of 4,016 rows have a non-numeric id (fragment rows from embedded newlines); examples ['']
RESULT: UCN UCN_OK_1000007347_PCI_DETAILS.csv: 1 of 4016 rows have a non-numeric id (malformed rows)
RESULT: UCN inventory UCN_OK_1000007347_PCI_DETAILS.csv: 260 cols, id=M3LIFE_no, 4016 sampled rows
  UCN_OK_1000007347_PCI_DETAILS_R.csv
    encoding=utf-8 sep=';' rows(sampled)=50,000 cols=19
    columns: ['M3LIFE_no', 'Groep', 'Teller', 'Stelling', 'Antwoord', 'XAntwoord', 'XScore', 'Xext_code', 'Status', 'SublijstID', 'HoofdLijstID', 'Lijsten', 'VraagID', 'VraagType', 'OnzzAntw', 'L_Inactief', 'V_Inactief', 'Vervallen', 'Hierarchy']
    detected id column: 'M3LIFE_no' (98 distinct)
RESULT: UCN inventory UCN_OK_1000007347_PCI_DETAILS_R.csv: 19 cols, id=M3LIFE_no, 50000 sampled rows
  UCN_OK_1000007350_PCI_L_EN_P.csv
    encoding=cp1252 sep=';' rows(sampled)=19,481 cols=142
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00002', 'v00003', 'v00004', 'v00005', 'v00006', 'v00007', 'v00008', 'v00009', 'v00010', 'v00011', 'v00012', 'v00013', 'v00014', 'v00015', 'v00016', 'v00103', 'v00104'] ... (+122 more)
    detected id column: 'M3LIFE_no' (2,033 distinct)
RESULT: UCN inventory UCN_OK_1000007350_PCI_L_EN_P.csv: 142 cols, id=M3LIFE_no, 19481 sampled rows
  UCN_OK_1000007371_OKNAZORG2.csv
    encoding=utf-8 sep=';' rows(sampled)=15 cols=16
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00002', 'v00003', 'v00004', 'v00005', 'v00006', 'v00007', 'v00008', 'v00009', 'v00010', 'v00011', 'v00012', 'v00013', 'DEFINITIEF']
    detected id column: 'M3LIFE_no' (15 distinct)
RESULT: UCN inventory UCN_OK_1000007371_OKNAZORG2.csv: 16 cols, id=M3LIFE_no, 15 sampled rows
  UCN_OK_1000007373_OKNAZORG3.csv
    encoding=cp1252 sep=';' rows(sampled)=643 cols=9
    columns: ['M3LIFE_no', 'GROEP_nr', 'v00001', 'v00002', 'v00003', 'v00004', 'v00005', 'v00006', 'DEFINITIEF']
    detected id column: 'M3LIFE_no' (453 distinct)
RESULT: UCN inventory UCN_OK_1000007373_OKNAZORG3.csv: 9 cols, id=M3LIFE_no, 643 sampled rows
  UCN_PATIENT_DEMOGRAFISCH.csv
    encoding=utf-8 sep=';' rows(sampled)=2,948 cols=6
    columns: ['M3LIFE_no', 'Land', 'Geslacht', 'Geboortejaar', 'Overleden', 'Overledenjaar']
    detected id column: 'M3LIFE_no' (2,948 distinct)
RESULT: UCN inventory UCN_PATIENT_DEMOGRAFISCH.csv: 6 cols, id=M3LIFE_no, 2948 sampled rows

=== 2. id-space overlap (reported, NOT evidence) ==========================
  Two independent assignments over one range overlap at the chance rate, which is
  exactly how this project was misled before. Value tests below are the evidence.
  UCN_ALG_1000008241_UCORBIOFORM.csv (id=M3LIFE_no)
    vs registry: 2,708 vs 13,806 ids, overlap 640; chance would give 2,323 (ratio 0.276)
    vs EHR ecg: 2,708 vs 15,390 ids, overlap 2,589; chance would give 2,591 (ratio 0.999)
  UCN_ALG_CS00005657_HEARTTEAM.csv (id=M3LIFE_no)
    vs registry: 1,610 vs 13,806 ids, overlap 400; chance would give 1,381 (ratio 0.290)
    vs EHR ecg: 1,610 vs 15,390 ids, overlap 1,535; chance would give 1,541 (ratio 0.996)
  UCN_CAR_1000010899_XPERIM.csv (id=M3LIFE_no)
    vs registry: 869 vs 13,806 ids, overlap 246; chance would give 745 (ratio 0.330)
    vs EHR ecg: 869 vs 15,390 ids, overlap 835; chance would give 832 (ratio 1.004)
  UCN_CAR_1000011395_UCORBIOFU.csv (id=M3LIFE_no)
    vs registry: 2,505 vs 13,806 ids, overlap 609; chance would give 2,149 (ratio 0.283)
    vs EHR ecg: 2,505 vs 15,390 ids, overlap 2,394; chance would give 2,397 (ratio 0.999)
  UCN_ECG_DETAILS.csv (id=QRS_Area_ECG)
    vs registry: 21,413 vs 13,806 ids, overlap 7,266; chance would give 4,511 (ratio 1.611)
    vs EHR ecg: 21,413 vs 15,390 ids, overlap 8,230; chance would give 5,029 (ratio 1.637)
  UCN_ECG_TEST.csv (id=M3LIFE_no)
    vs registry: 2,402 vs 13,806 ids, overlap 640; chance would give 2,060 (ratio 0.311)
    vs EHR ecg: 2,402 vs 15,390 ids, overlap 2,292; chance would give 2,299 (ratio 0.997)
  UCN_ECG_TEST_EXAMINATION.csv (id=ECG_TestID)
    vs registry: 58,817 vs 13,806 ids, overlap 239; chance would give 573 (ratio 0.417)
    vs EHR ecg: 58,817 vs 15,390 ids, overlap 260; chance would give 639 (ratio 0.407)
  UCN_ECHO_FINDING.csv (id=M3LIFE_no)
    vs registry: 1,679 vs 13,806 ids, overlap 433; chance would give 1,440 (ratio 0.301)
    vs EHR ecg: 1,679 vs 15,390 ids, overlap 1,599; chance would give 1,607 (ratio 0.995)
  UCN_ECHO_GROUP.csv (id=M3LIFE_no)
    vs registry: 1,080 vs 13,806 ids, overlap 274; chance would give 926 (ratio 0.296)
    vs EHR ecg: 1,080 vs 15,390 ids, overlap 1,029; chance would give 1,034 (ratio 0.996)
  UCN_ECHO_MEASUREMENT.csv (id=M3LIFE_no)
    vs registry: 1,735 vs 13,806 ids, overlap 438; chance would give 1,488 (ratio 0.294)
    vs EHR ecg: 1,735 vs 15,390 ids, overlap 1,651; chance would give 1,660 (ratio 0.994)
  UCN_ECHO_STUDY.csv (id=M3LIFE_no)
    vs registry: 1,860 vs 13,806 ids, overlap 464; chance would give 1,595 (ratio 0.291)
    vs EHR ecg: 1,860 vs 15,390 ids, overlap 1,774; chance would give 1,780 (ratio 0.997)
  UCN_LAB_BEPALING_KLINCHEM.csv (id=M3LIFE_no)
    vs registry: 2,707 vs 13,806 ids, overlap 640; chance would give 2,322 (ratio 0.276)
    vs EHR ecg: 2,707 vs 15,390 ids, overlap 2,588; chance would give 2,591 (ratio 0.999)
  UCN_OKVCAR_1000009333_CAGOK.csv (id=M3LIFE_no)
    vs registry: 96 vs 13,806 ids, overlap 25; chance would give 82 (ratio 0.304)
    vs EHR ecg: 96 vs 15,390 ids, overlap 91; chance would give 92 (ratio 0.990)
  UCN_OK_1000004189_OKNAZORG1.csv (id=M3LIFE_no)
    vs registry: 720 vs 13,806 ids, overlap 167; chance would give 618 (ratio 0.270)
    vs EHR ecg: 720 vs 15,390 ids, overlap 692; chance would give 689 (ratio 1.004)
  UCN_OK_1000007347_PCI_DETAILS.csv (id=M3LIFE_no)
    vs registry: 2,020 vs 13,806 ids, overlap 489; chance would give 1,733 (ratio 0.282)
    vs EHR ecg: 2,020 vs 15,390 ids, overlap 1,930; chance would give 1,933 (ratio 0.998)
  UCN_OK_1000007347_PCI_DETAILS_R.csv (id=M3LIFE_no)
    vs registry: 1,310 vs 13,806 ids, overlap 355; chance would give 1,124 (ratio 0.316)
    vs EHR ecg: 1,310 vs 15,390 ids, overlap 1,248; chance would give 1,254 (ratio 0.995)
  UCN_OK_1000007350_PCI_L_EN_P.csv (id=M3LIFE_no)
    vs registry: 2,033 vs 13,806 ids, overlap 493; chance would give 1,744 (ratio 0.283)
    vs EHR ecg: 2,033 vs 15,390 ids, overlap 1,942; chance would give 1,946 (ratio 0.998)
  UCN_OK_1000007371_OKNAZORG2.csv (id=M3LIFE_no)
    vs registry: 15 vs 13,806 ids, overlap 2; chance would give 13 (ratio 0.155)
    vs EHR ecg: 15 vs 15,390 ids, overlap 15; chance would give 15 (ratio 1.032)
  UCN_OK_1000007373_OKNAZORG3.csv (id=M3LIFE_no)
    vs registry: 453 vs 13,806 ids, overlap 123; chance would give 389 (ratio 0.317)
    vs EHR ecg: 453 vs 15,390 ids, overlap 434; chance would give 434 (ratio 1.001)
  UCN_PATIENT_DEMOGRAFISCH.csv (id=M3LIFE_no)
    vs registry: 2,948 vs 13,806 ids, overlap 658; chance would give 2,529 (ratio 0.260)
    vs EHR ecg: 2,948 vs 15,390 ids, overlap 2,816; chance would give 2,821 (ratio 0.998)

=== 3. UCN <-> EHR at VALUE level (ECG measurements) =====================
  10 column pair(s) to compare
      QRS_Duration_ECG vs ecg.QRS_Duration: n=2,291 rho=-0.006  best-case |diff| 4.00 vs 4.00 permuted
RESULT: UCN value check QRS_Duration_ECG vs ecg.QRS_Duration: n=2291 rho=-0.006 best-case 4.00 vs 4.00 permuted
      Q_TInterval_ECG vs ecg.QT_Interval: n=2,291 rho=+0.041  best-case |diff| 5.00 vs 4.00 permuted
RESULT: UCN value check Q_TInterval_ECG vs ecg.QT_Interval: n=2291 rho=+0.041 best-case 5.00 vs 4.00 permuted
      POnset_ECG vs ecg.P_Onset: n=2,241 rho=-0.022  best-case |diff| 6.00 vs 6.00 permuted
RESULT: UCN value check POnset_ECG vs ecg.P_Onset: n=2241 rho=-0.022 best-case 6.00 vs 6.00 permuted
      POffset_ECG vs ecg.P_Offset: n=2,241 rho=-0.022  best-case |diff| 6.00 vs 6.00 permuted
RESULT: UCN value check POffset_ECG vs ecg.P_Offset: n=2241 rho=-0.022 best-case 6.00 vs 6.00 permuted
      T_Onset_ECG vs ecg.T_Onset: n=2,291 rho=-0.006  best-case |diff| 3.00 vs 3.00 permuted
RESULT: UCN value check T_Onset_ECG vs ecg.T_Onset: n=2291 rho=-0.006 best-case 3.00 vs 3.00 permuted
      T_Offset_ECG vs ecg.T_Offset: n=2,291 rho=+0.020  best-case |diff| 3.00 vs 3.00 permuted
RESULT: UCN value check T_Offset_ECG vs ecg.T_Offset: n=2291 rho=+0.020 best-case 3.00 vs 3.00 permuted
      QRS_Onset_ECG vs ecg.QRS_Onset: n=2,291 rho=+0.010  best-case |diff| 2.00 vs 2.00 permuted
RESULT: UCN value check QRS_Onset_ECG vs ecg.QRS_Onset: n=2291 rho=+0.010 best-case 2.00 vs 2.00 permuted
      QRS_Offset_ECG vs ecg.QRS_Offset: n=2,291 rho=+0.008  best-case |diff| 2.00 vs 2.00 permuted
RESULT: UCN value check QRS_Offset_ECG vs ecg.QRS_Offset: n=2291 rho=+0.008 best-case 2.00 vs 2.00 permuted

=== 4. UCN <-> registry at VALUE level (demographics) ====================
  detected sex='Geslacht' birth-year-like='Geboortejaar'
  sex agreement 1.000 on 658 patients (chance at this cohort's ratio is 0.545)
RESULT: UCN demographics sex agreement with registry: 1.000 on 658 patients (chance 0.545)
  birth-year vs registry age: rho=-0.891 on 658 (a working join gives a strong NEGATIVE rho)
RESULT: UCN demographics birth-year vs registry age: rho=-0.891 on 658 patients (negative is correct)

=== 5. verdict ==============================================================
  UCN <-> EHR (value level): 0.041
  UCN <-> registry: sex 1.000 vs chance 0.545, birth-year vs age rho -0.891
RESULT: ** UCN SHARES THE REGISTRY ID SPACE ** (sex 1.000 vs chance 0.545, birth-year vs age rho -0.891; EHR 0.041): UCN's own clinical content -- echo, ECG, heart-team, biobank -- is therefore usable against the registry, so the research question is answerable from UCN data even without repairing the EHR link
  ** UCN sits in the REGISTRY space. Its echo/ECG/heart-team/biobank content is
     usable against the registry: the research question becomes answerable from
     UCN data without waiting for the EHR crosswalk. **
```

</details>
