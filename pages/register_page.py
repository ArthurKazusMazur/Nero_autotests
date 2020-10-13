from .base_page import BasePage
from pages.locators import RegisterPageLocators
from pages.locators import LoginPageLocators


class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_page()()
        self.should_be_register_form()

    def should_be_register_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True