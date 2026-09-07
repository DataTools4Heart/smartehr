# Results log — provenance pointer

The live, append-only results log is committed at the repository root as
[`ALL_RESULTS.md`](../ALL_RESULTS.md).

That file is the transfer mechanism between the VM and this repository: results cannot be
copied off the VM by hand, so every script appends to one file (`$RESULTS`, see
`scripts/smartehr/results_log.py`) and that file is committed. Its regenerated `## Index`
sits at the top and is the complete summary of every run.

Every number quoted in `baseline-free-event-survival-report.md` and
`free-text-arm-runbook.md` is traceable to a `### RUN <timestamp>` block there, each of which
carries the resolved arguments, the full stdout and the `RESULT:` lines.

| snapshot | runs | covers |
|---|---|---|
| 2026-09-03 | 91 | + tiered concept terms (T2 re-run), `incr` text-on-full-baseline, `sens` without `ok.OMSCHR` |
| 2026-08-27 | 58 | + the recovered upper references (0.7576 / 0.7394) and the cross-path agreement check |
| 2026-08-26 | 39 | free-text arm T0/T1/T2 and matched controls |

No raw clinical text is ever written to the log: values and terms appear only at
`--min-show-count` (default 20) occurrences or above.
