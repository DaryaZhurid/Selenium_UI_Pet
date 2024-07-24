import pytest
from pages.profile_page import ProfilePage
import time
import config


@pytest.mark.regression
def test_check_profile_not_empty(browser, profile_page):
    link = config.VALID_LINK_PROFILE_PAGE
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    pet_count = page.get_pet_count()
    time.sleep(2)
    assert pet_count != 0, 'Нет ни одной карточки питомца в профиле'


@pytest.mark.smoke
def test_add_new_pet_cat_male(browser, profile_page):
    link = config.VALID_LINK_PROFILE_PAGE
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    pet_count = page.get_pet_count()
    time.sleep(2)
    page.add_new_pet_cat_male(config.PET_MALE_NAME1, config.AGE4, 'resources/pets1catsJake.jpeg')
    time.sleep(2)
    new_pet_count = page.get_pet_count()
    time.sleep(2)
    assert new_pet_count == pet_count + 1, 'Новая карточка питомца не добавлена'


@pytest.mark.smoke
def test_delete_first_pet_profile(browser, profile_page):
    link = config.VALID_LINK_PROFILE_PAGE
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    pet_count = page.get_pet_count()
    assert pet_count > 0, 'Нет ни одного питомца на странице профиля'
    page.delete_first_pet_profile()
    time.sleep(2)
    new_pet_count = page.get_pet_count()
    time.sleep(2)
    if pet_count > 0:
        assert new_pet_count == pet_count - 1


@pytest.mark.smoke
def test_edit_name_first_pet_profile(browser, profile_page):
    link = config.VALID_LINK_PROFILE_PAGE
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    first_name = page.edit_name_first_pet_profile(config.PET_MALE_NAME2)
    time.sleep(2)
    assert first_name != config.PET_MALE_NAME2, 'Имя питомца изменено на аналогичное'


@pytest.mark.regression
def test_list_all_pets_names_empty_name(browser, profile_page):
    link = config.VALID_LINK_PROFILE_PAGE
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    list_all_pets_names = page.get_all_pets_names()
    for name in list_all_pets_names:
        assert name.strip() != '', 'Среди имен питомцев найдена пустая строка'
