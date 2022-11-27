import asyncio
import functools
from typing import cast

import aiometer
import typer
from cyclonedx.model.component import Component
from loguru import logger

from jsac2023.cyclonedx.schemas import BomModel
from jsac2023.utils import convert_as_json

from .client import OSV

app = typer.Typer()


async def check_component(osv: OSV, component: Component):
    logger.info(f"Check {component.purl}...")

    component = cast(Component, component)
    res = await osv.query_by_purl(component.purl)

    logger.info(f"{component.purl} has {len(res.vulns)} vulnerabilities")

    for vuln in res.vulns:
        component.add_vulnerability(
            vuln.to_cyclonedx_vulnerability(component=component)
        )


@app.command()
def query(
    path: str = typer.Argument(..., help="Path to CycloneDX SBOM path"),
    max_at_once: int = typer.Option(4, help="Max number of concurrent HTTP requests"),
) -> None:
    bom_model = BomModel.parse_file(path)
    bom = bom_model.to_bom()

    osv = OSV()

    jobs = [functools.partial(check_component, osv, c) for c in bom.components]
    asyncio.run(aiometer.run_any(jobs, max_at_once=max_at_once))

    print(convert_as_json(bom))  # noqa: T201
