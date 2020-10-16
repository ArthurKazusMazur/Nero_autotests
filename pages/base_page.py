import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def take_a_screenshot(self, browser):  # делает скриншот для отчета allure
        with allure.step('Taking a screenshot'):
            allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
