from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .util import console


def lssr(items: Iterable[Path]) -> tuple[list[Path], list[Path]]:
    dirs: list[Path] = []
    files: list[Path] = []

    for p in items:
        if p.is_dir():
            dirs.append(p)
        else:
            files.append(p)

    return sorted(dirs), sorted(files)


def main(args: list[str]) -> None:
    current_directory = Path()
    items = current_directory.iterdir()
    dirs, files = lssr(items)

    message = f"{len(dirs) + len(files)} items ({len(dirs)} dirs, {len(files)} files)"
    console.print(message)

    console.print(*dirs, sep="\n", style="blue")
    console.print(*files, sep="\n")
