from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://nudining.com/public/menus")
time.sleep(10)
elem = driver.find_elements_by_css_selector('[data-label="Menu item"]')
print(elem)

# web-driver.close()