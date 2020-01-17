import time

import pytest

configurations = [
    pytest.param({"a": 1, "b": 99}, id="ab"),
    pytest.param({"a": 2}, id="a"),
    pytest.param({"a": 3, "b": 1723, "c": 1001}, id="abc"),
]

@pytest.fixture(params=configurations, scope="session")
def options(request):
    time.sleep(2)
    return request.param

def test_with_options(options):
    assert options == 17

def test_with_options_2(options):
    assert options == 17

def test_with_options_3(options):
    assert options == 17
