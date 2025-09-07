import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver

from pages_shop_new.authorization import Authorization
from pages_shop_new.inventory import Inventory
from pages_shop_new.cart import Cart
from pages_shop_new.checkout_step_one import ClientInfo
from pages_shop_new.checkout_step_two import CheckoutOverview
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver() -> WebDriver:
    """
    Фикстура для инициализации и завершения работы драйвера.
    Открытие страницы через инкогнито - убрать плашку 'Смените пароль'.
    """
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(50)
    yield driver
    driver.quit()

@allure.title("Тестирование оформления заказа продукции")
@allure.description("Тест проверяет корректность расчета суммы заказа")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_order(driver):
    with allure.step("Авторизация пользователя"):
        authorization = Authorization(driver, "standard_user", "secret_sauce")
        authorization.authorize()
    with allure.step("Добавление товаров в корзину"):
        inventory = Inventory(driver)
        inventory.add_to_cart()
    with allure.step("Ожидание загрузки страницы'корзина. "
                     "Переход на следующую страницу заказа"):
        cart = Cart(driver)
        cart.checkout()
    with allure.step("Занесение данных клиента "
                     "(имя, фамилия, индекс почты) в форму"):
        client_info = ClientInfo(driver, "Юлия", "Егорова", "141021")
        client_info.add_client_info()
    with allure.step("Проверка результата"):
        checkout_overview = CheckoutOverview(driver)
        to_be = "$58.29"
        as_is = checkout_overview.get_total_amount()

        assert to_be == as_is
