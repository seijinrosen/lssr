from lssr.core import get_info_message
from tests.conftest import EXAMPLE_DIR


def test():
    items = [*EXAMPLE_DIR.iterdir()]
    assert get_info_message(items) == "17 items (1 dirs, 16 files)"
