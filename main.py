#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained one-liner joke to /output/entry.txt.

The line is a fixed, hand-written joke: one irony, punchline at the end,
1-140 UTF-8 characters. No network, no randomness, no external input —
the program is fully deterministic and self-contained.
"""

import os

ENTRY = "My agent reviewed my dating profile, flagged me as a duplicate, and merged me with my ex."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry length {len(text)} outside 1-140"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
