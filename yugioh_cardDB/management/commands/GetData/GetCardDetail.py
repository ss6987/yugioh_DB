from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from .GetCardHTML import options


def getCardDetail(url, driver):
    flag = True
    count = 0
    while flag and count <= 10:
        try:
            driver.get("https://www.db.yugioh-card.com" + url + "&request_locale=ja")
            soup = BeautifulSoup(driver.page_source, "html.parser")
            flag = False
        except WebDriverException as e:
            count += 1
            sleep(10)
            driver = webdriver.Chrome(options=options)
    if flag:
        print("chromedriver_error")
        exit()
    return soup
