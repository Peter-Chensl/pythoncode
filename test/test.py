from selenium import  webdriver

driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)
driver.find_element_by_id("kw").send_keys("迪丽热巴")
driver.find_element_by_id("su").click()

driver.quit()