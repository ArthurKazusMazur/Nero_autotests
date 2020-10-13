from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

register_url = "https://alpha.unic-lab.by/auth/register"
link = "https://alpha.unic-lab.by/"


def test_go_to_register_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_registration_page(register_url)
    assert browser.current_url == register_url, "REDIRECT TO REGISTRATION PAGE is FAILED!!!"
