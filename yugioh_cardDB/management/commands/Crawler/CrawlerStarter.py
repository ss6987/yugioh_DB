from .PriceSearch import *
from yugioh_cardDB.models.Shop import SearchPage
import concurrent.futures


def crawlerStarter():
    shop_all = SearchPage.objects.all()
    priceSearch(shop_all.filter(page_name="駿河屋").first())
    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=32)
    # for shop in shop_all:
    #     executor.submit(priceSearch,shop)
