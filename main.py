#!/usr/bin/env python3
"""Your Week in One Line — make.fun bounty entry.

Writes a single line (<=100 chars) summarising the week to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    # One-line summary of the week: a rest plan that collapsed into
    # an apology to the fridge — the sharp turn lands in the last third.
    "Monday I planned to rest; by Friday the fridge had a personality "
    "and I owed it an apology."
)


def main():
    text = ENTRY_TEXT
    if not (1 <= len(text) <= 100):
        raise ValueError(f"entry must be 1-100 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
