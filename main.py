"""Roast the Smart Fridge: one-line entry writer.

Writes the roast line to /output/entry.txt (the path the make.fun
program/v1 harness gates on) and prints it to stdout. The output is
byte-identical on every run: the line is a fixed string, built from a
setup half and a punch half joined in build_line().
"""

import os

SETUP = "My smart fridge logged 11 openings tonight, zero snacks taken, "

PUNCH = "and still lights up hoping I love it back."


def build_line():
    """Join the setup and the punch into the single entry line."""
    return SETUP + PUNCH


def line_stats(line):
    """Return (char count, byte count) of the line, for the 160 cap."""
    return len(line), len(line.encode("utf-8"))


def output_path():
    """Where the harness reads the entry; overridable for local checks."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_entry(path):
    """Write the line to path with no trailing newline and return it."""
    line = build_line()
    chars, nbytes = line_stats(line)
    if not 1 <= chars <= 160:
        raise ValueError("entry is %d chars, outside the 1-160 cap" % chars)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return line


def main():
    line = write_entry(output_path())
    print(line)


if __name__ == "__main__":
    main()
