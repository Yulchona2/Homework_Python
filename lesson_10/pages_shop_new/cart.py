from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        """
        Конструктор класса Cart.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    def checkout(self):
        """
        Ожидание загрузки страницы 'корзина'
        """
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
        """
        Нажатие на кнопку 'Checkout' для перехода на следующую страницу заказа
        """
        self.driver.find_element(By.ID, "checkout").click()
