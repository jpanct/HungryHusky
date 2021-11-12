from find import select_hall
from selenium import webdriver
import time
import json


STETSON_WEST_STATIONS = ["Salsas & Dips", "Soup & Co", "Homestyle", "500 Degrees", "Bok Choy Express",
                         "Bok Choy Express Fast lane"]
#Salsa is not working because in the x path we are looking for 'Salsa's & Dip' and since it uses one apostrophe the string get cut off
STETSON_EAST_STATIONS = ["Trattoria", "Pizza", "Soup", "Menutainment", "Char Broil"]
driver_directory = '/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver'
driver = webdriver.Chrome(driver_directory)

# select-stations : [List-of Stations] -> [List-of Items]
def select_hall_v2(all_stations, hall, meal):
    # Search website, allow HTML to load asdf
    select_hall(driver, hall, meal)


    for station in all_stations:
        station_menu = driver.find_elements_by_xpath(f"//caption[contains(text(), '{station}')]/../tbody/tr/td/div/span/strong")
        print(f"{station}")
        for value in station_menu:
            print(f"---- {value.text} -----")

    time.sleep(10)

    select_hall_v2(STETSON_EAST_STATIONS, "building_612d4606e8297100cdc427ee", "Dinner")