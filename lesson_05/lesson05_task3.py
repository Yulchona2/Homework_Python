from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get(" http://the-internet.herokuapp.com/inputs")
driver.find_element(By.CSS_SELECTOR, "input[type='number']").send_keys("Sky")
driver.find_element(By.CSS_SELECTOR, "input[type='number']").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='number']").send_keys("Pro")

driver.quit()
