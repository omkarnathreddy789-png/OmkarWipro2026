import pytest

@pytest.fixture
def data():
    return [1,2,3]

def test_one(data):
    assert 2 in data

def test_two(data):

    assert len(data)==3
