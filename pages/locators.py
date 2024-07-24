from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    REGISTER_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a > span')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '#typesSelector')
    DROPDOWN_OPTIONS = (By.CSS_SELECTOR, '.p-dropdown-item')
    LOGO = (By.CSS_SELECTOR, '#app > header > div > div > img')
    PET_FILTER = (By.ID, 'petName')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BUTTON = (By.CLASS_NAME, 'p-button-label')


class ProfilePageLocators:
    PETS = (By.CSS_SELECTOR, '.col-12')
    ADD_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > '
                                       'button')
    PET_NAME_INPUT = (By.ID, 'name')
    PET_TYPE_DROPDOWN = (By.ID, 'typeSelector')
    PET_TYPE_DOG = (By.XPATH, '//div[3]/div/ul/li')
    PET_TYPE_CAT = (By.XPATH, '//div[3]/div/ul/li[2]')
    PET_TYPE_REPTILE = (By.XPATH, '//li[3]')
    PET_TYPE_HAMSTER = (By.XPATH, '//li[4]')
    PET_TYPE_PARROT = (By.XPATH, '//li[5]')
    PET_AGE_INPUT = (By.CSS_SELECTOR, '#age > input')
    PET_GENDER_DROPDOWN = (By.ID, 'genderSelector')
    PET_GENDER_MALE = (By.XPATH, '//div[3]/div/ul/li')
    PET_GENDER_FEMALE = (By.XPATH, '//div[3]/div/ul/li[2]')
    SUBMIT_DESCRIPTION_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > form > div > '
                                                  'div.p-card-body > div.p-card-footer > '
                                                  'button.p-button.p-component.p-button-success')
    CHOOSE_PHOTO_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div:nth-child(2) > '
                                            'div.col-12.justify-content-center.flex > div > span')
    PET_PHOTO_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
    ACCEPT_PHOTO_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div:nth-child(2) > '
                                            'div.col-12.justify-content-center.flex > div > span')
    DELETE_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[2]/span[2]')

    DELETE_PET_BUTTON_YES = (By.XPATH, '/html/body/div[3]/div[2]/button[2]/span')
    EDIT_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) > div '
                                    '> div.product-list-action > button:nth-child(1) > span.p-button-label')
    EDIT_NAME_PROFILE = (By.ID, 'name')
    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, '#app > main > div > form > div > div.p-card-body > div.p-card-footer > '
                                            'button > span.p-button-label')
    PETS_NAMES = (By.CSS_SELECTOR, '.product-name')
    FIRST_PET_NAME = (By.CSS_SELECTOR, '.product-name')


class RegisterPageLocators:
    LOGIN_EMAIL_NEW = (By.ID, 'login')
    PASSWORD_NEW = (By.XPATH, '//*[@id="password"]/input')
    PASSWORD_CONFIRM = (By.XPATH, '//*[@id="confirm_password"]/input')
    REGISTER_BUTTON_SUBMIT = (By.XPATH, '//span[2]')
