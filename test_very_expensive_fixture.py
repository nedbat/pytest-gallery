import time

import pytest

configurations = [
    pytest.param({"a": 1, "b": 99}, id="ab"),
    pytest.param({"a": 2}, id="a"),
    pytest.param({"a": 3, "b": 1723, "c": 1001}, id="abc"),
]

@pytest.fixture(params=configurations, scope="session")
def options(request):
    time.sleep(1)
    return request.param

def test_with_options(options):
    assert "a" in options

def test_with_options_2(options):
    assert "a" in options

def test_with_options_3(options):
    assert "a" in options
