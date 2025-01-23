import pytest
from HW_calculator.app.app import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-6, 6) == 0
    assert add(0,0) == 0
    assert add(-2, -3) == -5
    assert add(2.3, 2.7) == 5


def test_divide():
    assert divide(12, 2) == 6
    assert divide(25, 5) == 5
    assert divide(-6, -3) == 2
    with pytest.raises(ValueError):
        divide(16, 0)


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-6, 6) == -12
    assert subtract(0, 0) == 0
    assert subtract(-3, -3) == 0
    assert subtract(0, 6) == -6
    assert subtract(5.2, 1.2) == 4


def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-6, 6) == -36
    assert multiply(2, 0) == 0
    assert multiply(-1, -1) == 1
    assert multiply(1.5, 2) == 3