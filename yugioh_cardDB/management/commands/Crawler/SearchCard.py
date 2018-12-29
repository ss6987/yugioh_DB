import urllib
import urllib3
from bs4 import BeautifulSoup
from yugioh_cardDB.models.Shop import Price, ShopURL
from yugioh_cardDB.models.CardId import Rarity,CardId


def searchCard(card, shop):
    if "駿河屋" in shop.page_name:
        searchSurugaya(card, shop)


def searchSurugaya(card, shop):
    http = urllib3.PoolManager()
    url_name = urllib.parse.quote_plus("遊戯王　" + card.card_name, encoding="utf-8")
    request = http.request('GET',
                           shop.search_url + "/search?category=9905&search_word=" + url_name)
    soup = BeautifulSoup(request.data, "html.parser")
    for div in soup.find_all("div", class_="item"):
        condition = div.find("p", class_="condition").text
        title = div.find("p", class_="title").text
        if "中古" in condition and "英語" not in condition and "版" not in condition:
            card_url = div.find("a")["href"]
            if "/" in condition:
                card_id = title[:title.index(" ")]
                print(card_id)
                if not (CardId.objects.filter(card_id=card_id).exists() or CardId.objects.filter(card_name=card,card_id__icontains=card_id[:card_id.index("-")])):
                    print()

            else:
                print("error")
            # if "[" in title.text and "]" in title.text:
            #     rarity = title.text[title.text.index("[") + 1:title.text.index("]")]
            # else:
            #     rarity = condition.text[condition.text.index("/") + 1:]
            #     rarity = rarity[:condition.text.index("/")]
            # print(rarity)
            # if not rarity:
            #     print()
            # shop_url = ShopURL(
            #     card_url=card_url,
            #     card=card,
            #     search_page=shop,
            #     rarity="",
            # )


def getRarity(rarity_string):
    if "N" == rarity_string:
        return Rarity.objects.filter(rarity="ノーマル").first()
    elif "R" == rarity_string:
        return Rarity.objects.filter(rarity="レア").first()

    return Rarity.objects.filter(rarity=rarity_string).first()
