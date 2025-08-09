from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Client_info:

    def __init__(self, driver, name, last_name, zip_code):
        self.driver = driver
        self.name = name
        self.last_name = last_name
        self. zip_code = zip_code

    def add_client_info(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
        self.driver.find_element(By.ID, "first-name").send_keys(self.name)
        self.driver.find_element(By.ID, "last-name").send_keys(self.last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(self.zip_code)
        self.driver.find_element(By.ID, "continue").click()
