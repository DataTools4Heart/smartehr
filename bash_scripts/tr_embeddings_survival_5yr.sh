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
#   # ...or, if you don't have the sequence embeddings, extract straight to pooled:
#   ...extract... --pool --out-dir <EMB_pool>
#   python scripts/train_lightning_model.py \
#       dataset=smartehr_embeddings dataset.root_path=<EMB_pool> \
#       model=mlp model.input_size=2048 model.num_nodes='[128,128]' model.dropout=0.5 \
#       training=lightning_survival_5yr training.precision=32 training.weight_decay=1e-2 \
#       training.lr=1e-3 "training.devices=[0]"   # input_size = 2 * embedding_dim (0.6B -> 2048)
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
