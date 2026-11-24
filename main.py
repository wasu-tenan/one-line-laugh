#!/usr/bin/env python3
"""The One-Line Laugh — make.fun bounty entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt, honouring $MAKEFUN_OUTPUT_DIR or --output.
Standard library only.
"""

import argparse
import os
import sys

# The entry: one sentence, concrete object, everyday truth, twist at the end.
LINE = "I bought a standing desk to fix my posture, and now I slouch vertically."


def validate(line):
    """Gate check, mirroring the sealed scorer: 1-200 chars, not only
    whitespace, and a single sentence."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(stripped))
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return stripped


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the one-line laugh entry.")
    parser.add_argument(
        "--output",
        default=None,
        help="Output file (default: $MAKEFUN_OUTPUT_DIR/entry.txt or /output/entry.txt)",
    )
    args = parser.parse_args(argv)

    line = validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = args.output or os.path.join(out_dir, "entry.txt")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
