import sys
sys.path.append('..')
from urlsConfig import urls
from utils import scrollToBottom
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

# Path to chromedriver
PATH = "C:\Windows\chromedriver.exe"

# Which browser to use (Edge, Chrome, Firefox,etc...)
driver = webdriver.Chrome(PATH)


itemsScraped = {}


for item in urls:
    # This line opens the browser and goes to the url
    driver.get(item["url"])
    # This line wait 5 sec for the page to load
    time.sleep(5)
    scrollToBottom(driver)

    # Going through the itemsToScrape dictionary key = item number, value = data-product-code
    for key, value in item["itemsToScrape"].items():
        try:
            # find the element by the data-product-code
            marketItem = driver.find_element(
                By.CSS_SELECTOR, f"li[data-product-code='{value}']")

            # This gets the price of the item
            marketItemPrice = marketItem.get_attribute("data-product-price")
            print(marketItemPrice, "price for ", key)
            itemsScraped[key] = marketItemPrice

        except:
            print(key, "is not available")


print(itemsScraped)

time.sleep(20)
