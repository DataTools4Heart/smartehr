# Plan — T3: does clinical free text carry 15-year prognostic signal?

Companion to `docs/free-text-arm-runbook.md` and `docs/baseline-free-event-survival-report.md`.
Status: **planned, not started.**

---

## 1. Why run this at all, given two nulls

T1 (TF-IDF) and T2 (concepts) both landed at chance. T3 is not "the same question with a
bigger model" — the report's own interpretation (§10.1) predicts *where* those two failed,
and that prediction is testable:

> Prose records **that** a condition was mentioned; a curated variable records **how much** —
> pack-years, systolic pressure, creatinine, percent stenosis.

But the grading **is in the notes**: *"ernstige stenose van de proximale LAD"*, *"EF 35%"*,
*"geringe atherosclerose"*, *"NYHA III"*. TF-IDF discards it (bag of words, no composition),
and binary concept indicators discard it by construction. So:

> **T3 hypothesis.** The prognostic content of these notes is *graded and compositional*.
> Representations that preserve grading may capture what bag-of-words and binary indicators
> throw away.

That is a falsifiable hypothesis derived from the previous null, not a fishing expedition.

**Benchmarks (matched text subcohort, 9,644 patients / 257 test events):** full curated
baseline **0.7394**, demographics **0.6727**, best text arm so far **0.6750**, text alone
0.482–0.521.

---

## 2. Hard constraints

- **No cloud LLM APIs.** Clinical text cannot leave the environment. Local weights only,
  which rules out every hosted model and constrains the generative arm in §6.
- **Event budget.** 828 training events. Any representation must be reduced to roughly
  60–120 effective dimensions; a raw 1024–4096-dim embedding will overfit exactly as the
  256-dim TF-IDF did (train 0.66 → test 0.49).
- **Multiplicity is the main threat.** 6 models × 4 poolings × 3 prompts = 72 configurations
  will produce a "winner" from noise alone. §7 fixes this with an outcome-blind selection
  rule, decided before any survival number is computed.
- **The test split is touched once per final arm.** Never for model, pooling, prompt or
  dimensionality choice.

---

## 2b. Prerequisites from clinical review (2026-08-27) — **all three resolved 2026-09-03**

Three items raised by the data manager / clinical researcher come **before** any T3 work,
because two of them change what the existing numbers mean.

1. **`ok.OMSCHR` — can it be used?** It is the *operation* description (per the project's own
   data dictionary), and its median row sits at **+98 days**, with 16,671 of 35,117 rows
   post-baseline. Under the day-180 landmark it is formally available and the leakage
   invariant prints 0, but it contributes mostly **post-baseline treatment** — "this patient
   had a CABG two months after enrolment". That is legitimate for a model anchored at day
   180, which is what every arm here is, and inadmissible for one framed as "risk at
   enrolment". It is used only in the structured arm's occurrence pivot, never in the text
   arm, so the practical exposure is small — quantified by the `sens` phase, which rebuilds
   the structured arm without it.
2. **`perifeer_vaatlijden` and `nierfunctie` — issue or quantity?** Both were conflated, and
   the review was right. Fixed by tiering the term lists (see the report's §10.1 correction);
   `nierfunctie` no longer fires on a normal eGFR, and `aneurysma` is now its own concept
   rather than being counted as peripheral arterial disease. **T2 must be re-run before T3
   is interpreted**, since the concept arm was the most on-question of the two nulls.
3. **T2 + the full curated baseline.** Never run: the concept arm was only ever compared
   against demographics. The practically relevant increment is over **all 183 curated
   variables**, because those already exist in this cohort. Added as the `incr` phase, for
   concepts, TF-IDF and volume alike, against the `CTRL_full_rt` reference of 0.7394.

**Outcome (run 2026-09-03, 91 runs in the log).** All three are settled and none of them
rescues the free-text arm:

| item | result | reading |
|---|---|---|
| 1. `ok.OMSCHR` | structured arm **0.6884** without it vs 0.6890 with (532 vs 534 features) | the concern is moot — the result never depended on it |
| 2. tiered concept terms | **0.5098** corrected vs 0.5114 conflated; all-tier variant 0.5092; 0 of 39 clear the floor in every variant | prevalences moved exactly as predicted (renal 21.0% → 5.2%), the verdict did not |
| 3. text + full curated baseline | 0.7394 → concepts **0.7397**, volume **0.7394**, TF-IDF **0.7388** | text adds +0.0003 to what is already collected |

Item 3 sets T3's success criterion, and it is much harsher than the one this plan was
drafted against: **a frozen-LLM arm has to beat 0.7394, not 0.6727, to matter clinically.**
Beating 0.6727 would only show that an LLM can read age and sex out of a letter.

Item 2 also removes the last "the extraction was broken" escape from the concept null. The
term lists *were* wrong in what they meant, they are now right, and the arm reads the same
to three decimals — so T3 cannot be justified as fixing concept extraction. Its only
remaining justification is the one in §1: that TF-IDF and binary concepts discard *grading*,
which §3's headroom check tests without a GPU.

## 3. T3-0 — the headroom check (no GPU, do this FIRST)

Before spending GPU time, establish whether *any* text method could help, by asking what
the curated variables achieve when restricted to facts our narrative corpus could plausibly
contain. That bounds the ceiling for every text method at once.

### 3.1 The split is the whole experiment, so it is written out by name

**This section was rewritten on 2026-09-07.** The original version split the 183 variables
by name prefix (`vg_,vgok_,vgt_,vz_,roken,packyrs,...`). Checked against the registry's own
labels in `data/smartehr/data_dicts/smart.csv`, that rule is wrong in three ways, all of
which shrink the chart-derivable half and therefore bias the check toward "no headroom" —
the conclusion we already expect. A check that can only confirm the prior is not worth
running.

| mis-sorted by the prefix rule | n | why it is chart-derivable |
|---|---|---|
| `mht*`, `mli*`, `mas*`, `mgl*`, `mmpr`, `mhmc`, `Thyr`, `Amiodar`, `Lithium` | 44 | medication lists are the most chart-derivable data in any EHR; every discharge letter carries one |
| `KliMaC`, `KliMaYr`, `KliMaDur`, `KliMaDrD` | 4 | type, year and duration of the first manifest event — "myocardinfarct in 2003" is exactly what a letter states. Also among the strongest curated features (0.6138 / 0.6313 / 0.6078 / 0.5976) |
| `hyptns_b`, `hypgly_b`, `hyplip_b`, `VgBh_HpL` | 4 | *reported treatment* from the questionnaire. Note the `_n`/`_b` pair splits: `hyptns_n` is derived from the **measured** pressure and is protocol; `hyptns_b` is "behandeling; vraag 6.03" and is chart. No substring rule can express that |

And `leeftijd`/`geslacht` landed in the protocol half, which hands it ~0.673 for free while
the chart half starts from nothing — the comparison would have measured the split, not the
data.

The partition therefore lives by exact name in `scripts/smartehr/feature_matrix.py`
(`CURATED_CHART`, `CURATED_IMAGING`, `CURATED_PROTOCOL`, `CURATED_DEMOG`, `CURATED_ADMIN`),
selected with `--baseline-cols group:<name>`, and **an unassigned column is a hard error**:
if a curated variable belonged to no group it would vanish from both halves and they would
no longer sum to the full baseline whose 0.7394 they are compared against.

| group | n | contents |
|---|---|---|
| `chart` (generous) | 114 | history, diagnoses, medication, smoking/alcohol status, disease onset, **plus** `imaging` |
| `chart_strict` | 97 | the same without the imaging findings |
| `imaging` | 17 | carotid stenosis grade, aortic diameter, kidney size/volume, renal failure — study measurements in origin, but radiology and MRI reports are **in our corpus** and can state the same numbers |
| `protocol` | 69 | research ultrasound (IMT, ABI), anthropometry, study labs and their derived flags, metabolic-syndrome criteria, and the questionnaire instruments (SF-36, METs, diet, education, country of birth) |
| `demographics` | 2 | age and sex — in **neither** half, the floor both are measured against |
| `admin` | 4 | identifiers and dates, carried only to prove the partition exhaustive |

Review it before believing any number it produces:

```bash
python scripts/smartehr/prepare_text_features.py --smart-csv $SMART --list-baseline-groups
```

The generous half is `chart` = chart + imaging. Reporting `chart_strict` alongside it is what
shows the assignment of the arguable group is not doing the work.

### 3.2 Running it

```bash
./bash_scripts/run_all_phases.sh t3headroom screens
```

Seven arms, all CPU and seconds each (no text is read — `--mode baseline` emits curated
columns on whatever cohort the text flags define): each half alone, each half plus
demographics, the strict chart variant, and both halves on the full cohort so the pair is
comparable to the 0.7576 reference as well as to 0.7394.

### 3.3 What each outcome means

Read `HR_chart_demo_rt` against the **matched** demographics control, 0.6727 — not 0.6883,
which is a full-cohort number.

| chart-derivable + demographics | meaning |
|---|---|
| ≈ 0.673 | Chart-derivable facts carry no signal beyond demographics. **No text method can help**, because even having those facts *perfectly* adds nothing — the ceiling for text is demographics. T3 is unnecessary and the free-text negative becomes structural and mechanistic, which is a stronger result than a fourth null. |
| 0.69–0.72 | Partial headroom. Text would have to recover these facts *well* to realise it. Worth one embedding arm with a concrete target, not a sweep. |
| ≈ 0.73–0.74 | Full headroom: nearly all of the curated skill is in principle text-derivable, and T1/T2 simply failed to extract it. T3 is justified and the grading hypothesis in §1 is the thing to test. |

The `protocol` half is the counterpart: if it carries most of the skill (≈ 0.73) while the
chart half sits at demographics, that **is** the mechanism behind §10.1's "that versus how
much" claim, stated quantitatively — the prognostic information lives in protocol
measurement, which no amount of reading the notes can recover.

## 4. T3-1 — model selection, outcome-blind

**The problem.** We cannot choose a model by survival C: 828 training events plus many
candidates equals guaranteed overfitting of the *selection*.

**The solution.** Choose by whether the embedding encodes clinical facts **we already have
labels for** — the curated variables — with the survival outcome never consulted.

For each candidate model: encode a **subsample of 2,000 patients** (cheap), then fit a
linear probe (ridge / logistic, train-on-train, scored on validation) for ~10 targets chosen
to span the grading question:

| target | type | why |
|---|---|---|
| `roken` (smoking) | binary | stated plainly in prose; a floor test — if this fails, nothing will work |
| `vz_DM` (diabetes) | binary | stated plainly |
| `vz_hart` (cardiac history) | binary | stated plainly |
| `packyrs` | continuous | **graded**: is severity recoverable, or only presence? |
| `labkrea` (creatinine) | continuous | graded, and often quoted numerically in letters |
| `MDRD` (eGFR) | continuous | graded |
| `stenACIl` (carotid stenosis) | ordinal | **the grading test**: "ernstige" vs "geringe" |
| `bdsys` | continuous | graded, often quoted |
| `leeftijd` (age) | continuous | **sanity/leakage probe** — age is often written in notes; a very high score here warns that the embedding partly encodes demographics, which the survival arm must then control for |
| `geslacht` (sex) | binary | same |

Report AUC for binary targets and Spearman ρ / R² for continuous ones. Rank models by mean
probe score over the **graded** targets specifically, since that is the hypothesis.

This probe is worth running for its own sake: it produces a publishable sub-result
("embeddings recover stated smoking status at AUC 0.x but explain only y% of creatinine
variance") and, crucially, it **converts a possible third null into an informative one**:

- probe **high** + survival **null** → the facts *are* in the text and *are* recoverable;
  the failure is that these facts do not predict 15-year risk. Much stronger than "we tried
  a model and it didn't work".
- probe **low** → the text does not encode the graded facts at all; the null is about the
  notes, not the model.

### Candidate models

Verify availability and licence on the VM first (`--list-models` step below); clinical
Dutch models may need an access request.

| model | why | notes |
|---|---|---|
| `Qwen/Qwen3-Embedding-0.6B` | strong multilingual retrieval embedder, instruction-aware, Matryoshka dims | already wired into `extract_qwen_embeddings_longitudinal.py`; the natural first run |
| `Qwen/Qwen3-Embedding-4B` | same family, larger | run only if 0.6B probes well; ~10× cost |
| `intfloat/multilingual-e5-large` | strong multilingual, well-tested Dutch | needs the `passage: ` / `query: ` prefix — a prompt variant, see §5 |
| `BAAI/bge-m3` | multilingual, long context (8k), good for 3.5k-char letters | dense + sparse output; use dense |
| `jinaai/jina-embeddings-v3` | multilingual, task-adapter LoRAs | task adapter is effectively a prompt choice |
| **`CLTL/MedRoBERTa.nl`** | **Dutch clinical** encoder, trained on Dutch hospital notes | strongest domain fit; encoder LM, so mean-pool — not retrieval-trained, so probe it rather than assuming |
| `DTAI-KULeuven/robbert-2023-dutch-large` | Dutch general encoder | domain-general Dutch control for MedRoBERTa |

Order of work: Qwen3-0.6B and MedRoBERTa.nl first — they bracket the two hypotheses
(general multilingual retrieval versus in-domain Dutch clinical).

---

## 5. T3-2 — encoding decisions, and the prompt

Each is a **separate axis**, chosen on the probe (never on survival):

**Prompt / instruction.** Instruction-aware embedders change materially with the prefix, so
this is a real hyperparameter, not decoration. Test per model:

1. none (raw text);
2. the model's documented default (`passage: ` for E5, `Instruct: <task>\nQuery: ` for Qwen3);
3. a task-specific instruction, in **Dutch and English** variants, e.g.
   *"Vat de cardiovasculaire voorgeschiedenis en ernst van de aandoeningen van deze patiënt
   samen"* / *"Summarise this patient's cardiovascular history and disease severity"*.

The Dutch-versus-English instruction comparison is itself informative for a multilingual
model on Dutch text, and cheap.

**Chunking.** Documents reach 7,235 tokens and per-patient totals 41,913, so per-patient
concatenation is impossible. Embed **per document**, then pool. Long documents are chunked at
the model's context limit with `--max-tokens-per-block`.

**Pooling per patient** (each a separate arm):
- mean over documents;
- **recency-weighted** mean (weight ∝ exp(−Δt/τ), τ ≈ 1 year) — clinically the most
  defensible, and untested by T1/T2;
- most-recent document only;
- per-source mean then concatenate (keeps a radiology report distinct from a letter);
- max over documents.

**Dimensionality.** Mandatory: SVD/PCA to 64 / 128 / 256, or Qwen3's Matryoshka
`--truncate-dim`. Fit on train only. Report explained variance.

**Section restriction.** `--section "voorgeschiedenis,anamnese"` and `--section conclusie`,
reusing the existing flag.

---

## 6. T3-3 — generative extraction (gated, and arguably the better use of an LLM)

If the §3 headroom check shows room and the §4 probe shows embeddings only partly recover
graded facts, the direct attack is to have a **local** generative model output the graded
variables, turning the text into the kind of features the curated set contains.

- **Schema-constrained**, small, and aimed at grading: LVEF (%), stenosis severity per
  territory (none/mild/moderate/severe), NYHA class, smoking status + pack-years, diabetes
  type + treatment, eGFR/creatinine if quoted, and an explicit `not_mentioned` for every
  field so the model is not pushed into inventing values.
- **Scope the cost**: only `conclusie` + `voorgeschiedenis` sections, or the most recent 3
  documents per patient. 46M tokens through a generative model is otherwise prohibitive.
- **Hallucination is measurable here, for free.** We have curated ground truth for these
  same quantities, so extraction accuracy can be quantified directly: agreement for
  categorical fields, and calibration for numeric ones, on the subset where both exist.
  Report it before any survival number. An extractor that disagrees with the curated value
  half the time cannot support a claim either way.
- Candidate local models: Qwen2.5/3-Instruct (7B–32B, strong multilingual), Llama-3.x
  Instruct, or a Dutch-tuned model such as GEITje. Verify licence and VRAM on the VM.

---

## 7. Multiplicity rules — fixed before any survival number

1. **Selection is outcome-blind.** Model, prompt, pooling and dimensionality are chosen on
   the §4 probe and on explained variance. The survival outcome is not consulted.
2. **At most 4 final survival arms**: the best configuration for each of (Qwen3-0.6B,
   MedRoBERTa.nl), each with and without demographics. Everything else stays in the probe
   stage.
3. **Correct across those 4.** Report the Bonferroni-adjusted threshold alongside the
   nominal one.
4. **Matched control mandatory.** Every arm is compared against `CTRL_demo_rt` on the
   identical subcohort, never against a full-cohort number.
5. **Pre-register the success criterion here:** T3 succeeds if a selected arm beats the
   matched demographics control (0.6727) by more than the ±0.062 test band — that is, test
   C ≥ **0.735** — or if it clears a bootstrap CI on the paired difference that excludes 0.
   Anything smaller is a null, however tempting the point estimate.

---

## 8. Compute

| step | scope | rough cost |
|---|---|---|
| T3-0 headroom | CPU, existing tooling | minutes |
| probe encode | 2,000 patients × ~7 models | 0.6B: ~2 min each; 4B: ~20 min |
| probe fit | CPU, ridge/logistic × 10 targets | seconds |
| full encode, selected model | 9,644 patients, ~35M tokens | 0.6B ≈ 10–20 min; 4B ≈ 2–3 h |
| generative extraction | sections only, subsample first | hours; scope before committing |

`pip install sentence-transformers` is still required — it is not installed, and
`extract_qwen_embeddings_longitudinal.py` depends on it.

---

## 9. Decision table

| §3 headroom | §4 probe | survival arm | conclusion |
|---|---|---|---|
| ≈ demographics | — | not run | **Structural null.** Chart-derivable facts carry nothing beyond age/sex; no text method could. Strongest and cheapest outcome. |
| headroom | low | not run | Text does not encode the graded facts. Null attributable to the notes. |
| headroom | high | ≥ 0.735 | **Signal.** Grading was the missing ingredient; T1/T2 failed by discarding it. |
| headroom | high | ≈ 0.673 | The facts are recoverable but do not predict 15-year risk. A strong, well-supported negative. |

---

## 10. Pitfalls specific to T3

| risk | mitigation |
|---|---|
| Selecting a model on survival C | outcome-blind probe (§4, §7) |
| 1024–4096 dims vs 828 events | mandatory reduction to 64–256, fitted on train |
| Embedding encodes age/sex, so "text" signal is demographics | age and sex are probe targets; if recoverable, report text-only *and* text+demographics and compare against the matched control |
| Instruction prefix silently omitted | the runbook's argument-echo rule: log the exact prompt string in the results block |
| Documents truncated at the context limit | log tokens-in versus tokens-encoded per source; `rad_report` is already truncated at 1024 chars upstream |
| Generative extractor hallucinating | quantify against curated ground truth *before* any survival number (§6) |
| A third null read as "we tried harder" | the probe makes either outcome informative (§4) |

---

## 11. Deliverables

- `scripts/smartehr/probe_embeddings.py` — encode a subsample with a named model/prompt,
  fit linear probes for the curated targets, report AUC/ρ. Outcome never read.
- `prepare_text_features.py --mode documents` already emits the schema the Qwen extractor
  consumes; extend the extractor for the additional models and pooling modes, and log the
  prompt.
- `bash_scripts/run_t3_phases.sh` in the style of `run_all_phases.sh`: phase-selectable,
  skip-if-built, one shared results file.
- Report gains a §12 for T3, and the runbook a T3 section plus changelog entry.
