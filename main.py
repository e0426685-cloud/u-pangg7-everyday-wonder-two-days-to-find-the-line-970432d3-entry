"""Everyday Wonder entry writer.

Writes one sentence about a small everyday moment of wonder to
/output/entry.txt. Python 3.13 standard library only: no third-party
imports, no network access, no image libraries.

The sentence catches a small morning moment -- the kettle switching
itself off just before a hand reaches for it -- and turns it at a
fresh angle: the morning itself was paying attention.

Revision notes (v2):
- validate() now also requires the entry to be a single sentence on
  one line: any newline or carriage return is rejected, so the output
  file can never be read as two entries or a truncated line.
- validate() rejects control characters other than ordinary spaces,
  keeping the entry plain readable text for any downstream reader.
- The docstring for validate() documents every check and the reason
  behind it, so a reviewer can see the gate logic at a glance.
"""

import os

ENTRY = "The kettle clicked off a second before I reached for it, as if the morning had been listening to me all along."


def is_single_sentence(text):
    """Return True when text reads as exactly one sentence.

    A single sentence ends with exactly one terminal mark (``.``,
    ``!`` or ``?``) and contains no other sentence-ending mark
    earlier in the text, so a stray abbreviation period or a second
    sentence smuggled into the entry is caught.
    """
    if not text or text[-1] not in ".!?":
        return False
    return not any(ch in ".!?" for ch in text[:-1])


def validate(text):
    """Return True when text is a valid entry.

    Checks, in order:
    1. ``text`` is a ``str``.
    2. Length is 1 to 200 characters (``len`` counts characters,
       matching the gate).
    3. Not only whitespace (``strip`` check rejects blank-only text).
    4. Single sentence on one line: no ``\\n`` or ``\\r`` anywhere, so
       the entry stays one sentence and the output file stays one line.
    5. No control characters (code points below U+0020 other than
       space, and U+007F), so the entry is plain readable text.
    6. Exactly one sentence: a single terminal mark at the end and
       none earlier (see ``is_single_sentence``).
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return False
    if not is_single_sentence(text):
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
