from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_partial_link_text("hao").click()
time.sleep(6)
browser.quit()