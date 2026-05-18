python scripts/train_lightning_model_copy.py \
    dataset=longitudinal_mimic_los \
    dataset.root_path=data/mimic_los/mimic_los_clinical_longformer/ \
    model=clinical_longformer \
    model.freeze_first_n_layers=0 \
    model.freeze_embeddings=false \
    training=lightning \
    training/task=multiclass_classification \
    training.batch_size=4 \
    training.accumulation_steps=16 \
    training.devices=[2,3,4,5] \
    training.num_workers=0 \
    training.lr=2e-5 \
    training.epochs=60 \
    training.resume_ckpt_path="lightning_logs/clinical_longformer/version_21/checkpoints/epoch\=12-step\=1482.ckpt" \
    training.patience=10
