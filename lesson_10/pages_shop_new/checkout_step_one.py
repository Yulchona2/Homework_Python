from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ClientInfo:

    def __init__(self, driver, name, last_name, zip_code):
        """
        Конструктор класса ClientInfo.
        :param driver: WebDriver — объект драйвера Selenium.
         """
        self.driver = driver
        self.name = name
        self.last_name = last_name
        self. zip_code = zip_code

    def add_client_info(self):
        """
        @allure.step(Ожидание загрузки страницы перед вводом данных клиента)
        """
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
        """
        Ввод имени пользователя в строку 'first-name'
        """
        self.driver.find_element(By.ID, "first-name").send_keys(self.name)
        """
        Ввод фамилии пользователя в строку 'last-name'
        """
        self.driver.find_element(By.ID, "last-name").send_keys(self.last_name)
        """
        Ввод индекса почты в строку 'Zip/Postal Code'
         """
        self.driver.find_element(By.ID, "postal-code").send_keys(self.zip_code)
        """
        Нажатие клавиши 'Continue' для перехода на следующую страницу заказа
        """
        self.driver.find_element(By.ID, "continue").click()
