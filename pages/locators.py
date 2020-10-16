from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LABEL = (By.XPATH, "//div/label[@class='base-label__label']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".base-form__content")
    LOGIN_INPUT = (By.XPATH, '//div/input[@name="login"]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//div/input[@name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    LOGIN_REG_LINK = (By.XPATH, '//div//button[2]')
    LOGIN_FORGOT_PASSWORD_LINK = (By.XPATH, '//div//button[3]')
    INVALID_CREDS = (By.CSS_SELECTOR, '[class="base-error-label"]')


class RegisterPageLocators():
    REGISTER_LABEL = (By.XPATH, "//div/label[@class='base-label__label']")
    REGISTER_FORM = (By.CSS_SELECTOR, ".base-form__content")
    REGISTER_INPUT = (By.CSS_SELECTOR, '[name="login"]')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '[name="email"]')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    REGISTER_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="repeatPassword"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    REGISTER_LOGIN_LINK = (By.XPATH, '//div/button[2]')
    LOGIN_LENGTH_MESSAGE = (By.XPATH, '//*[@id="app"]/div/span/div[1]/form/div[5]/label[1]')
    PASSWORD_MESSAGE = (By.XPATH, '//*[@id="app"]/div/span/div[1]/form/div[5]/label[2]')
    EMAIL_MESSAGE = (By.XPATH, '//*[@id="app"]/div/span/div[1]/form/div[5]/label[3]')