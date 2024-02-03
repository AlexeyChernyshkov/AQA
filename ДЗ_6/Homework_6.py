import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://calcus.ru/kalkulyator-ipoteki")



try:
    cost = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "cost"))
    )
    driver.find_element(By.NAME, "cost").send_keys("5000000")
    driver.find_element(By.NAME, "start_sum").send_keys("1500000")
    driver.find_element(By.NAME, "period").send_keys("30")
    driver.find_element(By.NAME, "percent").send_keys("5")
    driver.find_element(By.CSS_SELECTOR, ".calc-submit").click()

    result_wait = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".result-placeholder-ad"))
    )

    driver.execute_script("scroll(0, 800)")
    time.sleep(2)
    driver.save_screenshot("result.png")


finally:
    driver.quit()