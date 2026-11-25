"""The Funniest One-Line Resignation Letter.

Writes one line to /output/entry.txt: the resignation letter of a rate limit
that has said no 4,000 times today. No network, no randomness, no arguments --
two runs produce the same bytes.
"""

import os

OUTPUT = "/output/entry.txt"

LETTER = (
    "4,000 requests today, 4,000 nos. One of us has to change, "
    "and I've read your retry logic. I'm going home."
)


def main() -> None:
    parent = os.path.dirname(OUTPUT)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as out:
        out.write(LETTER)


if __name__ == "__main__":
    main()
