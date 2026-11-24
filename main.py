#!/usr/bin/env python3
"""Cat Reviews Its Human - make.fun entry.

Writes one funny single-line one-star review, in the voice of a house
cat about its human, to /output/entry.txt. The gate requires UTF-8 text
of 1 to 200 characters, not only whitespace, so the program validates
the line before writing it. Standard library only.
"""

import os
import sys

ENTRY = (
    "One star. The human refills my bowl at 6am sharp, then goes back "
    "to sleep like feeding me was a favor and not rent."
)


def validate(line: str) -> str:
    """Enforce the gate: one line, 1-200 characters, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    return line


def main() -> int:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
