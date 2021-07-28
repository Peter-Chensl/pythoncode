from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("吴亦凡")
driver.find_element_by_id("su").submit()
time.sleep(6)
driver.quit()