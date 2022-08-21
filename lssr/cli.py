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


def main(args: list[str]) -> None:
    if includes(args, {"-h", "--help"}):
        console.print(HELP_MESSAGE)
        return

    if includes(args, {"-V", "--version"}):
        console.print(__version__)
        return

    core.main(args)
