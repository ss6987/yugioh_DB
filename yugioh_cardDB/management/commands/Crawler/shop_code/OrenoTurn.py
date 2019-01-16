import urllib
import urllib3
from bs4 import BeautifulSoup
import re
from ...ReplaceName import replaceSymbol, replaceh2z, replacez2h, replacez2hNotDigit
from ..GetRarity import getRarity
from ..RegistrationData import registrationShopURL, registrationPrice
from yugioh_cardDB.models.Card import Card
from ...SleepTime import sleep2sec, setStart

http = urllib3.PoolManager()
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
cards = Card.objects.all()


def searchOrenoTurn(card, shop):
    url_name = urllib.parse.quote_plus(replaceSymbol(replaceh2z(card.card_name)), encoding="EUC-JP")
    url = shop.search_url + "?mode=srh&cid=1657307%2C0&keyword=" + url_name
    flag = True
    while flag:
        setStart()
        request = http.request("GET", url, headers=headers)
        soup = BeautifulSoup(request.data, "html.parser")
        pagenavi = soup.find("div", class_="pagenavi")
        if pagenavi is None:
            sleep2sec()
            return
        readOrenoTurn(card, shop, soup)
        a = pagenavi.find("a", class_="to_next_page")
        if a is None:
            flag = False
        else:
            url = shop.search_url + a["href"]
            print(url)
        sleep2sec()


def readOrenoTurn(card, shop, soup):
    product_items = soup.find_all("div", class_="product_item")
    for item in product_items:
        div_name = item.find("div", class_="name").extract()
        id_text = div_name.find("font").extract().text
        match = re.match("\w+-\w+", id_text)
        card_id = id_text[match.start():match.end()]
        id_list = card.card_id.filter(card_id__icontains=card_id).first()
        if id_list is None:
            if "【" in div_name.text:
                card_name = div_name.text[:div_name.text.index("【")].strip()
            else:
                card_name = div_name.text.strip()
            if replacez2h(card_name) in card.card_name or replacez2hNotDigit(card_name) in card.card_name:
                search = re.search("【[\w]+】", div_name.text)
                if search is not None:
                    rarity_string = div_name.text[search.start() + 1:search.end() - 1]
                else:
                    rarity_string = "ノーマル"
                rarity = getRarity(rarity_string)
            else:
                # print("name_error", card.card_name, card_name)
                continue
        elif id_list.rarity.all().count() == 1:
            rarity = id_list.rarity.first()
        else:
            search = re.search("【[\w]+】", div_name.text)
            if search is not None:
                rarity_string = div_name.text[search.start() + 1:search.end() - 1]
            else:
                rarity_string = "ノーマル"
            rarity = getRarity(rarity_string)
        if rarity is None:
            print("rarity_error", card, rarity_string)
            continue

        url = shop_url.search_page.search_url + div_name.find("a")["href"]
        shop_url = registrationShopURL(card, shop, url, rarity)
        div_price = item.find("div", class_="price")
        if "品切中" in div_price.text:
            price = None
        else:
            price = int(re.sub("[^0-9]+", "", div_price.text))
        registrationPrice(shop_url, shop.page_name, price)


def updateOrenoTurn(shop_url):
    setStart()
    request = http.request("GET", shop_url.card_url, headers=headers)
    soup = BeautifulSoup(request.data, "html.parser")
    tr_list = soup.find("table", class_="table").find_all("tr")
    stock = None
    price = None
    for tr in tr_list:
        if tr.find("td", class_="cell_1") is None:
            continue
        if "価格" in tr.find("td", class_="cell_1").text:
            price = re.sub("[^0-9]", "", tr.find("p", class_="price_detail").text)
        elif "在庫数" in tr.find("td", class_="cell_1").text:
            stock = tr.find("td", class_="cell_2").text
    if stock is not None and "品切中" in stock:
        price = None
    registrationPrice(shop_url, "俺のターン", price)
    sleep2sec()
    return
