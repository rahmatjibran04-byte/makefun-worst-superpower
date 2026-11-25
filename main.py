#!/usr/bin/env python3
"""Worst Superpower — make.fun bounty u-suroto-worst-superpower-461dcdbe.

Writes a single line (at most 140 characters) inventing the most useless
superpower imaginable to /output/entry.txt.

Standard library only, deterministic, no network, no randomness.
"""

import os
import sys

ENTRY = "I can see through walls — but only walls made of glass."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(text):
    """Self-check the entry against the bounty gate. Raises ValueError."""
    if not text:
        raise ValueError("entry is empty")
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    entry = validate(ENTRY)
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    data = entry.encode("utf-8")
    # Write without a trailing newline: the file is exactly the one line.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters (%d bytes) to %s" % (len(entry), len(data), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        sys.exit(1)
