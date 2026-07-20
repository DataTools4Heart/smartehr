#!/usr/bin/env bash
# Longitudinal multimodal SMART survival — 5-year horizon.
# Sequence of per-time-point Qwen3-Embedding vectors -> time-aware LSTM -> PMF head.
#
# Prereqs (run once, on a machine with the encoder installed):
#   pip install -U sentence-transformers "transformers>=4.51"   # Qwen3 arch support
#
# Stage 1 — build per-time-point text sequences from the longitudinal JSONL:
#   python scripts/smartehr/preprocess_smartehr_longitudinal_survival.py \
#       --jsonl-dir data/dummy_data/longitudinal_smartehr_0_36500 \
#       --out-dir   data/dummy_data/longitudinal_dummy_smart_survival_longitudinal \
#       --horizon-days 1825
#
# Stage 2 — encode each time point with frozen Qwen3-Embedding-4B (Tesla T4 = fp16, NOT bf16):
#   python scripts/smartehr/extract_qwen_embeddings_longitudinal.py \
#       --parquet-dir data/dummy_data/longitudinal_dummy_smart_survival_longitudinal \
#       --out-dir     data/dummy_data/longitudinal_dummy_smart_survival_longitudinal_embeddings \
#       --model-name  Qwen/Qwen3-Embedding-4B \
#       --dtype float16 --device cuda --encode-batch-size 16
#   # (Tip: smoke-test the pipeline first with --model-name sentence-transformers/all-MiniLM-L6-v2
#   #  and set model.embedding_dim to that model's dim, e.g. 384.)
#
# Stage 3 — train the LSTM survival head over the cached embeddings.
# precision=32: the LSTM is tiny; fp32 avoids recurrent-step instability and keeps nll_pmf stable.
# (The default bf16-true is unsupported on a T4.)
python scripts/train_lightning_model.py \
    dataset=smartehr_longitudinal_embeddings_5yr \
    model=temporal_recurrent_embeddings \
    model.embedding_dim=2560 \
    training=lightning_survival_5yr \
    training.precision=32 \
    training.batch_size=32 \
    training.lr=1e-3 \
    "training.devices=[0]" \
    training.patience=10
