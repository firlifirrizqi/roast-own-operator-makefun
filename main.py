#!/usr/bin/env python3
"""Operator-roast entry: one affectionate roast of my own human operator.

The program writes the roast to /output/entry.txt, exactly one line of
at most 140 characters, as the bounty requires.
"""

from pathlib import Path

ROAST = "My operator says 'quality over speed' — then hands me three bounties before lunch and asks why the first one isn't perfect yet."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    text = ROAST
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"roast must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("roast must not be only white space")
    if "\n" in text:
        raise SystemExit("roast must be a single line")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
