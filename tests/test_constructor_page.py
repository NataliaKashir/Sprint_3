from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

class TestConstructorPage:
    def test_constructor_page_souses_scroll_success(self, driver, main_page,
                                            constructor_link_buns,
                                            constructor_link_souses,
                                            constructor_tab_souses):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, constructor_tab_souses)))
        # координата вкладки по умолчанию (Булки)
        start_y = driver.find_element(By.XPATH, constructor_link_buns).location['y']
        start_margin = int(driver.find_element(By.XPATH, constructor_link_buns).value_of_css_property('margin-top').replace('px', ''))
        # Нажимаем на вкладку Соусы
        driver.find_element(By.XPATH, constructor_tab_souses).click()
        time.sleep(1)
        tab_y = driver.find_element(By.XPATH, constructor_link_souses).location['y']
        assert (start_y - start_margin) == tab_y
        driver.quit()

    def test_constructor_page_fillings_scroll_success(self, driver, main_page,
                                            constructor_link_buns,
                                            constructor_link_fillings,
                                            constructor_tab_fillings):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, constructor_tab_fillings)))
        # координата вкладки по умолчанию (Булки)
        start_y = driver.find_element(By.XPATH, constructor_link_buns).location['y']
        start_margin = int(driver.find_element(By.XPATH, constructor_link_buns).value_of_css_property('margin-top').replace('px', ''))
        # Нажимаем на вкладку Начинки
        driver.find_element(By.XPATH, constructor_tab_fillings).click()
        time.sleep(1)
        tab_y = driver.find_element(By.XPATH, constructor_link_fillings).location['y']
        assert (start_y - start_margin) == tab_y
        driver.quit()

    def test_constructor_page_buns_scroll_success(self, driver, main_page,
                                            constructor_link_buns,
                                            constructor_link_fillings,
                                            constructor_tab_fillings,
                                            constructor_tab_buns):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, constructor_tab_fillings)))
        # координата вкладки по умолчанию (Булки)
        start_y = driver.find_element(By.XPATH, constructor_link_buns).location['y']
        start_margin = int(driver.find_element(By.XPATH, constructor_link_buns).value_of_css_property('margin-top').replace('px', ''))
        # Нажимаем на вкладку Начинки
        driver.find_element(By.XPATH, constructor_tab_fillings).click()
        time.sleep(1)
        tab_y = driver.find_element(By.XPATH, constructor_link_fillings).location['y']
        # если прокрутка отработала
        if (start_y - start_margin) == tab_y:
            # Нажимаем на вкладку Булки
            driver.find_element(By.XPATH, constructor_tab_buns).click()
            time.sleep(1)
            tab_buns_y = driver.find_element(By.XPATH, constructor_link_buns).location['y']
            assert (start_y - start_margin) == tab_buns_y
        driver.quit()

    def test_constructor_page_souses_tab_success(self, driver, main_page,
                                            constructor_tab_souses,
                                            constructor_active_tab):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, constructor_tab_souses)))
        # Нажимаем на вкладку Соусы
        driver.find_element(By.XPATH, constructor_tab_souses).click()
        time.sleep(1)
        active_tab = driver.find_element(By.XPATH, constructor_active_tab).text
        assert active_tab == "Соусы"
        driver.quit()

    def test_constructor_page_fillings_tab_success(self, driver, main_page,
                                            constructor_tab_fillings,
                                            constructor_active_tab):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, constructor_tab_fillings)))
        # Нажимаем на вкладку Начинки
        driver.find_element(By.XPATH, constructor_tab_fillings).click()
        time.sleep(1)
        active_tab = driver.find_element(By.XPATH, constructor_active_tab).text
        assert active_tab == "Начинки"
        driver.quit()

    def test_constructor_page_buns_tab_success(self, driver, main_page,
                                                 constructor_tab_buns,
                                                 constructor_tab_souses,
                                                 constructor_active_tab):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, constructor_tab_souses)))
        # Нажимаем на вкладку Соусы, чтобы текущая вкладка сменилась относительно дефолтной
        driver.find_element(By.XPATH, constructor_tab_souses).click()
        time.sleep(1)
        # Нажимаем на вкладку Булки
        driver.find_element(By.XPATH, constructor_tab_buns).click()
        time.sleep(1)
        active_tab = driver.find_element(By.XPATH, constructor_active_tab).text
        assert active_tab == "Булки"
        driver.quit()
