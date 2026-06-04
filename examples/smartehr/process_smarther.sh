
python scripts/smartehr/smartehr_pipeline.py \
  --smart_csv data/dummy_data/smart/smart.csv \
  --event_csv_folder data/dummy_data/smartehr \
  --output_dir data/dummy_data/longitudinal_smartehr_0_36500 \
  --windowed_output_dir data/dummy_data/longitudinal_smartehr_0_36500_windowed \
  --baseline_time 0 \
  --end_of_study 36500
  