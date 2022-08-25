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
    return sorted(target_path.iterdir(), key=lambda p: (p.is_file(), p.name))


def get_target_strpath(args: list[str]) -> str:
    not_option_args = [x for x in args if not x.startswith("-")]
    if not not_option_args:
        return "."
    return not_option_args[0]


def main(args: list[str]) -> None:
    target_path = Path(get_target_strpath(args))

    if not target_path.exists():
        sys.exit(f"{target_path}: No such file or directory")

    if target_path.is_file():
        console.print(target_path.name + " is file.")
        console.print(create_table([target_path]))
        return

    sorted_items = get_sorted_items(target_path)
    console.print(get_info_message(sorted_items))
    console.print(create_table(sorted_items))
