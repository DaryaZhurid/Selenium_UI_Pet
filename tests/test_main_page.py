import pytest
from pages.main_page import MainPage
import time
import config


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_login_page()
    time.sleep(2)
    expected_url = config.VALID_LINK_LOGIN_PAGE
    time.sleep(2)
    current_url = browser.current_url
    assert expected_url == current_url, 'Не осуществлен переход на страницу ввода логина'


@pytest.mark.smoke
def test_go_to_register_page(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_register_page()
    time.sleep(2)
    expected_url = config.VALID_LINK_REGISTER_PAGE
    time.sleep(2)
    current_url = browser.current_url
    assert expected_url == current_url, 'Не осуществлен переход на страницу регистрации пользователя'


@pytest.mark.smoke
def test_dropdown_menu_displayed(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    dropdown_menu_displayed = page.check_dropdown_menu_displayed()
    time.sleep(2)
    assert dropdown_menu_displayed, 'Выпадающий список с наименованиями питомцев не отображается на странице'


@pytest.mark.smoke
def test_dropdown_menu_enabled(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    dropdown_menu_enabled = page.check_dropdown_menu_enabled()
    time.sleep(2)
    assert dropdown_menu_enabled, 'Выпадающий список с наименованиями питомцев не доступен для взаимодействия'


@pytest.mark.smoke
def test_logo_displayed(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    logo_displayed = page.check_logo_displayed()
    time.sleep(2)
    assert logo_displayed, 'Логотип не отображается на главной странице'


@pytest.mark.smoke
def test_filter_by_pet_name_input_is_enabled(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    input_pet_name_enabled = page.filter_by_pet_name_enabled()
    time.sleep(2)
    assert input_pet_name_enabled, 'Фильтр поиска по имени питомца не доступен'


@pytest.mark.smoke
def test_filter_by_pet_name_input(browser):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    filtered_pet_name = page.filter_by_pet_name_input(config.PET_FEMALE_NAME3)
    time.sleep(2)
    assert config.PET_FEMALE_NAME3 in filtered_pet_name, 'Введенный текст не соответствует отображаемому'


@pytest.mark.parametrize('option', config.DROPDOWN_OPTIONS)
def test_dropdown_options(browser, option):
    link = config.VALID_LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    dropdown_options = page.dropdown_options()
    time.sleep(2)
    assert option in dropdown_options, 'Доступны не все из обязательных видов питомцев'
