import pytest
from pytest import CaptureFixture
from pytest_mock import MockerFixture
from rich.console import Console

from lssr import core

EXAMPLE_DIR = "tests/example_dir/"


@pytest.fixture(autouse=True)
def mock_console(mocker: MockerFixture):
    yield mocker.patch.object(core, "console", new=Console(color_system=None))


def test_target_path_not_exists():
    with pytest.raises(SystemExit):
        assert core.main([EXAMPLE_DIR + "not_exist_file"]) is None


def test_file(capsys: CaptureFixture[str]):
    assert core.main([EXAMPLE_DIR + "A"]) is None
    out, err = capsys.readouterr()
    assert err == ""
    assert "A is file." in out
    assert "16 items (1 dirs, 15 files)" not in out


def test_dir(capsys: CaptureFixture[str]):
    assert core.main([EXAMPLE_DIR]) is None
    out, err = capsys.readouterr()
    assert err == ""
    assert "is file." not in out
    assert "16 items (1 dirs, 15 files)" in out
