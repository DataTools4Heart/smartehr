# Assumptions

Decisions in this repository that are **not** derivable from the project's own data or
dictionaries, and therefore rest on outside knowledge or on a judgement call. Each entry
says what was assumed, why it was necessary, what could go wrong, and how to check it
against the data.

Anything that *is* grounded in the repo is not listed here — it is cited in the code at the
point of use. The dictionaries relied on are:

| file | what it grounds |
|---|---|
| `data/smartehr/data_dicts/smart.csv` | SMART registry: variable labels **and value labels** for all 287 baseline variables |
| `data/smartehr/data_dicts/data_dict.csv` | EHR event columns: per-table column names, classes, coverage, descriptions |
| `data/smartehr/data_dicts/lab.csv`, `meting.csv`, `echo.csv` | coded-value maps for the long-format event sources |

Scope of this file: the graded/medication text-extraction arm
(`scripts/smartehr/graded_concepts.py`, `--mode graded`) and the curated-variable
provenance partition (`scripts/smartehr/feature_matrix.py`). Both were built for the
free-text arm described in `docs/baseline-free-event-survival-report.md`.

---

## 1. ATC prefixes implementing SMART's medication groups

**Assumed.** That SMART's internal medication groups map to WHO ATC prefixes as follows:

| SMART | registry label (verbatim from `smart.csv`) | assumed ATC |
|---|---|---|
| `mht01` | Niet/wel L10 med. (beta-rec.-blokk. sympathicolytica) | `C07` |
| `mht02` | Niet/wel L20 med. (diuretica) | `C03` |
| `mht03` | Niet/wel L30 med. (ACE-remmers) | `C09A`, `C09B` |
| `mht04` | Niet/wel L40 med. (calciumantagonisten) | `C08` |
| `mht05` | Niet/wel L50 med. (sel. alpha1-rec.-blokk. sympathicolytica) | `C02CA` |
| `mht07` | Niet/wel L70 med. (centraal aangrijpende antihypertensiva) | `C02A` |
| `mht12` | Niet/wel D20 med. (angiotensine II (AT1)-antagonisten) | `C09C`, `C09D` |
| `mht41` | Niet/wel direct-acting vasodilator | `C02DB`, `C02DD` |
| `mli01` | Niet/wel statines | `C10AA` |
| `mli02` | Niet/wel fibraten | `C10AB` |
| `mli03` | Niet/wel galzuurbindende harsen | `C10AC` |
| `mli04` | Niet/wel cholesterolabsorptie-remmers | `C10AX09` |
| `mas01` | Niet/wel plaatjes-remmers | `B01AC` |
| `mas02` | Niet/wel orale anticoagulantia | `B01AA` |
| `mas02c` | Niet/wel laag moleculair gewicht heparine | `B01AB` |
| `mas03` | Niet/wel DOAC (specifieke stollingseiwit remmer) | `B01AE`, `B01AF` |
| `mgl01` | Niet/wel glucoseverlagende middelen | `A10B` |
| `mgl02` | Niet/wel insulines | `A10A` |

**Why it is needed.** The registry names each group by its Dutch *pharmacological class*
and by an internal code (`L10`, `L20`, `D20`). No table in this repository maps those codes
to ATC — verified by grepping all five dictionaries. The event data carries only ATC
(`med_ZIatc`, documented in `data_dict.csv` as "Medication ATC code"), so a bridge is
required to reproduce `mht_alln` from text at all.

**What is grounded, and what is not.** The *class* each group denotes is grounded — it is
written out in the registry label. The ATC prefix implementing that class is standard WHO
ATC, from outside the repo. The prefixes are therefore an interpretation of a stated class,
not a guess at an unknown one.

**Residual risk, ranked.** `mht06` ("combinatiepreparaten") is deliberately **omitted**: a
fixed-dose combination sits under `C09BA`/`C09DA`/`C07F` and more, and assigning it a single
prefix would double-count drugs already captured by their component classes. `mht02a`–`d`
(loop / thiazide / potassium-sparing / aldosterone antagonist) are omitted for the same
reason — they are subsets of `C03`, which `mht02` already covers, and including both would
inflate a *count* feature. `mht33` ("restgroep") has no principled prefix and is omitted.
So `graded.n_antihypertensive_classes` counts **8** groups where `mht_alln` counts up to 10;
it is a lower bound on the curated variable, not a reproduction of it.

**How to check.** The derived lexicon is written to the path given by `--med-lexicon` and
every class's ATC prefixes, name count and first names are printed into `$RESULTS`. A class
whose names look pharmacologically wrong indicates a bad prefix. A class printed with
`<- NONE` has no matching prescription in this cohort and is silently undetectable in text,
which is also reported via `emit`.

---

## 2. Drug names are derived, not assumed

**Not an assumption — recorded here because it is the alternative to one.** The Dutch drug
names searched for in text are **not** written by hand. They are derived from the cohort's
own `med_*.csv` by taking every `med_genNaam` whose `med_ZIatc` starts with a prefix in §1,
over **train patients only**.

**Why this way.** A hand-written Dutch drug list would be an unverifiable guess about which
names this site actually uses, and it would silently miss local spellings and brand names.
Deriving it means the lexicon is auditable against the data that produced it.

**Residual risk.** A drug prescribed but never *named in narrative text* contributes nothing;
conversely a drug named in text but never prescribed in this cohort is invisible to the
matcher. Both push medication features toward under-detection, so
`graded.n_antihypertensive_classes` is a lower bound (compounding §1).

---

## 3. Curated-variable provenance partition (chart-derivable vs protocol-measured)

**Assumed.** Which of the 183 numeric baseline variables a clinical note could plausibly
state. The partition is in `scripts/smartehr/feature_matrix.py`
(`CURATED_CHART`, `CURATED_IMAGING`, `CURATED_PROTOCOL`, `CURATED_DEMOG`, `CURATED_ADMIN`)
and is printable with `--list-baseline-groups`.

**Why it is needed.** The T3-0 headroom check compares what each half achieves; there is no
provenance column in the registry, so the assignment is a clinical judgement.

**What is grounded.** Every assignment was made from the variable's own registry label, and
several turn on it: `hyptns_n` ("Niet/wel hypertensie", derived from the measured pressure)
is protocol while `hyptns_b` ("Niet/wel behandeling hypertensie; vraag 6.03", reported
treatment) is chart-derivable. The same `_n`/`_b` split applies to hyperglycaemia and
hyperlipidaemia.

**Residual risk.** `CURATED_IMAGING` (17 variables: carotid stenosis grade, aortic diameter,
kidney size and volume, renal failure) is the group a reasonable reviewer could move. They
are study measurements in origin, but radiology and MRI reports **are** in the text corpus
and can state the same numbers. This is why the check reports `chart_strict` (without
imaging, 0.7024) alongside `chart` (with, 0.7310): the conclusion holds either way, and the
disputable group is visibly not carrying it.

**How to check.** An unassigned column is a hard error, so the halves always sum to the
whole. Show the `--list-baseline-groups` output to a clinical reviewer.

---

## 4. Dutch severity words mapped to stenosis bands

**Assumed.** That in Dutch duplex reporting `geringe`/`lichte`/`minimale`/`laaggradige`
denote the `<= 29%` band, `matige`/`middelmatige` the `30-49%` band, and
`ernstige`/`forse`/`hooggradige`/`significante` the `>= 70%` band.

**Why it is needed.** Many reports grade a stenosis in words rather than a percentage, and
discarding those findings would bias `graded.stenosis_max` toward the minority of reports
that quote a number.

**What is grounded.** The *bands themselves* and their numeric edges are verbatim from
`stenACIl`/`stenACIr`'s value labels (0 geen, 1 `<=29%`, 2 `30-49%`, 3 `50-69%`, 4 `>=70%`,
5 subtotaal, 6 occlusie, 7 pre-occlusief), as is the percentage-to-band mapping and the
`csten_50`/`csten_70` thresholds. Only the **word**-to-band step is assumed.

**Residual risk.** `significante` is the weakest link: it is used clinically for
"haemodynamically significant", conventionally `>= 50%`, which is band 3 rather than the
band 4 assigned here. It is grouped with `ernstige` because in carotid reporting the
significance threshold usually quoted is 70%. This will over-grade some findings by one
band. `matige` mapping to band 2 (`30-49%`) rather than 3 (`50-69%`) is the mirror-image
risk.

**How to check.** Compare `graded.stenosis_max` against curated `stenACIl`/`stenACIr` on
the patients who have both — a confusion matrix of the two would settle every word mapping
empirically, and needs no outcome. **This is worth running before the arm is believed** and
is the cheapest available validation of the whole graded approach.

---

## 5. Aggregation across documents

**Assumed.** Which document's value represents the patient when several disagree.

**Grounded where possible**, from the registry's own wording: `aorta_hg` is "**Grootste**
diameter aorta" so the aorta feature takes the maximum; `KliMaYr` is "Jaar **eerste** uiting
klin.manifest vaatlijden" so onset takes the earliest year. For stenosis both the maximum
(worst ever recorded) and the most recent document's grade are emitted, because the registry
records a single study-visit measurement and neither aggregate is obviously its analogue.

**Residual risk.** The maximum is sensitive to a single mis-parse in any document, whereas
the curated variable is one measurement. The paired `_last` features exist so this can be
compared rather than assumed.

---

## 6. Unstated quantities are missing, not zero

**Assumed.** That a quantity never mentioned in a patient's notes is unknown (`NaN`) rather
than zero, while an explicit denial ("geen stenose of plaque") is the scale's zero.

**Why.** The registry codes "Geen stenose of plaque" as `0`, so a denial genuinely is a
measurement. Silence is not. Conflating them is what made `gfr_count` read C=0.851 in the
structured arm — an artefact of *who got measured* rather than of any value.

**Residual risk.** Missingness in notes is not random: sicker patients are documented more.
Every quantity therefore also gets an explicit `_measured` indicator, so the screen sees a
missingness artefact as its own feature instead of having it hide inside a value column.
Read those indicators first, exactly as the T0 volume gate is read first.

---

## 7. Preserving years reintroduces calendar era

**Assumed.** That extracting onset years is worth reintroducing year-granularity calendar
information into the text.

**Why it is needed.** `--strip-dates` (the default for every earlier arm) removes full
dates, so "CABG op 12-05-2003" loses its year entirely. `KliMaYr` is one of the four
carriers the headroom check identified, so `--date-mode year` replaces a full date with its
year alone.

**Residual risk.** Calendar era correlates with enrolment date and therefore with
follow-up length and treatment era — pitfall #4 in the free-text plan. Mitigation: the
paired arm runs with `--date-mode strip`, so the era contribution is measured rather than
assumed away. **If the two arms differ materially, believe the stripped one.**

---

## 8. What is deliberately not attempted

- **Temporal scoping of a quantity to its own date.** An extracted stenosis grade is
  attributed to the document that states it, but a document may recite a *historical*
  finding ("in 2009 een stenose van 70%"). No attempt is made to separate the two, so
  `_last` is the last *mention*, not the last *measurement*.
- **Laterality beyond left/right adjacency.** A side is assigned only when "links"/"rechts"
  occurs within 40 characters of the finding; bilateral and unstated findings feed only the
  side-agnostic features.
- **Reconciling contradictions.** If one note says ex-smoker and a later one says current
  smoker, the later mention wins for `_last` and the higher code for `_max`. No consistency
  model is applied.
