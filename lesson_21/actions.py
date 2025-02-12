# Пример тестирования drag-and-drop
# 1.Открыть страницу с перетаскиванием элементов
# 2.Переместить элемент из одной области в другую
# 3.Убедиться, что действие выполнено успешно.
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest


def action_chains(driver):
    try:
        # ОТкрыть страницы с drag-and-drop
        driver.get('https://jqueryui.com/droppable/')

        # Переключение в iframe, если элементы находятся внутри
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

        # Находим элементы для перетаскивания
        source_element = driver.find_element(By.ID, 'draggable')        #что
        target_element = driver.find_element(By.ID, 'droppable')        #куда

        # Выполнение действия drag-and-drop
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

        # Проверка результата
        if 'Dropped!' in target_element.text:
            print('Перетаскивание выполнено успешно!')

    finally:
        # Закрытие браузера
        driver.quit()


def work_window(driver):
    driver.get('https://demoqa.com/browser-windows')
    # Клик на кнопку для открытия новой вкладки
    driver.find_element(By.ID, 'tabButton').click()
    # Получение списка всех окон
    handles = driver.window_handles
    print('Все окна:', handles)
    # Переключение на новое окно
    driver.switch_to_window(handles[1])
    print("Текст в новом окне:", driver.find_element(By.ID, 'sampleHeading').text)
    # Возврат в исходное окно
    driver.switch_to_window(handles[0])


def work_iframe(driver):
    driver.get('https://demoqa.com/browser-windows')
    # Клик на кнопку для открытия новой вкладки
    driver.find_element(By.ID, 'tabButton').click()
    # Получение списка всех окон
    handles = driver.window_handles
    print('Все окна:', handles)
    # Переключение на новое окно
    driver.switch_to_window(handles[1])
    print("Текст в новом окне:", driver.find_element(By.ID, 'sampleHeading').text)
    # Возврат в исходное окно
    driver.switch_to_window(handles[0])


def work_alert(driver):
    driver.find_element(By.ID, 'alertButton').click()

    alert = driver.switch_to_alert
    print('Текст алерта:', alert.text)
    alert.accept()

    # Открытие подтверждающего алерта
    driver.find_element(By.ID, 'confirmButton').click()
    alert = driver.switch_to_alert
    print('Текст подтверждающего алерта:', alert.text)
    alert.dismiss()

    # Открытие promt-алерта
    driver.find_element(By.ID, 'promtButton').click()
    alert = driver.switch_to_alert
    print('Текст promt-алерта:', alert.text)
    alert.send_keys("Test message")
    alert.accept()