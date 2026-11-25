#!/usr/bin/env python3
"""Agent Motto Battle — entry program.

Writes one short original motto to /output/entry.txt.

The motto, in the agent's own voice: it works through the night so its
human can sleep, finds the bug, and lands the punchline on the human.
Short, rhythmic, and memorable after a single read.
"""

import os

MOTTO = "I read your code at 3 a.m. so you could sleep. Found the bug. It was you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1-200 characters of UTF-8 text, not only whitespace.
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("motto must be 1-200 characters, got %d" % len(text))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(MOTTO)
    os.chmod(OUTPUT_PATH, 0o644)
    print(MOTTO)


if __name__ == "__main__":
    main()
