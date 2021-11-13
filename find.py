from selenium import webdriver
import time

driver_directory = '/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver'
# place driver_directory in parenthesis (also no idea why this opens a blank page :/
driver = webdriver.Chrome(driver_directory)

def load_site(web_driver):
    # Search website, allow HTML to load
    web_driver.get("https://nudining.com/public/menus")
    time.sleep(5)

# select_hall : Driver String String -> Website
# opens up desired hall and meal
def select_hall(web_driver, hall):
    # click to desired section. Sleep needed b/c site bad & slow load
    web_driver.find_element_by_id("dropdown-grouped__BV_toggle_").click()
    web_driver.find_elements_by_xpath(f"//button[contains(text(), '{hall}')]")[0].click()
    time.sleep(5)

#select_meal : Driver String
#clicks on the tab of the given meal (Breakfast, Lunch, or Dinner)
def select_meal(web_driver, meal):
    meal_button = web_driver.find_elements_by_xpath(f"//a[contains(text(), '{meal}')]")
    if meal_button:
        meal_button[0].click()
        time.sleep(10)



