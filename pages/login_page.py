import time
from .base_page import BasePage
from .locators import LoginPageLocators
import config


class LoginPage(BasePage):
    def go_to_login_valid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(config.VALID_EMAIL)
        return

    def go_to_login_valid_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(config.VALID_PASSWORD)
        return

    def go_to_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
        return

    def valid_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(config.VALID_EMAIL)
        time.sleep(1)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(config.VALID_PASSWORD)
        time.sleep(1)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
        return

    def valid_login_parametrize(self, login, password):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(login)
        time.sleep(1)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password)
        time.sleep(1)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
        return

    def go_to_login_invalid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(config.INVALID_EMAIL)
        return

    def go_to_login_invalid_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(config.INVALID_PASSWORD)
        return

    def invalid_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(config.INVALID_EMAIL)
        time.sleep(1)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(config.INVALID_PASSWORD)
        time.sleep(1)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
        return
