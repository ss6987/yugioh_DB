import urllib
import re
from ...ReplaceName import replaceSymbol, replaceh2z, replacez2h, replacez2hNotDigit
from ..GetRarity import getRarity
from ..RegistrationData import registrationShopURL, registrationPrice
from yugioh_cardDB.models.Card import Card
from ...SleepTime import sleep2sec, setStart
from ..GetRequest import getSoup

cards = Card.objects.all()


def searchTakarazima(card, shop):
    url_name = urllib.parse.quote_plus(replaceSymbol(replaceh2z(card.card_name)), encoding="utf-8")
    submit = urllib.parse.quote_plus("検索", encoding="utf-8")
    url = shop.search_url + "product-list?keyword=" + url_name + "&Submit=" + submit
    flag = True
    while flag:
        soup = getSoup(url)
        setStart()
        category_item_count = soup.find("div", class_="category_item_count")
        item_count = int(re.sub("[^0-9]", "", category_item_count.find("span", class_="number").text))
        if item_count == 0:
            sleep2sec()
            return
        readTakarazima(card, shop, soup)
        a = soup.find("a", class_="to_next_page")
        if a is None:
            flag = False
        else:
            url = shop.search_url + a["href"]
        sleep2sec()


def readTakarazima(card, shop, soup):
    li_list = soup.find_all("li", class_="list_item_cell")
    for li in li_list:
        item_name = li.find("p", class_="item_name")
        card_id = item_name.find("span", class_="model_number_value")
        id_list = card.card_id.filter(card_id__icontains=card_id.text).first()
        if id_list is None:
            continue
        if id_list.rarity.all().count() == 1:
            rarity = id_list.rarity.first()
        else:
            rarity_string = item_name.find("span", class_="goods_name").text
            if " " in rarity_string:
                rarity_string = rarity_string.split(" ")[-1]
            if "　" in rarity_string:
                rarity_string = rarity_string.split("　")[-1]
            if replacez2h(rarity_string) in card.card_name or replacez2hNotDigit(
                    rarity_string) in card.card_name or rarity_string == "":
                rarity_string = "ノーマル"
            rarity = getRarity(rarity_string)
        if rarity is None:
            print("error", card, rarity_string)
            continue
        url = li.find("a")["href"]
        shop_url = registrationShopURL(card, shop, url, rarity)
        if li.find("span", class_="price") is None:
            continue
        price = re.sub("[^0-9]+", "", li.find("span", class_="price").text)
        registrationPrice(shop_url, shop.page_name, price)


def updateTakarazima(shop_url):
    soup = getSoup(shop_url.card_url)
    setStart()
    span = soup.find("span", id="pricech")
    if span is not None:
        price = re.sub("[^\d]+", "", span.text)
    else:
        price = None
    registrationPrice(shop_url, "宝島", price)
    sleep2sec()
    return
