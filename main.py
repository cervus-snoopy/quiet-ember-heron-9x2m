#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke excusing a missed deadline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only. No network, no randomness, no clock.
"""

import os
import sys

LINE = (
    "My deadline didn't move \u2014 my calendar just filed it under "
    "'someday', between 'learn Spanish' and 'call Grandma'."
)

MAX_CHARS = 200


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not LINE:
        print("entry line is empty", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            f"entry line is {len(LINE)} characters, over the "
            f"{MAX_CHARS}-character gate",
            file=sys.stderr,
        )
        return 1
    if "\n" in LINE:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("round-trip verification failed", file=sys.stderr)
            return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
