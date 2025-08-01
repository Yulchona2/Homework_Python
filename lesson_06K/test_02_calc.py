import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-"
        "java/slow-calculator.html")
    element_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    element_delay.clear()
    element_delay.send_keys("45")
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
    WebDriverWait(driver, 48).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "div.screen"), "15"))
    field_screen = driver.find_element(By.CSS_SELECTOR, "div.screen")
    assert field_screen.text == "15"
