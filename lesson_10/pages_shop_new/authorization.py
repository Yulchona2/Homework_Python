from selenium.webdriver.common.by import By
import allure


class Authorization:

    def __init__(self, driver, user_name, password):
        """
        Конструктор класса CalcMainPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param user_name: str — логин пользователя для авторизации
        :param password: str — пароль пользователя для авторизации
                """
        self.driver = driver
        self.user_name = user_name
        self.password = password

    allure.step("Ввод логина и пароля, нажатие на клавишу 'Login'")

    def authorize(self):
        self.driver.find_element(By.ID, "user-name").send_keys(self.user_name)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "login-button").click()
