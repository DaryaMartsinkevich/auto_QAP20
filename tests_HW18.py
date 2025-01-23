import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://omayo.blogspot.com/'
URL_2 = 'https://demoqa.com/webtables'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()

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


def test_level_3(driver):
    driver.get(URL_2)
    add = driver.find_element(By.ID, 'addNewRecordButton')
    add.click()
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    driver.find_element(By.ID, 'age').send_keys('30')
    driver.find_element(By.ID, 'salary').send_keys('50000')
    driver.find_element(By.ID, 'department').send_keys('IT')
    driver.find_element(By.ID, 'submit').click()

    edit = driver.find_element(By.ID, 'edit-record-4')
    driver.execute_script('arguments[0].scrollIntoView(true)', edit)
    time.sleep(2)
    edit.click()

    age = driver.find_element(By.ID, 'age')
    age.clear()
    age.send_keys('35')

    salary = driver.find_element(By.ID, 'salary')
    salary.clear()
    salary.send_keys('55000')
    driver.find_element(By.ID, 'submit').click()
    time.sleep(5)

    delite = driver.find_element(By.ID, 'delete-record-4')
    driver.execute_script('arguments[0].scrollIntoView(true)', delite)
    delite.click()




