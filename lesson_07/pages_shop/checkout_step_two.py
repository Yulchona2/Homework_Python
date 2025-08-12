from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverview:

    def __init__(self, driver):
        self.driver = driver

    def get_total_amount(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
        total_text = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        total_amount = total_text[7:]
        return total_amount
