python scripts/train_lightning_model.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_tr_mlp/ \
    model=temporal_recurrent_mlp \
    model.input_size=33 \
    model.num_nodes=[512,512,512,512] \
    model.dropout=0.3 \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=256 \
    training.accumulation_steps=1 \
    training.devices=[3] \
    training.num_workers=0 \
    training.lr=2e-4