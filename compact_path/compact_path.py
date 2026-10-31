import os


def compact_path(
    path: str, trigger: int = 0, dot_exception: bool = True, truncate: bool = False
) -> str:
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

    # If there is a trigger length but the compacted path is longer than that,
    # truncate the base name (last part of the path) with an ellipsis.
    if truncate and trigger > 0 and len(compacted) > trigger:
        # Length of the path without the base name
        path_len = len(os.sep.join(compacted_parts[:-1]))
        # Add a trailing separator only if there are multiple parts in the path
        if len(compacted_parts) > 1:
            path_len += len(os.sep)

        # Truncate the base name to fit within the trigger length
        base_name = compacted_parts[-1]
        max_base_len = max(
            1,  # Always print at least one character of the base name
            trigger - path_len - 1,  # Reserve one character for the ellipsis
        )
        truncated_base = base_name[:max_base_len]

        compacted = os.sep.join(compacted_parts[:-1] + [truncated_base + "…"])

    return compacted
