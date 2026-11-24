"""One Letter for Your Day: M for mango-sticky.

The letter stands for the day in one word: mango-sticky, juice running
down to the elbows after eating a ripe mango straight over the sink,
hands sweet, chin sweet, grinning anyway. A warm, sunny, specific
picture of a small perfect moment rather than a vague mood, funny the
instant you hear it, and true to any ordinary summer day that went
exactly right at the fruit stall.
Writes exactly one character, M, to /output/entry.txt, and nothing else.
No trailing newline: the file must be exactly one byte.
"""

import os

LETTER = b"M"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Binary mode: exactly one byte, no newline translation, no extra output.
    with open("/output/entry.txt", "wb") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
