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
# Phases: p0 t0 t1 t2 ctrl struct screens t3
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

mkdir -p "$OUT" "$(dirname "$RESULTS")" "$(dirname "$CACHE")"
PHASES=("$@")
[ ${#PHASES[@]} -eq 0 ] && PHASES=(p0 t0 t1 t2 ctrl struct screens)
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
