import os
import time
from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):

    def get_pet_count(self):
        pets = self.browser.find_elements(*ProfilePageLocators.PETS)
        return len(pets)

    def add_new_pet_cat_male(self, name, age, photo_path):
        pet_button = self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON)
        pet_button.click()
        pet_name_input = self.browser.find_element(*ProfilePageLocators.PET_NAME_INPUT)
        pet_name_input.send_keys(name)
        time.sleep(1)
        pet_type_dropdown = self.browser.find_element(*ProfilePageLocators.PET_TYPE_DROPDOWN)
        pet_type_dropdown.click()
        pet_type_cat = self.browser.find_element(*ProfilePageLocators.PET_TYPE_CAT)
        pet_type_cat.click()
        time.sleep(1)
        pet_age_input = self.browser.find_element(*ProfilePageLocators.PET_AGE_INPUT)
        pet_age_input.send_keys(age)
        time.sleep(1)
        pet_gender_dropdown = self.browser.find_element(*ProfilePageLocators.PET_GENDER_DROPDOWN)
        pet_gender_dropdown.click()
        pet_gender_male = self.browser.find_element(*ProfilePageLocators.PET_GENDER_MALE)
        pet_gender_male.click()
        time.sleep(1)
        submit_button = self.browser.find_element(*ProfilePageLocators.SUBMIT_DESCRIPTION_BUTTON)
        submit_button.click()
        time.sleep(1)
        pet_photo_input = self.browser.find_element(*ProfilePageLocators.PET_PHOTO_INPUT)
        pet_photo_input.send_keys(os.path.abspath(photo_path))
        time.sleep(1)
        accept_button = self.browser.find_element(*ProfilePageLocators.ACCEPT_PHOTO_BUTTON)
        accept_button.click()
        return

    def delete_first_pet_profile(self):
        delete_pet_button = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BUTTON)
        delete_pet_button.click()
        time.sleep(1)
        delete_pet_yes = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BUTTON_YES)
        delete_pet_yes.click()
        return

    def edit_name_first_pet_profile(self, name):
        edit_button = self.browser.find_element(*ProfilePageLocators.EDIT_BUTTON)
        edit_button.click()
        time.sleep(1)
        edit_name = self.browser.find_element(*ProfilePageLocators.EDIT_NAME_PROFILE)
        edit_name.clear()
        edit_name.send_keys(name)
        save_button = self.browser.find_element(*ProfilePageLocators.SAVE_CHANGES_BUTTON)
        save_button.click()
        first_name = self.browser.find_element(*ProfilePageLocators.FIRST_PET_NAME).text.split()[0]
        return first_name

    def get_all_pets_names(self):
        pet_name_elements = self.browser.find_elements(*ProfilePageLocators.PETS_NAMES)
        pets_names = [element.text for element in pet_name_elements]
        return pets_names
