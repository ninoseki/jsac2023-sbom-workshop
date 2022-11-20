import pytest

from jsac2023.python.requirements import parse_requirements


@pytest.mark.parametrize(
    "path,expected_name_and_versions,expected_purls",
    [
        (
            "tests/fixtures/requirements.txt",
            [
                ("fastapi", "0.86.0"),
                ("jinja2", "2.7.1"),
                ("uvicorn", "0.19.0"),
            ],
            [
                "pkg:pypi/fastapi@0.86.0",
                "pkg:pypi/jinja2@2.7.1",
                "pkg:pypi/uvicorn@0.19.0",
            ],
        )
    ],
)
def test_parse_requirements(
    path: str,
    expected_name_and_versions: list[tuple[str, str]],
    expected_purls: list[str],
):
    components = parse_requirements(path)

    name_and_versions = [(c.name, c.version) for c in components]
    for name_and_version in expected_name_and_versions:
        assert name_and_version in name_and_versions

    purls = [str(c.purl) for c in components if c.purl is not None]
    for purl in expected_purls:
        assert purl in purls
