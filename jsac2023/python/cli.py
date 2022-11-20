import typer
from cyclonedx.model.component import Component

from jsac2023.cyclonedx.bom import components_to_bom
from jsac2023.utils import convert_as_json

from .process import get_py_processes
from .requirements import parse_requirements
from .site_packages import get_site_packages, site_package_to_components

app = typer.Typer()


@app.command()
def requirements(
    path: str = typer.Argument(..., help="Path to requirement.txt")
) -> None:
    components = parse_requirements(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201


@app.command()
def site_packages() -> None:
    processes = get_py_processes()

    site_packages: set[str] = set()
    for p in processes:
        site_packages.update(get_site_packages(p) or [])

    components: list[Component] = []
    for site_package in site_packages:
        components.extend(site_package_to_components(site_package))

    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
