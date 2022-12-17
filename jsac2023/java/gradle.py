import typer
from cyclonedx.model.component import Component

from jsac2023.cyclonedx.bom import components_to_bom, convert_as_json

from .app import app


def parse_gradle_lock(path: str) -> list[Component]:
    """Parse gradle.lockfile and convert it into a list of components"""
    raise NotImplementedError()


@app.command(help="Parse gradle.lockfile and build CycloneDX SBOM")
def gradle(path: str = typer.Argument(..., help="Path to gradle.lockfile")) -> None:
    components = parse_gradle_lock(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
