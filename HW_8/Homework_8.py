#Тест кейсы:
# 1. Отображение кнопки с выбором пользователя. ОР - кнопка отображается
# 2. Отображение кнопки без выбора пользователя. ОР - кнопка не отображается


#При успешном выполнении сохраняются скриншоты в папку.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_1_check_button_with_users_choice(browser):
    dropdown_menu = Select(browser.find_element(By.ID, "userSelect"))
    dropdown_menu.select_by_visible_text("Harry Potter")
    selected_customer = dropdown_menu.first_selected_option.text
    assert selected_customer == "Harry Potter"
    button = browser.find_element(By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > form > button")
    assert button.is_displayed(), "Кнопка не отображается"
    browser.save_screenshot("test_1_button_is_displayed.png")

def test_2_check_button_without_users_choice(browser):
    dropdown_menu = Select(browser.find_element(By.ID, "userSelect"))
    dropdown_menu.select_by_visible_text("---Your Name---")
    selected_customer = dropdown_menu.first_selected_option.text
    assert selected_customer == "---Your Name---"
    button = browser.find_element(By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > form > button")
    assert not button.is_displayed(), "Кнопка отображается"
    browser.save_screenshot("test_2_button_is_not_displayed.png")
