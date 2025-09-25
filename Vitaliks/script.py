from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich.text import Text

first_name = Text("Віталій", style="bold red")
last_name = Text("Родич", style="blink #005fff")
group = Text("КБ-101", style="bold #5fd7ff")
variant = Text("17", style="italic #d75f00")

rprint(first_name)
rprint(last_name)
rprint(group)
rprint(variant)

console = Console()
table = Table(
    title=Text("Інформація про студента", style="bold bright_red"),
    header_style="bold bright_green"
)

table.add_column("Ім'я", style="bold red", justify="center")
table.add_column("Прізвище", style="blink #005fff", justify="center")
table.add_column("Група", style="bold #5fd7ff", justify="center")
table.add_column("Варіант", style="italic #d75f00", justify="center")

table.add_row("Віталій", "Родич", "КБ-101", "17")
console.print(table, justify="center")

# В терміналі писати "python script.py"