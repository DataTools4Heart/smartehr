# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (1 runs)

- **2026-09-08T15:12:55Z | join check: events vs registry**
  - RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.021)
  - RESULT: join check meting.Lengte vs lengte: n=8202 rho=-0.017 (shuffled +0.006)
  - RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.029)
  - RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
  - RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.012 (shuffled +0.020)
  - RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.017 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn
  - RESULT: NO KEY IN smart.csv RECOVERS ROUTINE WEIGHT (best +0.011 (m3life_no)): the EHR-to-registry linkage cannot be repaired from the files we hold and must be re-derived by the data manager
  - RESULT: registry self-consistency: BMI vs weight/height^2 rho=+0.798 on 13731 rows (median abs diff 6.25)
  - RESULT: event self-consistency: BMI vs weight/height^2 rho=+0.941 on 3180 patients (median abs diff 0.31)
  - RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949

---

### RUN 2026-09-08T15:12:55Z | join check: events vs registry

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
- RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949

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
RESULT: identifier spaces: registry 13806 ids [1, 16096], events 12771 ids [2, 15877], overlap 10949
```

</details>
