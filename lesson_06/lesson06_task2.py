from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()

print((driver.find_element(By.ID, "updatingButton")).text)

driver.quit()
