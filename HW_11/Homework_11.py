# В качестве примера использования параметризации привел свою работу из домашки 7
# По той простой причине, что еще определяюсь с выбором проекта.
# Если такой вариант домашней работы не подойдет, прошу отправить ДЗ в журнале на доработку. Переделаю.


# Чек-листы:
# 1	    Валидный токен	    Прошлая дата. OP = passed
# 2	    Валидный токен	    Сегодняшняя дата. OP = passed
# 3	    Валидный токен	    Будущая дата. OP = failed(400)
# 4	    Валидный токен	    Невалидная дата. OP = failed(400)
# 5	    Валидный токен	    Пробел вместо даты. OP = failed(400)
# 6	    Валидный токен	    Пустая дата. OP = passed

# 7	    Валидный токен	    дата формата DD.MM.YYYY. OP = failed(400)
# 8	    Валидный токен	    дата формата DD-MM-YYYY. OP = failed(400)
# 9	    Валидный токен	    дата формата DD/MM/YYYY. OP = failed(400)
# 10	Валидный токен	    дата формата YY-MM-DD. OP = failed(400)
# 11	Валидный токен	    дата формата YYYY.MM.DD. OP = failed(400)
# 12	Валидный токен	    дата формата YYYY/MM/DD. OP = failed(400)
# 13	Валидный токен	    текстовая дата. OP = failed(400)


# 14	Невалидный токен	Прошлая дата. OP = failed(403)
# 15	Невалидный токен	Сегодняшняя дата. OP = failed(403)
# 16	Невалидный токен	Будущая дата. OP = failed(403)
# 17    Невалидный токен	Невалидная дата. OP = failed(403)
# 18	Невалидный токен	Пробел вместо даты. OP = failed(403)
# 19	Невалидный токен	Пустая дата. OP = failed(403)

# 20	Пустой токен	    Прошлая дата. OP = failed(403)
# 21	Пустой токен	    Сегодняшняя дата. OP = failed(403)
# 22	Пустой токен	    Будущая дата. OP = failed(403)
# 23	Пустой токен        Невалидная дата. OP = failed(403)
# 24	Пустой токен	    Пробел вместо даты. OP = failed(403)
# 25	Пустой токен	    Пустая дата. OP = failed(403)



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
