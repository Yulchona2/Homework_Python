import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Инициализация драйвера
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
    driver.find_element(By.ID, "checkout").click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
    driver.find_element(By.ID, "first-name").send_keys("Юлия")
    driver.find_element(By.ID, "last-name").send_keys("Егорова")
    driver.find_element(By.ID, "postal-code").send_keys("141021")
    driver.find_element(By.ID, "continue").click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
    total_text = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    total_amount = total_text[7:]
    expected_total_amount = "$58.29"
    assert total_amount == expected_total_amount
