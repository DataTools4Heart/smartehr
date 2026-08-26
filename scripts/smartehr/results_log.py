"""Append every run's output to ONE shared results file.

The analysis runs on a VM whose files can only be retrieved through a slow admin request,
so results must not live in terminal scrollback and should not require one download per
experiment. Every script therefore appends to a single append-only markdown file: run as
many arms as you like, then request that one file.

Each run becomes one block:

    ### RUN <utc timestamp> | <title>
    - status: ok | FAILED
    - context: the arm-defining arguments
    - RESULT: the headline numbers, one line each
    <details><summary>full output</summary> ...fenced log... </details>

`RESULT:` lines are pulled out of the captured output and hoisted into the header, so the
file stays skimmable even after dozens of runs:

    grep -E '^### RUN|^- RESULT' results/ALL_RESULTS.md

Full output is kept inside a collapsed block and capped, so one file remains pasteable.
Failures are recorded too — a crashed arm is a result worth seeing.
"""

import contextlib
import io
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_RESULTS_FILE = "results/ALL_RESULTS.md"
MAX_BLOCK_LINES = 400


class _Tee(io.TextIOBase):
    """Write to the real stdout and capture at the same time."""

    def __init__(self, real):
        self.real = real
        self.buf = io.StringIO()

    def write(self, s):
        self.real.write(s)
        self.buf.write(s)
        return len(s)

    def flush(self):
        self.real.flush()


def add_results_arg(parser, default=DEFAULT_RESULTS_FILE):
    parser.add_argument("--results-file", default=default,
                        help="Append this run's output to a single shared markdown file "
                             f"(default {default}). Run every arm, then request that one "
                             "file from the VM rather than one download per experiment.")
    parser.add_argument("--no-results-file", dest="results_file", action="store_const",
                        const=None, help="Do not append to the shared results file.")
    return parser


@contextlib.contextmanager
def results_block(path, title, context=None, max_lines=MAX_BLOCK_LINES):
    """Capture stdout for the duration and append it to `path` as one run block."""
    if not path:
        yield
        return
    tee = _Tee(sys.stdout)
    started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    status, err = "ok", None
    try:
        with contextlib.redirect_stdout(tee):
            yield
    except SystemExit as exc:                      # argparse/SystemExit carries a message
        status = "ok" if not exc.code else f"FAILED (exit {exc.code})"
        err = str(exc) if exc.code else None
        raise
    except BaseException:
        status, err = "FAILED", traceback.format_exc()
        raise
    finally:
        text = tee.buf.getvalue()
        if err:
            text += "\n" + err
        lines = text.splitlines()
        truncated = ""
        if len(lines) > max_lines:
            head, tail = lines[:max_lines - 60], lines[-60:]
            truncated = (f"\n... [{len(lines) - len(head) - len(tail)} lines omitted; "
                         "reduce --screen-top or --top for a shorter block] ...\n")
            lines = head + [truncated] + tail
        results = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("RESULT:")]
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        block = [f"### RUN {started} | {title}", "", f"- status: {status}"]
        if context:
            block.append("- context: " + " ".join(f"{k}={v}" for k, v in context.items()
                                                  if v is not None))
        block += [f"- {r}" for r in results] or ["- RESULT: (none emitted)"]
        block += ["", "<details><summary>full output</summary>", "", "```",
                  "\n".join(lines).rstrip(), "```", "", "</details>", ""]
        # Rewrite the whole file so the index at the top always reflects every run: the file
        # is downloaded and pasted as a unit, so its first lines must be the summary.
        prev = p.read_text() if p.exists() else ""
        blocks = [b.strip("\n") for b in prev.split("\n---\n") if b.strip().startswith("### RUN")]
        blocks.append("\n".join(block).strip("\n"))
        index = []
        for b in blocks:
            head = b.splitlines()[0].replace("### RUN ", "")
            index.append(f"- **{head}**")
            index += ["  " + ln for ln in b.splitlines()
                      if ln.startswith("- RESULT") or ln.startswith("- status: FAILED")]
        p.write_text(
            "# Results log — baseline-free survival experiments\n\n"
            "Append-only, one block per run, newest last. The index below is regenerated on "
            "every run, so the top of this file is always the complete summary.\n\n"
            "No raw clinical text is ever written here.\n\n"
            f"## Index ({len(blocks)} runs)\n\n" + "\n".join(index) + "\n\n"
            "---\n\n" + "\n\n---\n\n".join(blocks) + "\n")
        sys.stdout.write(f"\n[results appended to {p}]\n")


def emit(fmt, *a, **kw):
    """Print a headline number that gets hoisted into the run block's header."""
    print("RESULT: " + (fmt.format(*a, **kw) if (a or kw) else fmt))
