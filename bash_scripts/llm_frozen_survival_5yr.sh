#!/usr/bin/env bash
# Train classification head only (frozen LLaMA-3.2-1B backbone) for 5-year survival analysis.
# Optimised for Tesla T4 (16 GB):
#   - Pretrained backbone weights, fully frozen → no activation storage for 1B params
#   - fp16 mixed precision (T4 has native fp16 tensor cores, not bf16)
#   - chunk_size=512: sequences longer than 512 tokens are split into chunks and
#     their last-token embeddings are mean-pooled, so no patient is discarded.
#   - batch_size=8 + accumulation=4 = effective batch 32
python scripts/train_lightning_model.py \
    dataset=smartehr_5yr \
    model=llm_frozen \
    training=lightning_survival_5yr \
    training.precision=16-mixed \
    training.batch_size=8 \
    training.accumulation_steps=4 \
    "training.devices=[0]" \
    training.num_workers=0 \
    training.lr=1e-3 \
    training.patience=10
