from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestPrivateAccountTranfgers:
    def test_main_page_link_private_account_btn_success(self, driver, login_page, register_user,
                                                              main_page_private_account_btn, login_page_enter_btn,
                                                              login_page_login, login_page_password,
                                                              private_account_header):
        if register_user['email']:
            driver.get(login_page)
            # login account
            driver.find_element(By.XPATH, login_page_login).send_keys(register_user['email'])
            driver.find_element(By.XPATH, login_page_password).send_keys(register_user['password'])
            driver.find_element(By.CLASS_NAME, login_page_enter_btn).click()

            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.XPATH, main_page_private_account_btn)))
            driver.find_element(By.XPATH, main_page_private_account_btn).click()
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.XPATH, private_account_header)))
            assert driver.find_element(By.XPATH, private_account_header).text == 'Профиль'
            driver.quit()

    def test_private_account_constractor_link_success(self, driver, login_page, register_user,
                                                              main_page_private_account_btn, login_page_enter_btn,
                                                              login_page_login, login_page_password,
                                                              private_account_header, constractor_link,
                                                              main_page_order_btn):
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
            # нажимаем по ссылке Конструктор
            driver.find_element(By.XPATH, constractor_link).click()
            # ожидаем появления кнопки Оформить заказ
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, main_page_order_btn)))

            assert driver.find_element(By.CLASS_NAME, main_page_order_btn).text == 'Оформить заказ'
            driver.quit()


    def test_private_account_logo_link_success(self, driver, login_page, register_user,
                                                      main_page_private_account_btn, login_page_enter_btn,
                                                      login_page_login, login_page_password,
                                                      private_account_header, logo_link,
                                                      main_page_order_btn):
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
            # нажимаем по ссылке Логотипа
            driver.find_element(By.XPATH, logo_link).click()
            # ожидаем появления кнопки Оформить заказ
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, main_page_order_btn)))

            assert driver.find_element(By.CLASS_NAME, main_page_order_btn).text == 'Оформить заказ'
            driver.quit()
