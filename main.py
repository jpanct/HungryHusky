from find import select_hall
from scrape_hall import make_menu_json
from selenium import webdriver

driver_directory = '/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver'
# place driver_directory in parenthesis
chrome_driver = webdriver.Chrome()


# scrape_the_hall : Driver, String, String, String -> json
# select driver type, hall id, meal id, and output json file name, outputs a json file
def scrape_the_hall(driver, hall, meal, file_name):

    # open up driver to desired hall and meal
    print("selecting hall bitch")
    select_hall(driver, hall, meal)

    # Determine Dining Hall
    dining_hall = driver.find_element_by_class_name('location-name')
    print(dining_hall)
    print(dining_hall)
    print(dining_hall.text)

    # Determine menu and apply to function
    menu = driver.find_elements_by_css_selector('[data-label="Menu item"]')

    # Create a dictionary of food, then make it into a json file
    make_menu_json(driver, dining_hall, menu, file_name)

    driver.close()


scrape_the_hall(chrome_driver, 'building_5f4f8a925e42ad17557d1f95', '__BVID__950___BV_tab_button__', 'iv_lunch')

# for reference IV lunch was __BVID__933___BV_tab_button__ on 11/8/21
# on 11/9/21 it was __BVID__950___BV_tab_button__
