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

## 3. T3-0 — the headroom check (no GPU, do this FIRST)

Before spending GPU time, establish whether *any* text method could help, by asking what
the curated variables achieve when restricted to facts a note could plausibly state.

Split the 183 curated variables into:

- **chart-derivable** — history and status that appears in prose: `vg_*`, `vgok_*`, `vgt_*`,
  `vz_*` (histories), `roken`, `packyrs`, `alcohol`, `diagnsco`, `vaatzkt1`, `klinman`,
  and medication flags `statine`, `aspirine`, `pamid`, `lipmid`;
- **protocol-measured** — quantities that exist only because a study visit measured them:
  `imt_gm`, `abi_*`, `stenACI*`, `csten_*`, `Aort*`, `aorta_*`, `nrlng_*`, `nrvol_*`,
  `lab*`, `bdsys`/`bddia`, anthropometry, and the questionnaire blocks `kl*`, `mht*`,
  `mli*`, `mas*`, `mgl*`, `MBS*`.

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode baseline --require-text \
  --baseline-cols "vg_,vgok_,vgt_,vz_,roken,packyrs,alcohol,diagnsco,vaatzkt1,klinman,statine,aspirine,pamid,lipmid" \
  --out-dir arms/CTRL_chartderivable_rt
```

```bash
python scripts/smartehr/prepare_text_features.py $COMMON --cache $CACHE --mode baseline --require-text \
  --baseline-cols "~vg_,vgok_,vgt_,vz_,roken,packyrs,alcohol,diagnsco,vaatzkt1,klinman,statine,aspirine,pamid,lipmid" \
  --out-dir arms/CTRL_protocolonly_rt
```

**This can end the arm early.** Interpretation:

| chart-derivable C | meaning |
|---|---|
| ≈ 0.673 (demographics) | Chart-derivable facts carry no signal beyond demographics. **No text method can help** — the null is structural, T3 is unnecessary, and this is a *stronger* result than another null because it explains the mechanism. |
| ≈ 0.70–0.74 | Real headroom exists between text-derivable facts and what T1/T2 achieved. T3 is justified and has a concrete target. |

Also run the same split on the **full curated** ladder so the two halves are comparable, and
report the pair in the report's §10.1 as the quantitative version of the "that versus how
much" claim.

---

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
