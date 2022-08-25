from __future__ import annotations

from pytest import mark

from lssr.core import get_target_strpath


@mark.parametrize(
    ("args", "expected"),
    [
        ([], "."),
        (["dir"], "dir"),
    ],
)
def test(args: list[str], expected: str):
    assert get_target_strpath(args) == expected
