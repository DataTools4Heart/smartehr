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
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eda_events_survival import calibrate_null_scale, effective_n_tests, null_floor
from results_log import add_results_arg, emit, results_block


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
    # Heavily imputed low-coverage features arrive here as near-constant columns. They
    # explain both the "low variance" / zero-division warnings from Cox and a screen that
    # reads ~0.5 everywhere despite the RAW screen finding signal.
    sd = Xtr.std(axis=0)
    n_uniq = np.array([len(np.unique(Xtr[:, j])) for j in range(Xtr.shape[1])])
    # A count feature legitimately takes few distinct values, so a low distinct-COUNT is
    # not evidence of degeneracy. Only near-zero variance, or a single dominant value
    # covering almost every patient, actually flattens a column.
    dominant = np.array([np.max(np.bincount(
        np.unique(Xtr[:, j], return_inverse=True)[1])) / max(len(Xtr), 1)
        for j in range(Xtr.shape[1])])
    flat = (sd < 1e-8) | (dominant > 0.99)
    n_flat = int(flat.sum())
    n_lowvar = int((n_uniq <= 10).sum())
    print(f"\n  feature spread: {n_flat:,} of {Xtr.shape[1]:,} effectively constant "
          f"(zero variance, or one value in >99% of patients); "
          f"{n_lowvar:,} take <=10 distinct values (normal for counts)")
    if n_flat:
        print("     The effectively-constant ones carry nothing and dilute a penalised model:")
        print("     raise --min-coverage-frac. Low distinct-count alone is NOT a problem.")
    n_ev = int(etr.sum())
    k = calibrate_null_scale(ttr, etr, n_perm=args.permutations)
    thr = null_floor(k, n_ev)
    print(f"\n  permutation-calibrated null: SE(C) = {k:.3f}/sqrt(events); 2-SE floor on "
          f"train ({n_ev:,} events) = {thr:.4f}")
    print(f"  (the analytic 0.5/sqrt(events) would give {2*math.sqrt(0.25/max(n_ev,1)):.4f} — "
          "too wide under heavy censoring, which discards real signal)")

    # ---- 2. univariate screen on train (the decisive, model-free test)
    print("\n--- univariate Harrell C per feature, TRAIN ---")
    print("  C_mono = the value itself; C_udev = |value - median|, which catches U-shaped")
    print("  risk (both extremes harmful) that a monotone C-index reads as 0.50")
    rows = []
    for j, nm in enumerate(names):
        c = harrell_c(ttr, etr, Xtr[:, j])
        if c is None:
            continue
        v = Xtr[:, j]
        cu = harrell_c(ttr, etr, np.abs(v - np.nanmedian(v)))
        best = max(abs(c - 0.5), abs((cu if cu is not None else 0.5) - 0.5))
        rows.append((best, nm, c, cu, j))
    rows.sort(reverse=True)
    cleared = [r for r in rows if r[0] >= thr]
    print(f"  features clearing the floor (either form): {len(cleared):,} of {len(rows):,}")
    emit("univariate: {} of {} features clear the {:.4f} floor{}",
         len(cleared), len(rows), thr,
         f"; strongest {cleared[0][1]} C={cleared[0][2]:.4f}" if cleared else "")
    print(f"  {'feature':<50s} {'C_mono':>8s} {'C_udev':>8s} {'C_test':>8s}")
    Xte, tte, ete = data.get("test", (None, None, None))
    for best, nm, c, cu, j in rows[:args.top]:
        cte = harrell_c(tte, ete, Xte[:, j]) if Xte is not None else None
        print(f"  {nm[:50]:<50s} {c:8.4f} {(f'{cu:.4f}' if cu else '   -  '):>8s} "
              f"{(f'{cte:.4f}' if cte else '   -  '):>8s}" + ("  <-" if best >= thr else ""))
    n_eff = effective_n_tests(Xtr)
    exp_fp = 0.05 * n_eff
    print(f"\n  {len(rows):,} features are only ~{n_eff:,} INDEPENDENT tests "
          f"(PCs for 95% of variance): last/mean/slope/count of one code are near-duplicates.")
    print(f"  Pure noise would therefore clear the floor ~{exp_fp:.0f} times, not "
          f"~{0.05*len(rows):.0f}.")
    if not cleared and exp_fp >= 3:
        print(f"  ** 0 cleared vs ~{exp_fp:.0f} expected from noise: mildly surprising. Check that")
        print("     features are not flattened by imputation — screen the RAW matrix with")
        print("     prepare_pivoted_event_features --screen-features. **")
    elif not cleared:
        print("  ** No feature clears the floor, and with this few independent tests that is")
        print("     consistent with a genuine absence of univariate signal. **")

    # ---- 3. overfitting gap: how much did the feature block memorise?
    if Xte is not None and cleared:
        best = cleared[0]
        print(f"\n--- best feature train vs test: {best[1]} ---")
        print(f"  train C={best[2]:.4f}  test C={harrell_c(tte, ete, Xte[:, best[4]]):.4f}")

    # ---- 4. properly regularised linear model (the right model class at this n)
    if args.cox:
        try:
            from lifelines import CoxPHFitter
        except ImportError:
            raise SystemExit("lifelines not installed; drop --cox")
        kind = ("lasso" if args.l1_ratio >= 0.99 else
                "elastic-net" if args.l1_ratio > 0 else "ridge")
        print(f"\n--- penalised Cox ({kind}, l1_ratio={args.l1_ratio}): tuned on validation, "
              "reported on test ---")
        if args.l1_ratio == 0:
            print("  NOTE: ridge spreads weight over all features; with a few real signals among")
            print("  hundreds of nulls, rerun with --l1-ratio 1.0 (lasso), which selects instead.")
        Xva, tva, eva = data.get("validation", (None, None, None))
        # Effectively-constant columns make the design singular and are what broke the fit
        # on the 183-feature baseline block (21 of them). They carry no information, so
        # drop them before fitting rather than losing the arm's headline number.
        keep = np.where(~flat)[0]
        if len(keep) < Xtr.shape[1]:
            print(f"  dropped {Xtr.shape[1]-len(keep)} effectively-constant columns before "
                  "fitting (they make the design singular)")
        Xtr_c = Xtr[:, keep]
        Xva_c = Xva[:, keep] if Xva is not None else None
        Xte_c = Xte[:, keep] if Xte is not None else None
        cols = [f"x{j}" for j in range(Xtr_c.shape[1])]
        tr = pd.DataFrame(Xtr_c, columns=cols).assign(_t=ttr, _e=etr)
        best = None
        used_l1 = args.l1_ratio
        for pen in [float(p) for p in args.penalizers.split(",")]:
            cph = None
            for l1 in (args.l1_ratio, 0.0) if args.l1_ratio > 0 else (0.0,):
                try:
                    cph = CoxPHFitter(penalizer=pen, l1_ratio=l1)
                    cph.fit(tr, duration_col="_t", event_col="_e")
                    used_l1 = l1
                    if l1 != args.l1_ratio:
                        print(f"  penalizer={pen:<8g} lasso did not converge; "
                              f"fell back to ridge (l1_ratio=0)")
                    break
                except Exception as exc:
                    cph = None
                    last = type(exc).__name__
            if cph is None:
                print(f"  penalizer={pen:<8g} fit failed: {last}")
                continue
            risk_tr = cph.predict_partial_hazard(pd.DataFrame(Xtr_c, columns=cols)).to_numpy()
            c_tr = harrell_c(ttr, etr, risk_tr)
            c_va = None
            if Xva is not None:
                risk_va = cph.predict_partial_hazard(pd.DataFrame(Xva_c, columns=cols)).to_numpy()
                c_va = harrell_c(tva, eva, risk_va)
            print(f"  penalizer={pen:<8g} train C={c_tr:.4f}  val C="
                  f"{f'{c_va:.4f}' if c_va else '  -   '}")
            score = c_va if c_va is not None else c_tr
            if score is not None and (best is None or score > best[0]):
                best = (score, pen, cph)
        if best and Xte_c is not None:
            _, pen, cph = best
            risk_te = cph.predict_partial_hazard(pd.DataFrame(Xte_c, columns=cols)).to_numpy()
            c_te = harrell_c(tte, ete, risk_te)
            se = math.sqrt(0.25 / max(int(ete.sum()), 1))
            print(f"\n  selected penalizer={pen:g} -> TEST C={c_te:.4f} "
                  f"(test 2-SE band around 0.5 is +/-{2*se:.3f})")
            verdict = ("signal" if abs(c_te - 0.5) >= 2 * se else "indistinguishable from chance")
            print(f"  verdict: {verdict}")
            emit("COX {} penalizer={:g} TEST C={:.4f} (2-SE band +/-{:.3f}) -> {}",
                 ("ridge" if used_l1 == 0 else kind), pen, c_te, 2 * se, verdict)
        elif not best:
            # Without this the index shows only the univariate line and the missing
            # headline number is easy to overlook.
            emit("COX FAILED to converge at every penalizer ({}); no test C for this arm",
                 args.penalizers)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--parquet-dir", required=True)
    p.add_argument("--top", type=int, default=25, help="How many features to list.")
    p.add_argument("--cox", action="store_true", help="Also fit an L2-penalised Cox model.")
    p.add_argument("--penalizers", default="0.01,0.1,1.0,10.0,100.0",
                   help="Penalizer grid. Larger values are included because a wide, partly-collinear\n                        baseline block needs heavy shrinkage to fit at all.")
    p.add_argument("--l1-ratio", type=float, default=0.0,
                   help="0 = ridge (default), 1 = lasso. Lasso is far better at isolating a few "
                        "real features among many null ones; ridge dilutes them.")
    p.add_argument("--permutations", type=int, default=200,
                   help="Permutations used to calibrate the null SE of the C-index.")
    add_results_arg(p)
    a = p.parse_args()
    with results_block(a.results_file, f"screen: {Path(a.parquet_dir).name}",
                       {"parquet_dir": a.parquet_dir, "cox": a.cox,
                        "l1_ratio": a.l1_ratio if a.cox else None}):
        main(a)
