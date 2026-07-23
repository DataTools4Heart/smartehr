"""TF-IDF features from the free-text events (radiology/op-report/consult), for the MLP.

The decisive "is there signal in these words?" test, independent of LLM-embedding
quality: concatenate each patient's free-text within the window, TF-IDF (word n-grams)
+ TruncatedSVD to a dense vector, optionally concatenate the numeric SMART baseline,
standardize (train-fit), and write the MLP parquet.

Run it on a JSONL built from ONLY the target source CSVs (e.g. radiologie_verslag,
ok_verslag, consult) so only their fields are present. --window-days 180 = last 6 months.

    python scripts/smartehr/prepare_text_tfidf_features.py \
        --jsonl-dir <3SOURCE_JSONL> --out-dir <TFIDF_text> --window-days 180        # text only
    #   add --include-baseline for baseline+text. Then:
    #   dataset=smartehr_embeddings dataset.root_path=<OUT> model=mlp model.input_size=<n_features>

Compare text-only vs baseline-only (prepare_event_numeric_features --only-baseline) and
baseline+text vs baseline-only via bootstrap_ci_compare.py.
"""

import argparse
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import Dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


def apply_censoring(first_event: float, cd_event: int, horizon: int) -> tuple[float, int]:
    if cd_event == 0:
        return (float(min(first_event, horizon)), 0)
    if first_event <= horizon:
        return (float(first_event), 1)
    return (float(horizon), 0)


def _is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and not (isinstance(v, float) and v != v)


def _patient_text(rec: dict, window_days: int | None) -> str:
    """Concatenate all free-text (string) event field values within the window."""
    parts = []
    for ev in rec.get("events", []):
        if window_days is not None and not (-window_days <= ev["datediff"] <= 0):
            continue
        for k, v in ev.items():
            if k == "datediff":
                continue
            if isinstance(v, str) and v.strip():
                parts.append(v.strip())
    return " ".join(parts)


def _baseline_features(rec: dict) -> dict[str, float]:
    out, past = {}, False
    for k, v in rec["smart"].items():
        if k == "SmrtRisk":
            past = True
        if past or k in ("first_event", "cd_event"):
            continue
        if _is_num(v):
            out[f"baseline__{k}"] = float(v)
    return out


def _read_split(path: Path, window_days, include_baseline, horizon):
    texts, base_rows, dur, evt = [], [], [], []
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            fe = rec["smart"].get("first_event")
            if fe is None:
                continue
            cd = rec["smart"].get("cd_event")
            cd = int(cd) if cd is not None else 1
            texts.append(_patient_text(rec, window_days))
            base_rows.append(_baseline_features(rec) if include_baseline else {})
            d, e = apply_censoring(fe, cd, horizon)
            dur.append(d)
            evt.append(e)
    return texts, base_rows, dur, evt


def main(jsonl_dir, out_dir, window_days, include_baseline, horizon,
         max_features, ngram_max, min_df, n_components):
    jsonl_dir, out_dir = Path(jsonl_dir), Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    splits = {s: _read_split(jsonl_dir / f"{s}.jsonl", window_days, include_baseline, horizon)
              for s in ["train", "validation", "test"]}

    train_texts = splits["train"][0]
    n_nonempty = sum(1 for t in train_texts if t.strip())
    print(f"Train patients: {len(train_texts):,} ({n_nonempty:,} with any text in the window)")
    if n_nonempty == 0:
        raise SystemExit("No text found in the window — is this a JSONL from the free-text source CSVs? "
                         "Check --window-days and that the source CSVs have text columns.")

    tfidf = TfidfVectorizer(max_features=max_features, ngram_range=(1, ngram_max), min_df=min_df,
                            sublinear_tf=True, strip_accents="unicode", lowercase=True)
    Xtr = tfidf.fit_transform(train_texts)
    k = min(n_components, Xtr.shape[1] - 1)
    svd = TruncatedSVD(n_components=k, random_state=42).fit(Xtr)
    print(f"TF-IDF vocab={len(tfidf.vocabulary_):,} -> SVD dim={k} "
          f"(explained var={svd.explained_variance_ratio_.sum():.2f})")

    # baseline feature vocabulary fixed from train
    base_cols = sorted({c for row in splits["train"][1] for c in row}) if include_baseline else []

    def features_for(split):
        texts, base_rows, dur, evt = split
        T = svd.transform(tfidf.transform(texts))
        cols = [f"svd_{i}" for i in range(T.shape[1])]
        df = pd.DataFrame(T, columns=cols)
        if include_baseline:
            B = pd.DataFrame(base_rows, columns=base_cols)
            df = pd.concat([df.reset_index(drop=True), B.reset_index(drop=True)], axis=1)
        return df, dur, evt

    train_df, _, _ = features_for(splits["train"])
    means = train_df.mean(numeric_only=True)
    stds = train_df.std(numeric_only=True).replace(0.0, 1.0)
    n_features = train_df.shape[1]

    for s in ["train", "validation", "test"]:
        df, dur, evt = features_for(splits[s])
        std_df = ((df - means) / stds).fillna(0.0)
        ds = Dataset.from_dict({
            "inputs": std_df.to_numpy(dtype=np.float32).tolist(),
            "duration": [float(x) for x in dur],
            "event": [float(x) for x in evt],
        })
        ds.to_parquet(out_dir / f"{s}.parquet")
        n, ne = len(ds), int(sum(evt))
        print(f"  {s:12s}: {n:5,} patients | events={ne} ({100*ne/max(n,1):.1f}%) | features={n_features}")

    with open(out_dir / "metadata.json", "w") as f:
        json.dump({
            "representation": "tfidf_text" + ("+baseline" if include_baseline else ""),
            "window_days": window_days, "include_baseline": include_baseline, "horizon_days": horizon,
            "tfidf_max_features": max_features, "ngram_max": ngram_max, "min_df": min_df,
            "svd_components": int(k), "n_features": n_features,
        }, f, indent=2)

    print(f"\nSaved to {out_dir}")
    print(f"Train with:  dataset=smartehr_embeddings dataset.root_path={out_dir} "
          f"model=mlp model.input_size={n_features}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--jsonl-dir", required=True, help="JSONL built from the free-text source CSVs only.")
    p.add_argument("--out-dir", required=True)
    p.add_argument("--window-days", type=int, default=180, help="Events within this many days before baseline.")
    p.add_argument("--include-baseline", action="store_true", help="Concatenate numeric SMART baseline features.")
    p.add_argument("--horizon-days", type=int, default=1825)
    p.add_argument("--max-features", type=int, default=50000)
    p.add_argument("--ngram-max", type=int, default=2, help="Use word n-grams up to this length (2 = unigrams+bigrams).")
    p.add_argument("--min-df", type=int, default=5, help="Ignore terms in fewer than this many patients.")
    p.add_argument("--svd-components", type=int, default=256)
    args = p.parse_args()
    main(args.jsonl_dir, args.out_dir, args.window_days, args.include_baseline, args.horizon_days,
         args.max_features, args.ngram_max, args.min_df, args.svd_components)
