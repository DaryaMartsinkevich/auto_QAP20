import pytest
from lesson_19.app.app import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (-1, 1, 0),
    (3, 5, 8)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.new
# Тестирование функции add
@pytest.mark.parametrize("a, b, expected", [
    (-1, 1, 0),
    (3, 5, 8)
], ids=["add_negative_and_positive", "add_two_positives"])
def test_add_1(a, b, expected):
    assert add(a, b) == expected


# Тестирование функции subtract
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 7, -7)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


# Тестирование функции multiply
@pytest.mark.parametrize("a, b, expected", [
    (4, 3, 12),
    (-2, 6, -12)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


# Тестирование функции divide
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (5, 0, 0)
])
def test_divide(a, b, expected):
    if b == 0:
        with pytest.raises(ValueError):
            divide(a, b)
    assert divide(a, b) == expected


# Тестирование деления на ноль
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
