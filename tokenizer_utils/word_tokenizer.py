import json
from pathlib import Path
import spacy


class WordTokenizer:
    def __init__(self, vocab_path: str, lang: str = "en"):
        self.vocab_path = Path(vocab_path)
        with open(self.vocab_path, "r") as f:
            self.vocab = json.load(f)
        self.tokenizer = spacy.blank(lang)

    def encode(self, text: str) -> list[int]:
        ids = []
        for token in self.tokenizer(text):
            token = token.text
            if token not in self.vocab:
                token = "[UNK]"
            ids.append(self.vocab[token])
        return ids


def load_tokenizers(root_path: Path):
    tokenizers = {}
    for vocab_file in root_path.glob("*.json"):
        feature_type = vocab_file.name.split(".")[0]
        tokenizer = WordTokenizer(vocab_path=vocab_file, lang="en")
        tokenizers[feature_type] = tokenizer
    return tokenizers


def load_tann_tokenizer(root_path: Path):
    tokenizer = WordTokenizer(vocab_path=root_path, lang="en")
    return tokenizer
