# Dead simple schemas to parse CycloneDX SBOM
# Note that the schemas do not have 100% coverage

from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, Property
from humps import camelize
from packageurl import PackageURL
from pydantic import BaseModel as BaseModel_
from pydantic import Field


class BaseModel(BaseModel_):
    class Config:
        orm_mode = True
        alias_generator = camelize
        allow_population_by_field_name = True


class PropertyModel(BaseModel):
    name: str
    value: str

    def to_property(self) -> Property:
        return Property(name=self.name, value=self.value)


class ComponentModel(BaseModel):
    type: str
    bom_ref: str = Field(..., alias="bom-ref")
    name: str
    version: str
    purl: str

    properties: list[PropertyModel] | None

    def to_component(self) -> Component:
        properties: list[Property] | None = None
        if self.properties is not None:
            properties = [p.to_property() for p in self.properties]

        return Component(
            name=self.name,
            version=self.version,
            purl=PackageURL.from_string(self.purl),
            properties=properties,
        )


class BomModel(BaseModel):
    components: list[ComponentModel]

    def to_bom(self) -> Bom:
        components = [c.to_component() for c in self.components]
        return Bom(components=components)
