from selenium.webdriver.common.by import By
import pytest
import time
from definitions import *

class TestRegistration:
    def test_registration_correct_data_successful(self, driver):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email())
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password())
        driver.find_element(By.XPATH, registration_form_submit).click()

        time.sleep(1)
        current_url = driver.current_url
        assert current_url == login_page

    def test_registration_empty_login_no_registration (self, driver):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email())
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password())
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)
        current_url = driver.current_url

        assert current_url == registration_page

    @pytest.mark.parametrize('wrong_email_format', wrong_email_format_list)
    def test_registration_wrong_email_format_user_exist(self, driver, wrong_email_format):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(wrong_email_format)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password())
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)

        assert driver.find_element(By.XPATH, registration_page_error_p).text == "Такой пользователь уже существует"

    @pytest.mark.parametrize('correct_email_format', correct_email_format_list)
    def test_registration_wrong_correct_format_successful_registration(self, driver, correct_email_format):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(correct_email_format)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password())
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)

        current_url = driver.current_url
        assert current_url == login_page

    @pytest.mark.parametrize('correct_password_length', correct_password_length_list)
    def test_registration_correct_password_length_successful (self, driver, correct_password_length):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email())
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(correct_password_length)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)

        assert driver.current_url == login_page

    def test_registration_empty_password_no_registration (self, driver):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email())
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)

        assert driver.current_url == registration_page

    @pytest.mark.parametrize('wrong_password_length', wrong_password_length_list)
    def test_registration_wrong_password_length_incorrect_password (self, driver, wrong_password_length):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login())
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email())
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(wrong_password_length)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)
    
        assert driver.find_element(By.XPATH, registration_form_field_password_error).text == "Некорректный пароль"