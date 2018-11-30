from .SettingDriver import settingDriver,executeSearch
from .GetCardDetailURL import getCardDetailURL, checkDataExist
import os
from time import sleep


def getCardHTML():
    driver = settingDriver()
    executeSearch(driver)
    fileExist()
    current_url = driver.current_url
    while True:
        last_tr = driver.find_elements_by_css_selector("tr.row")[-1]
        td = last_tr.find_elements_by_tag_name("td")[1]
        name = td.text.replace(",", "&44;")
        if not checkDataExist(name):
            getCardDetailURL(driver)
        page_num = driver.find_element_by_css_selector("div.page_num")
        page_num.find_elements_by_tag_name("a")[-1].click()
        if current_url == driver.current_url:
            break
        current_url = driver.current_url
        sleep(2)
    driver.close()


def fileExist():
    if not os.path.isdir("yugioh_cardDB/texts/search_result"):
        os.mkdir("yugioh_cardDB/texts/search_result")
    if not os.path.isfile("yugioh_cardDB/texts/search_result/search_result.txt"):
        file = open("yugioh_cardDB/texts/search_result/search_result.txt", "w", encoding="utf-8")
        file.close()




