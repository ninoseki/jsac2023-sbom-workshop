# SBOM 101

- [What is SBOM?](#what-is-sbom)
- [SBOM use cases](#sbom-use-cases)
- [SBOM standards](#sbom-standards)
- [SBOM types](#sbom-types)
- [Why CycloneDX?](#why-cyclonedx)
- [Package URL](#package-url)
- [SBOM examples with/without package URL](#sbom-examples-withwithout-package-url)

## What is SBOM?

> A “software bill of materials” (SBOM) has emerged as a key building block in software security and software supply chain risk management. A SBOM is a nested inventory, a list of ingredients that make up software components.
>
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

#### CycloneDX example

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "version": 1,
  "components": [
    {
      "bom-ref": "pkg:pypi/requests@2.18.1?package-id=eb69e0d8ffbe36cd",
      "type": "library",
      "name": "requests",
      "version": "2.18.1",
      "cpe": "cpe:2.3:a:python-requests:python-requests:2.18.1:*:*:*:*:*:*:*",
      "purl": "pkg:pypi/requests@2.18.1"
    }
  ]
}
```

### SPDX

- [Overview](https://spdx.dev/about/)
- [JSON schema (spdx/spdx-spec)](https://github.com/spdx/spdx-spec/blob/development/v2.3.1/schemas/spdx-schema.json)
- [Examples (spdx/spdx-spec)](https://github.com/spdx/spdx-spec/tree/development/v2.3.1/examples)

#### SPDX example

```json
{
  "spdxVersion": "SPDX-2.2",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "dummy",
  "creationInfo": {
    "created": "2022-12-18T01:41:33Z",
    "creators": []
  },
  "documentDescribes": ["SPDXRef-RootPackage"],
  "packages": [
    {
      "name": "requests",
      "SPDXID": "SPDXRef-Package-A246603723488138A7C126B0E7E0441D189E84D136E3CC4250114C790EFFCE80",
      "versionInfo": "2.18.1",
      "externalRefs": [
        {
          "referenceCategory": "PACKAGE-MANAGER",
          "referenceType": "purl",
          "referenceLocator": "pkg:pypi/requests@2.18.1"
        }
      ]
    }
  ]
}
```

### SWID

- [Overview](https://csrc.nist.gov/projects/Software-Identification-SWID)
- [SWID Tag tools](https://pages.nist.gov/swid-tools/)

## SBOM types

![](https://i.imgur.com/aWjPAgB.png)

(Source: [Satisfying Safety Standards with the SPDX Build Profile - Brandon Lum, Google & Kate Stewart, The Linux Foundation](https://static.sched.com/hosted_files/ocs2022/25/OSS%20JP_%20Satisfying%20Safety%20Standards%20with%20the%20SPDX%20Build%20Profile.pdf))

## Why CycloneDX?

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I’ve looked into SWID and SPDX and neither in their current state are robust enough to be used for software security. So ended up writing <a href="https://twitter.com/hashtag/CycloneDX?src=hash&amp;ref_src=twsrc%5Etfw">#CycloneDX</a> because nothing else existed. Support for <a href="https://twitter.com/hashtag/PackageURL?src=hash&amp;ref_src=twsrc%5Etfw">#PackageURL</a> is crucial in identifying a components ecosystem though. <a href="https://twitter.com/hashtag/SBoM?src=hash&amp;ref_src=twsrc%5Etfw">#SBoM</a> <a href="https://twitter.com/hashtag/NTIA?src=hash&amp;ref_src=twsrc%5Etfw">#NTIA</a></p>&mdash; Steve Springett (@stevespringett@infosec.exchange) (@stevespringett) <a href="https://twitter.com/stevespringett/status/1019980949730283520?ref_src=twsrc%5Etfw">July 19, 2018</a></blockquote>

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
>
> --- https://github.com/package-url/purl-spec

- Examples:
  - `pkg:pypi/requests@2.28.1`
    - https://pypi.org/project/requests/2.28.1/
  - `pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1` (or `pkg:gradle/org.apache.logging.log4j/log4j-core@2.14.1`)
    - https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core/2.14.1
    - Note: `org.apache.logging.log4j` is a namespace (= Maven Group ID)

## SBOM examples with/without package URL

### CycloneDX

**Without Package URL**

```json
{
  "bom-ref": "dummy",
  "type": "library",
  "name": "requests",
  "version": "2.18.1"
}
```

**With Package URL**

```json
{
  "bom-ref": "dummy",
  "type": "library",
  "name": "requests",
  "version": "2.18.1",
  "purl": "pkg:pypi/requests@2.18.1"
}
```

### SPDX

**Without Package URL**

```json
{
  "name": "requests",
  "SPDXID": "SPDXRef-Package-A246603723488138A7C126B0E7E0441D189E84D136E3CC4250114C790EFFCE80",
  "versionInfo": "2.18.1"
}
```

**With Package URL**

```json
{
  "name": "requests",
  "SPDXID": "SPDXRef-Package-A246603723488138A7C126B0E7E0441D189E84D136E3CC4250114C790EFFCE80",
  "versionInfo": "2.18.1",
  "externalRefs": [
    {
      "referenceCategory": "PACKAGE-MANAGER",
      "referenceType": "purl",
      "referenceLocator": "pkg:pypi/requests@2.18.1"
    }
  ]
}
```
