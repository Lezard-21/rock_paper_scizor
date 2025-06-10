import typer
import random as rd
from rich.console import Console
from typing_extensions import Annotated

app = typer.Typer()
console = Console()

# current rules
#   winner | loser
current_rules = {
    "rock": "scizor",
    "paper": "rock",
    "scizor": "paper"
}


def define_result(option: str, oponent_option: str):
    if option == oponent_option:
        return "Draw"
    loser = current_rules.get(oponent_option)
    if loser == option:
        return "You lose"
    else:
        return "You Win"


@app.command()
def play(item: Annotated[str, typer.Argument()]):
    print(current_rules.keys())
    oponent_choice = rd.choice(["rock", "paper", "scizor"])
    console.print("Oponent choice: " + oponent_choice)
    result = define_result(item, oponent_choice)
    console.print(result)


if __name__ == "__main__":
    app()
