from selenium.webdriver.common.by import By

class Inventory:

    def __init__(self, driver):
        """
        Конструктор класса Inventory.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.sauce_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.sauce_labs_bolt_t_shirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.sauce_labs_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def add_to_cart(self):
        """
        Выбор товара 'Sauce Labs Backpack'
        """
        self.driver.find_element(*self.sauce_labs_backpack).click()
        """
        Выбор товара 'Sauce Labs Bolt T-Shirt'
         """
        self.driver.find_element(*self.sauce_labs_bolt_t_shirt).click()
        """
        Выбор товара 'Sauce Labs Onesie'
         """
        self.driver.find_element(*self.sauce_labs_onesie).click()
        """
        Нажатие на кнопку 'Корзина' в верхнем правом углу
         """
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
