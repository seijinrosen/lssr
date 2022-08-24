from __future__ import annotations

import sys
from pathlib import Path

from rich import box
from rich.table import Table

from .util import console, ts2dt

# IGNORED_ITEMS = {".DS_Store"}


def get_info_message(items: list[Path]) -> str:
    dir_count = sum(p.is_dir() for p in items)
    file_count = len(items) - dir_count
    return f"{len(items)} items ({dir_count} dirs, {file_count} files)"


def colored(p: Path) -> str:
    # if p.name in IGNORED_ITEMS:
    #     return "[dim]"
    if p.is_dir():
        return "[blue]"
    return ""


def create_table(items: list[Path]) -> Table:
    table = Table(box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column(justify="right")
    table.add_column("Name")
    table.add_column("Last updated")
    table.add_column("Size", justify="right")
    for i, p in enumerate(items, start=1):
        table.add_row(
            str(i),
            colored(p) + p.name,
            ts2dt(p.stat().st_mtime),
            f"{p.stat().st_size:,}",
        )
    return table


def get_sorted_items(target_path: Path) -> list[Path]:
    if target_path.is_file():
        return [target_path]
    return sorted(target_path.iterdir(), key=lambda x: (x.is_file(), x))


def main(args: list[str]) -> None:
    target_path = Path(next((arg for arg in args if not arg.startswith("-")), "."))

    if not target_path.exists():
        sys.exit(f"{target_path}: No such file or directory")

    sorted_items = get_sorted_items(target_path)

    console.print(get_info_message(sorted_items))
    console.print(create_table(sorted_items))
