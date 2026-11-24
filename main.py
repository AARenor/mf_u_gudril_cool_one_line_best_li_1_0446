#!/usr/bin/env python3
"""Write this entry's one-line text into the make.fun output folder."""

import os
from pathlib import Path
import sys

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. "
    "Gerald has been dead since Tuesday. The tag is new."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
