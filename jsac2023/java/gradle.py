import pyparsing as pp
from cyclonedx.model.component import Component
from packageurl import PackageURL

alphanums_plus = pp.Word(pp.alphanums + ".-_")
pattern = (
    pp.LineStart()
    + alphanums_plus.set_results_name("group_id")
    + ":"
    + alphanums_plus.set_results_name("artifact_id")
    + ":"
    + alphanums_plus.set_results_name("version")
    + "="
    + alphanums_plus
    + pp.LineEnd()
)


def to_component(*, group_id: str, artifact_id: str, version: str) -> Component:
    component_name = f"{group_id}:{artifact_id}"
    return Component(
        name=component_name,
        version=version,
        purl=PackageURL(
            type="maven", namespace=group_id, name=artifact_id, version=version
        ),
    )


def parse_gradle_lock(path: str) -> list[Component]:
    """Parse gradle.lockfile and convert it into a list of components"""
    components: list[Component] = []

    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            try:
                parsed = pattern.parse_string(line.strip()).as_dict()
            except pp.exceptions.ParseException:
                continue

            group_id = parsed.get("group_id", "")
            artifact_id = parsed.get("artifact_id", "")
            version = parsed.get("version", "")

            components.append(
                to_component(
                    group_id=group_id, artifact_id=artifact_id, version=version
                )
            )

    return components
