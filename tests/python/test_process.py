import pytest

from jsac2023.python.process import python_version


@pytest.mark.parametrize(
    "v,expected", [("Python 3.10.1", True), ("Python 2.6.8", True), ("foo", False)]
)
def test_python_version(v: str, expected: bool):
    assert python_version.matches(v) is expected
