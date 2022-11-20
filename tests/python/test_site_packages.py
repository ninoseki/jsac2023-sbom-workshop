import os
import site

import psutil
import pytest

from jsac2023.python.site_packages import get_site_packages


@pytest.fixture
def pid() -> int:
    return os.getpid()


@pytest.fixture
def process(pid: int) -> psutil.Process:
    return psutil.Process(pid)


def test_get_site_packages(process: psutil.Process):
    site_packages = get_site_packages(process)
    assert set(site.getsitepackages()) == site_packages
