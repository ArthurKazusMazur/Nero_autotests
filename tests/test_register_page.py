import pytest
import allure
import faker
from faker import Faker
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from pages.locators import LoginPageLocators, RegisterPageLocators
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

register_url = "https://alpha.unic-lab.by/auth/register"
link = "https://alpha.unic-lab.by/"
faker = Faker()
email = faker.email()
non_valid_email = 'asfd@'
login = faker.name()
password = "123456789"
login_less_then_8 = "asdfg"
login_more_then_18 = "qwerty________kleer"
password_less_then_8 = "1234567"
password_more_then_18 = "123456789012345678"


@allure.feature("Go to Register page")
@allure.severity('critical')  # blocker, critical, major, minor,  trivial
def test_go_to_register_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_registration_page(register_url)
    page.take_a_screenshot(browser)


@pytest.mark.shoulds(scope="class")
@allure.feature("Register page elements")
@allure.severity('critical')  # blocker, critical, major, minor,  trivial
class TestShouldBeRegisterPageElements():
    def test_should_be_registration_label(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_label()
        page.take_a_screenshot(browser)

    def test_should_be_registration_form(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_form()
        page.take_a_screenshot(browser)

    def test_should_be_login_input_field(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_login_input()
        page.take_a_screenshot(browser)

    def test_should_be_email_input_field(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_email_input()
        page.take_a_screenshot(browser)

    def test_should_be_password_input_field(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_password_input()
        page.take_a_screenshot(browser)

    def test_should_be_repeat_password_input_field(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_repeat_password_input()
        page.take_a_screenshot(browser)

    def test_should_be_registration_button(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.should_be_register_btn()
        page.take_a_screenshot(browser)


@pytest.mark.creds(scope="class")
@allure.feature("User register scenarios")
@allure.severity('major')  # blocker, critical, major, minor,  trivial
class TestRegisterInputFieldsInspection():
    def test_login_input_field_short_length(self, browser):  # должна быть не меньше 8 символов и не больше 18 символов
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_login_non_valid(login_less_then_8)
        page.take_a_screenshot(browser)

    def test_login_input_long_length(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_login_non_valid(login_more_then_18)
        page.take_a_screenshot(browser)

    @pytest.mark.xfail
    def test_login_input_valid(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_login_valid(login)
        page.take_a_screenshot(browser)

    def test_email_input_mask(self, browser):  # негативный
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_email_non_valid(non_valid_email)
        page.take_a_screenshot(browser)

    @pytest.mark.xfail
    def test_password_input_short_length(self, browser):  # должна быть не меньше 8 символов и не больше 18 символов
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_password_non_valid(password_less_then_8)
        page.take_a_screenshot(browser)

    def test_password_input_long_length(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_password_non_valid(password_more_then_18)
        page.take_a_screenshot(browser)

    def test_passwords_are_not_match(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.enter_password(login, password)
        page.take_a_screenshot(browser)

    def test_user_registration(self, browser):
        page = RegisterPage(browser, register_url)
        page.open()
        page.user_register(login, email, password, password)
        page.take_a_screenshot(browser)
