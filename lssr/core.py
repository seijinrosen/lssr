from __future__ import annotations

from pathlib import Path

from rich import box
from rich.table import Table

from .util import console, ts2dt

IGNORED_ITEMS = {".DS_Store"}


def info_message(items: list[Path]) -> str:
    dir_count = sum(p.is_dir() for p in items)
    file_count = len(items) - dir_count
    return f"{len(items)} items ({dir_count} dirs, {file_count} files)"


def colored(p: Path) -> str:
    if p.name in IGNORED_ITEMS:
        return "[dim]"
    if p.is_dir():
        return "[blue]"
    return ""


def create_table(items: list[Path]) -> Table:
    table = Table(box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column(justify="right")
    table.add_column("Name")
    table.add_column("Last updated")
    for i, p in enumerate(items, start=1):
        table.add_row(str(i), colored(p) + p.name, ts2dt(p.stat().st_mtime))
    return table


def main(args: list[str]) -> None:
    current_directory = Path()
    items = sorted(current_directory.iterdir(), key=lambda x: (x.is_file(), x))
    console.print(info_message(items))
    console.print(create_table(items))
