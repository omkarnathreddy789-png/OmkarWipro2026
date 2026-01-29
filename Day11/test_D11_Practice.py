import pytest
#simple test
def test_add():
    assert 2+3==5
#Assertion with message
def test_sub():
    assert 3-2==1,"Subtraction"
#Exception handling
def div(a,b):
    return a/b
def test_div():
    with pytest.raises(ZeroDivisionError):
        div(1,0)
# Pytest Command Line Arguments
# Run all tests
# --->pytest
# Run specific file
# ---->pytest filename.py
# Run a specific test
# ---->pytest test_math.py::test_addition
# Verbose output
# ----->pytest -v
# Show print statements
# ------>pytest -s



