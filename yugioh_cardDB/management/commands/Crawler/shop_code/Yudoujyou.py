import urllib
import re
from ..RegistrationData import registrationShopURL, registrationPrice
from ...ReplaceName import replaceName
from ..GetRarity import getRarity
from ...SleepTime import setStart, sleep2sec
from ..GetRequest import getSoup


def searchYudoujyou(card, shop):
    url_name = urllib.parse.quote_plus(card.card_name, encoding="utf-8")
    submit = urllib.parse.quote_plus("検索", encoding="utf-8")
    url = shop.search_url + "product-list?keyword=" + url_name + "&Submit=" + submit
    flag = True
    while flag:
        setStart()
        soup = getSoup(url)
        item_count = int(re.sub("[^0-9]", "", soup.find("div", class_="list_count").text))
        if item_count == 0:
            sleep2sec()
            return
        readYudoujyou(card, shop, soup)
        if soup.find("a", class_="to_next_page") is None:
            flag = False
        else:
            url = shop.search_url + soup.find("a", class_="to_next_page")["href"]
        sleep2sec()


def readYudoujyou(card, shop, soup):
    td_list = soup.find("table", class_="list_item_table").find_all("td")
    for td in td_list:
        h2 = td.find("h2")
        if h2 is None:
            continue
        card_name = re.sub("(【.*】|\[.*\]|\(.*\))+", "", h2.text)
        if "/" in card_name:
            card_name, rarity_string = card_name.split("/")
            rarity_string = re.sub("「.*」", "", rarity_string.strip())
        else:
            rarity_string = "ノーマル"
        if replaceName(card_name) == card.search_name:
            url = h2.find("a")["href"]
            try:
                price = re.sub("[^0-9]+", "", td.find("span", class_="pricech").text)
            except AttributeError:
                continue
            rarity = getRarity(rarity_string)
            if rarity is None:
                soup = getSoup(url)
                div = soup.find("div", class_="detail_desc_box")
                match = re.search("■.*/.*\r\n", div.text)
                rarity_string = div.text[match.start():match.end()]
                rarity_string = rarity_string[rarity_string.index("/") + 1:]
                rarity = getRarity(rarity_string.strip())
            if rarity is None:
                print(card.card_name, rarity_string)
                continue
            shop_url = registrationShopURL(card, shop, url, rarity)
            registrationPrice(shop_url, shop.page_name, price)


def updateYudoujyou(shop_url):
    soup = getSoup(shop_url.card_url)
    setStart()
    price = re.sub("[^0-9]", "", soup.find("span", id="pricech").text)
    registrationPrice(shop_url, "遊道場", price)
    sleep2sec()
    return
