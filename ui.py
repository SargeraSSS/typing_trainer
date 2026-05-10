from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console

console = Console()
layout = Layout()
layout.split_column(
    Layout(Panel("input here"), name="input", size=3),
    Layout(Panel("words here"), name="prompt")
)

with Live(layout, console=console, screen=True):
    input()
