from time import sleep
import os
import urllib


def getCardDetail():
    file = open("yugioh_cardDB/texts/search_result/search_result.txt", "r", encoding="utf-8")
    line = file.readline()
    if not os.path.isdir("yugioh_cardDB/texts/card_detail_html"):
        os.mkdir("yugioh_cardDB/texts/card_detail_html")
    while line:
        name, url = line.strip().split(",")
        name = name.replace("&44;", ",")
        print(name)
        cid = url[url.index("cid=") + 4:]
        request = urllib.request.Request("https://www.db.yugioh-card.com" + url + "&request_locale=ja")
        html = urllib.request.urlopen(request).read().decode("utf-8")
        html_file = open("yugioh_cardDB/texts/card_detail_html/" + cid + ".txt", "w", encoding="utf-8")
        html_file.write(html)
        html_file.close()
        sleep(2)
        line = file.readline()
    file.close()
