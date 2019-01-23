import urllib
import re
from ...ReplaceName import replaceName, replaceSymbol
from ..GetRarity import getRarity
from ..RegistrationData import registrationShopURL, registrationPrice
from ...SleepTime import sleep2sec, setStart
from ..GetRequest import getSoup



def searchWakain(card, shop):
    url_name = urllib.parse.quote_plus(replaceSymbol(card.card_name), encoding="EUC-JP")
    url_name = url_name.replace("-", "%A1%DD")
    url = shop.search_url + "?mode=srh&cid=1270248%2C0&keyword=" + url_name
    flag = True
    while flag:
        soup = getSoup(url)
        setStart()
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
        url = shop.search_url + li.find("a")["href"]
        if replaceName(card_name) != card.card_name:
            continue
        match = re.search("\(.*\)|（.*）", text)
        if match is not None:
            rarity_string = text[match.start() + 1:match.end() - 1]
            if "/" in rarity_string:
                setStart()
                soup = getSoup(url)
                table = soup.find("table", id="option_tbl")
                tr_list = table.find_all("tr")
                for tr in tr_list:
                    if tr.find("th", class_="cell_1") is None:
                        continue
                    th = tr.find("th", class_="cell_1")
                    td = tr.find("td", class_="cell_2")
                    rarity_string = th.text.replace("NEAR-MINT", "").strip()
                    rarity = getRarity(rarity_string)
                    if rarity is None:
                        print("error", card_name, rarity_string)
                        continue
                    shop_url = registrationShopURL(card, shop, url, rarity)
                    match = re.match("[\d,]+円", td.text)
                    price = re.sub("[^0-9]+", "", td.text[match.start():match.end()])
                    registrationPrice(shop_url, shop.page_name, price)
                sleep2sec()
                continue
        else:
            rarity_string = "ノーマル"
        rarity = getRarity(rarity_string)
        if rarity is None:
            print("error", card_name, rarity_string)
            continue
        shop_url = registrationShopURL(card, shop, url, rarity)
        if li.find("span", class_="price") is None:
            continue
        price = re.sub("[^0-9]+", "", li.find("span", class_="price").text)
        registrationPrice(shop_url, shop.page_name, price)


def updateWakain(shop_url):
    setStart()
    soup = getSoup(shop_url.card_url)
    tr = soup.find("tr", class_="sales")
    if tr is not None:
        price = re.sub("[^\d]+", "", tr.find("td").text)
    else:
        price = None
    registrationPrice(shop_url, "若院", price)
    sleep2sec()
    return
