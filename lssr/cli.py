from __future__ import annotations

from . import __version__, core


def main(args: list[str]) -> None:
    if "--version" in args:
        print(__version__)
        return
    core.main(args)
