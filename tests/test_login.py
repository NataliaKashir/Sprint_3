from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from definitions import *
import time

class TestLogin:
    def test_login_with_main_page_enter_account_btn_success (self, driver, register_user):
        # если регистрация прошла успешно
        if register_user['email']:
            driver.get(main_page)
            driver.find_element(By.CLASS_NAME, main_page_enter_account_btn).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, login_page_enter_btn)))
            # login account
            driver.find_element(By.XPATH, login_page_login).send_keys(register_user['email'])
            driver.find_element(By.XPATH, login_page_password).send_keys(register_user['password'])
            driver.find_element(By.CLASS_NAME, login_page_enter_btn).click()

            time.sleep(1)
            assert driver.find_element(By.CLASS_NAME, main_page_order_btn).text == 'Оформить заказ'

    def test_login_with_main_page_private_account_btn_success(self, driver, register_user):
        # если регистрация прошла успешно
        if register_user['email']:
            driver.get(main_page)
            driver.find_element(By.XPATH, main_page_private_account_btn).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, login_page_enter_btn)))
            # login account
            driver.find_element(By.XPATH, login_page_login).send_keys(register_user['email'])
            driver.find_element(By.XPATH, login_page_password).send_keys(register_user['password'])
            driver.find_element(By.CLASS_NAME, login_page_enter_btn).click()

            time.sleep(1)
            assert driver.find_element(By.CLASS_NAME, main_page_order_btn).text == 'Оформить заказ'

    def test_login_with_registration_form_login_btn_success(self, driver, register_user):
        # если регистрация прошла успешно
        if register_user['email']:
            driver.get(registration_page)
            driver.find_element(By.XPATH, registration_form_login_btn).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, login_page_enter_btn)))
            # login account
            driver.find_element(By.XPATH, login_page_login).send_keys(register_user['email'])
            driver.find_element(By.XPATH, login_page_password).send_keys(register_user['password'])
            driver.find_element(By.CLASS_NAME, login_page_enter_btn).click()

            time.sleep(1)
            assert driver.find_element(By.CLASS_NAME, main_page_order_btn).text == 'Оформить заказ'

    def test_login_with_restore_password_page_login_btn_success(self, driver, register_user):
        # если регистрация прошла успешно
        if register_user['email']:
            driver.get(restore_password_page)
            driver.find_element(By.XPATH, restore_password_page_enter_btn).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, login_page_enter_btn)))
            # login account
            driver.find_element(By.XPATH, login_page_login).send_keys(register_user['email'])
            driver.find_element(By.XPATH, login_page_password).send_keys(register_user['password'])
            driver.find_element(By.CLASS_NAME, login_page_enter_btn).click()

            time.sleep(1)
            assert driver.find_element(By.CLASS_NAME, main_page_order_btn).text == 'Оформить заказ'