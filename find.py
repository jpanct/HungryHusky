from selenium import webdriver
import time

driver_directory = '/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver'
# place driver_directory in parenthesis (also no idea why this opens a blank page :/
driver = webdriver.Chrome()
driver.close()


# select_hall : Driver String String -> Website
# opens up desired hall and meal
def select_hall(web_driver, hall, meal):
    # Search website, allow HTML to load
    web_driver.get("https://nudining.com/public/menus")
    time.sleep(10)

    # click to desired section. Sleep needed b/c site bad & slow load
    web_driver.find_element_by_id("dropdown-grouped__BV_toggle_").click()
    web_driver.find_element_by_id(hall).click()
    time.sleep(5)

    web_driver.find_elements_by_xpath(f"//a[contains(text(), '{meal}')]")[0].click()
    time.sleep(10)



stwest_hours = {"monday": "7:00am - 11:00pm", "tuesday": "7:00am - 11:00pm", "wednesday": "7:00am - 11:00pm",
                "thursday": "7:00am - 11:00pm", "friday": "7:00am - 10:00pm", "saturday": "8:00am - 10:00pm",
                "sunday": "8:00am - 10:00pm"}

hall_id_dict = \
    {'IV': 'building_5f4f8a925e42ad17557d1f95', 'Steast': 'building_612d4606e8297100cdc427ee', 'Stwest': 'insert here'}

