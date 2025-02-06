from selenium.webdriver.common.by import By
from lesson_23.pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BASKET = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')

    def do_checkout(self):
        self.click_element(self.CHECKOUT_BASKET)

    def enter_first_name(self, name):
        self.enter_text(self.FIRST_NAME, name)

    def enter_last_name(self, lastname):
        self.enter_text(self.LAST_NAME, lastname)

    def enter_zip_code(self, code):
        self.enter_text(self.ZIP_CODE, code)

    def move_to_overview_page(self):
        self.click_element(self.CONTINUE)
