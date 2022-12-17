import pkg_resources
import psutil
from cyclonedx.model.component import Component, Property
from packageurl import PackageURL

from jsac2023.cyclonedx import components_to_bom, convert_as_json

from .app import app
from .process import get_py_processes


def get_site_packages(process: psutil.Process) -> set[str]:
    """Get site packages used by a Python process"""
    raise NotImplementedError()


def distribution_to_component(dist: pkg_resources.Distribution) -> Component:
    """Convert a distribution into a component"""
    return Component(
        name=dist.project_name,
        version=dist.version,
        purl=PackageURL(type="pypi", name=dist.project_name, version=dist.version),
        properties=[
            Property(name="location", value=dist.location),
        ],
    )


def site_package_to_distributions(
    site_package: str,
) -> list[pkg_resources.Distribution]:
    """Convert a site package into a list of distributions"""
    return [dist for dist in pkg_resources.find_distributions(site_package)]


def site_package_to_components(site_package: str) -> list[Component]:
    """Convert a site package into a list of components"""
    distributions = site_package_to_distributions(site_package)
    return [distribution_to_component(d) for d in distributions]


@app.command(
    help="Build CycloneDX SBOM based on site packages used by running Python processes"
)
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
