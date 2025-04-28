import init
import json
import os
from pathlib import Path
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
import spacy
from datasets import load_dataset
from dataset_utils.mimic import preprocess_note
from dataset_utils.mimic_los import convert_numeric_to_str
import argparse


def compute_vocab(texts: list[str], tokenizer: spacy.Language):
    vocab = defaultdict(int)
    for text in tqdm(texts):
        for token in tokenizer(text):
            vocab[token.text] += 1
    for k in list(vocab.keys()):
        if vocab[k] < 2:
            vocab.pop(k, None)

    vocab = {k: i + 2 for i, k in enumerate(vocab)}
    vocab["[PAD]"] = 0
    vocab["[UNK]"] = 1
    return vocab


def train_tokenizer_mimic_los(data_path: str, out_path: str, train_featurewise: bool = True):
    datasets = load_dataset(data_path)
    train = datasets["train"]

    texts = defaultdict(list)
    print("Preprocessing texts...")
    for i in tqdm(range(len(train))):
        for j in range(len(train[i]["features"])):
            for feature_type in train[i]["features"][j]:
                for feature_name, feature_value in train[i]["features"][j][feature_type].items():
                    if feature_name == "text":
                        value = preprocess_note(feature_value)
                    else:
                        if pd.notna(feature_value):
                            value = convert_numeric_to_str(feature_value)
                            value = preprocess_note(f"{feature_name} {value}")
                    texts[feature_type].append(value)

    lang = "en"
    tokenizer = spacy.blank(lang)
    vocabs = {}
    if train_featurewise:
        for feature_type in texts:
            vocabs[feature_type] = compute_vocab(texts[feature_type], tokenizer)
    else:
        vocabs["vocab"] = compute_vocab([t for ts in texts.values() for t in ts], tokenizer)

    out_path = Path(out_path)
    os.makedirs(out_path, exist_ok=True)
    for feature_type in vocabs:
        with open(out_path / f"{feature_type}.json", "w") as f:
            json.dump(vocabs[feature_type], f, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True, help="The path to the dataset")
    parser.add_argument("--out_path", type=str, required=True, help="The path to save the vocab")
    parser.add_argument("--train_featurewise", action="store_true", help="Whether to train the tokenizer featurewise")
    args = parser.parse_args()
    train_tokenizer_mimic_los(args.data_path, args.out_path, args.train_featurewise)
