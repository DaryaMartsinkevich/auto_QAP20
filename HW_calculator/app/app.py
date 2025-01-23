def add(a, b):
    """
    Возвращает сумму двух чисел.
    """
    return a + b


def subtract(a, b):
    """
    Возвращает разность двух чисел.
    """
    return a - b


def multiply(a, b):
    """
    Возвращает произведение двух чисел.
    """
    return a * b


def divide(a, b):
    """
    Возвращает результат деления двух чисел.
    Если деление на ноль, вызывает ошибку ValueError.
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b