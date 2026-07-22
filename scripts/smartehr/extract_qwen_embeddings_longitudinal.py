"""Offline per-time-point embedding extraction with Qwen3-Embedding-4B.

Consumes the per-time-point text parquet from
``preprocess_smartehr_longitudinal_survival.py`` and produces, per patient, a
SEQUENCE of embeddings — one vector per time point — which a time-aware LSTM
(``TemporalRecurrentEmbeddings``) then aggregates into a discrete-time PMF
survival prediction.

Design notes
------------
* Encoder: Qwen/Qwen3-Embedding-4B (frozen, instruction-aware, last-token
  pooling, L2-normalized, output dim 2560). Run via sentence-transformers, which
  handles pooling + normalization + the instruction ``prompt`` for us.
* Tesla T4 supports fp16 but NOT bf16: load the backbone in fp16 (fast path), but
  sentence-transformers returns fp32 numpy embeddings, and we store fp32 — the
  LSTM downstream trains in fp32. A per-batch NaN guard catches fp16 overflow.
* No chunking: Qwen3-Embedding-4B's context (8k-32k) covers any single time point,
  so we drop the chunk-mean-pool hack used for the per-patient single-text path.
* The instruction is FROZEN and stored in metadata.json so train/val/test never
  diverge. Qwen recommends English instructions even for multilingual input.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.append(".")  # run from repo root, matching the other extraction scripts

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import torch
from datasets import load_dataset

_DTYPES = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}

# Frozen task instructions (English, per Qwen guidance). Applied identically to every
# item and split. Qwen3-Embedding query template is: "Instruct: {task}\nQuery:{text}".
# Per-time-point / per-item default (flat / pool / sequence modes):
DEFAULT_TASK = (
    "Represent this cardiovascular patient's clinical encounter — diagnoses, lab and vital "
    "measurements, medications, imaging findings, and clinical notes — for predicting the risk "
    "of a future cardiovascular event (vascular death, stroke, or myocardial infarction)."
)
# Whole-history default (joint mode): tells the encoder it is reading a chronological
# history and should integrate across records.
DEFAULT_TASK_JOINT = (
    "The following is a cardiovascular patient's clinical history — a baseline assessment at "
    "enrollment, followed by earlier records (labs, medications, consultations, imaging) each "
    "dated relative to baseline. Represent the patient's overall status for predicting the risk "
    "of a future cardiovascular event (vascular death, stroke, or myocardial infarction)."
)


def _time_phrase(dt_years: float) -> str:
    """Human-readable, LLM-friendly time for an event (all events are pre-baseline)."""
    y = abs(float(dt_years))
    if y < 1.0:
        m = max(1, round(y * 12))
        return f"about {m} month{'s' if m != 1 else ''} before baseline"
    return f"{y:.1f} years before baseline"


def build_joint_document(
    texts: list[str],
    time_deltas: list[float],
    exclude_baseline: bool = False,
    max_tokens_per_block: int | None = None,
    truncate_fn=None,
) -> str:
    """Join a patient's per-time-point texts into ONE chronological document.

    Baseline (index 0, delta 0) first, then events. Block titles are natural language
    wrapped in [] as section headers; fields inside stay newline-separated; blocks are
    separated by a blank line.

    If ``max_tokens_per_block`` and ``truncate_fn`` are given, each block's body is
    truncated to that many tokens BEFORE assembly. This spreads the token budget across
    time points — every time point stays represented (breadth) instead of a few
    note-heavy blocks consuming the whole document and dropping the rest.
    """
    blocks = []
    for i, (txt, dt) in enumerate(zip(texts, time_deltas)):
        if i == 0:
            if exclude_baseline:
                continue
            title = "At baseline (enrollment)"
        else:
            title = _time_phrase(dt)
        if max_tokens_per_block and truncate_fn is not None:
            txt = truncate_fn(txt, max_tokens_per_block)
        blocks.append(f"[{title}]\n{txt}")
    if not blocks:
        return "No clinical records before baseline."
    return "\n\n".join(blocks)


def load_encoder(model_name: str, device: str, dtype: str, max_seq_length: int | None):
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as e:
        raise SystemExit(
            "sentence-transformers is required for this script.\n"
            "  pip install -U sentence-transformers transformers\n"
            "Qwen3-Embedding also needs transformers >= 4.51 (the Qwen3 architecture). "
            "The repo currently pins transformers==4.45.1, so upgrade in the extraction env."
        ) from e

    model = SentenceTransformer(
        model_name,
        device=device,
        model_kwargs={"torch_dtype": _DTYPES[dtype]},
    )
    if max_seq_length is not None:
        model.max_seq_length = max_seq_length
    return model


def extract_split(
    model,
    split,
    prompt: str,
    encode_batch_size: int,
    patient_flush: int,
    truncate_dim: int | None,
    out_path: Path,
    mode: str = "sequence",
    exclude_baseline: bool = False,
    max_tokens_per_block: int | None = None,
) -> tuple[int, int]:
    """Encode patients and stream to parquet. ``mode`` picks the output schema:

    - "sequence" (default): per patient, encode every time point -> ``embeddings`` [L, E]
      sequence + ``time_deltas_list`` (for TemporalRecurrentEmbeddings).
    - "flat": encode ONLY the baseline time point -> flat ``inputs`` [E] vector
      (SMART-baseline-only MLP; schema for the ``mlp`` model / collate_fn_mlp).
    - "pool": encode all time points, write flat ``inputs`` [2E] =
      concat(baseline_embedding, mean(event_embeddings)); event-mean is zeros when a
      patient has no events. Diagnostic: MLP on [baseline ; mean(events)] vs flat.
    - "joint": serialize the WHOLE history into ONE chronological document and encode
      it once -> flat ``inputs`` [E]. Unlike pool, this lets the encoder integrate
      across events (cross-event self-attention). ``exclude_baseline`` drops the
      baseline block (events-jointly-with-context test).

    Buffers up to ``patient_flush`` patients, encodes their texts in one
    sentence-transformers call (internally batched at ``encode_batch_size``).
    """
    writer = None
    n_rows = 0
    n_tps = 0

    # Per-block truncation for joint mode: use the encoder's own tokenizer so the cap is
    # measured in the same tokens the model will see.
    _tok = getattr(model, "tokenizer", None)

    def _truncate_fn(text: str, n: int) -> str:
        if _tok is None:
            return text
        ids = _tok(text, add_special_tokens=False, truncation=True, max_length=n)["input_ids"]
        return _tok.decode(ids, skip_special_tokens=True)

    buf_texts: list[str] = []
    buf_lengths: list[int] = []
    buf_deltas: list[list[float]] = []
    buf_dur: list[float] = []
    buf_evt: list[float] = []

    def flush():
        nonlocal writer, n_rows, n_tps
        if not buf_lengths:
            return
        emb = model.encode(
            buf_texts,
            prompt=prompt,
            batch_size=encode_batch_size,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        emb = np.asarray(emb, dtype=np.float32)
        # NaN guard — fp16 overflow in the backbone shows up here as non-finite values.
        if not np.isfinite(emb).all():
            raise RuntimeError(
                "Non-finite embeddings detected (likely fp16 overflow on the backbone). "
                "Retry with --dtype float32, or load the model in 8-bit."
            )
        if truncate_dim is not None:
            # Matryoshka (MRL) truncation + renormalize.
            emb = emb[:, :truncate_dim]
            norms = np.linalg.norm(emb, axis=1, keepdims=True)
            norms[norms == 0] = 1.0
            emb = emb / norms

        if mode in ("flat", "joint"):
            # One text per patient -> one vector per patient, flat `inputs` schema.
            table = pa.table({"inputs": emb.tolist(), "duration": buf_dur, "event": buf_evt})
            n_tps += len(buf_lengths)
        elif mode == "pool":
            # Per patient: concat(baseline, mean(events)); event-mean = zeros if no events.
            vecs = []
            offset = 0
            for length in buf_lengths:
                base = emb[offset]
                ev_mean = emb[offset + 1 : offset + length].mean(axis=0) if length > 1 else np.zeros_like(base)
                vecs.append(np.concatenate([base, ev_mean]).tolist())
                offset += length
            table = pa.table({"inputs": vecs, "duration": buf_dur, "event": buf_evt})
            n_tps += offset
        else:  # sequence
            seqs = []
            offset = 0
            for length in buf_lengths:
                seqs.append(emb[offset : offset + length].tolist())
                offset += length
            table = pa.table(
                {"embeddings": seqs, "time_deltas_list": buf_deltas, "duration": buf_dur, "event": buf_evt}
            )
            n_tps += offset

        if writer is None:
            writer = pq.ParquetWriter(out_path, table.schema)
        writer.write_table(table)
        n_rows += len(buf_lengths)

        buf_texts.clear()
        buf_lengths.clear()
        buf_deltas.clear()
        buf_dur.clear()
        buf_evt.clear()

    try:
        for rec in split:
            if mode == "flat":
                buf_texts.append(rec["texts"][0])  # baseline time point only
                buf_lengths.append(1)
            elif mode == "joint":
                buf_texts.append(build_joint_document(
                    rec["texts"], rec["time_deltas_list"], exclude_baseline,
                    max_tokens_per_block=max_tokens_per_block, truncate_fn=_truncate_fn,
                ))
                buf_lengths.append(1)
            else:  # "pool" and "sequence" need all time points
                buf_texts.extend(rec["texts"])
                buf_lengths.append(len(rec["texts"]))
                if mode == "sequence":
                    buf_deltas.append([float(d) for d in rec["time_deltas_list"]])
            buf_dur.append(float(rec["duration"]))
            buf_evt.append(float(rec["event"]))

            if len(buf_lengths) >= patient_flush:
                flush()
                print(f"    ...{n_rows:,} patients / {n_tps:,} time points -> {out_path.name}")
        flush()
    finally:
        if writer is not None:
            writer.close()
    return n_rows, n_tps


def main(
    parquet_dir: str,
    out_dir: str,
    model_name: str,
    task: str,
    device: str,
    dtype: str,
    encode_batch_size: int,
    patient_flush: int,
    max_seq_length: int | None,
    truncate_dim: int | None,
    mode: str,
    exclude_baseline: bool = False,
    max_tokens_per_block: int | None = None,
):
    parquet_dir = Path(parquet_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    prompt = f"Instruct: {task}\nQuery:"  # Qwen3 template; text is appended by sentence-transformers.

    _mode_desc = {
        "flat": "flat (baseline-only)",
        "pool": "pool (baseline + mean events)",
        "joint": "joint (whole history, one embedding)" + (", events-only" if exclude_baseline else ""),
        "sequence": "sequence",
    }
    print(f"Device: {device}  |  dtype: {dtype}  |  model: {model_name}  |  mode: {_mode_desc[mode]}")
    if dtype == "bfloat16":
        print("  WARNING: Tesla T4 does not support bf16 — use --dtype float16 on a T4.")
    print(f"Loading frozen encoder ...")
    model = load_encoder(model_name, device, dtype, max_seq_length)
    model.eval()

    embedding_dim = model.get_sentence_embedding_dimension()
    if truncate_dim is not None:
        embedding_dim = truncate_dim
    print(f"Embedding dim: {embedding_dim}" + (f" (MRL-truncated to {truncate_dim})" if truncate_dim else ""))
    print(f"Instruction prompt: {prompt!r}")

    for split_name in ["train", "validation", "test"]:
        split_file = parquet_dir / f"{split_name}.parquet"
        out_path = out_dir / f"{split_name}.parquet"
        split = load_dataset("parquet", data_files=str(split_file), split="train")
        print(f"Extracting {split_name} ({split_file}): {len(split):,} patients ...")
        with torch.no_grad():
            n_rows, n_tps = extract_split(
                model, split, prompt, encode_batch_size, patient_flush, truncate_dim, out_path,
                mode=mode, exclude_baseline=exclude_baseline, max_tokens_per_block=max_tokens_per_block,
            )
        del split
        print(f"  {split_name:12s}: {n_rows:,} patients / {n_tps:,} time points -> {out_path}")

    metadata_path = parquet_dir / "metadata.json"
    metadata = json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
    metadata.update(
        {
            "encoder": model_name,
            "embedding_dim": embedding_dim,
            "normalized": True,
            "instruction": task,
            "prompt_template": prompt,
            "mode": mode,
        }
    )
    with open(out_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\nSaved embeddings to {out_dir}")
    if mode == "flat":
        print(f"Flat baseline-only embeddings: train with model=mlp model.input_size={embedding_dim}.")
    elif mode == "pool":
        print(f"Pooled [baseline; mean(events)]: train with model=mlp model.input_size={2 * embedding_dim} "
              f"and compare vs the flat baseline-only MLP to see if events add signal.")
    elif mode == "joint":
        print(f"Joint whole-history embedding: train with model=mlp model.input_size={embedding_dim} "
              f"and compare vs the flat baseline-only MLP (does cross-event context beat baseline?).")
    else:
        print(f"Set model.embedding_dim={embedding_dim} in config/model/temporal_recurrent_embeddings.yaml.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract per-time-point Qwen3-Embedding vectors from the text parquet produced by "
        "preprocess_smartehr_longitudinal_survival.py, writing per-patient embedding sequences for the "
        "temporal_recurrent_embeddings survival model."
    )
    parser.add_argument("--parquet-dir", type=str, required=True,
                        help="Directory with train/validation/test.parquet (output of the longitudinal builder).")
    parser.add_argument("--out-dir", type=str, required=True)
    parser.add_argument("--model-name", type=str, default="Qwen/Qwen3-Embedding-4B",
                        help="Encoder. Use a small sentence-transformers model to smoke-test the pipeline first.")
    parser.add_argument("--task", type=str, default=None,
                        help="Instruction task description (English). Frozen into metadata.json. "
                             "Default depends on mode (per-encounter for flat/pool/sequence, whole-history for --joint).")
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--dtype", type=str, default="float16", choices=list(_DTYPES),
                        help="Backbone precision. Use float16 on a Tesla T4 (no bf16). "
                             "Fall back to float32 if you hit non-finite embeddings.")
    parser.add_argument("--encode-batch-size", type=int, default=16,
                        help="sentence-transformers internal batch size (time points per forward).")
    parser.add_argument("--patient-flush", type=int, default=256,
                        help="Encode + write after buffering this many patients (streaming granularity).")
    parser.add_argument("--max-seq-length", type=int, default=None,
                        help="Override the encoder max token length per time point. Default: model default.")
    parser.add_argument("--truncate-dim", type=int, default=None,
                        help="MRL: truncate embeddings to this dim and renormalize (Qwen3-Embedding-4B supports 32..2560).")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--flat", action="store_true",
                       help="Baseline-only: encode ONLY the baseline time point per patient -> flat `inputs` [E] "
                            "vector (for `model=mlp`). The SMART-baseline MLP first step.")
    group.add_argument("--pool", action="store_true",
                       help="Diagnostic: write flat `inputs` [2E] = concat(baseline, mean(event embeddings)). "
                            "Train `model=mlp model.input_size=2E` and compare to --flat to test whether the "
                            "events carry signal beyond baseline (before investing in the LSTM).")
    group.add_argument("--joint", action="store_true",
                       help="Serialize the WHOLE history into ONE chronological document and encode it once -> "
                            "flat `inputs` [E]. Lets the encoder integrate across events (unlike --pool). "
                            "Train `model=mlp model.input_size=E` and compare vs --flat.")
    parser.add_argument("--exclude-baseline", action="store_true",
                        help="With --joint only: drop the baseline block (events-jointly-with-context test).")
    parser.add_argument("--max-tokens-per-block", type=int, default=None,
                        help="With --joint only: truncate EACH time-point block to this many tokens before "
                             "assembling the document. Spreads the budget across time points (breadth) so a few "
                             "long clinical-note blocks don't consume everything and drop later time points. "
                             "Total doc length ~= n_time_points * this; combine with --max-seq-length as a backstop.")
    args = parser.parse_args()

    mode = "flat" if args.flat else "pool" if args.pool else "joint" if args.joint else "sequence"
    if args.exclude_baseline and mode != "joint":
        parser.error("--exclude-baseline is only valid with --joint")
    if args.max_tokens_per_block and mode != "joint":
        parser.error("--max-tokens-per-block is only valid with --joint")
    task = args.task or (DEFAULT_TASK_JOINT if mode == "joint" else DEFAULT_TASK)
    main(
        parquet_dir=args.parquet_dir,
        out_dir=args.out_dir,
        model_name=args.model_name,
        task=task,
        device=args.device,
        dtype=args.dtype,
        encode_batch_size=args.encode_batch_size,
        patient_flush=args.patient_flush,
        max_seq_length=args.max_seq_length,
        truncate_dim=args.truncate_dim,
        mode=mode,
        exclude_baseline=args.exclude_baseline,
        max_tokens_per_block=args.max_tokens_per_block,
    )
