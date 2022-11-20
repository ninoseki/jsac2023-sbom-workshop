import pytest
import vcr
from packageurl import PackageURL

from jsac2023.osv import OSV, schemas


@pytest.fixture
def osv():
    return OSV()


@pytest.fixture
def maven_purl():
    return PackageURL.from_string(
        "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1"
    )


@vcr.use_cassette("tests/fixtures/vcr_cassettes/osv_query_by_purl.yaml")
def test_query_by_purl_maven(maven_purl: PackageURL, osv: OSV):
    res = osv.query_by_purl(maven_purl)
    assert isinstance(res, schemas.Vulnerabilities)
