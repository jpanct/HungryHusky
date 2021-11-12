from find import select_hall
from selenium import webdriver
from hall_dict import create_hall_dict

STETSON_WEST_STATIONS = ["Salsas & Dips", "Soup & Co", "Homestyle", "500 Degrees", "Bok Choy Express",
                         "Bok Choy Express Fast lane"]
#Salsa is not working because in the x path we are looking for 'Salsa's & Dip' and since it uses one apostrophe the string get cut off
STETSON_EAST_STATIONS = ["Trattoria", "Pizza", "Soup", "Menutainment", "Char Broil"]
IV_STATIONS = ["Halal", "Zone 8", "Pizza", "Tandori", "Bakery-Dessert", "Plant-Based",
                "Sushi", "Soup", "Pasta", "Comfort", "Grill", "Burger Toppings", "Salad",
                "Everday"]

driver_directory = '/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver'
# place driver_directory in parenthesis
chrome_driver = webdriver.Chrome(driver_directory)


# scrape_the_hall : Driver, String, String, String, [List-of Stations] -> json
# select driver type, hall id, meal id, and output json file name, outputs a json file
def scrape_the_hall(driver, hall, meal, file_name, stations):

    # open up driver to desired hall and meal
    select_hall(driver, hall, meal)

    # Determine Dining Hall
    dining_hall = driver.find_element_by_class_name('location-name')

    # Determine menu and apply to function
    #menu = driver.find_elements_by_css_selector('[data-label="Menu item"]')

    # Create a dictionary of food, then make it into a json file
    create_hall_dict (stations, file_name)

    driver.close()


scrape_the_hall(chrome_driver, 'building_5f4f8a925e42ad17557d1f95', 'Dinner', 'iv_dinner', IV_STATIONS)

# for reference IV lunch was __BVID__933___BV_tab_button__ on 11/8/21
# on 11/9/21 it was __BVID__950___BV_tab_button__
