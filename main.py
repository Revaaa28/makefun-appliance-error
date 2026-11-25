#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line to /output/entry.txt: the funniest honest error message
an appliance could show. The winner, chosen by manual ranking against the
judge brief (see candidates.md), is a vacuum cleaner reporting a full
dustbin — a flat inventory that turns into a confession of theft.
"""

import os

ENTRY = "Error: dustbin full. I have swallowed a sock, three coins and your earring. I am keeping the earring."

# The grader runs this in a sandbox where /output is the artifact dir.
# OUTPUT_PATH lets a local run point the same code at a scratch dir
# instead, so the entry can be verified byte-for-byte without touching /output.
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def build_entry() -> str:
    """Return the entry line, validated against the gate (1-200 chars, one line)."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or "  " in text:
        raise ValueError("entry has stray whitespace")
    return text


def main() -> None:
    text = build_entry()
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
