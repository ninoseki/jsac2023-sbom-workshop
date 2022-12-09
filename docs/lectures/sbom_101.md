- [What is SBOM?](#what-is-sbom)
- [SBOM use cases](#sbom-use-cases)
- [SBOM standards](#sbom-standards)
  * [CycloneDX](#cyclonedx)
  * [SPDX](#spdx)
  * [SWID](#swid)
- [Why CycloneDX?](#why-cyclonedx)
- [Package URL](#package-url)

## What is SBOM?

> A “software bill of materials” (SBOM) has emerged as a key building block in software security and software supply chain risk management. A SBOM is a nested inventory, a list of ingredients that make up software components.
> --- https://www.cisa.gov/sbom

## SBOM use cases

- Compliance/license management
- Vulnerability management

## SBOM standards

- [OWASP - CycloneDX](https://cyclonedx.org/)
- [Linux Foundation - The Software Package Data Exchange (SPDX)](https://spdx.dev/)
- [NIST - Software Identification (SWID)](https://csrc.nist.gov/projects/Software-Identification-SWID)

![](https://i.imgur.com/maPJgMX.png)
(Source: [NITA: Framing Software Component Transparency: Establishing a Common Software Bill of Materials (SBOM)](https://ntia.gov/files/ntia/publications/ntia_sbom_framing_2nd_edition_20211021.pdf))

### CycloneDX

- [Overview](https://cyclonedx.org/specification/overview/)
- [JSON schema](https://cyclonedx.org/docs/1.4/json/#vulnerabilities)
- [CycloneDX/bom-examples](https://github.com/CycloneDX/bom-examples)

### SPDX

- [Overview](https://spdx.dev/about/)
- [JSON schema (spdx/spdx-spec)](https://github.com/spdx/spdx-spec/blob/development/v2.3.1/schemas/spdx-schema.json)
- [Examples (spdx/spdx-spec)](https://github.com/spdx/spdx-spec/tree/development/v2.3.1/examples)

### SWID

- [Overview](https://csrc.nist.gov/projects/Software-Identification-SWID)
- [SWID Tag tools](https://pages.nist.gov/swid-tools/)

## Why CycloneDX?

![img](https://i.imgur.com/YcO4jVg.png)
(https://twitter.com/stevespringett/status/1019980949730283520)

Note: SPDX supports the package URL since 2019. ([chapters/appendix-VI: Add PURL #152](https://github.com/spdx/spdx-spec/pull/152))

## Package URL

> A purl is a URL composed of seven components:
>
> scheme:type/namespace/name@version?qualifiers#subpath
> Components are separated by a specific character for unambiguous > parsing.
>
> The definition for each components is:
>
> **scheme**: this is the URL scheme with the constant value of "pkg". One of the primary reason for this single scheme is to facilitate the future official registration of the "pkg" scheme for package URLs. Required.
> **type**: the package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. Required.
> **namespace**: some name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Optional and type-specific.
> **name**: the name of the package. Required.
> **version**: the version of the package. Optional.
> **qualifiers**: extra qualifying data for a package such as an OS, architecture, a distro, etc. Optional and type-specific.
> **subpath**: extra subpath within a package, relative to the package root. Optional.
> --- https://github.com/package-url/purl-spec

- Examples:
  - `pkg:pypi/requests@2.28.1`
    - https://pypi.org/project/requests/2.28.1/
  - `pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1` (or `pkg:gradle/org.apache.logging.log4j/log4j-core@2.14.1`)
    - https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core/2.14.1
    - Note: `org.apache.logging.log4j` is a namespace (= Maven Group ID)
