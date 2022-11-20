import typer

from jsac2023.cyclonedx.bom import components_to_bom
from jsac2023.utils import convert_as_json

from .gradle import parse_gradle_lock

app = typer.Typer()


@app.command()
def gradle(path: str = typer.Argument(..., help="Path to gradle.lockfile")) -> None:
    components = parse_gradle_lock(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
