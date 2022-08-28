from __future__ import annotations

import pytest

from lssr.core import SortMode, get_sort_mode


@pytest.mark.parametrize(
    ("options", "expected"),
    [
        ([], SortMode.DEFAULT),
        (["t"], SortMode.MTIME),
        (["S"], SortMode.SIZE),
        (["t", "S"], SortMode.SIZE),
        (["S", "t"], SortMode.MTIME),
        (["x"], SortMode.DEFAULT),
    ],
)
def test(options: list[str], expected: SortMode):
    assert get_sort_mode(options) == expected
