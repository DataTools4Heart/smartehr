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


def preprocess_mimic_los_for_llm(batch, tokenizer, style="default", truncate_decimals=2):
    input_ids_list = []
    attention_mask_list = []
    time_deltas_list = []
    outcomes = []
    all_texts = []
    sequence_lengths = []
    time_deltas_description = "This are the time deltas, they describe the time (in days) with the last time point as reference: "
    if style == "default":
        for batch_item, batch_item_time_delta, batch_item_outcome in zip(batch["features"], batch["time_deltas"], batch["outcomes"]):
            seq_len = 0
            batch_item_text = ""
            for i, time_point in enumerate(batch_item):
                for feature_type in time_point:
                    for feature_name, feature_value in time_point[feature_type].items():
                        batch_item_text += f"{feature_name}: {feature_value}\n"
                        seq_len += 1
                batch_item_text += f"Time delta: {batch_item_time_delta[i]}\n"
            sequence_lengths.append(seq_len)
            time_deltas_list.append(batch_item_time_delta)
            outcomes.append(batch_item_outcome["los"][0])
            all_texts.append(batch_item_text)
    elif style == "separate_features":
        for batch_item, batch_item_time_delta, batch_item_outcome in zip(batch["features"], batch["time_deltas"], batch["outcomes"]):
            seq_len = 0
            batch_item_text = ""
            for i, time_point in enumerate(batch_item):
                for feature_type in time_point:
                    for feature_name, feature_value in time_point[feature_type].items():
                        if truncate_decimals:
                            if isinstance(feature_value, float):
                                feature_value = round(feature_value, truncate_decimals)
                        batch_item_text += f"{feature_name.upper()}: {feature_value}\n"
                        seq_len += 1


            sequence_lengths.append(seq_len)
            time_deltas_list.append(batch_item_time_delta)
            outcomes.append(batch_item_outcome["los"][0])
            all_texts.append(batch_item_text)
    tokenized_texts = tokenizer(all_texts, truncation=False)
    #breakpoint()
    start_idx = 0
    return {"input_ids": tokenized_texts["input_ids"], "time_deltas_list": time_deltas_list, "labels": outcomes}


def preprocess_mimic_los(model: str, data_path: str, out_path: str, vocabs_path: str, device_id: int | None, jina_task: str, style: str = "default", truncate_decimals: int = 2):
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
                lambda x: preprocess_mimic_los_for_llm(x, tokenizer, style, truncate_decimals), batched=True, remove_columns=datasets[split].column_names
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
    args = parser.parse_args()

    preprocess_mimic_los(args.model, args.data_path, args.out_path, args.vocabs_path, args.device_id, args.jina_task, args.style, args.truncate_decimals)
