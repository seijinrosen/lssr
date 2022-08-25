from __future__ import annotations

import pytest

from lssr.core import get_target_strpath


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        ([], "."),
        (["dir"], "dir"),
    ],
)
def test(args: list[str], expected: str):
    assert get_target_strpath(args) == expected
