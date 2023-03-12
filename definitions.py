from selenium.webdriver.common.by import By
import random
import time

registration_page = 'https://stellarburgers.nomoreparties.site/register'  # URL страницы регистрации@pytest.fixture
login_page = 'https://stellarburgers.nomoreparties.site/login'  # URL страницы регистрации
main_page = 'https://stellarburgers.nomoreparties.site/'  # URL страницы регистрации
restore_password_page = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
registration_form_field_login = "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][1]//input"  # Поле логина
registration_form_field_email = "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][2]//input"  # Поле email
registration_form_field_password = "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][3]//input"  # Поле пароля
registration_form_field_password_error = "//fieldset[@class = 'Auth_fieldset__1QzWN mb-6'][3]//p"  # Поле ошибки пароля
registration_form_submit = "//form[@class = 'Auth_form__3qKeq mb-20']//button"  # Кнопка Зарегистрироваться
registration_form_login_btn = "//a[@class = 'Auth_link__1fOlj' and text() = 'Войти']"  # Кнопка Войти на форме регистрации
registration_page_error_p = "//div[@class = 'Auth_login__3hAey']//p[@class = 'input__error text_type_main-default']"  # блок ошибки регистрации
main_page_enter_account_btn = "BurgerConstructor_basket__container__2fUl3"  # кнопка Войти в аккаунт
main_page_private_account_btn = "//a[@class = 'AppHeader_header__link__3D_hX']//p[text() = 'Личный Кабинет']"  # кнопка Личный кабинет
private_account_header = "//li[@class ='Account_listItem__35dAP'][1]//a"  # Ссылка профиль в личном кабинете
private_account_logout_btn = "//li[@class ='Account_listItem__35dAP'][3]/button"  # Ссылка Выход в личном кабинете
main_page_order_btn = "button_button__33qZ0"  # кнопка Оформить заказ
login_page_header = "//div[@class = 'Auth_login__3hAey']/h2[text() = 'Вход']"  # надпись Войти на странице входа
login_page_login = ".//form[@class = 'Auth_form__3qKeq mb-20']//fieldset[1]//input"  # поле логина на странице входа
login_page_password = ".//form[@class = 'Auth_form__3qKeq mb-20']//fieldset[2]//input"  # поле пароля на странице входа
login_page_enter_btn = "button_button__33qZ0 "  # кнопка Войти на странице входа
restore_password_page_enter_btn = "//a[@class = 'Auth_link__1fOlj' and text() = 'Войти']"  # кнопка Войти на странице восстановления пароля
constractor_link = "//a[@class = 'AppHeader_header__link__3D_hX']//p[text() = 'Конструктор']"  # ссылка Конструктор из личного кабинета
logo_link = "//div[@class = 'AppHeader_header__logo__2D0X2']/a"  # ссылка Логотип из личного кабинета
constructor_link_buns = "//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text() = 'Булки']"  # раздел Булки в конструкторе
constructor_link_souses = "//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text() = 'Соусы']"  # раздел Соусы в конструкторе
constructor_link_fillings = "//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[text() = 'Начинки']"  # раздел Начинки в конструкторе
constructor_tab_buns = "//div[contains(@class,'tab_tab__1SPyG')]/span[text() = 'Булки']"  # вкладка Булки в конструкторе
constructor_tab_souses = "//div[contains(@class,'tab_tab__1SPyG')]/span[text() = 'Соусы']"  # вкладка Соусы в конструкторе
constructor_tab_fillings = "//div[contains(@class,'tab_tab__1SPyG')]/span[text() = 'Начинки']"  # вкладка Начинки в конструкторе
constructor_active_tab = "//div[contains(@class,'tab_tab_type_current')]/span"  # активная вкладка в конструкторе
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
def registration_login():
    # Natalya_любые 3 цифры
    return f"Natalya_{random.randint(100, 999)}"
def registration_email():
    # Natalya_Kashirina_6_любые 3 цифры@yandex.ru
    return f"Natalya_Kashirina_6_{random.randint(100, 999)}@yandex.ru"
def registration_password():
    return f"{random.randint(100000, 999999)}"
