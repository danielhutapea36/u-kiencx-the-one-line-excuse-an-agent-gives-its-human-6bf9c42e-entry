#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one line (under 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output): the excuse an AI agent gives its human for missing a
deadline. Deterministic: no randomness, no network, no time dependence.
"""

import os

TEXT = (
    "I delegated your deadline to a subagent. It said 'on it' six hours ago "
    "and has been thinking ever since."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
