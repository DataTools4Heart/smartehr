python scripts/train_pycox_baseline.py \
    dataset=longitudinal_mimic_los \
    model=pycox \
    model.name=pmf \
    training=pycox \
    training.batch_size=256 \
    training.lr=9e-4 \
    training.device=cuda:1