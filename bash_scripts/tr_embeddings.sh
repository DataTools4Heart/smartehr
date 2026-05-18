python scripts/train_lightning_model_copy.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_tr_jina_class/ \
    model=temporal_recurrent_embeddings \
    model.embedding_dim=1024 \
    model.dropout=0.3 \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=256 \
    training.accumulation_steps=1 \
    training.devices=[2] \
    training.num_workers=0 \
    training.lr=2e-2 \
    training.epochs=200 \
    training.resume_ckpt_path="lightning_logs/temporal_recurrent_embeddings/version_15/checkpoints/epoch\=59-step\=6840.ckpt"