import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://omayo.blogspot.com/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()


def test_level_1(driver):
    driver.get(URL)
    el = driver.find_element(By.ID, 'textbox1')
    el.send_keys('Selenium Test')


def test_level_2(driver):
    driver.get(URL)
    drop = driver.find_element(By.ID, "drop1")
    select = Select(drop)
    time.sleep(3)
    select.select_by_visible_text("doc 3")
    selected_option = select.first_selected_option
    assert selected_option.text == "doc 3", "Выбранная опция не установлена"

