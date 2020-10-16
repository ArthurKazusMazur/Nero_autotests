import pytest
import allure
from allure_commons.types import AttachmentType
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

link = "https://alpha.unic-lab.by/"
login = "user"
password = "123456789"
dashboard_link = "https://alpha.unic-lab.by/general"
wrong_login = "abrakadabra"
wrong_password = "1111221"
error_message = "Неправильно введен логин или пароль"


@pytest.mark.shoulds(scope="class")
@allure.feature("Login page elements")
@allure.severity('critical')  # blocker, critical, major, minor,  trivial
class TestShouldBeLoginPageElements():
    def test_should_be_login_label(self, browser):
        page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()
        page.should_be_login_label()  # выполняется метод страницы - проверка наличия элемента страницы

    def test_should_be_login_form(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()

    def test_should_be_login_input_field(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_input_field()

    def test_should_be_login_password_input_field(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_password_input_field()

    def test_should_be_login_button(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_button()

    def test_should_be_registration_link(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_registration_link()

    def test_should_be_forgot_password_link(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_forgot_password_link()


@pytest.mark.credentials(scope="class")
@allure.severity('critical')  # blocker, critical, major, minor,  trivial
class TestUserLoginScenarios():
    @allure.story("User login, using valid creds")
    def test_user_login_scenario(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_dashboard(login, password, dashboard_link)
        page.take_a_screenshot(browser)
        assert browser.current_url == dashboard_link, 'USER LOGIN is FAILED !!!'

    @allure.story("User login, using non valid login")
    def test_wrong_login_should_be_error_message(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.login(wrong_login, password)
        page.take_a_screenshot(browser)
        assert browser.find_element(*LoginPageLocators.INVALID_CREDS).text == error_message, "ERROR MESSAGE DIFFERS " \
                                                                                             "OR MISSED!!!"

    @allure.story("User login, using non valid password")
    def test_wrong_password_should_be_error_message(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.login(login, wrong_password)
        page.take_a_screenshot(browser)
        assert browser.find_element(*LoginPageLocators.INVALID_CREDS).text == error_message, "ERROR MESSAGE DIFFERS " \
                                                                                             "OR MISSED!!!"

    @allure.story("User login, using non valid both login & password")
    def test_wrong_login_and_password(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.login(login, wrong_password)
        assert browser.find_element(*LoginPageLocators.INVALID_CREDS).text == error_message, "ERROR MESSAGE DIFFERS " \
                                                                                             "OR MISSED!!!"
