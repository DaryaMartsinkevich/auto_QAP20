import pytest

from lesson_23.pages.login_page import LoginPage


def test_empty(driver):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.enter_username('standard_user')
    login_page.click_login()
    login_page.get_error_message()

    assert login_page.get_error_message() == "Epic sadface: Password is required", 'Неверно'
    # assert login_page.get_error_message() == "Epic sadface: Password is required_1", 'Неверно'
