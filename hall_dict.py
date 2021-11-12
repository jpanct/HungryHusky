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



# [List-of Stations] String String String -> Dictionary
# creates a dictionary with keys equal to the hall name with info representing the available menu items at the section
# and writes it to a json file of the given name
def create_hall_dict(all_stations, file_name):
    Foodz = {}
    for station in all_stations:
        station_menu = driver.find_elements_by_xpath(f"//caption[contains(text(), '{station}')]/../tbody/tr/td/div/span/strong")
        station_menu_txt = []
        for item in range(0, len(station_menu)):
            menu_item = station_menu[item].text
            station_menu_txt.append(menu_item)
        Foodz[station] = station_menu_txt
    write_json(Foodz, file_name)
    

def write_json (data, file_name):
    # Move to JSON file
    json_object = json.dumps(data, indent=4)

    # Writing to food.json
    with open(f"{file_name}.json", "w") as outfile:
        outfile.write(json_object)


create_hall_dict(STETSON_EAST_STATIONS, "building_612d4606e8297100cdc427ee", "Dinner", "steast_dinner")