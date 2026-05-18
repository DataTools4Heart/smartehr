#!/usr/bin/env bash
# Train classification head only (frozen LLaMA-3.2-1B backbone) on dummy Smart data.
# Optimised for Tesla T4 (16 GB):
#   - Pretrained backbone weights, fully frozen → no activation storage for 1B params
#   - fp16 mixed precision (T4 has native fp16 tensor cores, not bf16)
#   - chunk_size=512: sequences longer than 512 tokens are split into chunks and
#     their last-token embeddings are mean-pooled, so no patient is discarded.
#   - batch_size=8 + accumulation=4 = effective batch 32
python scripts/train_lightning_model.py \
    dataset=longitudinal_dummy_smart \
    dataset.root_path=data/dummy_data/longitudinal_dummy_smart_full \
    model=llm_frozen \
    training=lightning \
    training/task=binary_classification \
    training.precision=16-mixed \
    training.batch_size=8 \
    training.accumulation_steps=4 \
    "training.devices=[0]" \
    training.num_workers=0 \
    training.lr=1e-3 \
    training.epochs=20
