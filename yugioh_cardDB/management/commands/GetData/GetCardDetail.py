from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup


def getCardDetail(url, driver):
    flag = True
    count = 0
    while flag and count <= 10:
        try:
            driver.get("https://www.db.yugioh-card.com" + url + "&request_locale=ja")
            flag = False
        except WebDriverException as e:
            count += 1
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup
