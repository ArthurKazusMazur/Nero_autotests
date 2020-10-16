from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(BasePage):
    def login(self, user_login, user_password):
        self.browser.find_element(*LoginPageLocators.LOGIN_INPUT).send_keys(user_login)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def go_to_registration_page(self, reg_url):
        self.browser.find_element(*LoginPageLocators.LOGIN_REG_LINK).click()
        WebDriverWait(self.browser, 5).until(EC.url_to_be(reg_url))
        assert self.browser.current_url == reg_url, "REDIRECT TO REGISTRATION PAGE is FAILED!!!"

    def go_to_dashboard(self, user_login, user_password, dash_url):
        self.browser.find_element(*LoginPageLocators.LOGIN_INPUT).send_keys(user_login)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.browser, 5).until(EC.url_to_be(dash_url))

    def should_be_login_label(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LABEL), "LOGIN LABEL is MISSED!!!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN FORM is MISSED!!!"

    def should_be_login_input_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT), "LOGIN PAGE INPUT FIELD is MISSED!!!"

    def should_be_login_password_input_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), \
            "LOGIN PASSWORD INPUT FIELD is MISSED!!!"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "LOGIN PAGE LOGIN BUTTON IS MISSED!!!"

    def should_be_registration_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REG_LINK), \
            "LOGIN PAGE 'Registration' LINK IS MISSED!!!"

    def should_be_forgot_password_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_LINK), \
            "LOGIN PAGE 'Forgot password' LINK IS MISSED!!!"







