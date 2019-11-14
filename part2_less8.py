from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_id('book')      
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    cost = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    x = browser.find_element_by_id('input_value')
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = x.text
    x = calc(x)
    input_window = browser.find_element_by_id('answer')
    input_window.send_keys(x)
    btn = browser.find_element_by_id("solve")
    btn.click()
    time.sleep(15)


finally:
    browser.quit()