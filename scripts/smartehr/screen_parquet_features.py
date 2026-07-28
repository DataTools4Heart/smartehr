"""Diagnose a survival parquet: is a null result the FEATURES or the MODEL?

A deep net with hundreds of features and ~1k events returns test C ~= 0.5 whether the
features are empty or merely hard to exploit. This separates the two, model-free first:

  1. label sanity     — n, event rate and follow-up per split (catches broken targets)
  2. univariate screen — Harrell's C of every single feature against a 2-SE noise floor.
                         If NOTHING clears it on TRAIN, no model can rescue the features.
  3. overfitting gap  — train C vs test C for the same features
  4. --cox            — L2-penalised Cox on train, tuned on validation, reported on test.
                         The right model class at this event count; if Cox finds signal an
                         MLP missed, the MLP was the problem, not the data.

Works on any parquet dir produced by the builders here (pivoted, tf-idf, raw features):
it needs inputs/duration/event and, optionally, feature_names in metadata.json.

    python scripts/smartehr/screen_parquet_features.py --parquet-dir <DIR> --cox
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import Dataset


def harrell_c(time, event, risk):
    """Harrell's C. Higher risk should mean shorter time. NaN risks are dropped."""
    time, event, risk = np.asarray(time, float), np.asarray(event, int), np.asarray(risk, float)
    ok = ~np.isnan(risk)
    time, event, risk = time[ok], event[ok], risk[ok]
    if len(time) < 10 or event.sum() == 0:
        return None
    num = den = 0.0
    for i in np.where(event == 1)[0]:
        comp = time > time[i]
        n = int(comp.sum())
        if not n:
            continue
        rj = risk[comp]
        num += float((risk[i] > rj).sum()) + 0.5 * float((risk[i] == rj).sum())
        den += n
    return num / den if den else None


def load(parquet_dir):
    d = Path(parquet_dir)
    meta = {}
    if (d / "metadata.json").exists():
        meta = json.load(open(d / "metadata.json"))
    out = {}
    for split in ("train", "validation", "test"):
        f = d / f"{split}.parquet"
        if not f.exists():
            continue
        ds = Dataset.from_parquet(str(f))
        out[split] = (np.asarray(ds["inputs"], dtype=np.float64),
                      np.asarray(ds["duration"], dtype=np.float64),
                      np.asarray(ds["event"], dtype=int))
    if not out:
        raise SystemExit(f"no train/validation/test parquet in {d}")
    n_feat = out[next(iter(out))][0].shape[1]
    names = meta.get("feature_names") or [f"f{i}" for i in range(n_feat)]
    if len(names) != n_feat:
        print(f"NOTE: metadata lists {len(names)} names for {n_feat} columns; using generic names")
        names = [f"f{i}" for i in range(n_feat)]
    return out, names, meta


def main(args):
    data, names, meta = load(args.parquet_dir)
    print(f"=== {args.parquet_dir}")
    if meta:
        keys = ("representation", "landmark_days", "horizon_days", "aggregators",
                "min_patients", "n_features")
        print("  " + " | ".join(f"{k}={meta[k]}" for k in keys if k in meta))

    # ---- 1. label sanity
    print("\n--- label sanity (a broken target shows up here, not in the model) ---")
    for s, (X, t, e) in data.items():
        q = np.percentile(t, [0, 50, 100])
        print(f"  {s:11s} n={len(t):6,} features={X.shape[1]:5,} events={e.sum():5,} "
              f"({100*e.mean():4.1f}%) duration p0/p50/p100 = "
              f"{q[0]:.0f}/{q[1]:.0f}/{q[2]:.0f}")
        if X.shape[0] != len(t):
            print("    ** inputs and labels have different lengths — alignment is broken **")

    Xtr, ttr, etr = data["train"]
    n_ev = int(etr.sum())
    thr = 2.0 * math.sqrt(0.25 / max(n_ev, 1))
    print(f"\n  2-SE noise floor on train ({n_ev:,} events): |C-0.5| >= {thr:.3f}")

    # ---- 2. univariate screen on train (the decisive, model-free test)
    print("\n--- univariate Harrell C per feature, TRAIN ---")
    rows = []
    for j, nm in enumerate(names):
        c = harrell_c(ttr, etr, Xtr[:, j])
        if c is not None:
            rows.append((abs(c - 0.5), nm, c, j))
    rows.sort(reverse=True)
    cleared = [r for r in rows if r[0] >= thr]
    print(f"  features clearing the floor: {len(cleared):,} of {len(rows):,}")
    print(f"  {'feature':<58s} {'C(train)':>9s} {'C(test)':>9s}")
    Xte, tte, ete = data.get("test", (None, None, None))
    for _, nm, c, j in rows[:args.top]:
        cte = harrell_c(tte, ete, Xte[:, j]) if Xte is not None else None
        flag = " <-" if abs(c - 0.5) >= thr else ""
        print(f"  {nm[:58]:<58s} {c:9.4f} {(f'{cte:.4f}' if cte else '   -   '):>9s}{flag}")
    if not cleared:
        print("\n  ** NO single feature clears the noise floor on train. The features carry no")
        print("     detectable univariate signal, so no architecture or tuning can fix this. **")

    # ---- 3. overfitting gap: how much did the feature block memorise?
    if Xte is not None and cleared:
        best = cleared[0]
        print(f"\n--- best feature train vs test: {best[1]} ---")
        print(f"  train C={best[2]:.4f}  test C={harrell_c(tte, ete, Xte[:, best[3]]):.4f}")

    # ---- 4. properly regularised linear model (the right model class at this n)
    if args.cox:
        try:
            from lifelines import CoxPHFitter
        except ImportError:
            raise SystemExit("lifelines not installed; drop --cox")
        print("\n--- L2-penalised Cox: tuned on validation, reported on test ---")
        Xva, tva, eva = data.get("validation", (None, None, None))
        cols = [f"x{j}" for j in range(Xtr.shape[1])]
        tr = pd.DataFrame(Xtr, columns=cols).assign(_t=ttr, _e=etr)
        best = None
        for pen in [float(p) for p in args.penalizers.split(",")]:
            try:
                cph = CoxPHFitter(penalizer=pen, l1_ratio=0.0)
                cph.fit(tr, duration_col="_t", event_col="_e")
            except Exception as exc:
                print(f"  penalizer={pen:<8g} fit failed: {type(exc).__name__}")
                continue
            risk_tr = cph.predict_partial_hazard(pd.DataFrame(Xtr, columns=cols)).to_numpy()
            c_tr = harrell_c(ttr, etr, risk_tr)
            c_va = None
            if Xva is not None:
                risk_va = cph.predict_partial_hazard(pd.DataFrame(Xva, columns=cols)).to_numpy()
                c_va = harrell_c(tva, eva, risk_va)
            print(f"  penalizer={pen:<8g} train C={c_tr:.4f}  val C="
                  f"{f'{c_va:.4f}' if c_va else '  -   '}")
            score = c_va if c_va is not None else c_tr
            if score is not None and (best is None or score > best[0]):
                best = (score, pen, cph)
        if best and Xte is not None:
            _, pen, cph = best
            risk_te = cph.predict_partial_hazard(pd.DataFrame(Xte, columns=cols)).to_numpy()
            c_te = harrell_c(tte, ete, risk_te)
            se = math.sqrt(0.25 / max(int(ete.sum()), 1))
            print(f"\n  selected penalizer={pen:g} -> TEST C={c_te:.4f} "
                  f"(test 2-SE band around 0.5 is +/-{2*se:.3f})")
            verdict = ("signal" if abs(c_te - 0.5) >= 2 * se else "indistinguishable from chance")
            print(f"  verdict: {verdict}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--parquet-dir", required=True)
    p.add_argument("--top", type=int, default=25, help="How many features to list.")
    p.add_argument("--cox", action="store_true", help="Also fit an L2-penalised Cox model.")
    p.add_argument("--penalizers", default="0.01,0.1,1.0,10.0")
    main(p.parse_args())
