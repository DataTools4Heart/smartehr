#!/usr/bin/env bash
# Train a small MLP survival head directly on raw (imputed, standardized) SMART
# baseline features — no LLM involved. Controlled baseline against
# mlp_llm_embeddings_survival.sh and the Cox model, isolating whether routing
# tabular features through an LLM embedding helps, hurts, or is neutral.
#
# Preprocessing step (run once):
#   python scripts/smartehr/prepare_smart_features_for_mlp.py \
#       --jsonl-dir <output of smartehr_pipeline.py> \
#       --out-dir data/dummy_data/longitudinal_dummy_smart_survival_raw_features \
#       --horizon-days 1825
#   -> prints n_features; set model.input_size below to match.
python scripts/train_lightning_model.py \
    dataset=smartehr_raw_features \
    model=mlp \
    model.input_size=30 \
    model.num_nodes=[64,64] \
    model.dropout=0.2 \
    training=lightning_survival_10yr \
    training.batch_size=256 \
    training.accumulation_steps=1 \
    "training.devices=[0]" \
    training.num_workers=0 \
    training.lr=1e-3 \
    training.patience=10
