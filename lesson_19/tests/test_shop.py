from lesson_19.src.shop import Shop
import pytest


def test_add_to_cart(shop):
    result = shop.add_to_cart('vino', 3)
    assert result == {'vino': 3}


@pytest.mark.parametrize("item, price, expected", [
    ({'apple': 5}, {'apple': 9}, 45),
    ({'vino': 15}, {'vino': 3}, 45),
    ({'water': 0}, {'water': 0}, 0)
])
def test_calculate_total(shop, item, price, expected):
    shop.cart = item
    assert shop.calculate_total(price) == expected
