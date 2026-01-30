from rich.console import Console
from rich.progress import Progress, track
from rich.align import Align
from rich.live import Live
from rich.table import Table
from rich.tree import Tree
from rich import print
from time import sleep

####################
print("Custom print, [bold green] vs. [/bold green]~")
####################
tree_example = Tree("Tree's root node")
for i in range(1,10):
    tree_example.add(f"Node {i}")
print(tree_example, end="\n") 
####################

console = Console(width=100)

tree = Tree("Programming Languages")

python_tree = tree.add("[b green]Python~[/]")
python_tree.add("Numpy")
python_tree.add("Pandas")
python_tree.add("Django")
python_tree.add("Flask")

java_tree = tree.add("[b dark_orange]Java~[/]")
java_tree.add("Spring")
java_tree.add("Apache")

frameworks = ["Express", "React", "Next", "Vue", "Angular"]
js_tree = tree.add("[b yellow]Javascript~[/]")
for frame in frameworks:
    js_tree.add(frame)

console.print(tree)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo">{code}</pre>
"""
#####################
console = Console()
tasks = [f"Task {n}" for n in range(1,5)]
with console.status("[bold dark_blue]finishing tasks...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
######################
TABLE_DATA = [
    [
        "[b white]DSA Course[/]: [i]Beginner[/]",
        "[magenta]$[/]10",
        "[green]Try Hack Me[/]",
        "15 hours",
    ],
    [
        "[b white]DSA Course[/]: [i]Intermediate[/]",
        "[magenta]$[/]20",
        "[green]Try Hack Me[/]",
        "25 hours",
    ],
    [
        "[b white]DSA Course[/]: [i]Advanced[/]",
        "[magenta]$[/]40",
        "[green]Try Hack Me",
        "35 hours",
    ],
]

console = Console()

table = Table(show_footer=False)
table_centered = Align.center(table)

console.clear()

with Live(table_centered, console=console, screen=False):
    table.add_column("Course Name", no_wrap=True)
    table.add_column("Price", no_wrap=True)
    table.add_column("Organization", no_wrap=True)
    table.add_column("Duration", no_wrap=True)
    for row in TABLE_DATA:
        table.add_row(*row)

    table_width = console.measure(table).maximum

    table.width = None
#########################
for step in track(range(5)):
    sleep(1)
#########################
with Progress() as progress:
    task1 = progress.add_task("[red]Doing Task 1", total=100)
    task2 = progress.add_task("[blue]Doing Task 2", total=40)
    task3 = progress.add_task("[green]Doing Task 3", total=80)

    while not progress.finished:
        progress.update(task1, advance=0.25)
        progress.update(task2, advance=0.1)
        progress.update(task3, advance=0.2)
        sleep(0.01)
##########################