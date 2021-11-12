from selenium import webdriver
import time


STETSON_WEST_STATIONS = ["Salsa's & Dips", 'Soup & Co', 'Homestyle', '500 Degrees', 'Bok Choy Express',
                         "Bok Choy Express Fast lane"]


driver = webdriver.Chrome()


def select_hall_v2():
    # Search website, allow HTML to load asdf
    driver.get("https://nudining.com/public/menus")
    time.sleep(10)

    foodz = {}
    for station in STETSON_WEST_STATIONS:
        something_good_maybe = driver.find_elements_by_xpath(f"//caption[contains(text(), '{station}')]/../tbody/tr/td/div/span/strong")

        for value in something_good_maybe:
            print(f"{station} ---- {value.text} ------ Zbob")

    time.sleep(10)

select_hall_v2()

