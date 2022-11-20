import pyparsing as pp
from cyclonedx.model.component import Component
from packageurl import PackageURL

alphanums_plus = pp.Word(pp.alphanums + ".-_")
pattern = (
    pp.LineStart()
    + alphanums_plus.set_results_name("group")
    + ":"
    + alphanums_plus.set_results_name("artifact")
    + ":"
    + alphanums_plus.set_results_name("version")
    + "="
    + alphanums_plus
    + pp.LineEnd()
)


def to_component(*, group: str, artifact: str, version: str) -> Component:
    component_name = f"{group}:{artifact}"
    return Component(
        name=component_name,
        version=version,
        purl=PackageURL(type="maven", namespace=group, name=artifact, version=version),
    )


def parse_gradle_lock(path: str) -> list[Component]:
    components: list[Component] = []

    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            try:
                parsed = pattern.parse_string(line.strip()).as_dict()
            except pp.exceptions.ParseException:
                continue

            group = parsed.get("group", "")
            artifact = parsed.get("artifact", "")
            version = parsed.get("version", "")

            components.append(
                to_component(group=group, artifact=artifact, version=version)
            )

    return components
