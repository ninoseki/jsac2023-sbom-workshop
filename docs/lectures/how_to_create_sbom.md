- [Very basics of CycloneDX/cyclonedx-python](#very-basics-of-cyclonedxcyclonedx-python)
- [microsoft/sbom-tool](#microsoftsbom-tool)
- [anchore/syft](#anchoresyft)

## Very basics of CycloneDX/cyclonedx-python

```python
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output import OutputFormat, get_instance
from packageurl import PackageURL

component_name = "requests"
component_version = "2.18.1"

component = Component(
    name=component_name,
    version=component_version,
    component_type=ComponentType.LIBRARY,
    purl=PackageURL(type="pypi", name=component_name, version=component_version),
)

bom = Bom(components=[component])

output_instance = get_instance(bom, output_format=OutputFormat.JSON)
print(output_instance.output_as_string())
```

## microsoft/sbom-tool

> The SBOM tool is a highly scalable and enterprise ready tool to create SPDX 2.2 compatible SBOMs for any variety of artifacts.
> --- https://github.com/microsoft/sbom-tool

**Usage**

```bash
sbom-tool generate -b <drop path> -bc <build components path> -pn <package name> -pv <package version> -ps <package supplier> -nsb <namespace uri base>
```

```bash
# create SPDX SBOM from requirements.txt
sbom-tool generate -b ./ -bc /app/python-vulnerable-app/ -nsb http://example.com -pn foo -pv 0.1 -ps foo
cat _manifest/spdx_2.2/manifest.spdx.json | jq ".packages[] | .externalRefs[]? | .referenceLocator"

rm -rf _manifest/

# create SPDX SBOM from gradle.lockfile
sbom-tool generate -b ./ -bc /app/log4j-vulnerable-app/ -nsb http://example.com -pn foo -pv 0.1 -ps foo
cat _manifest/spdx_2.2/manifest.spdx.json | jq ".packages[] | .externalRefs[]? | .referenceLocator"
```

- Notes:
  - `sbom-tool` v0.3.0 overlooks a PyPI requirement which has extras.

## anchore/syft

> A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems. Exceptional for vulnerability detection when used with a scanner like Grype.
> --- https://github.com/anchore/syft

**Usage**

```bash
syft <image_or_path> -o <format>
```

```bash
syft /app/python-vulnerable-app/ -o cyclonedx-json | jq ".components[] | .purl"
syft /app/log4j-vulnerable-app/ -o cyclonedx-json | jq ".components[] | .purl"
```
