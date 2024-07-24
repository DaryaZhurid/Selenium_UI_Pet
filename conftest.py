import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import config


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def profile_page(browser):
    link = config.VALID_LINK_LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.valid_login()
    return page
