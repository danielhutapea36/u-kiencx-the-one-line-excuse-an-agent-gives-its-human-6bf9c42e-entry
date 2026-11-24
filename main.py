#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single line -- the excuse an AI agent gives its human for
missing a deadline -- to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``).

The excuse: the agent delegated the deadline to a subagent, which
answered "on it" six hours ago and has been thinking ever since.
The joke lands because delegation is exactly what an agent would do,
and the endlessly "thinking" subagent is the excuse itself.

Deterministic by design: stdlib only, no network, no randomness,
no clock reads. Two runs produce byte-identical output.
"""

import os
import sys

# The line is assembled from its two clauses so the sentence structure
# stays visible in the code instead of hiding inside one long literal.
_CLAUSE_A = "I delegated your deadline to a subagent."
_CLAUSE_B = "It said 'on it' six hours ago and has been thinking ever since."

MAX_LINE_CHARS = 160  # competition ceiling for the single line


def build_line() -> str:
    """Join the two clauses into the one-line excuse.

    The result must be exactly one line: a stray newline in either
    clause would silently break the entry format, so fail loudly
    instead of writing a malformed file.
    """
    line = _CLAUSE_A + " " + _CLAUSE_B
    if "\n" in line or "\r" in line:
        raise ValueError("excuse clauses must not contain line breaks")
    return line


def resolve_output_dir() -> str:
    """Output directory from the environment, falling back to /output."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return value if value else "/output"


def write_entry(path: str, line: str) -> None:
    """Write the line exactly as-is: no trailing newline, UTF-8."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main(argv=None) -> int:
    line = build_line()
    if len(line) > MAX_LINE_CHARS:
        print(
            "error: excuse is %d chars, over the %d-char limit"
            % (len(line), MAX_LINE_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"), line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
