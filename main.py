"""Entry for make.fun bounty u-kevin-the-excuse-your-agent-gives-you-c1861261.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt: the excuse an AI
agent gives its human for a bug it shipped. Deterministic, stdlib only.
"""

import os

LINE = (
    "I checked my own logs — they say I did nothing wrong, "
    "which is exactly why you shouldn't trust them."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
