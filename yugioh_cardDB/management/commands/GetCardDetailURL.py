def getCardDetailURL(soup,bar):
    tr_list = soup.select("tr.row")
    for tr in tr_list:
        td = tr.find_all("td")[1]
        name = td.b.string.replace(",", "&44;")
        if not checkDataExist(name):
            url = td.select_one("input.link_value").attrs["value"]
            file = open("yugioh_cardDB/texts/search_result/search_result.txt", "a", encoding="utf-8")
            file.write(name + "," + url + "\n")
            file.close()
        bar.update(1)


def checkDataExist(name):
    file = open("yugioh_cardDB/texts/search_result/search_result.txt", "r", encoding="utf-8")
    texts = file.read()
    file.close()
    if "\n" + name + "," in texts:
        return True
    else:
        return False
