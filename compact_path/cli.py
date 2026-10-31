#! /usr/bin/env python

"""
Print a compacted version of the given path.

Usage:
    compact_path.py [--trigger=LENGTH] [--single-char] [--truncate] PATH
    compact_path.py (-h | --help)
    compact_path.py --version

Parent path components are compacted to one character. By default, dot-aware compaction
retains the dot and the following character in dot-prefixed components, so '.config'
becomes '.c' rather than just '.'. Use --single-char to enforce one character per
compacted component. The basename (last component) is unchanged unless --truncate
is used. Optionally, compact only when the path exceeds a given trigger length.

    PATH     The path to compact

Options:
    -t, --trigger=LENGTH   The path length at which path compaction takes place [default: 0]
    --single-char          Compact each parent component to one character, including dot-prefixed names.
    --truncate             Truncate the basename with an ellipsis. Preserves the compacted path
                           prefix and at least one basename character.
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
            single_char=args["--single-char"],
            truncate=args["--truncate"],
        )
    )


if __name__ == "__main__":
    main()
