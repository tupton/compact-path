import pytest

from .compact_path import compact_path


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


@pytest.mark.parametrize(
    "input_path,expected",
    [
        ("/.config/.profile/file.txt", "/././file.txt"),
    ],
)
def test_single_char(input_path: str, expected: str) -> None:
    assert expected == compact_path(input_path, single_char=True)


@pytest.mark.parametrize(
    "input_path,trigger,expected",
    [
        ("/usr/local/bin", 6, "/u/l/b…"),
        ("/usr/local/bin", 7, "/u/l/b…"),
        ("/usr/local/bin", 8, "/u/l/bin"),
        ("/usr/local/bin", 10, "/u/l/bin"),
        ("a/longname", 5, "a/lo…"),
        ("/longname", 5, "/lon…"),
        ("longname", 5, "long…"),
        ("longname", 1, "l…"),
        (
            "/really/long/path/with/even/longer/basename-with-a-long-long-long-tail",
            20,
            "/r/l/p/w/e/l/basena…",
        ),
    ],
)
def test_truncate(input_path: str, trigger: int, expected: str) -> None:
    assert expected == compact_path(input_path, trigger=trigger, truncate=True)


@pytest.mark.parametrize(
    "input_path,trigger",
    [
        ("/usr/local/bin", 7),
        ("a/longname", 5),
        ("/longname", 5),
        ("longname", 5),
        ("longname", 2),
        (
            "/really/long/path/with/even/longer/basename-with-a-long-long-long-tail",
            20,
        ),
    ],
)
def test_truncate_fits_when_prefix_and_ellipsis_fit(
    input_path: str, trigger: int
) -> None:
    assert len(compact_path(input_path, trigger=trigger, truncate=True)) <= trigger
