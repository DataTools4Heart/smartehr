#!/usr/bin/env bash
# Longitudinal multimodal SMART survival — 5-year horizon.
# Sequence of per-time-point Qwen3-Embedding vectors -> time-aware LSTM -> PMF head.
#
# Prereqs (run once, on a machine with the encoder installed):
#   pip install -U sentence-transformers "transformers>=4.51"   # Qwen3 arch support
#
# Stage 1 — build per-time-point text sequences from the longitudinal JSONL.
#   --enrich maps coded field names/values to human-readable text via the data
#   dictionaries in --dict-dir (data_dict/lab/meting/echo/smart.csv), e.g.
#   "vgok_nie: 0.0" -> "Voorgeschiedenis; nier-operatie: Nooit"; this is what lets the
#   LLM encoder use its semantic prior. It also prints a coverage report (how much of
#   your extraction the dictionaries match). Build BOTH (with and without --enrich, to
#   different --out-dir) to run the coded-vs-enriched ablation.
#   python scripts/smartehr/preprocess_smartehr_longitudinal_survival.py \
#       --jsonl-dir data/dummy_data/longitudinal_smartehr_0_36500 \
#       --out-dir   data/dummy_data/longitudinal_dummy_smart_survival_longitudinal \
#       --horizon-days 1825 \
#       --enrich \
#       --dict-dir data/smartehr/data_dicts
#
# Stage 2 — encode with a frozen Qwen3-Embedding model (Tesla T4 = fp16, NOT bf16).
# On a RAM-limited box use the 0.6B model (dim 1024) instead of 4B (dim 2560).
#   python scripts/smartehr/extract_qwen_embeddings_longitudinal.py \
#       --parquet-dir data/dummy_data/longitudinal_dummy_smart_survival_longitudinal \
#       --out-dir     data/dummy_data/longitudinal_dummy_smart_survival_longitudinal_embeddings \
#       --model-name  Qwen/Qwen3-Embedding-0.6B \
#       --dtype float16 --device cuda --encode-batch-size 16
#   # (Tip: smoke-test the pipeline first with --model-name sentence-transformers/all-MiniLM-L6-v2
#   #  and set model.embedding_dim to that model's dim, e.g. 384.)
#
# STEP 0 (recommended first) — SMART baseline only -> MLP. Add --flat to Stage 2 to encode
# ONLY the baseline time point per patient into a flat `inputs` vector, then train the small
# MLP head. Lowest capacity; isolates "does the encoder embedding carry signal" from temporal
# modeling, and is directly comparable to the numeric static baseline (smartehr_raw_features).
#   ...extract... --flat  --out-dir <EMB_flat>
#   python scripts/train_lightning_model.py \
#       dataset=smartehr_embeddings dataset.root_path=<EMB_flat> \
#       model=mlp model.input_size=1024 model.num_nodes='[128,128]' model.dropout=0.5 \
#       training=lightning_survival_5yr training.precision=32 training.weight_decay=1e-2 \
#       training.lr=1e-3 "training.devices=[0]"
#
# DIAGNOSTIC (do this BEFORE the LSTM) — is there signal beyond baseline?
# inputs = concat(baseline, mean(event embeddings)) [dim 2E]. Train the SAME MLP on it and
# compare CI/AUC vs the --flat baseline-only MLP: if pool does NOT beat flat, the events are
# redundant with baseline and no LSTM will help (a valid finding).
#   # REUSE existing sequence embeddings (no re-extraction / no GPU):
#   python scripts/smartehr/pool_embeddings.py --seq-dir <EMB_sequence> --out-dir <EMB_pool> --mode pool
#   #   (pool_embeddings.py also has --mode events/last/max and pool_last/pool_max to test whether
#   #    the event representation carries ANY signal, and recency/max instead of mean.)
#   # ...or, if you don't have the sequence embeddings, extract straight to pooled:
#   ...extract... --pool --out-dir <EMB_pool>
#
# JOINT (whole-history, one embedding) — needs a cheap re-extract (one forward per patient),
# but unlike --pool it lets the encoder integrate ACROSS events (cross-event self-attention).
# Serializes the full history into one chronological document (baseline + time-stamped blocks)
# and encodes it once. Compare vs the --flat baseline-only MLP; --exclude-baseline tests the
# events jointly, without baseline.
#   # Use the ENRICHED <TEXT> build so the encoder can read the fields. Joint docs are long
#   # (whole history + clinical notes) -> OOM. Don't blindly cap --max-seq-length (that right-
#   # truncates the doc and drops recent time points); instead cap EACH block with
#   # --max-tokens-per-block so every time point stays represented (breadth). Total doc length
#   # ~= n_time_points * max-tokens-per-block; add --max-seq-length as a hard backstop.
#   python scripts/smartehr/extract_qwen_embeddings_longitudinal.py \
#       --parquet-dir <TEXT_enriched> --out-dir <EMB_joint> \
#       --model-name Qwen/Qwen3-Embedding-0.6B --dtype float16 --device cuda \
#       --joint --max-tokens-per-block 48 --max-seq-length 4096
#   python scripts/train_lightning_model.py \
#       dataset=smartehr_embeddings dataset.root_path=<EMB_joint> \
#       model=mlp model.input_size=1024 model.num_nodes='[128,128]' model.dropout=0.5 \
#       training=lightning_survival_5yr training.precision=32 training.weight_decay=1e-2 \
#       training.lr=1e-3 "training.devices=[0]"
#   python scripts/train_lightning_model.py \
#       dataset=smartehr_embeddings dataset.root_path=<EMB_pool> \
#       model=mlp model.input_size=2048 model.num_nodes='[128,128]' model.dropout=0.5 \
#       training=lightning_survival_5yr training.precision=32 training.weight_decay=1e-2 \
#       training.lr=1e-3 "training.devices=[0]"   # input_size = 2 * embedding_dim (0.6B -> 2048)
#
# NUMERIC EVENTS (no serialization, no LLM) — aggregate numeric event fields into a fixed
# feature vector and train the MLP. Frozen text embeddings blur numeric magnitude/trend; this
# uses the actual values. Compare vs baseline and vs the embedding-based runs.
#   python scripts/smartehr/prepare_event_numeric_features.py \
#       --jsonl-dir <JSONL> --out-dir <NUM_events> --pivot-codes           # events only
#   #   --include-baseline: baseline+events additivity. --only-baseline: baseline through the
#   #   SAME pipeline (fair comparison target). --pivot-codes: each lab/measurement its own
#   #   feature (real data). aggregators incl. trajectory: last,mean,min,max,count,delta,slope
#   #   (delta/slope capture "is it rising?" — the thing a single baseline snapshot can't).
#
# FREE-TEXT EXPERIMENT (expert-picked sources: radiologie_verslag, ok_verslag, consult;
# last 6 months before baseline). Definitive test of whether these reports predict risk,
# using TWO representations so "no signal" isn't confounded by one bad encoder.
#   # 1. Build a JSONL from ONLY those 3 source CSVs (so only their fields are present):
#   python scripts/smartehr/smartehr_pipeline.py --smart_csv <smart.csv> \
#       --event_csv_folder <folder_with_only_the_3_csvs> --split_json <splits.json> \
#       --output_dir <3SRC_JSONL> --windowed_output_dir <3SRC_JSONL_win> --baseline_time 0 --legacy
#   # 2a. TF-IDF (litmus: signal in the words, no token budget):
#   python scripts/smartehr/prepare_text_tfidf_features.py --jsonl-dir <3SRC_JSONL> \
#       --out-dir <TF_text> --window-days 180                       # text only
#   python scripts/smartehr/prepare_text_tfidf_features.py --jsonl-dir <3SRC_JSONL> \
#       --out-dir <TF_bt> --window-days 180 --include-baseline      # baseline+text
#   #  SVD explained-var is LOW for real text LSA (~0.4 at 256 dims) — normal, not "no signal".
#   #  If val CI keeps rising, raise --svd-components (512/1024); or --svd-components 0 (--no-svd:
#   #  full TF-IDF dense, no compression) with a smaller --max-features (e.g. 5000) if memory tight.
#   # 2b. LLM-embed of the same window (reuses the extractor; --exclude-baseline = events only):
#   python scripts/smartehr/preprocess_smartehr_longitudinal_survival.py --jsonl-dir <3SRC_JSONL> \
#       --out-dir <3SRC_TEXT> --window-days 180 --enrich
#   python scripts/smartehr/extract_qwen_embeddings_longitudinal.py --parquet-dir <3SRC_TEXT> \
#       --out-dir <3SRC_EMB> --model-name Qwen/Qwen3-Embedding-0.6B --dtype float16 --device cuda \
#       --joint --exclude-baseline --max-tokens-per-block 64
#   # 3. Fair baseline (same pipeline): prepare_event_numeric_features --only-baseline.
#   # 4. Train model=mlp on each (model.input_size printed by each builder), then compare with the
#   #    significance test below (baseline vs baseline+text).
#
# SIGNIFICANCE — is the baseline+events improvement real, not noise?
#   # dump per-patient test survival curves from each run's checkpoint:
#   python scripts/predict_survival.py <same dataset/model/training args as the run> \
#       training.resume_ckpt_path=<lightning_logs/.../checkpoints/xxx.ckpt>   # -> *_test_predictions.parquet
#   # bootstrap the concordance difference (95% CI excludes 0 => significant):
#   python scripts/smartehr/bootstrap_ci_compare.py \
#       --pred-a <baseline>_test_predictions.parquet \
#       --pred-b <baseline+events>_test_predictions.parquet --times 12,24,36,48,57
#   python scripts/train_lightning_model.py \
#       dataset=smartehr_embeddings dataset.root_path=<NUM_events> \
#       model=mlp model.input_size=<n_features printed by the script> \
#       model.num_nodes='[128,128]' model.dropout=0.5 \
#       training=lightning_survival_5yr training.precision=32 training.weight_decay=1e-2 \
#       training.lr=1e-3 "training.devices=[0]"
#
# Stage 3 — train the time-aware LSTM head over the cached embedding SEQUENCES.
# precision=32 (T4 has no bf16). If it overfits: keep the small hidden_dim/time_delta_dim
# defaults (model config), raise weight_decay / input_dropout, and/or coarsen the PMF bins
# (training.task.num_time_intervals). Set model.embedding_dim to the encoder dim (0.6B=1024).
python scripts/train_lightning_model.py \
    dataset=smartehr_longitudinal_embeddings_5yr \
    model=temporal_recurrent_embeddings \
    model.embedding_dim=1024 \
    training=lightning_survival_5yr \
    training.precision=32 \
    training.batch_size=32 \
    training.lr=1e-3 \
    training.weight_decay=1e-2 \
    "training.devices=[0]" \
    training.patience=10
