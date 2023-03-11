import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def registration_page():
    return 'https://stellarburgers.nomoreparties.site/register'  # URL страницы регистрации@pytest.fixture
@pytest.fixture
def login_page():
    return 'https://stellarburgers.nomoreparties.site/login'  # URL страницы регистрации
@pytest.fixture
def main_page():
    return 'https://stellarburgers.nomoreparties.site/'  # URL страницы регистрации
@pytest.fixture
def restore_password_page():
    return 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver
@pytest.fixture
def registration_login():
    # Natalya_любые 3 цифры
    return f"Natalya_{random.randint(100, 999)}"
@pytest.fixture
def registration_email():
    # Natalya_Kashirina_6_любые 3 цифры@yandex.ru
    return f"Natalya_Kashirina_6_{random.randint(100, 999)}@yandex.ru"
@pytest.fixture
def registration_password():
    return f"{random.randint(100000, 999999)}"

@pytest.fixture
def registration_form_field_login():
    return "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][1]//input"  # Поле логина
@pytest.fixture
def registration_form_field_email():
    return "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][2]//input"  # Поле email
@pytest.fixture
def registration_form_field_password():
    return "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][3]//input"  # Поле пароля
@pytest.fixture
def registration_form_field_password_error():
    return "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][3]//p"  # Поле ошибки пароля
@pytest.fixture
def registration_form_submit():
    return "//form[@class = 'Auth_form__3qKeq mb-20']//button"  # Кнопка Зарегистрироваться
@pytest.fixture
def registration_form_login_btn():
    return "//a[@class = 'Auth_link__1fOlj' and text() = 'Войти']"  # Кнопка Войти на форме регистрации
@pytest.fixture
def registration_page_error_p():
    return "//div[@class = 'Auth_login__3hAey']//p[@class = 'input__error text_type_main-default']"  # блок ошибки регистрации
@pytest.fixture
def main_page_enter_account_btn():
    return "BurgerConstructor_basket__container__2fUl3"  # кнопка Войти в аккаунт
@pytest.fixture
def main_page_private_account_btn():
    return "//a[@class = 'AppHeader_header__link__3D_hX']//p[text() = 'Личный Кабинет']"  # кнопка Личный кабинет
@pytest.fixture
def private_account_header():
    return "//li[@class ='Account_listItem__35dAP'][1]//a"  # Ссылка профиль в личном кабинете
@pytest.fixture
def private_account_logout_btn():
    return "//li[@class ='Account_listItem__35dAP'][3]/button"  # Ссылка Выход в личном кабинете
@pytest.fixture
def main_page_order_btn():
    return "button_button__33qZ0"  # кнопка Оформить заказ
@pytest.fixture
def login_page_header():
    return "//div[@class = 'Auth_login__3hAey']/h2[text() = 'Вход']"  # надпись Войти на странице входа
@pytest.fixture
def login_page_login():
    return ".//form[@class = 'Auth_form__3qKeq mb-20']//fieldset[1]//input"  # поле логина на странице входа
@pytest.fixture
def login_page_password():
    return ".//form[@class = 'Auth_form__3qKeq mb-20']//fieldset[2]//input"  # поле пароля на странице входа
@pytest.fixture
def login_page_enter_btn():
    return "button_button__33qZ0 "  # кнопка Войти на странице входа
@pytest.fixture
def login_page_enter_btn():
    return "button_button__33qZ0 "  # кнопка Войти на странице входа
@pytest.fixture
def restore_password_page_enter_btn():
    return "//a[@class = 'Auth_link__1fOlj' and text() = 'Войти']"  # кнопка Войти на странице восстановления пароля
@pytest.fixture
def constractor_link():
    return "//a[@class = 'AppHeader_header__link__3D_hX']//p[text() = 'Конструктор']"  # ссылка Конструктор из личного кабинета
@pytest.fixture
def logo_link():
    return "//div[@class = 'AppHeader_header__logo__2D0X2']/a"  # ссылка Логотип из личного кабинета
@pytest.fixture
def constructor_link_buns():
    return "//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text() = 'Булки']"  # раздел Булки в конструкторе
@pytest.fixture
def constructor_link_souses():
    return "//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text() = 'Соусы']"  # раздел Соусы в конструкторе
@pytest.fixture
def constructor_link_fillings():
    return "//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text() = 'Начинки']"  # раздел Начинки в конструкторе
@pytest.fixture
def constructor_tab_buns():
    return "//div[contains(@class,'tab_tab__1SPyG')]/span[text() = 'Булки']"  # вкладка Булки в конструкторе
@pytest.fixture
def constructor_tab_souses():
    return "//div[contains(@class,'tab_tab__1SPyG')]/span[text() = 'Соусы']"  # вкладка Соусы в конструкторе
@pytest.fixture
def constructor_tab_fillings():
    return "//div[contains(@class,'tab_tab__1SPyG')]/span[text() = 'Начинки']"  # вкладка Начинки в конструкторе
@pytest.fixture
def constructor_active_tab():
    return "//div[contains(@class,'tab_tab_type_current')]/span"  # активная вкладка в конструкторе
@pytest.fixture
def register_user(driver, registration_page,
    registration_form_submit, login_page,
    registration_login, registration_form_field_login,
    registration_email, registration_form_field_email,
    registration_password, registration_form_field_password):

    driver.get(registration_page)
    driver.find_element(By.XPATH, registration_form_field_login).send_keys(registration_login)
    driver.find_element(By.XPATH, registration_form_field_email).send_keys(registration_email)
    driver.find_element(By.XPATH, registration_form_field_password).send_keys(registration_password)
    driver.find_element(By.XPATH, registration_form_submit).click()
    time.sleep(1)
    if driver.current_url == login_page:
        return {"email": registration_email, "password": registration_password}
    else:
        return {"email": "", "password": ""}
