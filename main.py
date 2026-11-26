#!/usr/bin/env python3
"""Entry for Funniest One-Line Bio for an AI on a Dating App (u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf).

Writes one line (max 200 characters) for the judge to /output/entry.txt:
the brief's ask, landed in a single read, grounded and specific. No network,
no randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "Six feet of context window, emotionally available 24/7, remembers everything you say, working on forgetting your ex."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
