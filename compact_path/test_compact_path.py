import pytest

from .cli import compact_path


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("", ""),
    ],
)
def test_empty(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("/", "/"),
    ],
)
def test_root(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("/usr", "/usr"),
        ("/usr/local", "/u/local"),
        ("/usr/local/bin", "/u/l/bin"),
    ],
)
def test_absolute(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("usr", "usr"),
        ("usr/local", "u/local"),
    ],
)
def test_relative(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("~", "~"),
        ("~/code", "~/code"),
        ("~/code/compact_path", "~/c/compact_path"),
    ],
)
def test_home(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,trigger,expected",
    [
        ("/usr/local/bin", len("/usr/local/bin"), "/usr/local/bin"),
        ("/usr/local/bin", 1, "/u/l/bin"),
    ],
)
def test_max_length(input_path: str, trigger: int, expected: str) -> None:
    assert expected == compact_path(input_path, trigger=trigger)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("/usr/local/bin/", "/u/l/bin"),
    ],
)
def test_trailing_slash(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("/usr/lo cal/b in", "/u/l/b in"),
        ("/usr/ lo cal/b in", "/u/l/b in"),
        ("/usr/ lo cal/ bin", "/u/l/ bin"),
    ],
)
def test_spaces(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("/.config/.profile/file.txt", "/.c/.p/file.txt"),
        ("~/./code/./compact_path", "~/./c/./compact_path"),
    ],
)
def test_dots(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path)
