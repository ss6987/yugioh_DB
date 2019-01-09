from .shop_code.Surugaya import searchSurugaya
from .shop_code.Yudoujyou import searchYudoujyou
from .shop_code.Wakain import searchWakain
from .shop_code.Takarazima import searchTakarazima


def searchCard(card, shop):
    if "駿河屋" in shop.page_name:
        searchSurugaya(card, shop)
    elif "遊道場" in shop.page_name:
        searchYudoujyou(card, shop)
    elif "若院" in shop.page_name:
        searchWakain(card, shop)
    elif "宝島" in shop.page_name:
        searchTakarazima(card, shop)
