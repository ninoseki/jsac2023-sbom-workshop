- [Very basics of CycloneDX/cyclonedx-python-lib](#very-basics-of-cyclonedxcyclonedx-python-lib)
- [microsoft/sbom-tool](#microsoftsbom-tool)
- [anchore/syft](#anchoresyft)

## Very basics of CycloneDX/cyclonedx-python-lib

- [CycloneDX/cyclonedx-python-lib](https://github.com/CycloneDX/cyclonedx-python-lib) ([Docs](https://cyclonedx-python-library.readthedocs.io/en/latest/))

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

### How it works

`sbom-tool` scans the filesystem along with [microsoft/component-detection](https://github.com/microsoft/component-detection).

`component-detection` supports the following ecosystems.

| Ecosystem | Detection mechanisms                                                                                                       |
|-----------|----------------------------------------------------------------------------------------------------------------------------|
| Cargo     | `Cargo.lock` or `Cargo.toml`                                                                                               |
| CocoaPods | `Podfile.lock`                                                                                                             |
| Go        | `go list -m -json all`, `go mod graph`, `go.mod`, `go.sum`                                                                 |
| Gradle    | `.lockfile`                                                                                                                |
| Maven     | `pom.xml` or `mvn dependency:tree -f {pom.xml}`                                                                            |
| NPM       | `package.json`, `package-lock.json`, `npm-shrinkwrap.json`, `lerna.json`,`yarn.lock` (Yarn), `pnpm-lock.yaml` (Pnpm), etc. |
| NuGet     | `project.assets.json`, `.nupkg`, `.nuspec`, `nuget.config`                                                                 |
| PyPI      | `setup.py`, `requirements.txt`, `poetry.lock` (Poetry), etc.                                                               |
| RubyGems  | `Gemfile.lock`                                                                                                             |

(Based on `sbom-tool` v0.3.1 / `component-detection` v2.0.9)

See https://github.com/microsoft/component-detection/blob/main/docs/feature-overview.md for more details.

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

### How it works

`syft` scans the filesystem with supporting the following ecosystems and others.

| Ecosystem            | Notes                                                                                 |
|----------------------|---------------------------------------------------------------------------------------|
| .NET                 | `.deps.json`                                                                          |
| Cargo                | Inspecting Rust executable (`cargo-audit` is required), `Cargo.lock`                  |
| CocoaPods            | `Podfile.lock`                                                                        |
| Conan (C/C++)        | `conanfile.txt`, `conanfile.lock`                                                     |
| Go                   | Inspecting Go executable, `go.mod`                                                    |
| Stack (Haskell)      | `stack.yaml`, `stack.yaml.lock`                                                       |
| Maven                | `MANIFEST.MF`, `pom.properties`, `pom.xml`                                            |
| NPM                  | `package.json`, `package-lock.json`, `yarn.lock` (Yarn), `pnpm-lock.yaml` (Pnpm)      |
| Packagist (Composer) | `composer.lock`, `installed.json`                                                     |
| Pub (Dart)           | `pubspec.lock`                                                                        |
| PyPI                 | `setup.py`, `requirements.txt`, `pipfile.lock` (Pipenv), `poetry.lock` (Poetry), etc. |
| RubyGems             | `Gemfile.lock`, `.gemspec`                                                            |

(Based on `syft` v0.62.3)

See https://github.com/anchore/syft/tree/main/syft/pkg/cataloger for more details.
