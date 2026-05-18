python scripts/train_lightning_model.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_tr_longformer/ \
    model=temporal_recurrent_lm \
    model.lm_name=yikuan8/Clinical-Longformer\
    model.lm_batch_size=1 \
    model.is_encoder=true \
    model.max_tokens=2048 \
    model.max_seq_length=10 \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=1 \
    training.accumulation_steps=128 \
    training.devices=[3,4] \
    training.num_workers=0 \
    training.lr=2e-5 \
    training.epochs=30