import typer
from cyclonedx.model.component import Component
from packageurl import PackageURL
from pip_audit._dependency_source import RequirementSource, ResolveLibResolver
from pip_audit._service.interface import ResolvedDependency

from jsac2023.cyclonedx import components_to_bom, convert_as_json

from .app import app

"""
# very basic answer:
import pkg_resources

def requirement_to_component(requirement: pkg_resources.Requirement) -> Component:
    _, version = requirement.specs[0]
    return Component(
        name=requirement.project_name,
        version=version,
        purl=PackageURL(type="pypi", name=requirement.project_name, version=version),
    )

def parse_requirements(path: str) -> list[Component]:
    components: list[Component] = []

    with open(path, "r") as f:
        for r in pkg_resources.parse_requirements(f.read()):
            components.append(requirement_to_component(r))

    return components
"""


def dependency_to_component(dependency: ResolvedDependency) -> Component:
    return Component(
        name=dependency.name,
        version=str(dependency.version),
        purl=PackageURL(
            type="pypi", name=dependency.name, version=str(dependency.version)
        ),
    )


def parse_requirements(path: str) -> list[Component]:
    """Parse requirements.txt and convert it into a list of components"""
    source = RequirementSource(filenames=[path], resolver=ResolveLibResolver())
    return [dependency_to_component(dependency) for dependency in source.collect()]


@app.command(help="Parse requirements.txt and build CycloneDX SBOM")
def requirements(
    path: str = typer.Argument(..., help="Path to requirement.txt")
) -> None:
    components = parse_requirements(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
