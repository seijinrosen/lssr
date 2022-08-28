from pathlib import Path

from lssr.core import SortMode, get_sorted_items
from tests.conftest import EXAMPLE_DIR


def test():
    sorted_items = get_sorted_items(EXAMPLE_DIR)
    item_names = [item.name for item in sorted_items]
    expected = [
        "dir",
        "!",
        "-",
        "0",
        "1",
        "10",
        "9",
        "A",
        "Z",
        "[",
        "a_lower",
        "size_200bytes",
        "z_lower",
        "【",
        "あ",
        "ア",
        "亜",
    ]
    assert item_names == expected


def test_reverse():
    reversed_sorted_items = get_sorted_items(EXAMPLE_DIR, reverse=True)
    item_names = [item.name for item in reversed_sorted_items]
    expected = [
        "亜",
        "ア",
        "あ",
        "【",
        "z_lower",
        "size_200bytes",
        "a_lower",
        "[",
        "Z",
        "A",
        "9",
        "10",
        "1",
        "0",
        "-",
        "!",
        "dir",
    ]
    assert item_names == expected


def test_sort_by_size():
    sorted_items = get_sorted_items(EXAMPLE_DIR, sort_mode=SortMode.SIZE)
    item_names = [item.name for item in sorted_items]
    expected = [
        "size_200bytes",
        "dir",
        "!",
        "-",
        "0",
        "1",
        "10",
        "9",
        "A",
        "Z",
        "[",
        "a_lower",
        "z_lower",
        "【",
        "あ",
        "ア",
        "亜",
    ]
    assert item_names == expected


def test_sort_by_size_reversed():
    sorted_items = get_sorted_items(EXAMPLE_DIR, sort_mode=SortMode.SIZE, reverse=True)
    item_names = [item.name for item in sorted_items]
    expected = [
        "亜",
        "ア",
        "あ",
        "【",
        "z_lower",
        "a_lower",
        "[",
        "Z",
        "A",
        "9",
        "10",
        "1",
        "0",
        "-",
        "!",
        "dir",
        "size_200bytes",
    ]
    assert item_names == expected


def test_sort_by_mtime(tmp_path: Path):
    d = tmp_path / "sub"
    d.mkdir()
    file_names = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
    ]
    for name in file_names:
        (d / name).touch()
    sorted_items = get_sorted_items(d, sort_mode=SortMode.MTIME)
    assert len([*d.iterdir()]) == 10
    assert [item.name for item in sorted_items] == [*reversed(file_names)]


def test_sort_by_mtime_reversed(tmp_path: Path):
    d = tmp_path / "sub"
    d.mkdir()
    file_names = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
    ]
    for name in file_names:
        (d / name).touch()
    sorted_items = get_sorted_items(d, sort_mode=SortMode.MTIME, reverse=True)
    assert len([*d.iterdir()]) == 10
    assert [item.name for item in sorted_items] == file_names
