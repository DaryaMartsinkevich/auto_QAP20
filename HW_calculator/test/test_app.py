import pytest
from HW_calculator.app.app import add, subtract, multiply, divide


@pytest.mark.parametrize(
    'value_1, value_2, result',
    [
        (2, 3, 5),
        (-6, 6, 0),
        (0, 0, 0),
        (-2, -3, -5),
        (2.3, 2.7, 5)
    ]
)
def test_add(value_1, value_2, result):
    assert add(value_1, value_2) == result


@pytest.mark.parametrize(
    'value_1, value_2, result',
    [
        (12, 2, 6),
        (25, 5, 5),
        (-6, -3, 2)
    ]
)
def test_divide(value_1, value_2, result):
    assert divide(value_1, value_2) == result


@pytest.mark.parametrize(
    'value_1, value_2',
    [
        (16, 0)
    ]
)
def test_divide_error(value_1, value_2):
    with pytest.raises(ValueError):
        divide(value_1, value_2)


@pytest.mark.parametrize(
    'value_1, value_2, result',
    [
        (10, 5, 5),
        (-6, 6, -12),
        (0, 0, 0),
        (-3, -3, 0),
        (0, 6, -6),
        (5.2, 1.2, 4)
    ]
)
def test_subtract(value_1, value_2, result):
    assert subtract(value_1, value_2) == result


@pytest.mark.parametrize(
    'value_1, value_2, result',
    [
        (2, 3, 6),
        (-6, 6, -36),
        (2, 0, 0),
        (-1, -1, 1),
        (1.5, 2, 3)
    ]
)
def test_multiply(value_1, value_2, result):
    assert multiply(value_1, value_2) == result