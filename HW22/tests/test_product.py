import pytest

from lesson_22.pages.login_page import LoginPage
from lesson_22.pages.products_page import ProductPage
from lesson_22.pages.base_page import BasePage
from lesson_22.pages.basket_page import BasketPage


def test_add_to_basket(driver):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.success_login('standard_user', 'secret_sauce')

    product_page = ProductPage(driver)
    product_page.add_backpack_to_basket()
    product_page.move_to_basket()

    basket_page = BasketPage(driver)
    assert basket_page.count_products_in_basket() == 1
    assert basket_page.return_product() == "Sauce Labs Backpack"



