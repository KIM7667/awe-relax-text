"""A slow river at dusk.

The entry is one short scene: late light on a river, a heron standing
in the shallows, hills holding the evening, and a sky that keeps
widening until the first stars arrive. Nothing in it tells the reader
what to do or feel; the pace comes from the images themselves, each one
held a little longer than expected, so the thought can keep growing
after the last line.

Running this program writes the scene as UTF-8 text to entry.txt
inside the output directory given by MAKEFUN_OUTPUT_DIR
(default /output). The output is deterministic: the same text is
written on every run.
"""

import os
import sys

TEXT = (
    "Late light lies low over the river, and the water carries it "
    "downstream in long gold threads. A heron stands still in the "
    "shallows. The hills hold the evening without hurrying, "
    "and the sky keeps widening, patient as stone, until the first "
    "stars arrive one by one."
)


def main() -> int:
    text = TEXT
    if not 1 <= len(text) <= 280:
        print(f"entry must be 1-280 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
