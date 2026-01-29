import pytest
def add(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (5,5,10),
    (3,4,7),
])
def test_add(a,b,expected):
    assert add(a,b) == expected
# ---- SKIP TEST ----
@pytest.mark.skip(reason="Feature not implemented yet")
def test_skip_example():
    assert False

# ---- EXPECTED FAILURE ----
@pytest.mark.xfail(reason="Known bug - division by zero")
def test_xfail_example():
    assert 1 / 0