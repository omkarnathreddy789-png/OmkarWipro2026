import pytest

# -------- Calculator Module --------

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


calc = Calculator()

# -------- Pytest Test Cases --------

def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(5, 2) == 3


def test_multiply():
    assert calc.multiply(4, 3) == 12


def test_divide():
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
