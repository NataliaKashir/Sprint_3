from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

class TestLogin:
    def test_login_with_main_page_enter_account_btn_success (self, driver, main_page, register_user,
                                                                main_page_enter_account_btn, login_page_enter_btn,
                                                                login_page_login, login_page_password, main_page_order_btn):
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
            driver.quit()

    def test_login_with_main_page_private_account_btn_success(self, driver, main_page, register_user,
                                                        main_page_private_account_btn, login_page_enter_btn,
                                                        login_page_login, login_page_password, main_page_order_btn):
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
            driver.quit()

    def test_login_with_registration_form_login_btn_success(self, driver, registration_page, register_user,
                                                        registration_form_login_btn, login_page_enter_btn,
                                                        login_page_login, login_page_password, main_page_order_btn):
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
            driver.quit()

    def test_login_with_restore_password_page_login_btn_success(self, driver, restore_password_page, register_user,
                                                        restore_password_page_enter_btn, login_page_enter_btn,
                                                        login_page_login, login_page_password, main_page_order_btn):
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
            driver.quit()