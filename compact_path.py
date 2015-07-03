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

    parts = path.split(os.sep)
    parts = [parts[0]] + filter(None, parts[1:])
    compacted_parts = []
    for i, p in enumerate(parts):
        if i != len(parts) - 1:
            p = p.strip()
            compacted_parts.append(p[0] if len(p) > 0 else '')
        else:
            compacted_parts.append(p)

    compacted = os.sep.join(compacted_parts)

    return compacted

if __name__ == "__main__":
    args = docopt(__doc__, version="Compact Path 0.1")

    print(compact_path(args['PATH'], trigger=int(args['--trigger'])))
