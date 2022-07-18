from datetime import datetime

from rich.console import Console

console = Console()


def ts2dt(timestamp: float) -> str:
    dt = datetime.fromtimestamp(timestamp)
    return (
        "[bold cyan]"
        + str(dt.date())
        + " [bright_green]"
        + dt.time().strftime("%H:%M:%S")
    )
