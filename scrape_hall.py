from selenium import webdriver
import time
import json

driver = webdriver.Chrome()
driver.get("https://nudining.com/public/menus")
print("Searching...")

time.sleep(10)
print("found:")

# Determine Dining Hall
dining_hall = driver.find_element_by_class_name('location-name')
print(dining_hall.text)

# Determine Menu
menu = driver.find_elements_by_css_selector('[data-label="Menu item"]')

# get rid of the extra info
menu_list = []
for item in range(0, len(menu)):
    menu_item = menu[item].text
    cleaned_item = menu_item.split("\n", 1)
    menu_list.append(cleaned_item[0])

# menu_list = [menu[item].text for item in range(0, len(menu))]

# Creates Dictionary
food_dict = {dining_hall.text: menu_list}
print(food_dict)
driver.close()

# Move to JSON file

# Serializing json
json_object = json.dumps(food_dict, indent=4)

# Writing to food.json
with open("food.json", "w") as outfile:
    outfile.write(json_object)