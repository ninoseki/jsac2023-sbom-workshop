from typing import Any

import httpx
from packageurl import PackageURL

from . import schemas

COMPONENT_TYPE_TO_ECOSYSTEM = {
    "pypi": "PyPI",
    "maven": "Maven",
}


def component_type_to_ecosystem(component_type: str) -> str:
    return COMPONENT_TYPE_TO_ECOSYSTEM[component_type.lower()]


class OSV:
    def __init__(self, base_url: str = "https://api.osv.dev", *, timeout: int = 60):
        self.base_url = base_url
        self.timeout = timeout

    def _url_for(self, path: str) -> str:
        return self.base_url + path

    def _post(
        self,
        path: str,
        json=dict[Any, Any],
    ) -> httpx.Response:
        url = self._url_for(path)

        res = httpx.post(url, json=json, timeout=self.timeout)
        res.raise_for_status()

        return res

    def query_by_purl(self, purl: PackageURL) -> schemas.Vulnerabilities:
        ecosystem = component_type_to_ecosystem(purl.type)
        version = str(purl.version)

        name: str = ""
        if purl.namespace is not None:
            name = str(purl.namespace) + ":"

        name += str(purl.name)

        res = self._post(
            "/v1/query",
            json={
                "version": version,
                "package": {"name": name, "ecosystem": ecosystem},
            },
        )
        return schemas.Vulnerabilities.parse_raw(res.content)
