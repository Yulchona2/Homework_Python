from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverview:

    def __init__(self, driver):
        """
        Конструктор класса CheckoutOverview.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    def get_total_amount(self):
        """
      Ожидание загрузки страницы подтверждения заказа и получение общей суммы.
      :return: str — текст суммы покупки.
        """
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
        total_text = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        total_amount = total_text.replace("Total: ", "").strip()  # "58.29"

        return total_amount
