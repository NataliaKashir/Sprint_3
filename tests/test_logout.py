from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from definitions import *

class TestLogout:
    def test_private_account_logout_success(self, driver, register_user):
        if register_user['email']:
            driver.get(login_page)
            # login account
            driver.find_element(By.XPATH, login_page_login).send_keys(register_user['email'])
            driver.find_element(By.XPATH, login_page_password).send_keys(register_user['password'])
            driver.find_element(By.CLASS_NAME, login_page_enter_btn).click()
            # ждем появления ссылки на Личный кабинет и жмем ее
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.XPATH, main_page_private_account_btn)))
            driver.find_element(By.XPATH, main_page_private_account_btn).click()
            # ждем входа в профиль
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.XPATH, private_account_header)))
            # нажимаем по кнопке Выход
            driver.find_element(By.XPATH, private_account_logout_btn).click()
            # Ожидаем появления заголовка Вход
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.XPATH, login_page_header)))

            assert driver.current_url == login_page