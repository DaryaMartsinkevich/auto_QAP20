from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_presrnce(self, locator_type, locator):
        return self.wait.until(EC.presence_of_element_located((locator_type, locator)))

    def wait_for_clickable(self, locator_type, locator):
        return self.wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_visiblity(self, locator_type, locator):
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_for_invisibility(self, locator_type, locator):
        return self.wait.until(EC.invisibility_of_element_located((locator_type, locator)))

    def wait_for_text(self, locator_type, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

# Потом в тесте обращение через класс:
# wait = WaitHelper(driver())
# element = wait.wait_for_presrnce(By.ID, 'example_id')
# button = wait.wait_for_clickable(By.XPATH, '//button[@id="submit"')