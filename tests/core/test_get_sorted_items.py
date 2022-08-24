from pathlib import Path

from lssr.core import get_sorted_items

EXAMPLE_DIR = Path("tests/example_dir")


def test():
    sorted_items = get_sorted_items(EXAMPLE_DIR)
    name_of_sorted_items = [
        item.name for item in sorted_items if item.name != ".DS_Store"
    ]
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
        "z_lower",
        "【",
        "あ",
        "ア",
        "亜",
    ]
    assert name_of_sorted_items == expected


def test_is_file():
    target_path = EXAMPLE_DIR / "A"
    sorted_items = get_sorted_items(target_path)
    assert sorted_items == [target_path]
