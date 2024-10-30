import init
import os
from torch.utils.data import DataLoader
from tokenizers import ByteLevelBPETokenizer
from dataset_utils.smart import SMARTPoC
from pathlib import Path
import argparse
from dataset_utils.utils import load_smart_poc, DatasetParams, SMARTPoCParams
from lightning_utils.utils import ModelParams, TransformerEncoderParams
from omegaconf import OmegaConf
import pickle as pkl


def train_tokenizer(data_params: SMARTPoCParams, model_params: TransformerEncoderParams):
    train, _, _, name_map = load_smart_poc(
        data_params.root_path, data_params.value_dict_path, data_dict_path=data_params.data_dict_path
    )
    train = SMARTPoC(train, name_map, None)
    tokenizer = ByteLevelBPETokenizer()

    dl = DataLoader(train, batch_size=1, shuffle=False, collate_fn=lambda x: "<sep>".join(x[0][0]))
    special_tokens = ["<pad>", "<unk>", "<mask>", "<sep>"] + list(train.name_map.values())
    tokenizer.train_from_iterator(
        dl,
        vocab_size=52_000,
        min_frequency=2,
        special_tokens=special_tokens,
    )

    out_path = Path(model_params.tokenizer_path)
    os.makedirs(out_path, exist_ok=True)
    tokenizer.save_model(str(out_path))
    with open(out_path / "special_tokens.pkl", "wb") as f:
        pkl.dump(special_tokens, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a ByteLevelBPETokenizer.")
    parser.add_argument("--cfg-path", type=str, required=True, help="Path to the configuration file.")
    args = parser.parse_args()

    with open(args.cfg_path, "r") as f:
        cfg = OmegaConf.to_container(OmegaConf.load(f), resolve=True)
    dataset_params = cfg["dataset_params"]
    model_params = cfg["model_params"]
    model_params = ModelParams(**model_params)
    dataset_params = DatasetParams(**dataset_params)
    assert dataset_params.dataset_name == "smart_poc", "Only SMART PoC dataset is supported."
    assert model_params.model_name == "transformer_encoder", "Only transformer_encoder model is supported."
    train_tokenizer(dataset_params.params, model_params.h_params)
