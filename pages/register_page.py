from .base_page import BasePage
from pages.locators import RegisterPageLocators
from pages.locators import LoginPageLocators


class RegisterPage(BasePage):
    def should_be_register_label(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_LABEL), "REGISTER LABEL is MISSED!!!"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "REGISTER FORM is MISSED!!!"

    def should_be_register_login_input(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_INPUT), \
            "REGISTER LOGIN INPUT is MISSED!!!"

    def should_be_register_email_input(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_EMAIL_INPUT), \
            "REGISTER EMAIL INPUT is MISSED!!!"

    def should_be_register_password_input(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_PASSWORD_INPUT), \
            "REGISTER PASSWORD INPUT is MISSED!!!"

    def should_be_register_repeat_password_input(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_REPEAT_PASSWORD_INPUT), \
            "REGISTER REPEAT PASSWORD INPUT is MISSED!!!"

    def should_be_register_btn(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_BUTTON), "REGISTER BUTTON is MOSSED!!!"

    def enter_login_non_valid(self, login):
        self.browser.find_element(*RegisterPageLocators.REGISTER_INPUT).send_keys(login)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(*RegisterPageLocators.LOGIN_LENGTH_MESSAGE), \
            "ERROR MESSAGE is NOT DISPLAYED!!!"

    def enter_login_valid(self, login):
        self.browser.find_element(*RegisterPageLocators.REGISTER_INPUT).send_keys(login)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert self.is_not_element_present(*RegisterPageLocators.LOGIN_LENGTH_MESSAGE), \
            "ERROR MESSAGE is PRESENT!!!"

    def enter_email_non_valid(self, email):
        self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(*RegisterPageLocators.EMAIL_MESSAGE), \
            "ERROR MESSAGE is NOT DISPLAYED!!!"

    def enter_password_non_valid(self, password):
        self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(*RegisterPageLocators.PASSWORD_MESSAGE), \
            "ERROR MESSAGE is NOT DISPLAYED!!!"

    def enter_password(self, password, login):
        self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_REPEAT_PASSWORD_INPUT).send_keys(login)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(*RegisterPageLocators.PASSWORD_MESSAGE), \
            "ERROR MESSAGE is NOT DISPLAYED!!!"

    def enter_password_to_register(self, password, login):
        self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_REPEAT_PASSWORD_INPUT).send_keys(login)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    def user_register(self, login, email, password, repeat_password):
        self.browser.find_element(*RegisterPageLocators.REGISTER_INPUT).send_keys(login)
        self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_REPEAT_PASSWORD_INPUT).send_keys(repeat_password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

