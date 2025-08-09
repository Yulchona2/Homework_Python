from selenium.webdriver.common.by import By


class Inventory:

    def __init__(self, driver):
        self.driver = driver
        self.sauce_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.sauce_labs_bolt_t_shirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.sauce_labs_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def add_to_cart(self):
        self.driver.find_element(*self.sauce_labs_backpack).click()
        self.driver.find_element(*self.sauce_labs_bolt_t_shirt).click()
        self.driver.find_element(*self.sauce_labs_onesie).click()
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
