# Чек-листы:
# 1	    Валидный токен	    Прошлая дата
# 2	    Валидный токен	    Сегодняшняя дата
# 3	    Валидный токен	    Будущая дата
# 4	    Валидный токен	    Невалидная дата
# 5	    Валидный токен	    Пробел вместо даты
# 6	    Валидный токен	    Пустая дата

# 7	    Валидный токен	    дата формата DD.MM.YYYY
# 8	    Валидный токен	    дата формата DD-MM-YYYY
# 9	    Валидный токен	    дата формата DD/MM/YYYY
# 10	Валидный токен	    дата формата YY-MM-DD
# 11	Валидный токен	    дата формата YYYY.MM.DD
# 12	Валидный токен	    дата формата YYYY/MM/DD
# 13	Валидный токен	    текстовая дата


# 14	Невалидный токен	Прошлая дата
# 15	Невалидный токен	Сегодняшняя дата
# 16	Невалидный токен	Будущая дата
# 17    Невалидный токен	Невалидная дата
# 18	Невалидный токен	Пробел вместо даты
# 19	Невалидный токен	Пустая дата

# 20	Пустой токен	    Прошлая дата
# 21	Пустой токен	    Сегодняшняя дата
# 22	Пустой токен	    Будущая дата
# 23	Пустой токен        Невалидная дата
# 24	Пустой токен	    Пробел вместо даты
# 25	Пустой токен	    Пустая дата



# рекомендуется запуск через терминал с командой вида: pytest -s -v Homework_7.py


import requests
import pytest


@pytest.mark.parametrize('token', ["nHCHa5c7Cwk0IMdmPgthcyYL8vkajhxKR5HEVxZz"])
@pytest.mark.parametrize('date', ["2024-02-06", "2024-02-07", "2024-02-08", "2023-02-30", " ", ""])
def test_valid_token_any_date(token, date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={token}&date={date}"
    response = requests.get(url)
    result = response.status_code
    assert result != 400, f"{response.json().get('msg')}"


@pytest.mark.parametrize('token', ["nHCHa5c7Cwk0IMdmPgthcyYL8vkajhxKR5HEVxZz"])
@pytest.mark.parametrize('date', ["06.05.2023", "06-05-2023", "06/05/2023", "24-02-06", "2024.02.06", "2024/02/06", "Hello"])
def test_valid_token_any_non_format_date(token, date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={token}&date={date}"
    response = requests.get(url)
    result = response.status_code
    assert result != 400, f"{response.json().get('msg')}"


@pytest.mark.parametrize('token', ["XXXHa5c7Cwk0IMdmPgthcyYL8vkajhxKR5HEVxZz"])
@pytest.mark.parametrize('date', ["2024-02-06", "2024-02-07", "2024-02-08", "2023-02-30", " ", ""])
def test_invalid_token_any_date(token, date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={token}&date={date}"
    response = requests.get(url)
    result = response.status_code
    assert result != 403, f"{response.json().get('error').get('message')}"


@pytest.mark.parametrize('token', [""])
@pytest.mark.parametrize('date', ["2024-02-06", "2024-02-07", "2024-02-08", "2023-02-30", " ", ""])
def test_null_token_any_date(token, date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={token}&date={date}"
    response = requests.get(url)
    result = response.status_code
    assert result != 403, f"{response.json().get('error').get('message')}"
