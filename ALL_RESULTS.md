# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (1 runs)

- **2026-09-08T14:34:18Z | join check: events vs registry**
  - RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.021)
  - RESULT: join check meting.Lengte vs lengte: n=8202 rho=-0.017 (shuffled +0.006)
  - RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.029)
  - RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
  - RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.012 (shuffled +0.020)
  - RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.017 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn

---

### RUN 2026-09-08T14:34:18Z | join check: events vs registry

- status: ok
- context: landmark=180
- RESULT: join check meting.Gewicht vs gewicht: n=10923 rho=+0.011 (shuffled +0.021)
- RESULT: join check meting.Lengte vs lengte: n=8202 rho=-0.017 (shuffled +0.006)
- RESULT: join check meting.BMI vs bm_indx: n=2776 rho=-0.009 (shuffled -0.029)
- RESULT: join check lab_ezis.Creat-BL vs labkrea: n=6010 rho=+0.002 (shuffled -0.007)
- RESULT: join check lab_ezis.Chol-BL vs labchol: n=5161 rho=-0.012 (shuffled +0.020)
- RESULT: ** EVENT JOIN IS BROKEN ** (best |rho|=0.017 across 5 pairs): quantities measured in BOTH the EHR and the study visit do not agree for the same patient id, so every event AND text result in this project measures plumbing and must be withdrawn

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
```

</details>
