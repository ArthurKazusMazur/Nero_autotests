from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
from pages.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link = "https://alpha.unic-lab.by/"
login = "user"
password = "123456789"
dashboard_link = "https://alpha.unic-lab.by/general"


# def test_should_be_login_label(browser):
#     page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
#     page.open()
#     page.should_be_login_label()  # выполняется метод страницы - проверка наличия элемента страницы
#
#
# def test_should_be_login_form(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_should_be_login_input_field(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_input_field()
#
#
# def test_should_be_login_password_input_field(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_password_input_field()
#
#
# def test_should_be_login_button(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_button()
#
#
# def test_should_be_registration_link(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_registration_link()
#
#
# def test_should_be_forgot_password_link(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_forgot_password_link()


# Необходимо будет преключиться на новую страницу?
# def test_user_login_scenario(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.go_to_dashboard_page(login, password)
#     assert browser.current_url == dashboard_link, 'LOGIN FAILED !!!'

