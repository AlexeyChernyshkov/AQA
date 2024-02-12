#Пока что проект для диплома не выбрал.
# Тест-кейсы будут для страницы https://makarova1507ana.github.io/to_do_list_test_example/


#Ссылка на тесты: https://docs.google.com/spreadsheets/d/1qH_WlbfaGLw-Pnb8U2DdNistBdOlMPZ5RMr7R12uXzM/edit?usp=sharing

#На данный момент автотесты не написаны


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest



@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

link = 'https://makarova1507ana.github.io/to_do_list_test_example/'


@pytest.fixture
def find_and_click_input(browser):
    find_input = browser.find_element(By.ID, 'task-input')
    find_input.click()
    return find_input

@pytest.fixture
def create_click(browser):
    find_create = browser.find_element(By.ID, 'add-task')
    find_create.click()

def test_2_create_one_task(browser):
    input1 = find_and_click_input(browser)
    input1.send_keys('Task 1')
    create_click(browser)
    time.sleep(5)




