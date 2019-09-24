import pytest

@pytest.mark.parametrize("x, ans", [
    (1, 101),
    (2, 202),
])
def test_parametrized(x, ans):
    assert 100 * x + x == ans


@pytest.mark.parametrize("x, ans", [
    (1, 101),
    (2, 202),
], ids=['one', 'two'])
def test_parametrized_with_id(x, ans):
    assert 100 * x + x == ans


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_parametrized_twice(x, y):
    assert x + y > 0
