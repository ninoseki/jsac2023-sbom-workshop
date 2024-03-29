import typer
from cyclonedx.model.component import Component

from jsac2023.cyclonedx import components_to_bom, convert_as_json

from .app import app


def parse_jar(path: str) -> list[Component]:
    """Parse JAR file and convert it into a list of components"""
    raise NotImplementedError()


@app.command(help="Parse JAR file and build CycloneDX SBOM")
def jar(path: str = typer.Argument(..., help="Path to JAR file")) -> None:
    components = parse_jar(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
