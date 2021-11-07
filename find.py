from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver')

def select_hall(driver, hall, meal):

    driver.get("https://nudining.com/public/menus")
    print("Searching...")
    time.sleep(10)

    # Assume the button has the ID "submit" :)
    driver.find_element_by_id("dropdown-grouped__BV_toggle_").click()
    driver.find_element_by_id(hall).click()
    time.sleep(3)
    driver.find_element_by_id("__BVID__922___BV_tab_button__").click()


iv = "building_5f4f8a925e42ad17557d1f95"
iv_lunch = "__BVID__922___BV_tab_button__"

    # THIS IS IV building_5f4f8a925e42ad17557d1f95
    # THIS IS IV LUNCH __BVID__922___BV_tab_button__
    # THIS IS STEAST building_612d4606e8297100cdc427ee

select_hall(driver, iv, iv_lunch )



