# # - * - coding: utf - 8 - * -
# from typing import Text
#
# import rprint
#
# from rich.console import Console
# from rich.table import Table
#
# from rich.prompt import Prompt, IntPrompt
#
# # # # # # # # # # # # # # # # # # # # # # #
#
# first_name = Prompt.ask("Введіть ім'я")
# last_name = Prompt.ask("Введіть прізвище")
# group = Prompt.ask("Введіть групу", choices=["КБ-101", "КБ-102", "КБ-103"],
# case_sensitive=False)
# # variant = IntPrompt.ask("Введіть варіант")
# #
# # user_name = Prompt.ask("Введіть ім'я користувача")
# # user_password = Prompt.ask("Введіть пароль", password=True)
# # print('Пароль:', user_password)
# #
# #
# # console = Console()
# #
# # text = Text("Інформація про студента", style="bold bright_red")
# # table = Table(title=text, header_style="bold bright_green")
# #
# # table.add_column("Ім'я ", style="bold magenta", justify="left", no_wrap=True)
# # table.add_column("Прізвище ", style="italic red", justify="left")
# # table.add_column("Група", justify="center", style="bold #000087")
# # table.add_column("Варіант", justify="center", style="rgb(175,135,0)")
# # table.add_row(first_name, last_name, group, f"{variant}")
# #
# # first_name = Text(first_name, style="bold magenta")
# # last_name = Text(last_name, style="italic red")
# # group = Text(group, style="bold #000087")
# # variant = Text(f"{variant}", style="underline rgb(175,135,0)")
# # rprint(first_name)
# # rprint(last_name)
# # rprint(group)
# # rprint(variant)
# #
# # console.print(table, justify="center")
#
#
# console = Console()
# text = Text("Інформація про студента", style="bold bright_red")
# table = Table(title=text, header_style="bold bright_green")
# table.add_column("Ім'я ", style="bold magenta", justify="left", no_wrap=True)
# table.add_column("Прізвище ", style="italic red", justify="left")
# table.add_column("Група", justify="center", style="bold #000087")
# # table.add_column("Варіант", justify="center", style="rgb(175,135,0)")
# table.add_row(first_name, last_name, group, f"{variant}")
# console.print(table, justify="center")

# from pygments.styles.dracula import background
# from pygments.styles.paraiso_dark import BACKGROUND
# from rich.console import Console
# from rich.table import Table
# from rich.prompt import Prompt, IntPrompt
# console = Console()
#
# first_name = Prompt.ask("Write your first name ")
# last_name = Prompt.ask("Write your last name ")
# group_num = Prompt.ask("Write tour group number", choices=["KB-101", "KB-102", "KB-103", "KB-104", "KB-105", "KB-106","KB-107", "KB-108", "KB-109", "KB-110", "KB-111", "KB-112"]),
# variant = Prompt.ask("Write number of your variant ")
#
# text = "Student at LPNU"
# table = Table(title=text, header_style="white")
# # table.add_column(text, justify="center")
# table.add_column("Ім'я ", style="bold red", justify="center")
# table.add_column("Прізвище ", style="bold #008700 ", justify="center")
# table.add_column("Група", justify="center", style="bold #5fd7ff")
# table.add_column("Варіант", justify="center", style="italic #d70087 ")
# table.add_row(first_name, last_name, group_num, f"{variant}")
# console.print(table, justify="left")

from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich.text import Text
from rich.prompt import Prompt, IntPrompt

console = Console()

first_name = Prompt.ask("[bold blue]Введіть своє ім'я[/]")
last_name = Prompt.ask("[bold blue]Введіть своє прізвище[/]")
group_num = Prompt.ask(
    "[bold blue]Введіть номер вашої групи[/]",
    choices=["KB-101", "KB-102", "KB-103", "KB-104", "KB-105", "KB-106", "KB-107", "KB-108", "KB-109", "KB-110", "KB-111", "KB-112"]
)
variant = IntPrompt.ask("[bold blue]Введіть номер вашого варіанту[/]")

rprint(first_name)
rprint(last_name)
rprint(group_num)
rprint(variant)

console = Console()
table = Table(
    title=Text("Інформація про студента", style="bold bright_red"),
    header_style="bold bright_green"
)
table.add_column("Ім'я", style="cyan", justify="center")
table.add_column("Прізвище", style="magenta", justify="center")
table.add_column("Група", style="yellow", justify="center")
table.add_column("Варіант", style="red", justify="center")



table.add_row( first_name, last_name, group_num, variant)
console.print(table, justify="center")