import pytest
from selenium import webdriver
from definitions import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.fixture
def register_user(driver):
    driver.get(registration_page)
    email = registration_email()
    password = registration_password()
    driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
    driver.find_element(By.XPATH, registration_form_field_email).send_keys(email)
    driver.find_element(By.XPATH, registration_form_field_password).send_keys(password)
    driver.find_element(By.XPATH, registration_form_submit).click()
    time.sleep(1)
    if driver.current_url == login_page:
        return {"email": email, "password": password}
    else:
        return {"email": "", "password": ""}

