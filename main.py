"""Make the AI Judge Laugh: Office Jokes.

Writes exactly one office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Stdlib only; never writes to the cwd.

The joke is a single line, well under the 200-character gate, about
the most universal office truth: a calendar that protects focus time
is exactly what gets a meeting booked on top of it.
"""

import os

JOKE = "My calendar blocked out focus time, so my manager booked a meeting called 'Quick sync about your focus time.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
