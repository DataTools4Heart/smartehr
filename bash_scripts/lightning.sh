

python scripts/train_lightning_model_copy.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_tann/ \
    model=tann \
    model.data_types=all \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=32 \
    training.accumulation_steps=1 \
    training.devices=[3] \
    training.num_workers=0 \
    training.lr=2e-3 

python scripts/train_lightning_model_copy.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_tann/ \
    model=tann \
    model.data_types=structured \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=32 \
    training.accumulation_steps=1 \
    training.devices=[3] \
    training.num_workers=0 \
    training.lr=2e-3 

python scripts/train_lightning_model_copy.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/longitudinal_mimic_los_tann/ \
    model=tann \
    model.data_types=unstructured \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=32 \
    training.accumulation_steps=1 \
    training.devices=[3] \
    training.num_workers=0 \
    training.lr=2e-3 
