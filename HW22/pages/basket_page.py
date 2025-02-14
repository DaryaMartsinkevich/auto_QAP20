from selenium.webdriver.common.by import By
from lesson_22.pages.base_page import BasePage


class BasketPage(BasePage):
    PRODUCTS_IN_BASKET = (By.CLASS_NAME, 'cart_list')

    def count_products_in_basket(self):
        return len(self.find_elements(self.PRODUCTS_IN_BASKET))

    def return_product(self):
        return self.find_elements(self.PRODUCTS_IN_BASKET)[0].find_element(By.CLASS_NAME, 'inventory_item_name').text



