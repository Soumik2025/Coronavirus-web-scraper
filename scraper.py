from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Data from worldometer

PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "https://www.worldometers.info/coronavirus/"

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=options)


def scrape_world_data():
    driver.get(URL)
    num = [0, 1, 2]
    list_cases = []
    assert "Coronavirus" in driver.title
    container = driver.find_elements_by_id("maincounter-wrap")
    for i in num:
        text = container[i].find_element_by_tag_name("h1").text
        number_container = container[i].find_element_by_class_name(
            "maincounter-number")
        number = number_container.find_element_by_tag_name("span").text
        list_cases.append(number)
    return list_cases



def scrape_country_data(country):
    driver.get(f"{URL}/country/{country}/")
    assert "Coronavirus" in driver.title
    num = [0, 1, 2]
    list_cases = []
    container = driver.find_elements_by_id("maincounter-wrap")
    for i in num:
        text = container[i].find_element_by_tag_name("h1").text
        number_container = container[i].find_element_by_class_name(
            "maincounter-number")
        number = number_container.find_element_by_tag_name("span").text
        list_cases.append(number)
    return list_cases

country_name = "us" # the country data you want

country_info = scrape_country_data(country_name) # country info
world_info = scrape_world_data() # world info

print(country_info)
print(world_info)

driver.quit()
