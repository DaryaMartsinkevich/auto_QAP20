import time

import pytest
import os
import pdb
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
download_dir = "C:/Users/48574/Downloads"
file_name = "file-sample_100kB.doc"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()


@pytest.fixture
def driver_rus():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--lang=ru")
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("pdfjs.disabled", True)  # Открывать PDF вне браузера
    service = Service(GeckoDriverManager().install())
    config_driver = webdriver.Firefox(service=service, options=options)
    yield config_driver
    config_driver.quit()


@pytest.fixture
def driver_firefox():
    options = Options()
    options.add_argument("--start-maximized")
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.download.folderList", 2)
    # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    # options.set_preference("browser.download.manager.showWhenStarting", False)
    # options.set_preference("pdfjs.disabled", True)  # Открывать PDF вне браузера
    service = Service(GeckoDriverManager().install())
    config_driver = webdriver.Firefox(service=service, options=options)
    yield config_driver
    config_driver.quit()

def test_work_action(driver):
    driver.get('https://jqueryui.com/droppable/')
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
    source_element = driver.find_element(By.CSS_SELECTOR, 'div[id = "draggable"]')
    target_element = driver.find_element(By.CSS_SELECTOR, 'div[id="droppable"]')

    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    if 'Dropped!' in target_element.text:
        print('Успешно!')


def test_work_window(driver):
    driver.get('https://demoqa.com/browser-windows')
    driver.find_element(By.CSS_SELECTOR, '#tabButton').click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    print("Текст в новом окне:", driver.find_element(By.ID, 'sampleHeading').text)

    driver.switch_to.window(handles[0])


def test_work_iframe(driver):
    driver.get('https://demoqa.com/frames')
    driver.switch_to.frame("frame1")
    text = driver.find_element(By.ID, 'sampleHeading').text
    assert text == 'This is a sample page', f"ERROR: Текст: {text}"
    print(f'Text in {'frame1'} is correct')

    driver.switch_to.default_content()


def test_simple_alert(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.CSS_SELECTOR, '#alertButton').click()
    alert = driver.switch_to.alert
    alert.accept()


def test_confirmation_alert(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.CSS_SELECTOR, '#confirmButton').click()
    alert = driver.switch_to.alert
    alert.dismiss()


def test_promt_alert(driver):
    driver.get("https://demoqa.com/alerts")
    promt_alert = driver.find_element(By.CSS_SELECTOR, '#promtButton')
    driver.execute_script("arguments[0].scrollIntoView();", promt_alert)
    promt_alert.click()
    alert = driver.switch_to.alert
    alert.send_keys("Selenium Test")
    alert.accept()
    result = driver.find_element(By.CSS_SELECTOR, "#promptResult")


def test_capabilities(driver_rus):
    driver_rus.get("https://www.google.com")
    print("Текст:", driver_rus.find_element(By.CSS_SELECTOR, 'div[id = "SIvCob"]').text)


def test_task4_2(driver_firefox):
    """Test to download a file and verify the download."""
    download_dir = "C:/Users/48574/Downloads"
    file_name = "file-sample_100kB.doc"

    # Set up explicit wait
    wait = WebDriverWait(driver_firefox, 10)

    # Open the website
    driver_firefox.get("https://file-examples.com/")

    # Close popups
    close_cookie_window(driver_firefox)
    close_ads(driver_firefox)

    # Click menu item
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-27"))).click()
    close_ads(driver_firefox)

    # Verify page navigation
    assert "index.php/sample-documents-download/" in driver_firefox.current_url, "Failed to navigate to documents page"

    # Find and click the download link for DOC/DOCX
    doc_file = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//tr[td[@class='file-ext' and contains(text(), 'DOC, DOCX')]]/td[@class='text-right file-link']/a")
    ))
    scroll_element(driver_firefox, doc_file)
    wait.until(EC.element_to_be_clickable(doc_file)).click()

    close_ads(driver_firefox)

    # Verify navigation to file page
    assert "index.php/sample-documents-download/sample-doc-download/" in driver_firefox.current_url, "Failed to navigate to file page"

    # Click the download button
    file_sizes = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".btn.btn-orange.btn-outline.btn-xl.page-scroll.download-button")
    ))

    scroll_element(driver_firefox, file_sizes[0])
    wait.until(EC.element_to_be_clickable(file_sizes[0])).click()

    # Check if the file is downloaded
    check_download(wait, download_dir, file_name)
    #


def close_cookie_window(driver):
    """Close the cookie banner if present."""
    try:
        cookie_close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-button.fc-cta-consent.fc-primary-button"))
        )
        cookie_close_button.click()
    except Exception:
        print("No cookie banner to close.")


def check_download(wait, download_dir, file_name):
    """Wait for the file to appear in the download directory."""
    wait.until(lambda driver: os.path.exists(os.path.join(download_dir, file_name)), "File not downloaded")
    print("Download completed!")


def close_ads(driver):
    """Перебирает все рекламные iframes, ищет кнопку 'Close' и закрывает рекламу."""
    try:
        # Находим все iframes на странице
        all_iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"Found {len(all_iframes)} iframes on the page.")

        for iframe in all_iframes:
            try:
                iframe_id = iframe.get_attribute("id")
                if not iframe_id or not iframe_id.startswith("aswift"):
                    continue  # Пропускаем не относящиеся к рекламе iframes

                print(f"Trying to switch to iframe: {iframe_id}")
                driver.switch_to.frame(iframe)

                # Проверяем кнопку закрытия сразу в этом iframe
                try:
                    ad_close_button = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.ID, "dismiss-button"))
                    )
                    ad_close_button.click()
                    print("Ad banner closed in main iframe.")
                    driver.switch_to.default_content()
                    return  # Выходим из функции сразу

                except Exception:
                    print("No close button found in main iframe, checking nested iframe.")

                # Ищем вложенный iframe с рекламой
                try:
                    nested_iframe = driver.find_element(By.TAG_NAME, "iframe")
                    driver.switch_to.frame(nested_iframe)
                    print("Switched to nested ad_iframe.")

                    # Проверяем кнопку закрытия внутри вложенного iframe
                    ad_close_button = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.ID, "dismiss-button"))
                    )
                    ad_close_button.click()
                    print("Ad banner closed in nested iframe.")
                    driver.switch_to.default_content()
                    return  # Выходим из функции сразу

                except Exception:
                    print(f"No ad found in nested iframe of {iframe_id}, switching back.")

            except Exception as e:
                print(f"Error switching to iframe {iframe_id}: {e}")

            finally:
                driver.switch_to.default_content()  # Возвращаемся в основной контент

        print("No ads found in any iframe.")

    except Exception as e:
        print(f"General error while handling ads: {e}")

    finally:
        driver.switch_to.default_content()
        print("Returned to main content.")


def scroll_element(driver_rus, element):
    driver_rus.execute_script("arguments[0].scrollIntoView();", element)


