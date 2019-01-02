from ...ReplaceName import replaceName
import re
import time
import urllib
import urllib3
from bs4 import BeautifulSoup
from ..GetRarity import getRarity
from ..RegistrationData import registrationShopURL, registrationPrice

pattern = "(（.*）|【.*】|\(.*\))"
http = urllib3.PoolManager()


def searchSurugaya(card, shop):
    url_name = urllib.parse.quote_plus("遊戯王　" + card.card_name, encoding="utf-8")
    url_name = "/search?category=9905&search_word=" + url_name
    flag = True
    while flag:
        request = http.request('GET',
                               shop.search_url + url_name)
        start = time.time()
        soup = BeautifulSoup(request.data, "html.parser")
        readSurugaya(card, shop, soup)
        if len(soup.find_all("li", class_="next")) == 0:
            flag = False
        else:
            url_name = soup.find("li", class_="next").find("a")["href"]
        sleep_time = 2 - (time.time() - start)
        if sleep_time > 0:
            time.sleep(sleep_time)


def readSurugaya(card, shop, soup):
    for div in soup.find_all("div", class_="item"):
        condition = div.find("p", class_="condition").text
        title = div.find("p", class_="title").text
        if "中古" in condition and "英語" not in condition and "版" not in condition:
            if "/" in condition:
                try:
                    card_name = title[title.index("：") + 2:]
                except ValueError:
                    continue
                card_name = re.sub(pattern, "", card_name)
                card_name = replaceName(card_name)
                if card.search_name == card_name or card.search_phonetic == card_name:
                    card_url = div.find("a")["href"]
                    price = re.sub("[^0-9]+", "", div.find("p", class_="price").text)
                    rarity_match = re.search("\[.*\]", title)
                    if rarity_match is not None:
                        rarity_string = title[rarity_match.start() + 1:rarity_match.end() - 1].strip()
                        rarity = getRarity(rarity_string)
                    if rarity_match is None or rarity is None:
                        rarity_match = re.search("\/.*\/", condition)
                        rarity_string = condition[rarity_match.start() + 1:rarity_match.end() - 1].strip()
                        rarity = getRarity(rarity_string)
                    if rarity is None:
                        print()
                    shop_url = registrationShopURL(card, shop, card_url, rarity)
                    registrationPrice(shop_url, "駿河屋", price)
                else:
                    pass
                    # print(card.card_name + "," + card_name)
            else:
                pass
                # print("error")


def updateSurugaya(shop_url):
    start = time.time()
    request = http.request("GET", shop_url.card_url)
    soup = BeautifulSoup(request.data, "html.parser")
    price = re.sub("[^0-9]","",soup.find("p",id="price").text)
    registrationPrice(shop_url,"駿河屋",price)
    sleep_time = 2 - (time.time() - start)
    if sleep_time > 0:
        time.sleep(sleep_time)
    return
