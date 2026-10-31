import os

def compact_path(path: str, trigger: int = 0, dot_exception: bool = True) -> str:
    if not path or len(path) <= trigger or path == os.sep:
        return path

    # Filter out empty path components
    parts = [p for p in path.split(os.sep) if p]
    # ... but add one to the beginning if we're dealing with an absolute path
    if os.path.isabs(path):
        parts.insert(0, "")

    # Use the first character of each nonzero-length path component
    compacted_parts = [
        p.strip()[:2]
        if dot_exception and len(p.strip()) > 0 and p.strip()[0] == "."
        else p.strip()[:1]
        for p in parts[:-1]
    ] + [parts[-1]]

    # Join the path back up with the proper separator
    # This strips trailing slashes from the input path
    compacted = os.sep.join(compacted_parts)

    return compacted
