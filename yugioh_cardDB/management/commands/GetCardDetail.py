from time import sleep
import os
import urllib3
from tqdm import tqdm
from bs4 import BeautifulSoup


def getCardDetail():
    file = open("yugioh_cardDB/texts/search_result/search_result.txt", "r", encoding="utf-8")
    max_line = len(file.readlines())
    file.seek(0)
    bar = tqdm(total=max_line,position=0)
    line = file.readline()
    if not os.path.isdir("yugioh_cardDB/texts/card_detail_html"):
        os.mkdir("yugioh_cardDB/texts/card_detail_html")
    while line:
        name, url = line.strip().split(",")
        cid = url[url.index("cid=") + 4:]
        if not os.path.isfile("yugioh_cardDB/texts/card_detail_html/" + cid + ".txt"):
            http = urllib3.PoolManager()
            request = http.request('GET', "https://www.db.yugioh-card.com" + url + "&request_locale=ja")
            soup = BeautifulSoup(request.data,"html.parser")
            html_data = soup.find("article")
            html_file = open("yugioh_cardDB/texts/card_detail_html/" + cid + ".txt", "w", encoding="utf-8")
            html_file.write(str(html_data))
            html_file.close()
            sleep(1)
        line = file.readline()
        bar.update(1)
    bar.close()
    file.close()
