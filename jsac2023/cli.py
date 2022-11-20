import typer

from .java.cli import app as java_app
from .osv.cli import app as osv_app
from .python.cli import app as python_app

app = typer.Typer()
app.add_typer(python_app, name="python")
app.add_typer(java_app, name="java")
app.add_typer(osv_app, name="osv")


if __name__ == "__main__":
    app()
