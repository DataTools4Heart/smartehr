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
         max_features, ngram_max, min_df, n_components, require_text, baseline_only):
    jsonl_dir, out_dir = Path(jsonl_dir), Path(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    if baseline_only:
        include_baseline = True  # baseline block is the only content in this mode

    read_baseline = include_baseline  # need baseline features whenever they'll be emitted
    splits = {s: _read_split(jsonl_dir / f"{s}.jsonl", window_days, read_baseline, horizon)
              for s in ["train", "validation", "test"]}

    # How many patients have NO report in the window (baseline-only patients -> empty text)?
    print("Patients with text in the window (rest are baseline-only -> zero text vector):")
    for s in ["train", "validation", "test"]:
        texts = splits[s][0]
        nz = sum(1 for t in texts if t.strip())
        n = len(texts)
        print(f"  {s:12s}: {nz:5,}/{n:5,} have text ({100*nz/max(n,1):.1f}%) | "
              f"{n-nz:,} baseline-only")

    if require_text:  # restrict every split to patients with >=1 report -> removes the empty-vector confound
        for s in splits:
            texts, base_rows, dur, evt = splits[s]
            keep = [i for i, t in enumerate(texts) if t.strip()]
            splits[s] = ([texts[i] for i in keep], [base_rows[i] for i in keep],
                         [dur[i] for i in keep], [evt[i] for i in keep])
        print(f"--require-text: restricted to the with-report subcohort "
              f"(train {len(splits['train'][0]):,}).")

    svd = None
    base_cols = sorted({c for row in splits["train"][1] for c in row}) if include_baseline else []

    if not baseline_only:
        train_texts = splits["train"][0]
        n_nonempty = sum(1 for t in train_texts if t.strip())
        if n_nonempty == 0:
            raise SystemExit("No text found in the window — is this a JSONL from the free-text source CSVs? "
                             "Check --window-days and that the source CSVs have text columns.")
        tfidf = TfidfVectorizer(max_features=max_features, ngram_range=(1, ngram_max), min_df=min_df,
                                sublinear_tf=True, strip_accents="unicode", lowercase=True)
        Xtr = tfidf.fit_transform(train_texts)
        vocab = len(tfidf.vocabulary_)
        if n_components == 0:  # --no-svd: feed the full TF-IDF vocabulary (dense) to the MLP
            k = vocab
            print(f"TF-IDF vocab={vocab:,} | no SVD (dense {vocab}-dim input)")
            if vocab > 8000:
                print(f"  NOTE: {vocab} dense features is large — lower --max-features (e.g. 5000) if memory tight.")
        else:
            k = min(n_components, Xtr.shape[1] - 1)
            svd = TruncatedSVD(n_components=k, random_state=42).fit(Xtr)
            print(f"TF-IDF vocab={vocab:,} -> SVD dim={k} "
                  f"(explained var={svd.explained_variance_ratio_.sum():.2f}; low % is normal for text LSA)")
    else:
        k = 0
        print(f"--baseline-only: emitting only the {len(base_cols)} numeric baseline features "
              f"(reference cohort for a fair baseline vs baseline+text comparison).")

    def features_for(split):
        texts, base_rows, dur, evt = split
        frames = []
        if not baseline_only:
            X = tfidf.transform(texts)
            if svd is None:
                T = X.toarray()
                cols = [f"tf_{i}" for i in range(T.shape[1])]
            else:
                T = svd.transform(X)
                cols = [f"svd_{i}" for i in range(T.shape[1])]
            frames.append(pd.DataFrame(T, columns=cols))
        if include_baseline:
            frames.append(pd.DataFrame(base_rows, columns=base_cols).reset_index(drop=True))
        df = pd.concat([f.reset_index(drop=True) for f in frames], axis=1)
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
        rep = "baseline_only" if baseline_only else ("tfidf_text" + ("+baseline" if include_baseline else ""))
        json.dump({
            "representation": rep, "require_text": require_text, "baseline_only": baseline_only,
            "window_days": window_days, "include_baseline": include_baseline, "horizon_days": horizon,
            "tfidf_max_features": max_features, "ngram_max": ngram_max, "min_df": min_df,
            "svd_components": (0 if (baseline_only or svd is None) else int(k)),
            "no_svd": (not baseline_only) and svd is None, "n_features": n_features,
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
    p.add_argument("--svd-components", type=int, default=256,
                   help="TruncatedSVD dimensionality. Raise (512/1024) if downstream CI keeps improving; "
                        "set 0 for --no-svd (feed the full TF-IDF vocabulary dense — no compression bottleneck).")
    p.add_argument("--require-text", action="store_true",
                   help="Keep only patients with >=1 report in the window. Removes the empty-vector confound: "
                        "text-only CI is otherwise capped by baseline-only patients (all-zero text vector).")
    p.add_argument("--baseline-only", action="store_true",
                   help="Emit ONLY the numeric baseline block (no text). Combine with --require-text to get the "
                        "aligned baseline-only reference for a fair baseline vs baseline+text comparison.")
    args = p.parse_args()
    main(args.jsonl_dir, args.out_dir, args.window_days, args.include_baseline, args.horizon_days,
         args.max_features, args.ngram_max, args.min_df, args.svd_components,
         args.require_text, args.baseline_only)
