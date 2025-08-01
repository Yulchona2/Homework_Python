import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Инициализация драйвера
    # Подставить свой путь до драйвера
    edge_service = EdgeService(
        r"C:\Users\Юля\Desktop\driver_edge\msedgedriver.exe")
    driver = webdriver.Edge(service=edge_service)
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


def test_fill_fields(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    first_name = driver.find_element(
        By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.clear()
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.clear()
    last_name.send_keys("Петров")
    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.clear()
    address.send_keys("Ленина, 55-3")
    zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip_code.send_keys("")
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys("Россия")
    e_mail = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    e_mail.send_keys("test@skypro.com")
    phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone.send_keys("+7985899998787")
    job_position = driver.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position.send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    expected_color_zip_code_element = 'rgba(248, 215, 218, 1)'
    expected_color_others_elements = 'rgba(209, 231, 221, 1)'

    zip_code_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#zip-code')))
    assert zip_code_element.value_of_css_property(
        'background-color') == expected_color_zip_code_element

    others_fields_ids = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
        ]

    for field_id in others_fields_ids:
        field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, field_id)))
        assert field.value_of_css_property(
            'background-color') == expected_color_others_elements
