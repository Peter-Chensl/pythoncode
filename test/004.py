from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("火影")
driver.find_element_by_id("su").click()

time.sleep(6)
driver.quit()