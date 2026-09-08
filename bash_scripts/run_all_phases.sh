#!/usr/bin/env bash
# =============================================================================
# run_all_phases.sh — every command for the free-text arm, in order.
#
# Env setup is deliberately NOT here. Export the three data paths first:
#
#     export SMART=/path/to/smart.csv
#     export EVENTS=/path/to/all_event_csvs
#     export SPLITS=/path/to/splits.json
#
# Everything else (cache, results file, landmark, horizon) has a default below and
# can be overridden by exporting it.
#
#     ./bash_scripts/run_all_phases.sh                # all phases
#     ./bash_scripts/run_all_phases.sh t1 t2 screens  # only those
#     DRY_RUN=1 ./bash_scripts/run_all_phases.sh      # print commands, run nothing
#     FORCE=1   ./bash_scripts/run_all_phases.sh      # redo arms that already exist
#     RUN_T3=1  ./bash_scripts/run_all_phases.sh t3   # frozen-LLM arm (needs GPU + install)
#
# Phases: p0 joincheck t0 t1 t2 incr sens graded t3headroom ctrl struct screens t3
#
# Every run appends to ONE results file ($RESULTS). Results cannot be copied off the
# VM by hand, so run as many arms as you like and then make a SINGLE download request
# for that file. Its regenerated index sits at the top.
#
# A failing arm does NOT abort the batch (no `set -e` on the arms): the results log
# records the failure with its traceback and the run continues, so an unattended batch
# is never wasted. Failures are also listed in the summary at the end.
# =============================================================================
set -uo pipefail

# ---- required ---------------------------------------------------------------
: "${SMART:?export SMART=/path/to/smart.csv}"
: "${EVENTS:?export EVENTS=/path/to/all_event_csvs}"
: "${SPLITS:?export SPLITS=/path/to/splits.json}"

# ---- overridable ------------------------------------------------------------
LANDMARK="${LANDMARK:-180}"           # prediction origin, days after the SMART baseline
HORIZON="${HORIZON:-5475}"           # 15y, measured FROM the landmark
CACHE="${CACHE:-$PWD/text_cache/documents.parquet}"
RESULTS="${RESULTS:-$PWD/results/ALL_RESULTS.md}"
OUT="${OUT:-$PWD/arms}"              # where arm directories are written
DEMOG="${DEMOG:-leeftijd,geslacht}"  # confirmed present; check with --list-baseline-cols
SVD="${SVD:-256}"
TOKENIZER="${TOKENIZER:-Qwen/Qwen3-Embedding-0.6B}"   # set empty to skip the download
PY="${PY:-python}"

S="scripts/smartehr"
COMMON=(--smart-csv "$SMART" --event-csv-folder "$EVENTS" --split-json "$SPLITS"
        --legacy --landmark-days "$LANDMARK" --horizon-days "$HORIZON"
        --results-file "$RESULTS")
TEXT=("${COMMON[@]}" --cache "$CACHE")

# ---- preflight: check the interpreter, then compile every script ------------
# Both failures below cost a full round-trip to the VM and back, and they resemble the
# argparse-level failures that exit BEFORE results_block opens — leaving no trace in the
# one file that leaves the machine. So they are caught here, before any arm runs.
#   * $PY must be Python 3: under Python 2 every script dies on f-strings, which reads
#     as "the code is broken" rather than "the interpreter is wrong".
#   * compile(), not ast.parse(), is what catches a stray `return` at module level —
#     that is a compile error, not a parse error, so a parse check passes it through.
if ! "$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null; then
  echo "== ABORT: \$PY ($PY) is not Python 3.8+. Set PY=python3 (or your venv python)." >&2
  exit 1
fi
if ! "$PY" -c '
import glob, sys
bad = 0
for f in sorted(glob.glob(sys.argv[1] + "/*.py")):
    try:
        compile(open(f).read(), f, "exec")
    except SyntaxError as e:
        print("  %s:%s: %s" % (f, e.lineno, e.msg))
        bad = 1
sys.exit(bad)' "$S"; then
  echo "== ABORT: a script under $S does not compile (see above). Nothing was run." >&2
  exit 1
fi

mkdir -p "$OUT" "$(dirname "$RESULTS")" "$(dirname "$CACHE")"
PHASES=("$@")
[ ${#PHASES[@]} -eq 0 ] && PHASES=(p0 joincheck t0 t1 t2 incr sens graded t3headroom ctrl struct screens)
declare -a FAILED=() SKIPPED=() RAN=()

want() { for p in "${PHASES[@]}"; do [ "$p" = "$1" ] && return 0; done; return 1; }

# step <name> <out-dir-or-"-"> <cmd...>
step() {
  local name="$1" dir="$2"; shift 2
  if [ "$dir" != "-" ] && [ -f "$dir/metadata.json" ] && [ -z "${FORCE:-}" ]; then
    echo "== SKIP $name (exists; FORCE=1 to redo)"; SKIPPED+=("$name"); return 0
  fi
  echo; echo "=============================================================="
  echo "== $name"; echo "=============================================================="
  if [ -n "${DRY_RUN:-}" ]; then printf '   %q' "$@"; echo; return 0; fi
  local logf rc
  logf=$(mktemp)
  "$@" 2>&1 | tee "$logf"          # tee: keep live progress AND capture for the log
  rc=${PIPESTATUS[0]}
  if [ "$rc" -eq 0 ]; then
    RAN+=("$name")
  else
    FAILED+=("$name")
    echo "== FAILED ($rc): $name"
    # Python-side failures are already in $RESULTS, but an argparse error or a killed
    # process exits before that code runs, so record it here or it is invisible in the
    # only file that leaves the VM.
    { echo; echo "---"; echo
      echo "### RUN $(date -u +%Y-%m-%dT%H:%M:%SZ) | SHELL FAILURE: $name"; echo
      echo "- status: FAILED (exit $rc)"
      echo "- context: $*"; echo
      echo "<details><summary>last 40 lines</summary>"; echo
      echo '```'; tail -40 "$logf"; echo '```'; echo
      echo "</details>"; } >> "$RESULTS"
  fi
  rm -f "$logf"
}

# ---- p0: measure the corpus before modelling it -----------------------------
if want p0; then
  tok=(); [ -n "$TOKENIZER" ] && tok=(--tokenizer "$TOKENIZER")
  step "p0 text EDA" "-" \
    "$PY" "$S/eda_text_events.py" "${COMMON[@]}" "${tok[@]}" --out-dir "$OUT/eda_text"
fi

# ---- t0: volume only. THE GATE. Any content arm must beat this, or a "text
#          signal" is only saying sicker patients accumulate more notes.
if want t0; then
  step "t0 volume (full cohort)" "$OUT/T0_volume" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode volume \
      --screen-features --out-dir "$OUT/T0_volume"
  step "t0 volume (text subcohort)" "$OUT/T0_volume_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode volume --require-text \
      --screen-features --out-dir "$OUT/T0_volume_rt"
fi

# ---- t1: TF-IDF. Headline is the subcohort arm, since 28% of the cohort has no
#          narrative text and would otherwise contribute all-zero rows.
if want t1; then
  step "t1 tfidf word (subcohort)" "$OUT/T1_tfidf_word" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --svd-components "$SVD" --screen-features --out-dir "$OUT/T1_tfidf_word"
  step "t1 tfidf word (full cohort)" "$OUT/T1_tfidf_word_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf \
      --svd-components "$SVD" --out-dir "$OUT/T1_tfidf_word_full"
  # char n-grams: robust to Dutch compounding and typos
  step "t1 tfidf char" "$OUT/T1_tfidf_char" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --analyzer char --ngram-max 5 --svd-components "$SVD" --out-dir "$OUT/T1_tfidf_char"
  # prior conditions are stated in voorgeschiedenis (79.9% of letters) / anamnese (69.1%)
  step "t1 tfidf history sections" "$OUT/T1_tfidf_history" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --section "voorgeschiedenis,anamnese" --svd-components 128 \
      --out-dir "$OUT/T1_tfidf_history"
  step "t1 tfidf conclusie" "$OUT/T1_tfidf_conclusie" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --section conclusie --svd-components 128 --out-dir "$OUT/T1_tfidf_conclusie"
  # de-id sensitivity: letters carry ~50 name-like tokens each. If this differs from the
  # headline arm, part of any signal was physician/site identity, not clinical content.
  step "t1 tfidf no-names" "$OUT/T1_tfidf_nonames" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --strip-nameish --svd-components "$SVD" --out-dir "$OUT/T1_tfidf_nonames"
  # drop the truncated source (rad_report caps at 1024 chars in 59.3% of its documents).
  # Separate cache: changing --text-cols changes what the cache holds.
  step "t1 tfidf 3 sources" "$OUT/T1_tfidf_3src" \
    "$PY" "$S/prepare_text_features.py" "${COMMON[@]}" \
      --cache "${CACHE%.parquet}_3src.parquet" --mode tfidf --require-text \
      --text-cols "consult:consult_tekst,uitgaandebrief:inhoud,radiologie_verslag:verslagtekst" \
      --svd-components "$SVD" --out-dir "$OUT/T1_tfidf_3src"
  step "t1 tfidf + demographics" "$OUT/T1_tfidf_demo" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --svd-components "$SVD" --add-baseline-cols "$DEMOG" --out-dir "$OUT/T1_tfidf_demo"
fi

# ---- t2: clinical concepts. READ THE PREVALENCE TABLE FIRST: a concept that fires
#          for 40 patients and one that fires for 8,000 both give C ~ 0.5.
if want t2; then
  step "t2 concepts (binary)" "$OUT/T2_concepts" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode concepts --require-text \
      --screen-features --out-dir "$OUT/T2_concepts"
  step "t2 concepts (counts too)" "$OUT/T2_concepts_both" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode concepts --require-text \
      --concept-encoding both --out-dir "$OUT/T2_concepts_both"
  step "t2 concepts + demographics" "$OUT/T2_concepts_demo" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode concepts --require-text \
      --add-baseline-cols "$DEMOG" --screen-features --out-dir "$OUT/T2_concepts_demo"
  step "t2 concepts history sections" "$OUT/T2_concepts_history" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode concepts --require-text \
      --section "voorgeschiedenis,anamnese" --out-dir "$OUT/T2_concepts_history"
  # The earlier, conflated term lists: measurement terms such as egfr and cholesterol fire
  # on NORMAL values, so this arm measures "a quantity was reported" rather than "disease is
  # present". Kept only to compare against the corrected default.
  step "t2 concepts all-tiers (conflated)" "$OUT/T2_concepts_alltiers" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode concepts --require-text \
      --concept-terms "disease,symptom,measurement,medication,procedure" \
      --screen-features --out-dir "$OUT/T2_concepts_alltiers"
fi

# ---- incr: does text add anything ON TOP OF the complete curated baseline? This is the
#            question that matters in practice -- the curated variables already exist, so
#            the only interesting increment is over all 183 of them, not over age and sex.
if want incr; then
  step "incr concepts + FULL baseline" "$OUT/INCR_concepts_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode concepts --require-text \
      --add-baseline-cols all --screen-features --out-dir "$OUT/INCR_concepts_full"
  step "incr tfidf + FULL baseline" "$OUT/INCR_tfidf_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode tfidf --require-text \
      --svd-components "$SVD" --add-baseline-cols all --out-dir "$OUT/INCR_tfidf_full"
  step "incr volume + FULL baseline" "$OUT/INCR_volume_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode volume --require-text \
      --add-baseline-cols all --out-dir "$OUT/INCR_volume_full"
fi

# ---- ctrl: the denominators. A --require-text arm sits on a different cohort, so
#            full-cohort benchmarks do NOT apply to it. These are cohort-identical.
if want ctrl; then
  step "ctrl demographics (subcohort)" "$OUT/CTRL_demo_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline \
      --baseline-cols "$DEMOG" --require-text --out-dir "$OUT/CTRL_demo_rt"
  step "ctrl full baseline (subcohort)" "$OUT/CTRL_full_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline \
      --baseline-cols all --require-text --out-dir "$OUT/CTRL_full_rt"
  step "ctrl demographics (full cohort)" "$OUT/CTRL_demo_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline \
      --baseline-cols "$DEMOG" --out-dir "$OUT/CTRL_demo_full"
  step "ctrl full baseline (full cohort)" "$OUT/CTRL_full_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline \
      --baseline-cols all --out-dir "$OUT/CTRL_full_full"
fi

# ---- sens: ok.OMSCHR is the OPERATION description, and its median row is +98 days, so it
#            is mostly post-baseline treatment. Legitimate at a day-180 prediction point,
#            but this arm quantifies how much of the structured result depends on it.
if want sens; then
  step "sens structured without ok.OMSCHR" "$OUT/SENS_no_omschr" \
    "$PY" "$S/prepare_pivoted_event_features.py" "${COMMON[@]}" --auto-occurrence \
      --occurrence-pivot "med:med_ZIatc:4,dbc:Diagnose,diag:diag_omschrijving" \
      --add-baseline-cols "$DEMOG" --out-dir "$OUT/SENS_no_omschr"
fi

# ---- joincheck: is the event data joined to the right patients? No text, no extraction,
#      no outcome. Weight, height, BMI, creatinine and cholesterol are measured BOTH in the
#      routine EHR and at the study visit, so per-patient agreement between the two tests
#      the identifier join directly. Run this whenever a text or event arm reads null: it
#      distinguishes "no signal" from "wrong patients", and it is seconds of CPU.
if want joincheck; then
  step "join check: events vs registry" "-" \
    "$PY" "$S/validate_event_join.py" --smart-csv "$SMART" \
      --event-csv-folder "$EVENTS" --landmark-days "$LANDMARK" --results-file "$RESULTS"
fi

# ---- graded: the response to the headroom check. T1/T2 encoded PRESENCE; the headroom
#      check showed every carrier of the chart-derivable half is GRADED or DATED
#      (stenACIl 0.6471 percent stenosis, KliMa* 0.5976-0.6313 dated onset, packyrs 0.6182
#      pack-years, mht_alln 0.5732 count of drug classes). So these arms extract quantities
#      and dates on the registry's own scales. CPU-only; run before any GPU work.
#
#      READ THE VALIDATION TABLE FIRST. `--validate-baseline` compares each extracted
#      quantity against the curated variable measuring the same thing, on train patients,
#      with the outcome never consulted. If agreement is near zero, a null survival result
#      is about the extractor and says nothing about the text -- and that table is also
#      what settles the Dutch severity-word mapping in ASSUMPTIONS.md #4.
if want graded; then
  MEDLEX="${MEDLEX:-$OUT/med_lexicon.json}"
  # --date-mode strip is PRIMARY. The 2026-09-07 run tried `year` first, on the theory
  # that full stripping destroys "CABG op 12-05-2003"; validation showed the opposite --
  # converting dates to years turned every letterhead date into a candidate onset year and
  # dragged the extracted median to 2009, where KliMaYr is the FIRST event years earlier
  # (rho -0.028). Onset now also demands a history cue ("in 2003", "sinds 1998"), which a
  # converted date never has, so `year` buys nothing and costs specificity.
  step "graded quantities (+validation)" "$OUT/GRADED_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode graded --require-text \
      --date-mode strip --med-lexicon "$MEDLEX" --validate-baseline --screen-features \
      --out-dir "$OUT/GRADED_rt"
  step "graded, dates kept as years (era sensitivity)" "$OUT/GRADED_year_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode graded --require-text \
      --date-mode year --med-lexicon "$MEDLEX" --validate-baseline \
      --out-dir "$OUT/GRADED_year_rt"
  step "graded + demographics" "$OUT/GRADED_demo_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode graded --require-text \
      --date-mode strip --med-lexicon "$MEDLEX" --add-baseline-cols "$DEMOG" \
      --out-dir "$OUT/GRADED_demo_rt"
  # every text feature we can build, against the 0.7310 chart-derivable ceiling
  step "graded + concepts + demographics" "$OUT/GRADED_all_demo_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode graded --require-text \
      --date-mode strip --med-lexicon "$MEDLEX" --with-concepts \
      --add-baseline-cols "$DEMOG" --out-dir "$OUT/GRADED_all_demo_rt"
  # incremental value over everything already collected
  step "graded + FULL curated baseline" "$OUT/GRADED_full_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode graded --require-text \
      --date-mode strip --med-lexicon "$MEDLEX" --add-baseline-cols all \
      --out-dir "$OUT/GRADED_full_rt"
fi

# ---- t3headroom: T3-0, the headroom check. NO GPU. Run before any embedding work.
#      Asks what the CURATED variables achieve when restricted to facts our narrative
#      corpus could plausibly contain — which bounds what ANY text method could reach.
#      Two arms can end the free-text arm with a mechanism instead of a fourth null:
#      if the chart-derivable half cannot beat demographics (0.6727 on this subcohort),
#      then the ceiling for text is demographics and no model changes that.
#
#      The split is by curated-variable PROVENANCE, written out by name in
#      feature_matrix.py and reviewable with:
#        python scripts/smartehr/prepare_text_features.py --smart-csv $SMART \
#          --event-csv-folder $EVENTS --split-json $SPLITS --list-baseline-groups
#      Read that before believing these numbers. Prefix rules were tried first and got
#      the 44 medication flags and the KliMa* onset block on the wrong side, both of
#      which shrink the chart half and bias the check toward the expected answer.
#
#      Age and sex are in NEITHER half (they are the floor both are measured against),
#      so each half also gets a +demographics arm — that is the like-for-like comparator
#      for the text arms, which all include demographics.
if want t3headroom; then
  step "t3-0 chart-derivable (generous: +imaging reports)" "$OUT/HR_chart_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline --require-text \
      --baseline-cols "group:chart" --out-dir "$OUT/HR_chart_rt"
  step "t3-0 chart-derivable + demographics" "$OUT/HR_chart_demo_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline --require-text \
      --baseline-cols "group:chart,leeftijd,geslacht" --out-dir "$OUT/HR_chart_demo_rt"
  step "t3-0 chart-derivable STRICT (no imaging)" "$OUT/HR_chartstrict_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline --require-text \
      --baseline-cols "group:chart_strict" --out-dir "$OUT/HR_chartstrict_rt"
  step "t3-0 protocol-measured only" "$OUT/HR_protocol_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline --require-text \
      --baseline-cols "group:protocol" --out-dir "$OUT/HR_protocol_rt"
  step "t3-0 protocol-measured + demographics" "$OUT/HR_protocol_demo_rt" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline --require-text \
      --baseline-cols "group:protocol,leeftijd,geslacht" --out-dir "$OUT/HR_protocol_demo_rt"
  # Same split on the FULL cohort, so the pair is comparable to the 0.7576 reference too.
  step "t3-0 chart-derivable (full cohort)" "$OUT/HR_chart_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline \
      --baseline-cols "group:chart" --out-dir "$OUT/HR_chart_full"
  step "t3-0 protocol-measured (full cohort)" "$OUT/HR_protocol_full" \
    "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode baseline \
      --baseline-cols "group:protocol" --out-dir "$OUT/HR_protocol_full"
fi

# ---- struct: re-confirm the plumbing once per session. If the curated baseline does
#              not reach ~0.755 here, no null from any arm is interpretable.
if want struct; then
  step "struct positive control" "$OUT/STRUCT_ctrl" \
    "$PY" "$S/prepare_pivoted_event_features.py" "${COMMON[@]}" \
      --positive-control --baseline-cols all --out-dir "$OUT/STRUCT_ctrl"
fi

# ---- screens: the number that actually answers the question -----------------
if want screens; then
  for d in "$OUT"/*/; do
    [ -f "$d/train.parquet" ] || continue
    n=$(basename "$d")
    step "screen $n" "-" \
      "$PY" "$S/screen_parquet_features.py" --parquet-dir "$d" --cox --l1-ratio 1.0 \
        --top 20 --results-file "$RESULTS"
  done
fi

# ---- t3: frozen LLM embeddings. GATED: only worth running if t1 or t2 showed
#          something, since a null LLM arm on top of two nulls adds no information.
if want t3; then
  if [ -z "${RUN_T3:-}" ]; then
    echo "== t3 skipped: set RUN_T3=1 (needs a GPU and 'pip install sentence-transformers')."
    echo "   Gate 1: only escalate if t1 or t2 cleared its floor or beat the matched control."
  else
    step "t3 documents" "$OUT/T3_docs" \
      "$PY" "$S/prepare_text_features.py" "${TEXT[@]}" --mode documents --require-text \
        --out-dir "$OUT/T3_docs"
    step "t3 embeddings" "-" \
      "$PY" "$S/extract_qwen_embeddings_longitudinal.py" --parquet-dir "$OUT/T3_docs" \
        --out-dir "$OUT/T3_emb" --model-name Qwen/Qwen3-Embedding-0.6B \
        --dtype float16 --device cuda --max-tokens-per-block 512
    step "screen t3" "-" \
      "$PY" "$S/screen_parquet_features.py" --parquet-dir "$OUT/T3_emb" --cox \
        --l1-ratio 1.0 --results-file "$RESULTS"
  fi
fi

# ---- summary ----------------------------------------------------------------
echo; echo "=============================================================="
echo "== phases: ${PHASES[*]}"
echo "== ran ${#RAN[@]}, skipped ${#SKIPPED[@]} (already present), failed ${#FAILED[@]}"
[ ${#FAILED[@]} -gt 0 ] && printf '   FAILED: %s\n' "${FAILED[*]}"
echo "=============================================================="
echo "Request ONE download: $RESULTS"
echo "Its ## Index section at the top summarises every run."
[ ${#FAILED[@]} -gt 0 ] && exit 1 || exit 0
