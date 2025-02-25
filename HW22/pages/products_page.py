from selenium.webdriver.common.by import By
from lesson_22.pages.base_page import BasePage


class ProductPage(BasePage):
    BUTTON_BACKPACK = (By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    BASKET = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')

    def add_backpack_to_basket(self):
        self.click_element(self.BUTTON_BACKPACK)

    def move_to_basket(self):
        self.click_element(self.BASKET)

