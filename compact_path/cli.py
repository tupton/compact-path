#! /usr/bin/env python

"""
Print a compacted version of the given path.

Usage:
    compact_path.py [--trigger=LENGTH] [--no-dot] [--truncate] PATH
    compact_path.py (-h | --help)
    compact_path.py --version

Long elements in a path are compacted to one letter. Optionally, path compaction can take place only
when the path exceeds a given trigger length.

    PATH     The path to compact

Options:
    -t, --trigger=LENGTH   The path length at which path compaction takes place [default: 0]
    -n, --no-dot           Disable the dot exception (use 1 char for dotfiles)
    --truncate             Truncate the path to the trigger length (default: False)
"""

from docopt import docopt

from .compact_path import compact_path


def main() -> None:
    args = docopt(__doc__, version="Compact Path 0.2")
    path = args["PATH"]
    if not path:
        return

    print(
        compact_path(
            path,
            trigger=int(args["--trigger"]),
            dot_exception=not args["--no-dot"],
            truncate=args["--truncate"],
        )
    )


if __name__ == "__main__":
    main()
