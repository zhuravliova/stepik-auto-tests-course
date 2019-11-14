from selenium import webdriver
import math
import time



try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	btn = browser.find_element_by_class_name("trollface")
	btn.click()
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	x = browser.find_element_by_id('input_value')
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x = x.text
	x = calc(x)
	input_window = browser.find_element_by_id('answer')
	input_window.send_keys(x)
	btn = browser.find_element_by_class_name("btn-primary")
	btn.click()
	time.sleep(15)


finally:
	browser.quit()