import pytest
import time
import config
from pages.register_page import RegisterPage


@pytest.mark.smoke
def test_registration_new_user_success(browser):
    link = config.VALID_LINK_REGISTER_PAGE
    page = RegisterPage(browser, link)
    page.open()
    time.sleep(2)
    page.registration_new_user_success(config.REGISTER_EMAIL1, config.REGISTER_PASSWORD1)
    time.sleep(2)
    expected_url = config.VALID_LINK_PROFILE_PAGE
    time.sleep(2)
    current_url = browser.current_url
    assert expected_url == current_url, 'Пользователь с такими данными уже существует'


@pytest.mark.xfail
def test_registration_new_user_fail_password(browser):
    link = config.VALID_LINK_REGISTER_PAGE
    page = RegisterPage(browser, link)
    page.open()
    time.sleep(2)
    page.registration_new_user_fail_password(config.REGISTER_EMAIL2, config.REGISTER_PASSWORD2,
                                             config.REGISTER_PASSWORD22)
    time.sleep(2)
    expected_url = config.VALID_LINK_REGISTER_PAGE
    time.sleep(2)
    current_url = browser.current_url
    assert expected_url == current_url, 'Регистрация прошла успешно при неправильно подтвержденном паролем'
