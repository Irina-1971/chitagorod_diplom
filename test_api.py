import requests
import pytest
import allure
from config import headers, base_url


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
@pytest.mark.positive
@pytest.mark.api
def test_api_book_by_author():
    resp = requests.get(
        f"{base_url}search/product?phrase=Агния Барто",
        headers=headers)
    assert resp.status_code == 200


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору на английском")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
@pytest.mark.positive
@pytest.mark.api
def test_api_book_by_author_english():
    resp = requests.get(
        f"{base_url}search/product?phrase=jonathan coe",
        headers=headers)
    assert resp.status_code == 200


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с китайской фразой")
@allure.description("Проверка, что API возвращает ошибку при "
                    "поиске с китайской фразой.")
@pytest.mark.negative
@pytest.mark.api
def test_negative_api_japanese():
    resp = requests.get(
        f"{base_url}search/product?phrase=你好", headers=headers)
    assert resp.status_code == 422


@allure.epic("API Тестирование")
@allure.feature("Получение категорий книг")
@allure.title("Тестирование получения списка категорий книг")
@allure.description("Проверка, что API возвращает успешный ответ "
                    "с доступными категориями книг.")
@pytest.mark.positive
@pytest.mark.api
def test_api_get_categories():
    resp = requests.get(
        f"{base_url}categories", headers=headers)
    assert resp.status_code == 200


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с пустым запросом")
@allure.description("Проверка, что API возвращает ошибку "
                    "при поиске с пустым запросом.")
@pytest.mark.negative
@pytest.mark.api
def test_negative_api_empty_query():
    resp = requests.get(
        f"{base_url}search/product?phrase=", headers=headers)
    assert resp.status_code == 400