import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_new import Calculator


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
     """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "на сложение двух целых чисел")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_sum_calculator(driver):
    with allure.step("Открытие страницы калькулятора"):
        calc = Calculator(driver)
    with allure.step("Установить задержку выполнения операций калькулятора"):
        calc.delay()
    with allure.step("Нажать на клавишу с цифрой 7"):
        calc.seven()
    with allure.step("Нажать на клавишу со знаком +"):
        calc.plus()
    with allure.step("Нажать на клавишу с цифрой 8"):
        calc.eight()
    with allure.step("Нажать на клавишу со знаком ="):
        calc.equal()
    with allure.step("Проверка результата"):
        assert calc.screen_result() == "15"
