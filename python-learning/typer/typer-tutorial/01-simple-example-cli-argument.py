'''
Typer Tutorial
'''

import typer

def main(name: str, last_name: str):
    typer.echo(f"Hello {name} {last_name}")

if __name__ == "__main__":
    typer.run(main)