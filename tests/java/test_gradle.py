import pytest

from jsac2023.java.gradle import parse_gradle_lock


@pytest.mark.parametrize(
    "path,expected_name_and_versions,expected_purls",
    [
        (
            "tests/fixtures/gradle.lockfile",
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
                ("com.fasterxml.jackson:jackson-bom", "2.13.0"),
                ("jakarta.annotation:jakarta.annotation-api", "1.3.5"),
                ("org.apache.logging.log4j:log4j-api", "2.14.1"),
                ("org.apache.logging.log4j:log4j-core", "2.14.1"),
                ("org.apache.logging.log4j:log4j-jul", "2.14.1"),
                ("org.apache.logging.log4j:log4j-slf4j-impl", "2.14.1"),
                ("org.apache.tomcat.embed:tomcat-embed-core", "9.0.55"),
                ("org.apache.tomcat.embed:tomcat-embed-el", "9.0.55"),
                ("org.apache.tomcat.embed:tomcat-embed-websocket", "9.0.55"),
                ("org.slf4j:jul-to-slf4j", "1.7.32"),
                ("org.slf4j:slf4j-api", "1.7.32"),
                ("org.springframework.boot:spring-boot", "2.6.1"),
                ("org.springframework.boot:spring-boot-autoconfigure", "2.6.1"),
                ("org.springframework.boot:spring-boot-starter", "2.6.1"),
                ("org.springframework.boot:spring-boot-starter-json", "2.6.1"),
                ("org.springframework.boot:spring-boot-starter-log4j2", "2.6.1"),
                ("org.springframework.boot:spring-boot-starter-tomcat", "2.6.1"),
                ("org.springframework.boot:spring-boot-starter-web", "2.6.1"),
                ("org.springframework:spring-aop", "5.3.13"),
                ("org.springframework:spring-beans", "5.3.13"),
                ("org.springframework:spring-context", "5.3.13"),
                ("org.springframework:spring-core", "5.3.13"),
                ("org.springframework:spring-expression", "5.3.13"),
                ("org.springframework:spring-jcl", "5.3.13"),
                ("org.springframework:spring-web", "5.3.13"),
                ("org.springframework:spring-webmvc", "5.3.13"),
                ("org.yaml:snakeyaml", "1.29"),
            ],
            [
                "pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.13.0",
                "pkg:maven/com.fasterxml.jackson.core/jackson-core@2.13.0",
                "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.13.0",
                "pkg:maven/com.fasterxml.jackson.datatype/jackson-datatype-jdk8@2.13.0",
                "pkg:maven/com.fasterxml.jackson.datatype/jackson-datatype-jsr310@2.13.0",
                "pkg:maven/com.fasterxml.jackson.module/jackson-module-parameter-names@2.13.0",
                "pkg:maven/com.fasterxml.jackson/jackson-bom@2.13.0",
                "pkg:maven/jakarta.annotation/jakarta.annotation-api@1.3.5",
                "pkg:maven/org.apache.logging.log4j/log4j-api@2.14.1",
                "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1",
                "pkg:maven/org.apache.logging.log4j/log4j-jul@2.14.1",
                "pkg:maven/org.apache.logging.log4j/log4j-slf4j-impl@2.14.1",
                "pkg:maven/org.apache.tomcat.embed/tomcat-embed-core@9.0.55",
                "pkg:maven/org.apache.tomcat.embed/tomcat-embed-el@9.0.55",
                "pkg:maven/org.apache.tomcat.embed/tomcat-embed-websocket@9.0.55",
                "pkg:maven/org.slf4j/jul-to-slf4j@1.7.32",
                "pkg:maven/org.slf4j/slf4j-api@1.7.32",
                "pkg:maven/org.springframework.boot/spring-boot-autoconfigure@2.6.1",
                "pkg:maven/org.springframework.boot/spring-boot-starter-json@2.6.1",
                "pkg:maven/org.springframework.boot/spring-boot-starter-log4j2@2.6.1",
                "pkg:maven/org.springframework.boot/spring-boot-starter-tomcat@2.6.1",
                "pkg:maven/org.springframework.boot/spring-boot-starter-web@2.6.1",
                "pkg:maven/org.springframework.boot/spring-boot-starter@2.6.1",
                "pkg:maven/org.springframework.boot/spring-boot@2.6.1",
                "pkg:maven/org.springframework/spring-aop@5.3.13",
                "pkg:maven/org.springframework/spring-beans@5.3.13",
                "pkg:maven/org.springframework/spring-context@5.3.13",
                "pkg:maven/org.springframework/spring-core@5.3.13",
                "pkg:maven/org.springframework/spring-expression@5.3.13",
                "pkg:maven/org.springframework/spring-jcl@5.3.13",
                "pkg:maven/org.springframework/spring-web@5.3.13",
                "pkg:maven/org.springframework/spring-webmvc@5.3.13",
                "pkg:maven/org.yaml/snakeyaml@1.29",
            ],
        )
    ],
)
def test_parse_gradle_lock(
    path: str,
    expected_name_and_versions: list[tuple[str, str]],
    expected_purls: list[str],
):
    components = parse_gradle_lock(path)

    name_and_versions = [(c.name, c.version) for c in components]
    for name_and_version in expected_name_and_versions:
        assert name_and_version in name_and_versions

    purls = [str(c.purl) for c in components if c.purl is not None]
    for purl in expected_purls:
        assert purl in purls
