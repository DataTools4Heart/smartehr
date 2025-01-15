import init
import os
from torch.utils.data import DataLoader
from tokenizers.implementations import ByteLevelBPETokenizer
from dataset_utils.smart import SMARTPoC
from pathlib import Path
from dataset_utils.utils import load_smart_poc, SmartPoCParams
import pickle as pkl
import hydra
from config.config import Config
from config.dataset.dataset import SmartPoCParams
from config.model.model import TransformerEncoderModelParams


@hydra.main(version_base=None, config_path="../config", config_name="config")
def train_tokenizer(cfg: Config):
    dataset_params = cfg.dataset
    model_params = cfg.model
    model_params = TransformerEncoderModelParams(**model_params)
    dataset_params = SmartPoCParams(**dataset_params)
    train, _, _, name_map = load_smart_poc(
        dataset_params.root_path, dataset_params.value_dict_path, dataset_params.data_dict_path
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
    train_tokenizer()
