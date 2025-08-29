import allure
import pytest
from main_page import MainPage



@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги по полному названию на кириллице")
@allure.description("Тест проверяет возможность поиска книги"
                    " по заголовку 'игрушки'.")
@pytest.mark.positive
@pytest.mark.ui
def test_search_by_full_name(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_book("игрушки")
    assert (("Показываем результаты по запросу "
            "«игрушки», найдено:")
            in main_page.get_search_results_text())


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги с символами вместо названия")
@allure.description("Тест проверяет поиск книги "
                    "с использование символов вместо названия")
@pytest.mark.negative
@pytest.mark.ui
def test_search_by_symbols_only(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_book("№?%")
    assert ("Поиск по запросу «№?%» не принёс результатов"
            in main_page.get_search_results_text())


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги  с символами и нозванием ")
@allure.description("Тест проверяет поиск книги с символами и нозванием")
@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.ui
def test_search_by_symbols_and_text(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_book("№?%игрушки")
    assert ("показывает результаты по запросу "
            " «№?%игрушки» , найдено"
            in main_page.get_search_results_text())


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги с неполным названием ")
@allure.description("Тест проверяет поиск книги с неполным нозванием")
@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.ui
def test_search_by_space_and_text(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_book(" нора")
    assert ("Поиск по запросу « нора» не принёс результатов"
            in main_page.get_search_results_text())


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги по названию на латинице")
@allure.description("Тест проверяет возможность поиска книги "
                    "по заголовку 'Python'.")
@pytest.mark.positive
@pytest.mark.ui
def test_search_by_name_with_numbers(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search_book("1984")
    assert ("Показываем результаты по запросу «1984», найдено:"
            in main_page.get_search_results_text())