import typer
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component

from jsac2023.cyclonedx import components_to_bom, convert_as_json

from .app import app


def parse_requirements(path: str) -> list[Component]:
    """Parse requirements.txt and convert it into a list of components"""
    raise NotImplementedError()


def get_bom_by_requirements(path: str) -> Bom:
    components = parse_requirements(path)
    return components_to_bom(components)


@app.command(help="Parse requirements.txt and build CycloneDX SBOM")
def requirements(
    path: str = typer.Argument(..., help="Path to requirement.txt")
) -> None:
    components = parse_requirements(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
