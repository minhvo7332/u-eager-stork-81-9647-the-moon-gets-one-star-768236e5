#!/usr/bin/env python3
"""The Moon Gets One Star — one-star review of the Moon, <= 120 chars.

Writes exactly one line (no trailing newline) to /output/entry.txt.
The line is a real one-star review: a star rating, a grievance, and the
reason the Moon earned its single star.
"""

import os

REVIEW = "★☆☆☆☆ Controls the tides but can't be bothered to stay full. Part-time moon, full-time attitude. One star."


def validate(review: str) -> None:
    """Gate checks, mirrored locally: 1-120 chars, one line, not blank."""
    if not 1 <= len(review) <= 120:
        raise ValueError(f"review is {len(review)} chars, must be 1-120")
    if "\n" in review or "\r" in review:
        raise ValueError("review must be a single line")
    if not review.strip():
        raise ValueError("review must not be only whitespace")
    if not review.startswith("★"):
        raise ValueError("review must open with its star rating")


def main() -> None:
    validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    # The harness collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
