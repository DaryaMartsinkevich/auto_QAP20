import pytest

from lesson_23.pages.login_page import LoginPage


def test_integration(driver, name, password):
    login_page = LoginPage(driver)
    login_page.valid_login()

    assert "inventory" in driver.current_url, "Ошибка: логин не удался"
