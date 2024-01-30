from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")

try:
    # По невнимательности сделал действия не со строкой поиска, а с shell на сайте.
    # Не ругайтесь :)

    # Страница долго загружается почему-то, поэтому нужно подождать секунд 10-20
    # print'ы ниже просто для проверки выполнения кода. Их можно раскомментить

    # Ждем и нажимаем на кнопку открытия shell
    shell_start = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "start-shell"))
    )
    shell_open = driver.find_element(By.ID, "start-shell")
    shell_open.click()

    # переходим к фрейму, в котором находится shell
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#dive-into-python > iframe"))
    # print("Frame 1")
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#id_console"))
    # print("Frame 2")
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#terminal > iframe"))
    # print("Frame 3")

    # Ждем, пока появится строка ввода
    shell_input_string = WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '//*[@id="hterm:row-nodes"]/x-row[3]'), ">>>")
            )
    # print("Find string with '>>>'")

    # Находим строку ввода
    input1 = driver.find_element(By.XPATH, '//*[@id="hterm:row-nodes"]/x-row[3]')
    # print("Find string to write")

    # Вводим код и жмем Enter
    input1.send_keys("""
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)""")
    input1.send_keys(Keys.ENTER)

    # тут sleep только для того, чтобы был виден результат выполнения команды в shell
    time.sleep(4)

    # Скриним пруфы выполнения :)
    driver.save_screenshot("result.png")
finally:
    driver.quit()


