from .shop_code.Surugaya import *


def updatePrice(shop_url):
    if "駿河屋" in shop_url.search_page.page_name:
        updateSurugaya(shop_url)
