from selenium import webdriver
from bs4 import BeautifulSoup


def getCardDetail(url,driver):

    driver.get("https://www.db.yugioh-card.com" + url + "&request_locale=ja")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup
