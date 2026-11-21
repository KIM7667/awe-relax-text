"""Awe / relaxation text entry for make.fun's "Make the AI judge feel awe".

Pure-stdlib Python 3.13, no network, deterministic: writes one short
text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The text (242 characters) is a single concrete scene, shown not
instructed: a river deciding its way, light crossing a field one slow
square at a time, a gate swinging in no wind, and the whole wide sky
leaning down to listen. No wellness stock phrases, no instruction to
the reader, no "breathe" or "relax" — the calm comes from the image
itself, and the last line keeps growing after it ends.
"""

import os
import sys

TEXT = (
    "The river below has been deciding which way to go all evening, "
    "and it is in no hurry. Light moves across the field one slow "
    "square at a time. Somewhere a gate swings, unlatched, in no wind "
    "at all \u2014 and the whole wide sky leans down to listen."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 280:
        print(f"entry is {len(TEXT)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
