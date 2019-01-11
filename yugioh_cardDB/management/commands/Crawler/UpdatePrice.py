from .shop_code.Surugaya import *
from .shop_code.Yudoujyou import updateYudoujyou
from .shop_code.Wakain import updateWakain
from .shop_code.Takarazima import updateTakarazima


def updatePrice(shop_url):
    if "駿河屋" in shop_url.search_page.page_name:
        updateSurugaya(shop_url)
    if "遊道場" in shop_url.search_page.page_name:
        updateYudoujyou(shop_url)
    if "若院" in shop_url.search_page.page_name:
        updateWakain(shop_url)
    if "宝島" in shop_url.search_page.page_name:
        updateTakarazima(shop_url)
