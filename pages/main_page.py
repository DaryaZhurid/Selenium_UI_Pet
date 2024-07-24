import time
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return login_link

    def go_to_register_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()
        return register_link

    def check_dropdown_menu_displayed(self):
        dropdown_menu = self.browser.find_element(*MainPageLocators.DROPDOWN_MENU)
        return dropdown_menu.is_displayed()

    def check_dropdown_menu_enabled(self):
        dropdown_menu = self.browser.find_element(*MainPageLocators.DROPDOWN_MENU)
        return dropdown_menu.is_enabled()

    def check_logo_displayed(self):
        logo_main_page = self.browser.find_element(*MainPageLocators.LOGO)
        return logo_main_page.is_displayed()

    def filter_by_pet_name_enabled(self):
        filter_input = self.browser.find_element(*MainPageLocators.PET_FILTER)
        return filter_input.is_enabled()

    def filter_by_pet_name_input(self, pet_name):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.PET_FILTER)
        filter_by_pet_name.clear()
        time.sleep(1)
        filter_by_pet_name.send_keys(pet_name)
        time.sleep(1)
        return filter_by_pet_name.get_attribute('value')

    def dropdown_options(self):
        dropdown_menu = self.browser.find_element(*MainPageLocators.DROPDOWN_MENU)
        dropdown_menu.click()
        time.sleep(1)
        dropdown_options = [option.text.lower() for option in
                            self.browser.find_elements(*MainPageLocators.DROPDOWN_OPTIONS)]
        return dropdown_options
