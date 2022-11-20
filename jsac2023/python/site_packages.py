import json
from typing import cast

import pkg_resources
import psutil
from cyclonedx.model.component import Component, Property
from packageurl import PackageURL

from jsac2023.utils import get_command

from .process import am_i_root, get_python_in_cmdline


def get_site_packages(process: psutil.Process) -> set[str]:
    """Get site packages used by a Python process"""
    site_packages: set[str] = set()
    output = None

    # Python may be nested like the following:
    # - exe: /usr/local/bin/python3.10
    # - cmdline: [/home/vscode/.cache/pypoetry/virtualenvs/jsac2023-oBdw23Ej-py3.10/bin/python]
    # (when using virtualenv)
    try:
        exe = get_python_in_cmdline(process.cmdline()) or process.exe()
        user = process.username()
    except psutil.Error:
        return site_packages

    get_site_packages_command = (
        "import site;import json;print(json.dumps(site.getsitepackages()))"
    )
    if am_i_root():
        sudo = get_command("sudo")
        try:
            c = f'{exe} -c "{get_site_packages_command}"'
            output = sudo("su", user, "-c", c)
        except Exception:
            return site_packages
    else:
        py = get_command(exe)
        try:
            output = py("-c", get_site_packages_command)
        except Exception:
            return site_packages

    if output is None:
        return site_packages

    site_packages_ = cast(list[str], json.loads(str(output)))
    site_packages.update(site_packages_)

    return site_packages


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
