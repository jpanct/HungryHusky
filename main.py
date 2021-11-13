from find import load_site
from find import select_hall
from find import select_meal
from selenium import webdriver
from hall_dict import create_hall_dict

STETSON_WEST_STATIONS = ["Salsas & Dips", "Soup & Co", "Homestyle", "500 Degrees", "Bok Choy Express",
                         "Bok Choy Express Fast lane"]
#Salsa is not working because in the x path we are looking for 'Salsa's & Dip' and since it uses one apostrophe the string get cut off
STETSON_EAST_STATIONS = ["Trattoria", "Pizza", "Soup", "Menutainment", "Char Broil"]

IV_STATIONS = ["Halal", "Zone 8", "Pizza", "Tandori", "Bakery-Dessert", "Plant-Based",
                "Sushi", "Soup", "Pasta", "Comfort", "Grill", "Burger Toppings", "Salad",
                "Everday"]

#hall_id_dict = \
#{'IV': 'building_5f4f8a925e42ad17557d1f95', 
#'Steast': 'building_612d4606e8297100cdc427ee', 
#'Stwest': 'building_612d4606e8297100cdc427ee'}

hall_id_dict = {'IV': 'International Village Dining',
                'Steast': 'Levine Marketplace',
                'Stwest': 'Food Hall at Stetson West'}

driver_directory = '/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver'
# place driver_directory in parenthesis
chrome_driver = webdriver.Chrome(driver_directory)


# scrape_the_hall : Driver, String, String, String, [List-of Stations] -> json
# select driver type, hall id, meal id, and output json file name, outputs a json file
def scrape_current_hall(driver, hall, file_name, stations):
    # Create a dictionary of food, then make it into a json file
    create_hall_dict (stations, file_name, driver)

#scrape_in_hall: Driver String String [List-of Stations]
#scrapes every meal in a given hall and their respective stations and saves them in a json file with file_name
def scrape_in_hall(driver, hall, file_name, stations):
    #select_meal(driver, 'Breakfast')
    scrape_current_hall(chrome_driver, hall_id_dict[hall] ,(file_name + "_breakfast") , stations)

    select_meal(driver, 'Lunch')
    scrape_current_hall(chrome_driver, hall_id_dict[hall] , (file_name + "_lunch"), stations)

    select_meal(driver, 'Dinner')
    scrape_current_hall(chrome_driver, hall_id_dict[hall] , (file_name + "_dinner"), stations)

# Driver -> Json
# selects Stwest and scrapes whats on its site (since theres only dinner)
def scrape_stwest (driver):
    #select_hall(driver, hall_id_dict['Stwest'])
    scrape_current_hall(driver, 'Stwest', 'stwest_dinner', STETSON_WEST_STATIONS)

# scrape_all_halls : Driver -> Jsons
# produces all the json files for each hall and each of their meals
def scrape_all_halls(driver):
    load_site(driver)
    
    scrape_stwest(driver)

    select_hall(driver, hall_id_dict['Steast'])
    scrape_in_hall(driver, 'Steast', 'steast', STETSON_EAST_STATIONS)

    select_hall(driver, hall_id_dict['IV'])
    scrape_in_hall(driver, 'IV', 'iv', IV_STATIONS)

    print('Finished')
    driver.close()

scrape_all_halls(chrome_driver)

# for reference IV lunch was __BVID__933___BV_tab_button__ on 11/8/21
# on 11/9/21 it was __BVID__950___BV_tab_button__
