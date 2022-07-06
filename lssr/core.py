from __future__ import annotations

from pathlib import Path


def lssr() -> list[Path]:
    dirs: list[Path] = []
    files: list[Path] = []

    for p in Path().iterdir():
        if p.is_dir():
            dirs.append(p)
        else:
            files.append(p)

    dirs.sort()
    files.sort()

    return [*dirs, *files]


def main(args: list[str]) -> None:
    items = lssr()
    print(*items, sep="\n")
