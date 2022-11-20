from cyclonedx.model.component import Component


def parse_gradle_lock(path: str) -> list[Component]:
    """Parse gradle.lockfile and convert it into a list of components"""
    raise NotImplementedError()
