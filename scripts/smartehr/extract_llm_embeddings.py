import argparse
import json
import sys
import time
from pathlib import Path

sys.path.append(".")  # run from repo root so `models` is importable, matching scripts/init.py

import pyarrow as pa
import pyarrow.parquet as pq
import torch
from datasets import Dataset, load_dataset
from transformers import AutoTokenizer

from models.llm import LLM

_DTYPES = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}


def extract_split_embeddings(
    model: LLM,
    tokenizer,
    split: Dataset,
    batch_size: int,
    device: str,
    out_path: Path,
) -> int:
    """Stream embeddings to `out_path` one batch at a time, so at most one batch's
    tensors/embeddings are ever held in memory — needed on low-RAM machines, since
    the alternative (accumulate the whole split, then write once) requires the
    entire split's embeddings resident at once."""
    writer = None
    n_rows = 0
    n_batches = (len(split) + batch_size - 1) // batch_size
    start_time = time.monotonic()
    try:
        for batch_idx, start in enumerate(range(0, len(split), batch_size)):
            batch = split[start : start + batch_size]
            input_ids = [torch.tensor(ids) for ids in batch["input_ids"]]
            attention_mask = [torch.ones_like(ids) for ids in input_ids]
            input_ids = torch.nn.utils.rnn.pad_sequence(
                input_ids, batch_first=True, padding_value=tokenizer.pad_token_id
            ).to(device)
            attention_mask = torch.nn.utils.rnn.pad_sequence(attention_mask, batch_first=True, padding_value=0).to(device)

            with torch.no_grad():
                emb = model.embed(input_ids=input_ids, attention_mask=attention_mask)
            embeddings = emb.cpu().tolist()

            table = pa.table({"duration": batch["duration"], "event": batch["event"], "inputs": embeddings})
            if writer is None:
                writer = pq.ParquetWriter(out_path, table.schema)
            writer.write_table(table)
            n_rows += table.num_rows

            del batch, input_ids, attention_mask, emb, embeddings, table
            if device.startswith("cuda"):
                torch.cuda.empty_cache()

            if batch_idx == 0 or (batch_idx + 1) % 10 == 0 or batch_idx + 1 == n_batches:
                elapsed = time.monotonic() - start_time
                rate = n_rows / elapsed if elapsed > 0 else 0.0
                print(f"    batch {batch_idx + 1}/{n_batches}  ({n_rows} rows, {rate:.1f} rows/s, {elapsed:.0f}s elapsed)")
    finally:
        if writer is not None:
            writer.close()
    return n_rows


def main(
    parquet_dir: str,
    out_dir: str,
    llm_name: str,
    chunk_size: int | None,
    batch_size: int,
    device: str,
    dtype: str,
):
    parquet_dir = Path(parquet_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Device: {device}" + (f"  (torch CPU threads: {torch.get_num_threads()})" if device == "cpu" else ""))
    if device == "cpu":
        print("  WARNING: running a 1B-parameter transformer on CPU is inherently slow (likely minutes, not "
              "seconds, per batch). If a GPU is available, pass --device cuda.")

    print(f"Loading frozen backbone {llm_name} (dtype={dtype}) ...")
    tokenizer = AutoTokenizer.from_pretrained(llm_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = LLM(
        llm_name=llm_name, num_outputs=1, freeze_backbone=True, chunk_size=chunk_size, torch_dtype=_DTYPES[dtype]
    )
    model.to(device)
    model.eval()
    embedding_dim = model.cls.in_features
    print(f"Embedding dim: {embedding_dim}")

    for split_name in ["train", "validation", "test"]:
        split_file = parquet_dir / f"{split_name}.parquet"
        out_path = out_dir / f"{split_name}.parquet"
        split = load_dataset("parquet", data_files=str(split_file), split="train")
        lengths = [len(ids) for ids in split["input_ids"]]
        n_chunked = sum(1 for length in lengths if chunk_size is not None and length > chunk_size)
        print(f"Extracting embeddings for {split_name} ({split_file}): {len(split):,} rows, "
              f"seq length min/mean/max = {min(lengths)}/{sum(lengths)/len(lengths):.0f}/{max(lengths)}"
              + (f", {n_chunked} rows require chunking (>{chunk_size} tokens)" if n_chunked else ""))
        n_rows = extract_split_embeddings(model, tokenizer, split, batch_size, device, out_path)
        del split
        print(f"  {split_name:12s}: {n_rows:,} rows -> {out_path}")

    metadata_path = parquet_dir / "metadata.json"
    metadata = json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
    metadata.update({"llm_name": llm_name, "chunk_size": chunk_size, "embedding_dim": embedding_dim})
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\nSaved embeddings to {out_dir}")
    print(f"Set model.input_size={embedding_dim} when training the MLP head.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract frozen-LLM patient embeddings from the tokenized output of "
        "preprocess_smartehr_survival.py, for offline training of a small MLP survival head."
    )
    parser.add_argument("--parquet-dir", type=str, required=True,
                        help="Directory containing train/validation/test.parquet (output of preprocess_smartehr_survival.py).")
    parser.add_argument("--out-dir", type=str, required=True)
    parser.add_argument("--llm-name", type=str, default="meta-llama/Llama-3.2-1B",
                         help="Pretrained backbone to use. No architecture overrides — always loads pretrained weights, frozen.")
    parser.add_argument("--chunk-size", type=int, default=512,
                        help="Split sequences longer than this into chunks and mean-pool their last-token embeddings. "
                             "Set to 0 to disable (process full sequence in one pass).")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--dtype", type=str, default="float32", choices=list(_DTYPES),
                        help="Model precision. float16/bfloat16 roughly halve compute/memory on GPU; on CPU "
                             "float32 is usually still the fastest option unless the CPU has bf16 acceleration.")
    args = parser.parse_args()

    main(
        parquet_dir=args.parquet_dir,
        out_dir=args.out_dir,
        llm_name=args.llm_name,
        chunk_size=args.chunk_size if args.chunk_size > 0 else None,
        batch_size=args.batch_size,
        device=args.device,
        dtype=args.dtype,
    )
