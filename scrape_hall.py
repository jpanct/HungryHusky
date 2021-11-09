import json


# Scrapes the page for the menu creates dict and outputs it as .json
def make_menu_json(driver, dining_hall, menu, file_name):

    # Clean up ugly html
    menu_list = []
    for item in range(0, len(menu)):
        menu_item = menu[item].text
        cleaned_item = menu_item.split("\n", 1)
        menu_list.append(cleaned_item[0])

    # Creates Dictionary
    food_dict = {dining_hall.text: menu_list}

    # Move to JSON file
    json_object = json.dumps(food_dict, indent=4)

    # Writing to food.json
    with open(f"{file_name}.json", "w") as outfile:
        outfile.write(json_object)
