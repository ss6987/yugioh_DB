from .shop_code.Surugaya import *
from .shop_code.Yudoujyou import updateYudoujyou


def updatePrice(shop_url):
    if "駿河屋" in shop_url.search_page.page_name:
        updateSurugaya(shop_url)
    if "遊道場" in shop_url.search_page.page_name:
        updateYudoujyou(shop_url)
