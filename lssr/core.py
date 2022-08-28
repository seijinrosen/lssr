from __future__ import annotations

import sys
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path

from rich import box
from rich.table import Table

from .util import console, ts2dt

# IGNORED_ITEMS = {".DS_Store"}


class SortMode(Enum):
    DEFAULT = auto()
    MTIME = auto()
    SIZE = auto()


@dataclass
class Options:
    reverse: bool
    sort_mode: SortMode


def get_single_hyphen_options(args: list[str]) -> list[str]:
    ret: list[str] = []
    for x in args:
        if not x.startswith("-"):
            continue
        if x.startswith("--"):
            continue
        ret += x.lstrip("-")
    return ret


def get_sort_mode(options: list[str]) -> SortMode:
    for x in options[::-1]:
        if x == "t":
            return SortMode.MTIME
        elif x == "S":
            return SortMode.SIZE
    return SortMode.DEFAULT


def get_options(args: list[str]) -> Options:
    single_hyphen_options = get_single_hyphen_options(args)
    double_hyphen_options = [x.lstrip("--") for x in args if x.startswith("--")]
    return Options(
        reverse="r" in single_hyphen_options or "reverse" in double_hyphen_options,
        sort_mode=get_sort_mode(single_hyphen_options),
    )


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


def get_sorted_items(
    target_path: Path,
    reverse: bool = False,
    sort_mode: SortMode = SortMode.DEFAULT,
) -> list[Path]:
    def get_sort_key(p: Path):
        if sort_mode == SortMode.DEFAULT:
            return (p.is_file(), p.name)
        if sort_mode == SortMode.MTIME:
            return (-p.stat().st_mtime_ns, p.is_file(), p.name)
        if sort_mode == SortMode.SIZE:
            return (-p.stat().st_size, p.is_file(), p.name)

    return sorted(target_path.iterdir(), key=get_sort_key, reverse=reverse)


def get_target_strpath(args: list[str]) -> str:
    not_option_args = [x for x in args if not x.startswith("-")]
    if not not_option_args:
        return "."
    return not_option_args[0]


def main(args: list[str]) -> None:
    target_path = Path(get_target_strpath(args))
    options = get_options(args)

    if not target_path.exists():
        sys.exit(f"{target_path}: No such file or directory")

    if target_path.is_file():
        console.print(target_path.name + " is file.")
        console.print(create_table([target_path]))
        return

    sorted_items = get_sorted_items(
        target_path, reverse=options.reverse, sort_mode=options.sort_mode
    )
    console.print(get_info_message(sorted_items))
    console.print(create_table(sorted_items))
