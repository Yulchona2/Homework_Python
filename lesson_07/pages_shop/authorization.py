from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, driver, user_name, password):
        self.driver = driver
        self.user_name = user_name
        self.password = password

    def authorize(self):
        self.driver.find_element(By.ID, "user-name").send_keys(self.user_name)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "login-button").click()
