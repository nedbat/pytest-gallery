import pytest

@pytest.fixture
def some_data():
    return [1, 2, 3]


def test_fixture(some_data):
    assert len(some_data) == 3


@pytest.fixture
def more_data(some_data):
    return [2*x for x in some_data]


def test_two_fixtures(some_data, more_data):
    assert len(some_data) == len(more_data)
