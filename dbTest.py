from selenium import webdriver
import time

from selenium.webdriver.common.by import By
# אלוהים שיעזור לי 

PATH = "C:\Windows\chromedriver.exe"
driver = webdriver.Chrome(PATH)
urls = [
    {
        "url": 'https://www.shufersal.co.il/online/he/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/%D7%A1%D7%95%D7%A4%D7%A8%D7%9E%D7%A8%D7%A7%D7%98/%D7%A4%D7%99%D7%A8%D7%95%D7%AA-%D7%95%D7%99%D7%A8%D7%A7%D7%95%D7%AA/%D7%A4%D7%99%D7%A8%D7%95%D7%AA/c/A0405',
        "category": "vegsAndFruits",
        "itemsToScrape": {
            "0": "P_967684",  # banana
            "1": "P_964560",  # clementine
            "2": "P_7296073440758",  # orange
            "3": "P_963136",  # apple
            "4": "P_964492",  # lemon
            "5": "P_965055",  # melon
            "6": "P_998251",  # strawberry
            "7": "P_964980",  # avocado
            "8": "P_964423",  # pomelo
            "9": "P_972800",  # red_grapefruit
            "10": "P_966656",  # kiwi
            "11": "P_966564",  # pomegranate
            "12": "P_7296073292012",  # pineapple
        },
    },
    {
        "url": "https://www.shufersal.co.il/online/he/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/%D7%A1%D7%95%D7%A4%D7%A8%D7%9E%D7%A8%D7%A7%D7%98/%D7%97%D7%9C%D7%91-%D7%95%D7%91%D7%99%D7%A6%D7%99%D7%9D/c/A01",
        "category": "vegsAndFruits",
        "itemsToScrape": {
            "20": "P_42442",  # milk 3%
        },
    },
]


def scrollToBottom():
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


for item in urls:
    driver.get(item["url"])
    time.sleep(5)
    scrollToBottom()

    for key, value in item["itemsToScrape"].items():
        try:
            marketItem = driver.find_element(
                By.CSS_SELECTOR, f"li[data-product-code='{value}']")

            marketItemPrice = marketItem.get_attribute("data-product-price")
            print(marketItemPrice, "price for ", key)

        except:
            print(key, "is not available")


time.sleep(20)
