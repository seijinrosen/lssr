from __future__ import annotations

import pytest

from lssr.core import get_options


@pytest.mark.parametrize(
    "args",
    [
        [],
        ["target/path"],
    ],
)
def test_no_option(args: list[str]):
    options = get_options(args)
    assert options.reverse == False


@pytest.mark.parametrize(
    "args",
    [
        ["-r"],
        ["--reverse"],
    ],
)
def test_reverse(args: list[str]):
    options = get_options(args)
    assert options.reverse == True
