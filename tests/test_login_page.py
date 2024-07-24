import pytest
from pages.login_page import LoginPage
import time
import config


@pytest.mark.smoke
def test_go_to_valid_login(browser):
    link = config.VALID_LINK_LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    time.sleep(2)
    page.valid_login()
    time.sleep(2)
    expected_url = config.VALID_LINK_PROFILE_PAGE
    time.sleep(2)
    current_url = browser.current_url
    assert expected_url == current_url, 'Не удалось перейти на страницу профиля'


@pytest.mark.xfail
def test_go_to_invalid_login(browser):
    link = config.VALID_LINK_LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    time.sleep(2)
    page.invalid_login()
    time.sleep(2)
    expected_url = config.VALID_LINK_LOGIN_PAGE
    time.sleep(2)
    current_url = browser.current_url
    assert expected_url == current_url, 'Выполнен вход по незалогиненным данным'


@pytest.mark.parametrize('login,password,expected_result', [
    (config.VALID_EMAIL, config.VALID_PASSWORD, config.VALID_LINK_PROFILE_PAGE),
    (config.INVALID_EMAIL, config.INVALID_PASSWORD, config.VALID_LINK_LOGIN_PAGE)
])
def test_login(browser, login, password, expected_result):
    link = config.VALID_LINK_LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    time.sleep(2)
    page.valid_login_parametrize(login, password)
    time.sleep(2)
    current_url = browser.current_url
    assert expected_result == current_url, 'Вводимые логин и пароль не прошли проверку'
