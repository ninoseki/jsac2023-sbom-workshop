from typing import cast

import typer
from cyclonedx.model.component import Component
from loguru import logger

from jsac2023.cyclonedx.schemas import BomModel
from jsac2023.utils import convert_as_json

from .client import OSV

app = typer.Typer()


@app.command()
def query(path: str = typer.Argument(..., help="Path to CycloneDX SBOM path")) -> None:
    bom_model = BomModel.parse_file(path)
    bom = bom_model.to_bom()

    osv = OSV()

    for component in bom.components:
        logger.info(f"Check {component}...")

        component = cast(Component, component)
        res = osv.query_by_purl(component.purl)

        logger.info(f"{component} has {len(res.vulns)} vulnerabilities")

        for vuln in res.vulns:
            component.add_vulnerability(
                vuln.to_cyclonedx_vulnerability(component=component)
            )

    print(convert_as_json(bom))  # noqa: T201
