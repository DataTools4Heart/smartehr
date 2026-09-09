# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (1 runs)

- **2026-09-09T09:46:21Z | join check: events vs registry**
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

---

### RUN 2026-09-09T09:46:21Z | join check: events vs registry

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
```

</details>
