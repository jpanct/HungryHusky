from find import select_hall
from selenium import webdriver
import time
import json
from pathlib import Path

base = Path('./dining_jsons')


# [List-of Stations] String String String -> Dictionary
# creates a dictionary with keys equal to the hall name with info representing the available menu items at the section
# and writes it to a json file of the given name
def create_hall_dict(all_stations, file_name, driver):
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
    jsonpath = base / (file_name + ".json")
    jsonpath.write_text(json.dumps(data, indent=4))


#create_hall_dict(STETSON_EAST_STATIONS, "building_612d4606e8297100cdc427ee", "Dinner", "steast_dinner")