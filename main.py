from selenium import webdriver
import time
import threading
from selenium.webdriver.common.by import By

# Path to chromedriver
PATH = "C:\Windows\chromedriver.exe"

# Which browser to use (Edge, Chrome, Firefox,etc...)


def firstOne():
    print("FIRST STARTED")
    driver = webdriver.Chrome(PATH)
    driver.get("https://friends.walla.co.il/login")


def second():
    print("SECOND STARTED")
    driver1 = webdriver.Chrome(PATH)
    driver1.get("https://www.youtube.com/")


def start():
    thread1 = threading.Thread(name='FirstOne', target=firstOne)
    thread2 = threading.Thread(name='secondOne', target=second)
    thread1.start()
    thread2.start()


start()
