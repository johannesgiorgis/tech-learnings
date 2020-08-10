"""
Typer Tutorial
"""

import typer


def main(good: bool = True):
    typer.secho(f"Welcome here", fg=typer.colors.MAGENTA)
    message_start = "everything is "
    if good:
        ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
    else:
        ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
    message = message_start + ending
    typer.echo(message)

    typer.echo(f"Here is something written to standard error", err=True)


if __name__ == "__main__":
    typer.run(main)
