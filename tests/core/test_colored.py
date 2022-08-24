from lssr.core import colored
from tests.conftest import EXAMPLE_DIR


def test_is_dir():
    p = EXAMPLE_DIR / "dir"
    assert colored(p) == "[blue]"


def test_is_file():
    p = EXAMPLE_DIR / "A"
    assert colored(p) == ""
