import time
from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def registration_new_user_success(self, login, password):
        registration_email = self.browser.find_element(*RegisterPageLocators.LOGIN_EMAIL_NEW)
        registration_email.send_keys(login)
        time.sleep(2)
        registration_password = self.browser.find_element(*RegisterPageLocators.PASSWORD_NEW)
        registration_password.send_keys(password)
        time.sleep(2)
        registration_password_confirm = self.browser.find_element(*RegisterPageLocators.PASSWORD_CONFIRM)
        registration_password_confirm.send_keys(password)
        time.sleep(2)
        registration_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON_SUBMIT)
        registration_button.submit()
        return

    def registration_new_user_fail_password(self, login, password1, password2):
        registration_email = self.browser.find_element(*RegisterPageLocators.LOGIN_EMAIL_NEW)
        registration_email.send_keys(login)
        time.sleep(2)
        registration_password = self.browser.find_element(*RegisterPageLocators.PASSWORD_NEW)
        registration_password.send_keys(password1)
        time.sleep(2)
        registration_password_confirm = self.browser.find_element(*RegisterPageLocators.PASSWORD_CONFIRM)
        registration_password_confirm.send_keys(password2)
        time.sleep(2)
        registration_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON_SUBMIT)
        registration_button.submit()
        return
