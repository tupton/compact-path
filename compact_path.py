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

from __future__ import print_function

import os

from docopt import docopt

def compact_path(path, trigger=0):
    if not path or len(path) == 0 or len(path) <= trigger or path == os.sep:
        return path

    # Filter out empty path components
    parts = list(filter(bool, path.split(os.sep)))
    # ... but add one to the beginning if we're dealing with an absolute path
    if path[0] == os.sep:
        parts.insert(0, '')

    # Use the first character of each nonzero-length path component
    compacted_parts = [(p.strip()[0] if len(p.strip()) > 0 else '') for p in parts[:-1]]
    # Add the full "basename" (last part) of the path
    compacted_parts.append(parts[-1])

    # Join the path back up with the proper separator
    # This strips trailing slashes from the input path
    compacted = os.sep.join(compacted_parts)

    return compacted

if __name__ == "__main__":
    args = docopt(__doc__, version="Compact Path 0.1")

    print(compact_path(args['PATH'], trigger=int(args['--trigger'])))
