#Exception handling testing
import pytest
def division(a,b):
    return a/b
def test_division():
    with pytest.raises(ZeroDivisionError):
        division(2,0)