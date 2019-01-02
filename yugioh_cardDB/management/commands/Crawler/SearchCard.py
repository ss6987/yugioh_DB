from .shop_code.Surugaya import *


def searchCard(card, shop):
    if "駿河屋" in shop.page_name:
        searchSurugaya(card, shop)
