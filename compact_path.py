#! /usr/bin/env python

from __future__ import print_function

import os
import sys
import argparse

def compact_path(path, trigger=0):
    if not path or len(path) == 0:
        return

    if len(path) <= trigger or path == os.sep:
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
    parser = argparse.ArgumentParser(description="Compact path elements to one letter")
    parser.add_argument('path', help='The path to compact')
    parser.add_argument('trigger', nargs='?', type=int, default=0, help='The limit at which path compaction takes place')

    args = parser.parse_args()

    if 1 < len(sys.argv) <= 3:
        print(compact_path(args.path, trigger=args.trigger))
