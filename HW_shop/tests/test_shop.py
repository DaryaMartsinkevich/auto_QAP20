from HW_shop.src.shop import Shop
import pytest


def test_add_to_cart(shop):
    result = shop.add_to_cart('vino', 3)
    assert result == {'vino': 3}


def test_add_to_cart_negatine(shop):
    with pytest.raises(ValueError):
        shop.add_to_cart('banan', -1)


@pytest.mark.parametrize("item, price, expected", [
    ({'apple': 5}, {'apple': 9}, 45),
    ({'vino': 15}, {'vino': 3}, 45),
    ({'water': 0}, {'water': 0}, 0)
])
def test_calculate_total(shop, item, price, expected):
    shop.cart = item
    assert shop.calculate_total(price) == expected


@pytest.mark.parametrize('total, discount', [
    (100, -20),
    (100, 110)
])
def test_apply_discount_negativ(shop, total, discount):
    with pytest.raises(ValueError):
        shop.apply_discount(total, discount)


@pytest.mark.parametrize('total, discount, expected', [
    (100, 30, 70),
    (90, 50, 45)
])
def test_apply_discount(shop, total, discount, expected):
    assert shop.apply_discount(total, discount) == expected