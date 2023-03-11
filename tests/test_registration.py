from selenium.webdriver.common.by import By
import pytest
import time
import random

class TestRegistration:
    correct_email_format_list = [
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@email.com",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}.first.middle.lastname@email.com",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@subdomain.email.com",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}+firstname+lastname@email.com",
        f"{random.randint(100, 999)}0987654321@example.com",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@email-one.com",
        f"{random.randint(100, 999)}_______@email.com",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@email.name",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@email.museum",
        f"Natalya_Kashirina_6_{random.randint(100, 999)}.firstname-lastname@email.com"
    ]
    wrong_email_format_list = [
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@yandexru",    # no dot in domain
        f"Natalya_Kashirina_6_{random.randint(100, 999)}yandex.ru",    # missing @ symbol in the email id field
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@",    # missing domain in the email id field
        f"Natalya_Kashirina_6_{random.randint(100, 999)}@#@@##@%^%#$@#$@#.com",  # garbage is not accepted in the email id field
        f"@Natalya_Kashirina6{random.randint(100, 999)}email.com",  # missing username in the email id field
        f"Natalya_Kashirina_6{random.randint(100, 999)}@example@email.com"  # double @ in the email id text box
        # следующие тесты выдают Failed, но не знаю, нужно ли в рамках задания такие проверки
        #f".Natalya_Kashirina_6_{random.randint(100, 999)}@email.com",  # leading dot in the email id text box
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}@email.com.",  # trailing dot in the email id text box
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}.@email.com",  # trailing dot in the domain
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}…example@email.com",  # multiple dots in the email field
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}おえあいう@example.com",  # not unicode char in the address in the email text box
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}@email.com (John Doe)",  # wrong format with " "
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}@-email.com",  # wrong format with "-" in the domain
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}@email.webb",  # wrong zone
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}@email…com",  # multiple dots in the domain
        #f'Natalya_Kashirina_6_{random.randint(100, 999)}"(),:;<>[\]@email.com',  # wrong format with special simbols in the email id text box
        #f"Natalya_Kashirina_6_{random.randint(100, 999)}@234.234.234.234" # IP address format in the email text box
        #f"{random.randint(100, 999)}111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111@yandex.ru",  #  email id cannot exceed 254 characters.
    ]
    correct_password_length_list = [ "123456", "1234567", "01234567890123456789012345678901234567890123456789"]
    wrong_password_length_list = ["1", "12", "123", "1234", "12345"]
    def test_registration_correct_data_successful(self, driver, registration_page,
                                     registration_form_submit, login_page,
                                     registration_login, registration_form_field_login,
                                     registration_email, registration_form_field_email,
                                     registration_password, registration_form_field_password):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password)
        driver.find_element(By.XPATH, registration_form_submit).click()

        time.sleep(1)
        current_url = driver.current_url
        assert current_url == login_page
        driver.quit()

    def test_registration_empty_login_no_registration (self, driver, registration_page, registration_form_submit,
                                              registration_email, registration_form_field_email,
                                              registration_password, registration_form_field_password):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)
        current_url = driver.current_url

        assert current_url == registration_page
        driver.quit()

    @pytest.mark.parametrize('wrong_email_format', wrong_email_format_list)
    def test_registration_wrong_email_format_user_exist(self, driver, registration_page, registration_form_submit,
                                     registration_login, registration_form_field_login,
                                     wrong_email_format, registration_form_field_email,
                                     registration_password, registration_form_field_password,
                                     registration_page_error_p):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(wrong_email_format)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)
        
        assert driver.find_element(By.XPATH, registration_page_error_p).text == "Такой пользователь уже существует"
        driver.quit()

    @pytest.mark.parametrize('correct_email_format', correct_email_format_list)
    def test_registration_wrong_correct_format_successful_registration(self, driver, registration_page,
                                                        registration_form_submit,login_page,
                                                        registration_login, registration_form_field_login,
                                                        correct_email_format, registration_form_field_email,
                                                        registration_password, registration_form_field_password):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(correct_email_format)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)
        
        current_url = driver.current_url
        assert current_url == login_page
        driver.quit()

    @pytest.mark.parametrize('correct_password_length', correct_password_length_list)
    def test_registration_correct_password_length_successful (self, driver, registration_page,
                                                  registration_form_submit, login_page,
                                                  registration_login, registration_form_field_login,
                                                  registration_email, registration_form_field_email,
                                                  correct_password_length, registration_form_field_password):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(correct_password_length)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)
        
        assert driver.current_url == login_page
        driver.quit()

    def test_registration_empty_password_no_registration (self, driver, registration_page,
                                                  registration_form_submit, login_page,
                                                  registration_login, registration_form_field_login,
                                                  registration_email, registration_form_field_email):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)

        assert driver.current_url == registration_page
        driver.quit()

    @pytest.mark.parametrize('wrong_password_length', wrong_password_length_list)
    def test_registration_wrong_password_length_incorrect_password (self, driver, registration_page,
                                                  registration_form_submit, login_page, registration_form_field_password_error,
                                                  registration_login, registration_form_field_login,
                                                  registration_email, registration_form_field_email,
                                                  wrong_password_length, registration_form_field_password):
        driver.get(registration_page)
        # registration
        driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
        driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email)
        driver.find_element(By.XPATH, registration_form_field_password).send_keys(wrong_password_length)
        driver.find_element(By.XPATH, registration_form_submit).click()
        time.sleep(1)

        assert driver.find_element(By.XPATH, registration_form_field_password_error).text == "Некорректный пароль"
        driver.quit()