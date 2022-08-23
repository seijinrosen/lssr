from __future__ import annotations

from . import __version__, core
from .util import console, includes

HELP_MESSAGE = """\
Alternative ls command.

[bold]Usage:[/bold]
  lssr

[bold]Global options:[/bold]
  [blue]-h, --help[/blue]      Show this help message and exit.
  [blue]-V, --version[/blue]   Show program's version number and exit.

See https://github.com/seijinrosen/lssr for more information.\
"""


def print_help_message() -> None:
    console.print(HELP_MESSAGE)


def print_version() -> None:
    print(__version__)


def main(args: list[str]) -> None:
    if includes(args, {"-h", "--help"}):
        print_help_message()
        return

    if includes(args, {"-V", "--version"}):
        print_version()
        return

    core.main(args)
