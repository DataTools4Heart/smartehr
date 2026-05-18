

python scripts/train_lightning_model_copy.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_wlstm/ \
    model=weighted_lstm \
    model.data_types=unstructured \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=256 \
    training.accumulation_steps=1 \
    training.devices=[0] \
    training.num_workers=0 \
    training.lr=2e-3 

