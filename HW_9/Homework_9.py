#Пока что проект для диплома не выбрал.
# Тест-кейсы будут для страницы https://makarova1507ana.github.io/to_do_list_test_example/


#Ссылка на тесты: https://docs.google.com/spreadsheets/d/1qH_WlbfaGLw-Pnb8U2DdNistBdOlMPZ5RMr7R12uXzM/edit?usp=sharing

#На данный момент автотесты не написаны


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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



def find_and_click_input(browser):
    find_input = browser.find_element(By.ID, 'task-input')
    find_input.click()
    return find_input


def create_task_click(browser):
    find_create = browser.find_element(By.ID, 'add-task')
    find_create.click()


def delete_task_click(browser):
    find_delete = browser.find_element(By.ID, 'delete-task')
    find_delete.click()


def element_is_not_present(browser, locator):
    try:
        browser.find_element(By.XPATH, f'{locator}')
    except NoSuchElementException:
        return False
    return True


def test_1_input_and_refresh(browser):
    input1 = find_and_click_input(browser)
    input1.send_keys('Task 1')
    browser.refresh()
    find_input = browser.find_element(By.ID, 'task-input').get_attribute("value")
    assert find_input == '', "Field is not empty"


def test_2_create_one_task(browser):
    input2 = find_and_click_input(browser)
    input2.send_keys('Task 2')
    create_task_click(browser)
    task_check = browser.find_element(By.XPATH, '/html/body/ul/li[text() = "Task 2"]')
    assert task_check.is_displayed(), "Task 2 not found"


def test_3_refresh_with_one_task(browser):
    input3 = find_and_click_input(browser)
    input3.send_keys('Task 3')
    create_task_click(browser)
    browser.refresh()
    task_check = browser.find_element(By.XPATH, '/html/body/ul/li[text() = "Task 3"]')
    assert task_check.is_displayed(), "Task 3 not found"


def test_4_check_one_task(browser):
    input4 = find_and_click_input(browser)
    input4.send_keys('Task 4')
    create_task_click(browser)
    check_box = browser.find_element(By.CSS_SELECTOR, 'body > ul > li > input[type=checkbox]')
    check_box.click()
    assert check_box.is_selected(), 'Checkbox is not selected'


def test_5_delete_task_without_check(browser):
    input5 = find_and_click_input(browser)
    input5.send_keys('Task 5')
    create_task_click(browser)
    delete_task_click(browser)
    task_check = browser.find_element(By.XPATH, '/html/body/ul/li[text() = "Task 5"]')
    assert task_check.is_displayed(), "Task 5 not found"


def test_6_delete_task_with_check(browser):
    input6 = find_and_click_input(browser)
    input6.send_keys('Task 6')
    create_task_click(browser)
    check_box = browser.find_element(By.CSS_SELECTOR, 'body > ul > li > input[type=checkbox]')
    check_box.click()
    delete_task_click(browser)
    locator = '/html/body/ul/li[text() = "Task 6"]'
    assert not element_is_not_present(browser, locator), "Element 'Task 6' found"


def test_7_create_two_task(browser):
    input7_1 = find_and_click_input(browser)
    input7_1.send_keys('Task 7_1')
    create_task_click(browser)
    input7_2 = find_and_click_input(browser)
    input7_2.send_keys('Task 7_2')
    create_task_click(browser)
    task7_1_check = browser.find_element(By.XPATH, '/html/body/ul/li[text() = "Task 7_1"]')
    assert task7_1_check.is_displayed(), "Task 7_1 not found"
    task7_2_check = browser.find_element(By.XPATH, '/html/body/ul/li[text() = "Task 7_2"]')
    assert task7_2_check.is_displayed(), "Task 7_2 not found"


