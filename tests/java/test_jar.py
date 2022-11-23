import pytest

from jsac2023.java.jar import parse_jar


@pytest.mark.parametrize(
    "path,expected_name_and_versions,expected_purls",
    [
        (
            "tests/fixtures/spring-boot-application.jar",
            [
                ("com.fasterxml.jackson.core:jackson-annotations", "2.13.0"),
                ("com.fasterxml.jackson.core:jackson-core", "2.13.0"),
                ("com.fasterxml.jackson.core:jackson-databind", "2.13.0"),
                ("com.fasterxml.jackson.datatype:jackson-datatype-jdk8", "2.13.0"),
                ("com.fasterxml.jackson.datatype:jackson-datatype-jsr310", "2.13.0"),
                (
                    "com.fasterxml.jackson.module:jackson-module-parameter-names",
                    "2.13.0",
                ),
                ("jakarta.annotation:jakarta.annotation-api", "1.3.5"),
                ("org.apache.logging.log4j:log4j-api", "2.14.1"),
                ("org.apache.logging.log4j:log4j-core", "2.14.1"),
                ("org.apache.logging.log4j:log4j-jul", "2.14.1"),
                ("org.apache.logging.log4j:log4j-slf4j-impl", "2.14.1"),
                ("org.slf4j:jul-to-slf4j", "1.7.32"),
                ("org.slf4j:slf4j-api", "1.7.32"),
                ("org.yaml:snakeyaml", "1.29"),
            ],
            [
                "pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.13.0",
                "pkg:maven/com.fasterxml.jackson.core/jackson-core@2.13.0",
                "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.0",
                "pkg:maven/com.fasterxml.jackson.datatype/jackson-datatype-jdk8@2.13.0",
                "pkg:maven/com.fasterxml.jackson.datatype/jackson-datatype-jsr310@2.13.0",
                "pkg:maven/com.fasterxml.jackson.module/jackson-module-parameter-names@2.13.0",
                "pkg:maven/jakarta.annotation/jakarta.annotation-api@1.3.5",
                "pkg:maven/org.apache.logging.log4j/log4j-api@2.14.1",
                "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1",
                "pkg:maven/org.apache.logging.log4j/log4j-jul@2.14.1",
                "pkg:maven/org.apache.logging.log4j/log4j-slf4j-impl@2.14.1",
                "pkg:maven/org.slf4j/jul-to-slf4j@1.7.32",
                "pkg:maven/org.slf4j/slf4j-api@1.7.32",
                "pkg:maven/org.yaml/snakeyaml@1.29",
            ],
        )
    ],
)
def test_parse_jar(
    path: str,
    expected_name_and_versions: list[tuple[str, str]],
    expected_purls: list[str],
):
    components = parse_jar(path)

    name_and_versions = [(c.name, c.version) for c in components]
    for name_and_version in expected_name_and_versions:
        assert name_and_version in name_and_versions

    purls = [str(c.purl) for c in components if c.purl is not None]
    for purl in expected_purls:
        assert purl in purls
