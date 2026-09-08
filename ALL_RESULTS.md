# Results log — baseline-free survival experiments

Append-only, one block per run, newest last. The index below is regenerated on every run, so the top of this file is always the complete summary.

No raw clinical text is ever written here.

## Index (1 runs)

- **2026-09-08T15:50:39Z | diagnose: did normalisation break the join?**
  - RESULT: ** ROW COUNT CHANGED in the registry: 13808 -> 13806 **
  - RESULT: registry id->weight preserved by normalisation: n=5223 rho=+1.000
  - RESULT: normalisation is NOT the culprit (best agreement across all four pairings: original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011): the originals do not join either, so the two extracts genuinely carry independent pseudonymisation runs and a crosswalk is required

---

### RUN 2026-09-08T15:50:39Z | diagnose: did normalisation break the join?

- status: ok
- context: orig_smart=data/smart/smart_22nov2022.csv norm_smart=data/smart/smart_utf8.csv
- RESULT: ** ROW COUNT CHANGED in the registry: 13808 -> 13806 **
- RESULT: registry id->weight preserved by normalisation: n=5223 rho=+1.000
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

=== 2. THE DECISIVE TEST: does the ORIGINAL pair join? ==================
  ORIGINAL events:
    meting_20251203.csv (encoding=cp1252, sep=;): weights for 12,771 ids
  NORMALISED events:
    no meting*.csv in data/smartehr-utf-8
    ORIGINAL pair matched on string ids: n=10,923  rho=+0.011
    ORIGINAL pair matched on int    ids: n=10,923  rho=+0.011
    norm registry + orig events matched on string ids: n= 4,067  rho=-0.004
    norm registry + orig events matched on int    ids: n=10,923  rho=+0.011
RESULT: normalisation is NOT the culprit (best agreement across all four pairings: original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011): the originals do not join either, so the two extracts genuinely carry independent pseudonymisation runs and a crosswalk is required

  -> The ORIGINAL files do not join either (original/string=+0.011, original/int=+0.011, norm_reg_orig_ev/string=-0.004, norm_reg_orig_ev/int=+0.011). The normalisation is
     exonerated: the two extracts carry independent pseudonymisation runs, and
     the crosswalk has to come from the data provider.
```

</details>
