import init
from dataset_utils.mimic import LongitudinalMIMICReadmission
import pandas as pd
import spacy
from collections import defaultdict
from tqdm import tqdm
import json
from pathlib import Path
import argparse
import os
from dataset_utils.mimic import preprocess_note


def train_word_tokenizer(dataset_path: str, out_path: str, lang: str = "en"):
    dataset = pd.read_csv(dataset_path)
    train = LongitudinalMIMICReadmission(dataset, split="train", only_one_readmission_label=True)
    tokenizer = spacy.blank(lang)
    vocab = defaultdict(int)
    for i in tqdm(range(len(train))):
        for text in train[i][0]["text"]:
            for token in tokenizer(text):
                vocab[token.text] += 1

    for k in list(vocab.keys()):
        if vocab[k] < 2:
            vocab.pop(k, None)

    vocab = {k: i + 2 for i, k in enumerate(vocab)}
    vocab["[PAD]"] = 0
    vocab["[UNK]"] = 1
    os.makedirs(Path(out_path), exist_ok=True)
    with open(Path(out_path) / "vocab.json", "w") as f:
        json.dump(vocab, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, required=True, help="Path to the longitudinal MIMIC readmission dataset")
    parser.add_argument("--out_path", type=str, required=True, help="Path where to save the JSON word tokenizer")
    parser.add_argument("--lang", type=str, default="en", help="Language of the dataset")
    args = parser.parse_args()
    train_word_tokenizer(args.dataset_path, args.out_path, args.lang)
