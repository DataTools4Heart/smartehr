#!/usr/bin/env bash
# Train a small MLP survival head on offline frozen-LLM patient embeddings.
#
# Two-step pipeline:
#   1. python scripts/smartehr/extract_llm_embeddings.py \
#          --parquet-dir <output of preprocess_smartehr_survival.py> \
#          --out-dir data/dummy_data/longitudinal_dummy_smart_survival_embeddings
#      -> prints the embedding dim; set model.input_size below to match.
#   2. This script trains the MLP head on those embeddings (cheap — no LLM forward pass).
python scripts/train_lightning_model.py \
    dataset=smartehr_embeddings \
    model=mlp \
    model.input_size=2048 \
    model.num_nodes=[256,256] \
    model.dropout=0.2 \
    training=lightning_survival_10yr \
    training.batch_size=256 \
    training.accumulation_steps=1 \
    "training.devices=[0]" \
    training.num_workers=0 \
    training.lr=1e-3 \
    training.patience=10
