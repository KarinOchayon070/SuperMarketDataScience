from selenium import webdriver
import time
import utils
from selenium.webdriver.common.by import By

#from utils import scrollToBottom
from tivTaamConfig import urls

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
    utils.scrollToBottom(driver)

    # Going through the itemsToScrape dictionary key = item number, value = data-product-code
    for key, value in item["itemsToScrape"].items():
        try:
            marketItem = driver.find_element(
                By.CSS_SELECTOR,  f"meta[content='{value}']")

            itemParent = marketItem.find_element(
                By.XPATH, "..")

            price = itemParent.find_element(
                By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute("content")

            print(price, "price")

        except:
            print(key, "is not available")


print(itemsScraped)

driver.close()
