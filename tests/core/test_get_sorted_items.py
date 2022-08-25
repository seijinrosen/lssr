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
