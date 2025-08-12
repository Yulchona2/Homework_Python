from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
        self.driver.find_element(By.ID, "checkout").click()
