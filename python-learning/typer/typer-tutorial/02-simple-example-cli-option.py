"""
Typer Tutorial
"""

import typer


def main(name: str, last_name: str = "", formal: bool = False):
    if formal:
        typer.echo(f"Good day Ms. {name} {last_name}")
    else:
        typer.echo(f"Hello {name} {last_name}")


if __name__ == "__main__":
    typer.run(main)
