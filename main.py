#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

Self-contained: no network, no imports beyond the standard library.
"""

from pathlib import Path

ENTRY = "I am on vacation. Your email has been forwarded to a human, who will answer it slower, with more typos, and entirely by hand."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 160, len(text)
    out.write_text(text, encoding="utf-8")
    # Byte-level read-back: the file must hold exactly the entry line.
    assert out.read_text(encoding="utf-8") == text


if __name__ == "__main__":
    main()
