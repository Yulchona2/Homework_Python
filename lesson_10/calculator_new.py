from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    """
    Класс для работы с калькулятором
    """

    def __init__(self, driver):
        """
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.delay_element = (By.CSS_SELECTOR, "#delay")
        self.seven_element = (By.XPATH, '//span[text()="7"]')
        self.plus_element = (By.XPATH, '//span[text()="+"]')
        self.eight_element = (By.XPATH, '//span[text()="8"]')
        self.equal_element = (By.XPATH, '//span[text()="="]')
        self.screen_element = (By.CSS_SELECTOR, "div.screen")

    def delay(self):
        """
        Устанавливает задержку выполнения операций калькулятора.
        """
        delay_element = self.driver.find_element(*self.delay_element)
        delay_element.clear()
        delay_element.send_keys("45")

    def seven(self):
        """Нажимает кнопку с цифрой 7."""
        seven_element = self.driver.find_element(*self.seven_element)
        seven_element.click()

    def plus(self):
        """Нажимает кнопку '+'."""
        plus_element = self.driver.find_element(*self.plus_element)
        plus_element.click()

    def eight(self):
        """Нажимает кнопку с цифрой 8."""
        eight_element = self.driver.find_element(*self.eight_element)
        eight_element.click()

    def equal(self):
        """Нажимает на кнопку '='."""
        equal_element = self.driver.find_element(*self.equal_element)
        equal_element.click()

    def screen_result(self):
        """
        Получает результат с экрана калькулятора после ожидания.
        """
        WebDriverWait(self.driver, 48).until(
            EC.text_to_be_present_in_element(self.screen_element, "15"))
        screen_element = self.driver.find_element(*self.screen_element)
        screen_element_result = screen_element.text
        """
         :return: str — текст результата на экране калькулятора.
        """
        return screen_element_result
