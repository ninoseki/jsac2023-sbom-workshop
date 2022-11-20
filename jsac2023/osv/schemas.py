from datetime import datetime
from typing import Any, cast

from cvss import CVSS2, CVSS3
from cyclonedx.model.component import Component
from cyclonedx.model.vulnerability import BomTarget
from cyclonedx.model.vulnerability import Vulnerability as CycloneDXVulnerability
from cyclonedx.model.vulnerability import VulnerabilityRating
from pydantic import BaseModel, Field


def severity_to_rating(severity: "Severity") -> VulnerabilityRating | None:
    severity_type_to_cvss = {
        "CVSS_V3": CVSS3,
        "CVSS_V2": CVSS2,
    }

    klass = severity_type_to_cvss.get(severity.type)
    if klass is None:
        return None

    c = cast(CVSS2 | CVSS3, klass(severity.score))
    score, _, _ = c.scores()
    severity_str, _, _ = c.severities()
    severity_str = str(severity_str).lower()

    return VulnerabilityRating(score=score, severity=severity_str)


class Severity(BaseModel):
    type: str
    score: str


class Package(BaseModel):
    ecosystem: str
    name: str
    purl: str | None


class Event(BaseModel):
    introduced: str | None
    fixed: str | None
    last_affected: str | None
    limit: str | None


class Range(BaseModel):
    type: str
    repo: str | None
    events: list[Event]
    database_specific: dict[str, Any] | None


class Affected(BaseModel):
    package: Package
    ranges: list[Range] | None
    versions: list[str] | None
    ecosystem_specific: dict[str, Any] | None
    database_specific: dict[str, Any] | None


class Reference(BaseModel):
    type: str
    url: str


class Credit(BaseModel):
    name: str
    contact: list[str] | None


class Vulnerability(BaseModel):
    schema_version: str | None
    id: str
    modified: datetime
    published: datetime | None
    withdrawn: datetime | None
    aliases: list[str] | None
    related: list[str] | None
    summary: str | None
    details: str | None
    severity: list[Severity] | None
    affected: list[Affected]
    references: list[Reference] | None
    credits: list[Credit] | None
    database_specific: dict[str, Any] | None

    def to_cyclonedx_vulnerability(
        self, component: Component | None = None
    ) -> CycloneDXVulnerability:
        vuln = CycloneDXVulnerability(
            id=self.id,
            detail=self.details,
            updated=self.modified,
            published=self.published,
        )

        ratings = [severity_to_rating(s) for s in self.severity or []]
        ratings = [r for r in ratings if r is not None]
        if len(ratings) > 0:
            vuln.ratings = ratings

        if component is not None:
            vuln.affects = [BomTarget(ref=component.bom_ref.value)]

        if component is not None:
            vuln.affects = [BomTarget(ref=component.bom_ref.value)]

        return vuln


class Vulnerabilities(BaseModel):
    vulns: list[Vulnerability] = Field(default_factory=list)
