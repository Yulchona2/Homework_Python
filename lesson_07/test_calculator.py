import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator import Calculator


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_sum_calculator(driver):
    calc = Calculator(driver)
    calc.delay()
    calc.seven()
    calc.plus()
    calc.eight()
    calc.equal()
    assert calc.screen_result() == "15"
