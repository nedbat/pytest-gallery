import sys

import pytest


def should_skip():
    return True


@pytest.mark.skipif(sys.version_info < (2, 0), reason="Python 1.x")
def test_always_run():
    assert 1 == 1


@pytest.mark.skipif(sys.version_info > (2, 0), reason="Python 2.x+")
def test_never_run():
    assert 1 == 13


@pytest.mark.skipif(should_skip(), reason="should_skip")
def test_always_skip():
    assert 1 == 13


@pytest.mark.skipif('should_skip()', reason="should_skip")
def test_always_skip_string():
    assert 1 == 13
