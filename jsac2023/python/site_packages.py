import pkg_resources
import psutil
from cyclonedx.model.component import Component, Property
from packageurl import PackageURL


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
