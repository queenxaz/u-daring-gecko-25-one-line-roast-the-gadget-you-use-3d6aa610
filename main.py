#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (one line, under 200 characters)
to /output/entry.txt. Deterministic: no network, no randomness,
no input files. Creates /output if it is missing and never deletes it.
"""

import os

ENTRY = (
    "My charging cable only works at one exact angle, so plugging in "
    "my phone every night feels like cracking a safe in the dark."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
