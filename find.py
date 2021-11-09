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
    print('waiting...')

    # click to desired section. Sleep needed b/c site bad & slow load
    web_driver.find_element_by_id("dropdown-grouped__BV_toggle_").click()
    web_driver.find_element_by_id(hall).click()
    time.sleep(5)
    print('waiting...')
    web_driver.find_element_by_id(meal).click()
    time.sleep(10)
    print('waiting...')


hall_id_dict = \
    {'IV': 'building_5f4f8a925e42ad17557d1f95', 'Steast': 'building_612d4606e8297100cdc427ee', 'Stwest': 'insert here'}
meal_id_dict = \
    {'IV Breakfast': 'insert id', 'IV Lunch': '__BVID__933___BV_tab_button__', 'IV Dinner': 'insert id',
     'Steast Breakfast': 'insert id', 'Steast Lunch': 'insert id', 'Steast Dinner': 'insert id',
     'Stwest Breakfast': 'insert id', 'Stwest Lunch': 'insert id', 'Stwest Dinner': 'insert id'}
