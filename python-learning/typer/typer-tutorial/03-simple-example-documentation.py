"""
Typer Tutorial
"""

import typer


def main(name: str, last_name: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --last_name.

    If --formal is used, say hi very formally.
    """
    if formal:
        typer.echo(f"Good day Ms. {name} {last_name}")
    else:
        typer.echo(f"Hello {name} {last_name}")


if __name__ == "__main__":
    typer.run(main)
