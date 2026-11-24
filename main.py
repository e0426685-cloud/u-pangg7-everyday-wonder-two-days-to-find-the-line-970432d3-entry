"""Everyday Wonder entry writer.

Writes one sentence about a small everyday moment of wonder to
/output/entry.txt. Python 3.13 standard library only: no third-party
imports, no network access, no image libraries.

The sentence catches a small morning moment -- the kettle switching
itself off just before a hand reaches for it -- and turns it at a
fresh angle: the morning itself was paying attention.
"""

import os

ENTRY = "The kettle clicked off a second before I reached for it, as if the morning had been listening to me all along."


def validate(text):
    """Return True when text is a valid entry.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace. ``len`` counts characters, matching the gate, and the
    strip check rejects blank-only text.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry failed validation")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Plain open() + explicit chmod 644: the grader (a different user)
    # must be able to read the file, so never use tempfile.mkstemp.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
