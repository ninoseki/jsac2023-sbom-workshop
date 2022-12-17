from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.output import OutputFormat, get_instance


def convert_as_json(bom: Bom) -> str:
    output = get_instance(bom, output_format=OutputFormat.JSON)
    return output.output_as_string()


def uniquify_components(components: list[Component]):
    """Uniquify components by PURL"""
    filtered: list[Component] = []
    seen: set[str] = set()

    for component in components:
        # assuming every component has purl
        purl_str = str(component.purl)
        if purl_str in seen:
            continue

        filtered.append(component)
        seen.add(purl_str)

    return filtered


def components_to_bom(components: list[Component], uniquify: bool = True) -> Bom:
    """Convert components into a BOM"""
    if uniquify:
        components = uniquify_components(components)

    return Bom(components=components)
