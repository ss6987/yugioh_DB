import urllib
import urllib3
import time
from bs4 import BeautifulSoup
import re
from ...ReplaceName import replaceName, replaceSymbol
from ..GetRarity import getRarity
from ..RegistrationData import registrationShopURL, registrationPrice
from yugioh_cardDB.models.Card import Card
from ...SleepTime import sleep2sec,setStart

http = urllib3.PoolManager()
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
cards = Card.objects.all()


def searchWakain(card, shop):
    url_name = urllib.parse.quote_plus(replaceSymbol(card.card_name), encoding="EUC-JP")
    url_name = url_name.replace("-", "%A1%DD")
    url = shop.search_url + "?mode=srh&cid=1270248%2C0&keyword=" + url_name
    flag = True
    while flag:
        setStart()
        request = http.request("GET", url, headers=headers)
        soup = BeautifulSoup(request.data, "html.parser")
        contents = soup.find("div", id="inn-box")
        p_list = contents.find_all("p")
        for p in p_list:
            if re.search("\d件の商品が見つかりました", p.text) is not None:
                item_count = int(re.sub("[^\d]+", "", p.text))
                break
        if item_count == 0:
            sleep2sec()
            return
        readWakain(card, shop, contents)
        last_li = contents.find("ul", class_="page").find_all("li")[-1]
        if last_li.find("a") is None:
            flag = False
        else:
            url = shop.search_url + last_li.find("a")["href"]
        sleep2sec()


def readWakain(card, shop, soup):
    li_list = soup.find("ul", class_="product").find_all("li")
    for li in li_list:
        text = li.find("a").text
        card_name = re.sub("(\(|（).*(\)|）)", "", text).replace("No Photo", "").strip()
        if replaceName(card_name) != card.card_name:
            continue
        if len(cards.filter(search_name=replaceName(card_name))) != 1:
            print(card.card_name, card.search_name, replaceName(card_name))
            continue
        match = re.search("\(.*\)|（.*）", text)
        if match is not None:
            rarity_string = text[match.start() + 1:match.end() - 1]
            if "/" in rarity_string:
                print("多重")
                continue
        else:
            rarity_string = "ノーマル"
        rarity = getRarity(rarity_string)
        if rarity is None:
            print("error", card_name, rarity_string)
            continue
        url = li.find("a")["href"]
        shop_url = registrationShopURL(card, shop, url, rarity)
        if li.find("span", class_="price") is None:
            continue
        price = re.sub("[^0-9]+", "", li.find("span", class_="price").text)
        registrationPrice(shop_url, shop.page_name, price)
