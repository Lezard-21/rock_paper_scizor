import typer
import random as rd
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

app = typer.Typer()
console = Console()

# current rules
# se divide en dos sets para poder dividir entre idiomas
# si key le gana a [nuevo item] se agrega al key
# se el [nuevo item] le gana a key entonces se agrega a [nuevo elemento]
#   winner | loser
current_rules = [{
    "rock": {"scizor"},
    "paper": {"rock"},
    "scizor": {"paper"},},
    {
    "piedra": {"tijera"},
    "papel": {"piedra"},
    "tijera": {"papel"},}
    # "spook": {"rock", "rock", "scizor"}
]


def define_result(option: str, oponent_option: str, idiom_set: dict):
    if option == oponent_option:
        return "Draw"
    losers = idiom_set.get(oponent_option)
    if option in losers:
        return "You lose"
    else:
        return "You Win"


@app.command()
def play(item: Annotated[str, typer.Argument()]):
    idiom_set = None
    for i in current_rules:
        if item in i:
            idiom_set = i
    oponent_choice = rd.choice(list(idiom_set.keys()))
    console.print("Oponent choice: " + oponent_choice)
    result = define_result(item, oponent_choice, idiom_set)
    console.print(result)


@app.command()
def add(item: Annotated[str, typer.Option(prompt="Insert the item to add")]):
    table = Table("index", "item", caption_justify="center", highlight=True)
    for index, x in enumerate(current_rules.keys()):
        table.add_row(str(index), x)
    console.print(table)
    wins = typer.prompt(f"A que items le gana {item}(ej:1,3)")
    print(wins.split(","))
    # TODO hacer que se agregen los wins al set del item
    # TODO hacer que a todos los demas items se les agrege el item
    console.print(current_rules)


if __name__ == "__main__":
    app()
