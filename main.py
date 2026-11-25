#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's one-line excuse for sending the driver down the wrong
road to /output/entry.txt. Standard library only, deterministic: the same
bytes on every run, from any working directory.
"""

import os

LINE = (
    "That dead end wasn't a wrong turn, it was a shortcut in beta "
    "\u2014 the road just hadn't finished loading yet."
)


def main() -> None:
    text = LINE.strip()
    # The gate accepts 1-200 characters of UTF-8 text; stay well inside it.
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Verify the round-trip: what the judge reads must be exactly this line.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "round-trip mismatch"
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
