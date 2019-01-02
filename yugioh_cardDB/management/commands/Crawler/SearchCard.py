from .shop_code.Surugaya import searchSurugaya
from .shop_code.Yudoujyou import searchYudoujyou


def searchCard(card, shop):
    if "駿河屋" in shop.page_name:
        searchSurugaya(card, shop)
    elif "遊道場" in shop.page_name:
        searchYudoujyou(card, shop)
