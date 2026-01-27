import pytest

# ---------- APPLICATION CODE (Calculator) ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ---------- xUNIT STYLE SETUP & TEARDOWN ----------

def setup_module(module):
    print("\nSetup module - start resources")

def teardown_module(module):
    print("\nTeardown module - release resources")

def setup_function(function):
    print("\nSetup function")

def teardown_function(function):
    print("\nTeardown function")


# ---------- FIXTURES (normally in conftest.py) ----------

@pytest.fixture(scope="module")
def operations():
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

@pytest.fixture(scope="function")
def numbers():
    return (10, 2)


# ---------- TEST FILE 1 (basic tests) ----------

def test_add_basic():
    assert add(2, 3) == 5

def test_subtract_basic():
    assert subtract(5, 3) == 2


# ---------- TEST FILE 2 (fixture-based tests) ----------

def test_add_with_fixture(operations, numbers):
    a, b = numbers
    assert operations["add"](a, b) == 12

def test_multiply_with_fixture(operations, numbers):
    a, b = numbers
    assert operations["multiply"](a, b) == 20

def test_divide_exception(operations):
    with pytest.raises(ValueError):
        operations["divide"](10, 0)
