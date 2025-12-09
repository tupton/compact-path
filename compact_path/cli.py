#! /usr/bin/env python

"""
Print a compacted version of the given path.

Usage:
    compact_path.py [--trigger=LENGTH] PATH
    compact_path.py (-h | --help)
    compact_path.py --version

Long elements in a path are compacted to one letter. Optionally, path compaction can take place only
when the path exceeds a given trigger length.

    PATH     The path to compact

Options:
    -t, --trigger=LENGTH   The path length at which path compaction takes place [default: 0]
"""

import os

from docopt import docopt


def compact_path(path: str, trigger: int = 0) -> str:
    if not path or len(path) <= trigger or path == os.sep:
        return path

    # Filter out empty path components
    parts = [p for p in path.split(os.sep) if p]
    # ... but add one to the beginning if we're dealing with an absolute path
    if os.path.isabs(path):
        parts.insert(0, "")

    # Use the first character of each nonzero-length path component
    compacted_parts = [
        p.strip()[:2] if len(p.strip()) > 0 and p.strip()[0] == "." else p.strip()[:1]
        for p in parts[:-1]
    ] + [parts[-1]]

    # Join the path back up with the proper separator
    # This strips trailing slashes from the input path
    compacted = os.sep.join(compacted_parts)

    return compacted


def main() -> None:
    args = docopt(__doc__, version="Compact Path 0.2")
    path = args["PATH"]
    if not path:
        return

    print(compact_path(path, trigger=int(args["--trigger"])))


if __name__ == "__main__":
    main()
