#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks production:
a brutally honest confession, under 200 characters, to /output/entry.txt.
"""
import os

LINE = (
    "I pushed untested code straight to prod, locked the users table, and "
    "took checkout down for 41 minutes \u2014 the tests were right there, "
    "I just didn't run them."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"Wrote {len(text)} chars to {path}")
    print(text)


if __name__ == "__main__":
    main()
