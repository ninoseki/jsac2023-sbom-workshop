import tempfile
import zipfile
from pathlib import Path

import typer
from cyclonedx.model.component import Component
from packageurl import PackageURL

from jsac2023.cyclonedx import components_to_bom, convert_as_json

from .app import app


def to_component(*, group: str, artifact: str, version: str) -> Component:
    component_name = f"{group}:{artifact}"
    return Component(
        name=component_name,
        version=version,
        purl=PackageURL(type="maven", namespace=group, name=artifact, version=version),
    )


def parse_pom_properties(path: str | Path) -> Component | None:
    memo: dict[str, str] = {}

    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                continue

            try:
                key, value = line.strip().split("=")
                memo[key] = value
            except Exception:
                pass

    group = memo.get("groupId")
    artifact = memo.get("artifactId")
    version = memo.get("version")

    if group is None or artifact is None or version is None:
        return None

    return to_component(group=group, artifact=artifact, version=version)


def unzip_jar(path: str | Path, *, destination: str):
    with zipfile.ZipFile(path) as zip:
        names = [Path(name) for name in zip.namelist()]

        # Extract .jar or .properties files
        jar_or_properties = [
            str(name) for name in names if name.suffix in [".jar", ".properties"]
        ]
        zip.extractall(destination, members=jar_or_properties)


def parse_jar(path: str | Path) -> list[Component]:
    """Parse JAR file and convert it into a list of components"""
    components: list[Component] = []

    with tempfile.TemporaryDirectory() as destination:
        # unzip JAR file into a temporal directory
        unzip_jar(path, destination=destination)

        pom_properties = Path(destination).glob("**/pom.properties")
        pom_components = [parse_pom_properties(p) for p in pom_properties]
        components.extend([c for c in pom_components if c is not None])

        jar_paths = Path(destination).glob("**/*.jar")
        for jar_path in jar_paths:
            components.extend(parse_jar(jar_path))

    return components


@app.command(help="Parse JAR file and build CycloneDX SBOM")
def jar(path: str = typer.Argument(..., help="Path to JAR file")) -> None:
    components = parse_jar(path)
    bom = components_to_bom(components)
    print(convert_as_json(bom))  # noqa: T201
