import init
import pandas as pd
from pathlib import Path
from datasets import load_dataset
from dataset_utils.mimic import preprocess_note
from dataset_utils.mimic_los import convert_numeric_to_str, save_datasets
from tokenizer_utils.word_tokenizer import load_tokenizers, load_tann_tokenizer
from transformers import AutoTokenizer, AutoModel
import argparse
import torch


feature_explanations = {
    # Admission Features
    "admission_location": "The specific location from which a patient was admitted to the hospital. This could be 'EMERGENCY ROOM' (implying an urgent/emergency case), 'PROCEDURE SITE' (indicating admission from a procedure location), or various other locations that represent the entry point of the patient into the hospital system.",

    "admission_type": "The classification of the admission based on urgency and planning. 'EW EMER.' indicates emergency admission through the emergency ward. Other possible values include 'ELECTIVE' (planned admission), 'URGENT' (required prompt attention but not an emergency), and 'OBSERVATION' (for monitoring without formally admitting).",

    # Care Unit Features
    "first_careunit": "The initial care unit where the patient was placed upon hospital admission. Examples include 'Coronary Care Unit (CCU)', 'Medical/Surgical Intensive Care Unit (MICU/SICU)', and 'Medical Intensive Care Unit (MICU)'. This indicates the initial assessment of the patient's critical care needs.",

    "last_careunit": "The final care unit where the patient was treated before discharge or the current sampling point. This may differ from the first care unit if the patient's condition changed during their stay, requiring transfer to a unit with different capabilities.",

    # Clinical Note
    "text": "The comprehensive clinical notes written by healthcare providers during the patient's stay. These notes contain detailed observations, assessments, treatment plans, medication information, and other critical information documented by physicians, nurses, and other clinical staff. These text entries provide rich contextual information about the patient's condition and care progression.",

    # Demographics
    "anchor_age": "The patient's age (in years) at the time of hospital admission. This is a critical demographic factor that influences diagnosis, treatment approaches, and risk assessment. Age is a strong predictor of health outcomes and length of stay.",

    "gender": "The patient's biological sex, typically recorded as 'M' for male or 'F' for female. Gender is an important demographic factor as many diseases have different prevalence rates, presentations, and treatment responses based on biological sex.",

    # Diagnoses
    "diagnosis_1": "The primary diagnosis code (typically ICD-9 or ICD-10) assigned to the patient's condition. This represents the main reason for the patient's admission or the condition requiring the most resources during the stay. For example, code '41011' may represent an acute myocardial infarction.",

    "diagnosis_2": "The secondary diagnosis code assigned to the patient, representing a significant comorbidity or complication. This diagnosis is considered clinically relevant but not the primary reason for admission. For example, code '486' may represent pneumonia.",

    # Laboratory Values
    "Anion Gap": "The difference between the primary measured cations (sodium, potassium) and the primary measured anions (chloride, bicarbonate) in the blood. Normal range is typically 8-16 mEq/L. Elevated levels may indicate metabolic acidosis, while decreased levels may indicate metabolic alkalosis or other electrolyte disorders.",

    "Bicarbonate": "The measurement of bicarbonate (HCO3-) in the blood, which is a critical component of the body's acid-base buffering system. Normal range is typically 22-28 mEq/L. Abnormal levels may indicate acid-base imbalances, kidney dysfunction, or respiratory disorders.",

    "Chloride": "An essential electrolyte that helps maintain fluid balance and is crucial for nerve and muscle function. Normal range is typically 96-106 mEq/L. Abnormal levels may indicate dehydration, kidney disease, acid-base imbalances, or other conditions.",

    "Creatinine": "A waste product from normal muscle breakdown that is filtered by the kidneys. Normal range is typically 0.6-1.2 mg/dL for men and 0.5-1.1 mg/dL for women. Elevated levels indicate decreased kidney function, potentially due to acute kidney injury or chronic kidney disease.",

    "Glucose": "Blood sugar level, representing the amount of glucose circulating in the bloodstream. Normal fasting range is typically 70-100 mg/dL. Elevated levels may indicate diabetes, stress response, or medication effects, while low levels may indicate hypoglycemia.",

    "Hematocrit": "The percentage of total blood volume that consists of red blood cells. Normal range is typically 41-50% for men and 36-44% for women. Abnormal values may indicate anemia, polycythemia, dehydration, or blood loss.",

    "Hemoglobin": "The protein in red blood cells that carries oxygen throughout the body. Normal range is typically 13.5-17.5 g/dL for men and 12.0-15.5 g/dL for women. Abnormal levels may indicate various types of anemia, blood disorders, or blood loss.",

    "MCH": "Mean Corpuscular Hemoglobin, the average amount of hemoglobin per red blood cell. Normal range is typically 27-33 picograms. Abnormal values may help classify types of anemia and blood disorders.",

    "MCHC": "Mean Corpuscular Hemoglobin Concentration, the average concentration of hemoglobin in a given volume of red blood cells. Normal range is typically 32-36 g/dL. Abnormal values assist in diagnosing and classifying different types of anemia.",

    "MCV": "Mean Corpuscular Volume, the average size of red blood cells. Normal range is typically 80-100 femtoliters. Increased values (macrocytosis) or decreased values (microcytosis) help classify different types of anemia and blood disorders.",

    "Magnesium": "An essential mineral that plays a role in over 300 enzyme reactions in the body. Normal range is typically 1.7-2.2 mg/dL. Abnormal levels may affect heart rhythm, muscle function, and neurological function.",

    "Platelet Count": "The number of platelets in the blood, which are essential for blood clotting. Normal range is typically 150,000-450,000 per microliter. Low counts (thrombocytopenia) increase bleeding risk, while high counts (thrombocytosis) may increase clotting risk.",

    "Potassium": "A critical electrolyte that regulates heart function, muscle contractions, and fluid balance. Normal range is typically 3.5-5.0 mEq/L. Abnormal levels can cause serious, sometimes life-threatening, cardiac arrhythmias and muscle dysfunction.",

    "RDW": "Red Cell Distribution Width, a measure of the variation in red blood cell size. Normal range is typically 11.5-14.5%. Elevated values indicate greater variation in cell size, which may suggest certain types of anemia or other conditions.",

    "Red Blood Cells": "The count of red blood cells per volume of blood. Normal range is typically 4.5-5.9 million cells/microliter for men and 4.1-5.1 million cells/microliter for women. Abnormal counts may indicate anemia, polycythemia, or other conditions.",

    "Sodium": "The main electrolyte in the extracellular fluid, crucial for maintaining fluid balance and nerve/muscle function. Normal range is typically 135-145 mEq/L. Abnormal levels can lead to neurological symptoms, seizures, and other serious complications.",

    "Urea Nitrogen": "Blood Urea Nitrogen (BUN) measures the amount of urea nitrogen in the blood. Normal range is typically 7-20 mg/dL. Elevated levels may indicate kidney dysfunction, dehydration, or increased protein catabolism.",

    "White Blood Cells": "The count of white blood cells, which are critical components of the immune system. Normal range is typically 4,500-11,000 cells/microliter. Elevated counts may indicate infection, inflammation, or certain blood disorders, while decreased counts may indicate immune suppression.",

    # Vital Signs
    "glc_eye": "Glasgow Coma Scale (GCS) Eye Response component. Scored from 1-4, with higher scores indicating better eye-opening response. This is part of the overall neurological assessment that evaluates consciousness level.",

    "glc_motor": "Glasgow Coma Scale (GCS) Motor Response component. Scored from 1-6, with higher scores indicating better motor responses to stimuli. This is a critical component for assessing neurological function and brain injury severity.",

    "glc_verbal": "Glasgow Coma Scale (GCS) Verbal Response component. Scored from 1-5, with higher scores indicating more appropriate verbal responses. This evaluates a patient's ability to communicate and orient verbally.",

    "heart_rate": "The number of heartbeats per minute. Normal resting range is typically 60-100 beats per minute. Abnormal rates (tachycardia or bradycardia) may indicate cardiac conditions, shock, medication effects, or other physiological stressors.",

    "respiration": "Respiratory rate, measured as breaths per minute. Normal adult range is typically 12-20 breaths per minute. Abnormal rates may indicate respiratory distress, metabolic disorders, neurological issues, or pain.",

    "saturation": "Oxygen saturation level, typically measured via pulse oximetry (SpO2). Normal is generally 95-100%. Lower levels indicate hypoxemia, which may result from respiratory or cardiac conditions, and may necessitate supplemental oxygen.",

    "temperature": "Body temperature, typically measured in degrees Fahrenheit or Celsius. Normal range is approximately 97.8-99.1°F (36.5-37.3°C). Abnormal values may indicate infection (fever), hypothermia, or other conditions affecting thermoregulation."
} 

def preprocess_mimic_los_for_wlstm(sample, tokenizers):
    for time_point in sample["features"]:
        for feature_type in time_point:
            value_list = []
            for feature_name, feature_value in time_point[feature_type].items():
                if feature_name == "text":
                    value = preprocess_note(feature_value)
                    value = tokenizers[feature_type].encode(value)
                    value_list.append(value)
                else:
                    if pd.notna(feature_value):
                        value = convert_numeric_to_str(feature_value)
                        value = preprocess_note(f"{feature_name} {value}")
                        value = tokenizers[feature_type].encode(value)
                        value_list.append(value)
            time_point[feature_type] = value_list
    return sample


def preprocess_mimic_los_for_tann(sample, tokenizer):
    for time_point in sample["features"]:
        for feature_type in time_point:
            ids = []
            for feature_name, feature_value in time_point[feature_type].items():
                if feature_name == "text":
                    value = preprocess_note(feature_value)
                    value = tokenizer.encode(value)
                    ids.extend(value)
                else:
                    if pd.notna(feature_value):
                        value = convert_numeric_to_str(feature_value)
                        value = preprocess_note(f"{feature_name} {value}")
                        value = tokenizer.encode(value)
                        ids.extend(value)
            time_point[feature_type] = ids
    return sample


def preprocess_mimic_los_for_clinical_longformer(batch, tokenizer):
    texts, outcomes = [], []
    for batch_item, batch_item_outcome in zip(batch["features"], batch["outcomes"]):
        last_time_point = batch_item[-1]
        for feature_type in last_time_point:
            for feature_name, feature_value in last_time_point[feature_type].items():
                if feature_name == "text":
                    text = preprocess_note(feature_value)
                    texts.append(text)

        outcomes.append(batch_item_outcome["los"][0])
    tokenized_texts = tokenizer(texts, truncation=False)
    return {"input_ids": tokenized_texts["input_ids"], "labels": outcomes}


def preprocess_mimic_los_for_tr_lm(batch, tokenizer):
    input_ids_list = []
    time_deltas_list = []
    outcomes = []
    all_texts = []
    sequence_lengths = []
    for batch_item, batch_item_time_delta, batch_item_outcome in zip(batch["features"], batch["time_deltas"], batch["outcomes"]):
        seq_len = 0
        for time_point in batch_item:
            for feature_type in time_point:
                for feature_name, feature_value in time_point[feature_type].items():
                    if feature_name == "text":
                        all_texts.append(feature_value)
                        seq_len += 1
        sequence_lengths.append(seq_len)
        time_deltas_list.append(batch_item_time_delta)
        outcomes.append(batch_item_outcome["los"][0])

    all_ids = tokenizer(all_texts, truncation=False, padding=False)["input_ids"]
    start_idx = 0
    for seq_len in sequence_lengths:
        input_ids_list.append(all_ids[start_idx : start_idx + seq_len])
        start_idx += seq_len
    return {"input_ids_list": input_ids_list, "time_deltas_list": time_deltas_list, "labels": outcomes}


def preprocess_mimic_los_for_mlp(batch):
    inputs = []
    labels = []
    for features, outcomes in zip(batch["features"], batch["outcomes"]):
        features = features[-1]
        values = []
        for feature_type in features:
            for feature_name in features[feature_type]:
                value = features[feature_type][feature_name]
                if not isinstance(value, str):
                    values.append(value)
        inputs.append(values)
        labels.append(outcomes["los"][0])
    return {
        "inputs": inputs,
        "labels": labels,
    }


def preprocess_mimic_los_for_tr_embedding(batch, embedder, jina_task):
    all_texts = []
    sequence_lengths = []
    time_deltas_list = []
    outcomes = []
    embeddings = []
    for batch_item, batch_item_time_delta, batch_item_outcome in zip(batch["features"], batch["time_deltas"], batch["outcomes"]):
        seq_len = 0
        for time_point in batch_item:
            for feature_type in time_point:
                for feature_name, feature_value in time_point[feature_type].items():
                    if feature_name == "text":
                        all_texts.append(feature_value)
                        seq_len += 1
        sequence_lengths.append(seq_len)
        time_deltas_list.append(batch_item_time_delta)
        outcomes.append(batch_item_outcome["los"][0])
    with torch.no_grad():
        all_embeddings = embedder.encode(all_texts, task=jina_task)
    start_idx = 0
    for seq_len in sequence_lengths:
        embeddings.append(all_embeddings[start_idx : start_idx + seq_len])
        start_idx += seq_len
    return {"embeddings": embeddings, "time_deltas_list": time_deltas_list, "labels": outcomes}


def preprocess_mimic_los_for_llm(batch, tokenizer, **llm_prompt_format):
    input_ids_list = []
    attention_mask_list = []
    time_deltas_list = []
    outcomes = []
    all_texts = []
    sequence_lengths = []
    time_deltas_description = "These are the time deltas, they describe the time (in days) with the last time point as reference: "
    
    for batch_item, batch_item_time_delta, batch_item_outcome in zip(batch["features"], batch["time_deltas"], batch["outcomes"]):
        seq_len = 0
        batch_item_text = ""
        for i, time_point in enumerate(batch_item):
            for feature_type in time_point:
                for feature_name, feature_value in time_point[feature_type].items():
                    if llm_prompt_format["truncate_decimals"]:
                        if isinstance(feature_value, float):
                            feature_value = round(feature_value, llm_prompt_format["truncate_decimals"])
                    if llm_prompt_format["feature_explanations"]:
                        feature_explanation = feature_explanations[feature_name]
                        batch_item_text += f"{feature_explanation}\n"
                    if llm_prompt_format["style"] == "separate_features":
                        batch_item_text += f"{feature_name.upper()}: {feature_value}\n"
                    else:
                        batch_item_text += f"{feature_name}: {feature_value}\n"
                    seq_len += 1
        time_delta_text = time_deltas_description+"\n" if llm_prompt_format["explain_time_deltas"] else ""
        batch_item_text += f"{time_delta_text}Time delta: {batch_item_time_delta}\n"


        sequence_lengths.append(seq_len)
        time_deltas_list.append(batch_item_time_delta)
        outcomes.append(batch_item_outcome["los"][0])
        all_texts.append(batch_item_text)
    tokenized_texts = tokenizer(all_texts, truncation=False)
    #breakpoint()
    start_idx = 0
    return {"input_ids": tokenized_texts["input_ids"], "time_deltas_list": time_deltas_list, "labels": outcomes}


def preprocess_mimic_los(model: str, data_path: str, out_path: str, vocabs_path: str, device_id: int | None, jina_task: str, llm_prompt_format: dict):
    datasets = load_dataset(data_path)

    if model == "weighted_lstm":
        tokenizers = load_tokenizers(Path(vocabs_path))
        for split in datasets.keys():
            datasets[split] = datasets[split].map(lambda x: preprocess_mimic_los_for_wlstm(x, tokenizers))
    elif model == "tann":
        tokenizer = load_tann_tokenizer(Path(vocabs_path))
        for split in datasets.keys():
            datasets[split] = datasets[split].map(lambda x: preprocess_mimic_los_for_tann(x, tokenizer))
    elif model == "mlp":
        for split in datasets.keys():
            datasets[split] = datasets[split].map(
                lambda x: preprocess_mimic_los_for_mlp(x), batched=True, remove_columns=datasets[split].column_names
            )
    elif model == "clinical_longformer":
        tokenizer = AutoTokenizer.from_pretrained("yikuan8/Clinical-Longformer")
        for split in datasets.keys():
            datasets[split] = datasets[split].map(
                lambda x: preprocess_mimic_los_for_clinical_longformer(x, tokenizer),
                batched=True,
                remove_columns=datasets[split].column_names,
            )
    elif model == "temporal_recurrent_lm":
        tokenizer = AutoTokenizer.from_pretrained(args.vocabs_path)
        for split in datasets.keys():
            datasets[split] = datasets[split].map(
                lambda x: preprocess_mimic_los_for_tr_lm(x, tokenizer), batched=True, remove_columns=datasets[split].column_names
            )
    elif model == "temporal_recurrent_embedding":
        if device_id is None:
            raise ValueError("Device must be specified for temporal_recurrent_embedding model")
        assert jina_task is not None, "Jina task must be specified for temporal_recurrent_embedding model"
        embedder = AutoModel.from_pretrained("jinaai/jina-embeddings-v3", trust_remote_code=True).to(f"cuda:{device_id}")
        for split in datasets.keys():
            datasets[split] = datasets[split].map(
                lambda x: preprocess_mimic_los_for_tr_embedding(x, embedder, jina_task),
                batched=True,
                remove_columns=datasets[split].column_names,
            )
    elif model == "llm":
        tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
        tokenizer.pad_token = tokenizer.eos_token
        for split in datasets.keys():
            datasets[split] = datasets[split].map(
                lambda x: preprocess_mimic_los_for_llm(x, tokenizer, **llm_prompt_format), batched=True, remove_columns=datasets[split].column_names
            )
    else:
        raise ValueError(f"Invalid model: {model}")
    save_datasets(out_path, datasets)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        choices=["weighted_lstm", "tann", "clinical_longformer", "temporal_recurrent_llm", "temporal_recurrent_embedding", "llm"],
        help="The model to preprocess for",
    )
    parser.add_argument("--data_path", type=str, required=True, help="The path to the longitudinal MIMIC LoS dataset")
    parser.add_argument("--out_path", type=str, required=True, help="The path to save the preprocessed dataset")
    parser.add_argument(
        "--vocabs_path",
        type=str,
        required=False,
        help="The path to the tokenizer(s) vocabolary or tokenizer path. Required for weighted_lstm, tann, and temporal_recurrent_llm models.",
    )
    parser.add_argument(
        "--jina_task",
        type=str,
        required=False,
        default="separation",
        help="The Jina task to use for the embedding model. Required for temporal_recurrent_embedding model.",
    )
    parser.add_argument(
        "--device_id",
        type=int,
        required=False,
        default=None,
        help="The device id to use for the embedding model. Required for temporal_recurrent_embedding model.",
    )
    parser.add_argument(
        "--style",
        type=str,
        required=False,
        default="default",
    )
    parser.add_argument(
        "--truncate_decimals",
        type=int,
        required=False,
        default=2,
    )
    parser.add_argument(
        "--explain_time_deltas",
        type=bool,
        required=False,
        default=True,
    )
    parser.add_argument(
        "--feature_explanations",
        type=str,
        required=False,
        default=None,
    )
    args = parser.parse_args()
    llm_prompt_format = {
        "style": args.style,
        "truncate_decimals": args.truncate_decimals,
        "explain_time_deltas": args.explain_time_deltas,
        "feature_explanations": args.feature_explanations,
    }
    preprocess_mimic_los(args.model, args.data_path, args.out_path, args.vocabs_path, args.device_id, args.jina_task, llm_prompt_format)


