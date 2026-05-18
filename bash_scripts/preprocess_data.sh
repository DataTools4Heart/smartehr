python scripts/preprocess_mimic_los.py \
    --model llm \
    --data_path data/mimic_los/longitudinal_mimic_los_raw \
    --out_path data/mimic_los/longitudinal_mimic_los_llm_gemma \
    --truncate_decimals 1 \
    --vocabs_path google/gemma-3-1b-pt \