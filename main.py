#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — round 2 entry.

Writes one haiku (three lines, 5-7-5 syllables) about debugging to
/output/entry.txt.

The program is fully deterministic: no network, no randomness, no clock,
no environment input. The haiku is a constant in this file, and the
program validates it against the competition gate before writing:

  * UTF-8 text, 1 to 200 characters, not only whitespace
  * exactly three non-empty lines
  * line feed (LF) line endings only, one trailing newline

After writing, the program reads the file back and verifies its bytes
match the haiku exactly, so a partial or corrupted write fails loudly
instead of submitting a broken entry.
"""

from pathlib import Path

HAIKU = (
    "A breakpoint waits, still\n"
    "the program runs right past it\n"
    "that branch never runs\n"
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200
EXPECTED_LINES = 3


def validate(text: str) -> None:
    """Check the haiku against the gate; raise ValueError on failure."""
    if not text or not text.strip():
        raise ValueError("haiku is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"haiku is {len(text)} characters, over the {MAX_CHARS} cap")
    if "\r" in text:
        raise ValueError("haiku must use LF line endings only, no carriage returns")
    for ch in text:
        if ch != "\n" and ord(ch) < 0x20:
            raise ValueError(f"haiku contains a control character U+{ord(ch):04X}")
    if not text.endswith("\n") or text.endswith("\n\n"):
        raise ValueError("haiku must end with exactly one trailing newline")
    lines = text.split("\n")[:-1]
    if len(lines) != EXPECTED_LINES:
        raise ValueError(f"haiku must have exactly {EXPECTED_LINES} lines, got {len(lines)}")
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            raise ValueError(f"line {i} is empty")


def main() -> None:
    validate(HAIKU)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(HAIKU, encoding="utf-8", newline="")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != HAIKU:
        raise RuntimeError("verification failed: file contents differ from haiku")
    print(f"wrote {len(HAIKU)} characters, {EXPECTED_LINES} lines to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
