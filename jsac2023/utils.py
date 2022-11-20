from functools import lru_cache

import sh
from cyclonedx.model.bom import Bom
from cyclonedx.output import OutputFormat, get_instance


def convert_as_json(bom: Bom) -> str:
    output = get_instance(bom, output_format=OutputFormat.JSON)
    return output.output_as_string()


@lru_cache
def get_command(path: str) -> sh.Command:
    return sh.Command(path)
