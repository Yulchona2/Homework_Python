import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages_shop.authorization import Authorization
from pages_shop.inventory import Inventory
from pages_shop.cart import Cart
from pages_shop.checkout_step_one import ClientInfo
from pages_shop.checkout_step_two import CheckoutOverview
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(50)
    yield driver
    driver.quit()


def test_order(driver):
    authorization = Authorization(driver, "standard_user", "secret_sauce")
    authorization.authorize()

    inventory = Inventory(driver)
    inventory.add_to_cart()

    cart = Cart(driver)
    cart.checkout()

    client_info = ClientInfo(driver, "Юлия", "Егорова", "141021")
    client_info.add_client_info()

    checkout_overview = CheckoutOverview(driver)
    to_be = "$58.29"
    as_is = checkout_overview.get_total_amount()

    assert to_be == as_is
