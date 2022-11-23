from pathlib import Path

from cyclonedx.model.component import Component


def parse_jar(path: str | Path) -> list[Component]:
    """Parse JAR file and convert it into a list of components"""
    raise NotImplementedError()
