from lssr.core import get_sorted_items
from tests.conftest import EXAMPLE_DIR


def test():
    sorted_items = get_sorted_items(EXAMPLE_DIR)
    name_of_sorted_items = [item.name for item in sorted_items]
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


def test_reverse():
    reversed_sorted_items = get_sorted_items(EXAMPLE_DIR, reverse=True)
    name_of_reversed_sorted_items = [item.name for item in reversed_sorted_items]
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
    ]
    assert name_of_reversed_sorted_items == expected
