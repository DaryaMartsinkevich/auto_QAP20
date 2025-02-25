import pytest

from lesson_23.pages.basket_page import BasketPage
from lesson_23.pages.checkout_page import CheckoutPage
from lesson_23.pages.login_page import LoginPage
from lesson_23.pages.products_page import ProductPage


def test_e2e(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    products = ProductPage(driver)
    products.add_backpack_to_basket()
    products.move_to_basket()
    assert "cart" in driver.current_url, 'Неверно'

    basket = BasketPage(driver)
    basket.count_products_in_basket()
    assert basket.count_products_in_basket() == 1
    assert basket.return_product() == "Sauce Labs Backpack"

    checkout = CheckoutPage(driver)
    checkout.do_checkout()
    assert "checkout-step-one" in driver.current_url, 'Неверно'

    information = CheckoutPage(driver)
    information.enter_first_name('Ivanov')
    information.enter_last_name('Ivan')
    information.enter_zip_code(43-315)
    information.move_to_overview_page()
    assert "checkout-step-two" in driver.current_url, 'Неверно'
