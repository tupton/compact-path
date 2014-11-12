#! /usr/bin/env python

from __future__ import print_function

import os
import sys

def compact_path(path):
    if not path or len(path) == 0:
        return
    parts = path.split(os.sep)
    compacted_parts = []
    for i, p in enumerate(parts):
        if i != len(parts) - 1:
            compacted_parts.append(p[0] if len(p) > 0 else '')
        else:
            compacted_parts.append(p)

    compacted = os.path.join(*compacted_parts)

    if path[0] == os.sep:
        compacted = os.sep + compacted

    return compacted

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(compact_path(sys.argv[1]))
