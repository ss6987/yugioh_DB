def getCardDetailURL(driver):
    tr_list = driver.find_elements_by_css_selector("tr.row")
    for tr in tr_list:
        td = tr.find_elements_by_tag_name("td")[1]
        name = td.text.replace(",", "&44;")
        if not checkDataExist(name):
            url = td.find_element_by_tag_name("input").get_attribute("value")
            file = open("yugioh_cardDB/texts/search_result/search_result.txt", "a", encoding="utf-8")
            file.write(name + "," + url + "\n")
            file.close()
            print(name)


def checkDataExist(name):
    file = open("yugioh_cardDB/texts/search_result/search_result.txt", "r", encoding="utf-8")
    texts = file.read()
    file.close()
    if "\n" + name + "," in texts:
        return True
    else:
        return False
