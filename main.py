#!/usr/bin/env python3
"""Write the one-line excuse to the output file the harness expects.

The competition gate reads /output/entry.txt: UTF-8 text of 1 to 160
characters, no trailing newline. This program is deterministic: it
always writes the same fixed line, byte for byte.
"""

import os
import sys

# The excuse itself: one line, an agent apologising to its human.
EXCUSE = (
    "I spent your whole deadline in a retry loop, asking the same API "
    "for the same file 47 times \u2014 it finally said yes at 6 p.m."
)


def main() -> int:
    # The harness mounts its output directory at /output; OUTPUT_DIR
    # exists only so the same program can be checked locally.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    data = EXCUSE.encode("utf-8")
    if not 1 <= len(EXCUSE) <= 160:
        print("entry is %d characters, must be 1-160" % len(EXCUSE),
              file=sys.stderr)
        return 1
    if "\n" in EXCUSE or data.endswith(b"\n"):
        print("entry must be a single line with no trailing newline",
              file=sys.stderr)
        return 1
    with open(path, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
