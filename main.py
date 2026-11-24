"""Everyday Wonder entry writer.

Writes one sentence about a small everyday moment of wonder to
/output/entry.txt. Python 3.13 standard library only.
"""

import os

ENTRY = "The kettle clicked off a second before I reached for it, as if the morning had been listening to me all along."


def validate(text):
    """Return True when text is a valid entry: 1-200 chars, not only whitespace."""
    return isinstance(text, str) and 1 <= len(text) <= 200 and text.strip() != ""


def main():
    if not validate(ENTRY):
        raise SystemExit("entry failed validation")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
