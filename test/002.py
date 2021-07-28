from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_class_name("s_ipt").send_keys("火影忍者")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.quit()