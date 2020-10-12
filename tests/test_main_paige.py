from pages.main_page import MainPage

link = "https://alpha.unic-lab.by/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page()  # выполняется метод страницы - переход на страницу логина


def test_guest_should_see_login_button(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_button()
