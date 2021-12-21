from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#from crawlers.utils import scrollToBottom
from urlsConfig import urls


# Path to chromedriver
PATH = "C:\Windows\chromedriver.exe"

# Which browser to use (Edge, Chrome, Firefox,etc...)
driver = webdriver.Chrome(PATH)

def scrollToBottom(driver):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(4)
        print("SCROLLING TO BOTTOM")

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

itemsScraped = {}


for item in urls:
    # This line opens the browser and goes to the url
    driver.get(item["url"])
    # This line wait 5 sec for the page to load
    time.sleep(6)
    scrollToBottom(driver)

    # Going through the itemsToScrape dictionary key = item number, value = data-product-code
    for key, value in item["itemsToScrape"].items():
        try:
            # find the element by the data-product-code
            h3MarketItem = driver.find_element(
                By.XPATH, f"// h3[contains(text(), ' {value} ')]")

            itemGrandParent = h3MarketItem.find_element(
                By.XPATH, "..").find_element(By.XPATH, "..")

            itemPrice = itemGrandParent.find_element(
                By.CSS_SELECTOR, "div[class='product_cube-price']").get_attribute("innerText")

            print(itemPrice.split("₪")[1])

        except Exception as e:
            print(key, "is not available")


# print(itemsScraped)

time.sleep(20)
