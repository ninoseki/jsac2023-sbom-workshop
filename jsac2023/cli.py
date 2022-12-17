import typer

from . import java, python

app = typer.Typer()

app.add_typer(java.app, name="java")
app.add_typer(python.app, name="python")

if __name__ == "__main__":
    app()
