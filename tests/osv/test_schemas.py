import pytest
from cyclonedx.model.component import Component
from cyclonedx.model.vulnerability import BomTarget

from jsac2023.cyclonedx.schemas import ComponentModel
from jsac2023.osv.schemas import Vulnerability


@pytest.fixture
def osv_vuln():
    return Vulnerability.parse_file("tests/fixtures/osv/vuln.json")


def test_to_cyclonedx_vulnerability(osv_vuln: Vulnerability):
    cyclonedx_vuln = osv_vuln.to_cyclonedx_vulnerability()

    assert cyclonedx_vuln.id == osv_vuln.id
    assert cyclonedx_vuln.detail == osv_vuln.details
    assert len(cyclonedx_vuln.ratings) > 0

    assert len(cyclonedx_vuln.affects) == 0


@pytest.fixture
def cyclonedx_component():
    return ComponentModel.parse_file(
        "tests/fixtures/cyclonedx/component.json"
    ).to_component()


def test_to_cyclonedx_vulnerability_with_component(
    osv_vuln: Vulnerability, cyclonedx_component: Component
):
    cyclonedx_vuln = osv_vuln.to_cyclonedx_vulnerability(component=cyclonedx_component)

    bom_targets: set[BomTarget] = {a for a in cyclonedx_vuln.affects}
    bom_refs = {t.ref for t in bom_targets}
    assert bom_refs == {cyclonedx_component.bom_ref.value}
