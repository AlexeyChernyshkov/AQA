# Чек-листы:
# 1	    Валидный токен	    Прошлая дата
# 2	    Валидный токен	    Сегодняшняя дата
# 3	    Валидный токен	    Будущая дата
# 4	    Валидный токен	    Невалидная дата
# 5	    Валидный токен	    Пробел вместо даты
# 6	    Валидный токен	    Пустая дата
# 7	    Невалидный токен	Прошлая дата
# 8	    Невалидный токен	Сегодняшняя дата
# 9	    Невалидный токен	Будущая дата
# 10    Невалидный токен	Невалидная дата
# 11	Невалидный токен	Пробел вместо даты
# 12	Невалидный токен	Пустая дата
# 13	Пустой токен	    Прошлая дата
# 14	Пустой токен	    Сегодняшняя дата
# 15	Пустой токен	    Будущая дата
# 16	Пустой токен        Невалидная дата
# 17	Пустой токен	    Пробел вместо даты
# 18	Пустой токен	    Пустая дата



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
