from .GetCardDetailURL import getCardDetailURL, checkDataExist
import os
from time import sleep
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

fields = {
    "ope": "1",
    "sess": "1",
    "keyword": "",
    "stype": "1",
    "link_m": "2",
    "othercon": "2",
    "rp": "100",
    "page": "1",
    "mode": "2",
    "request_locale": "ja",
}


def getCardHTML():
    fileExist()
    http = urllib3.PoolManager()
    page = 1
    max_page = 2
    bar = None
    while max_page / 100 + 1 >= page:

        request = http.request('GET', "https://www.db.yugioh-card.com/yugiohdb/card_search.action", fields=fields)
        soup = BeautifulSoup(request.data, "html.parser")
        last_tr = soup.select("tr.row")[-1]
        td = last_tr.find_all("td")[1]
        name = td.b.string.replace(",", "&44;")
        if page == 1:
            page_num_text = soup.select_one("div.page_num_title").find("strong").text
            max_page_text = page_num_text[page_num_text.index("検索結果 ") + 5:page_num_text.index("件中")]
            max_page = int(max_page_text.replace(",", ""))
            bar = tqdm(total=max_page,position=0)
        if not checkDataExist(name):
            getCardDetailURL(soup, bar)
        else:
            bar.update(100)
        page += 1
        fields["page"] = str(page)
        sleep(1)
    bar.close()


def fileExist():
    if not os.path.isdir("yugioh_cardDB/texts/search_result"):
        os.mkdir("yugioh_cardDB/texts/search_result")
    if not os.path.isfile("yugioh_cardDB/texts/search_result/search_result.txt"):
        file = open("yugioh_cardDB/texts/search_result/search_result.txt", "w", encoding="utf-8")
        file.close()
