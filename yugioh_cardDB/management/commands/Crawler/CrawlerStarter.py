from .PriceSearch import *
from yugioh_cardDB.models.Shop import SearchPage, ShopURL
import concurrent.futures


def crawlerStarter():
    # ShopURL.objects.all().delete()
    shop_all = SearchPage.objects.all()
    # priceSearch(shop_all.filter(page_name="宝島").first())
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=32)
    executor.submit(priceSearch, shop_all.filter(page_name="宝島").first(), 0)
    # executor.submit(priceSearch, shop_all.filter(page_name="若院").first(), 0)
    # for shop in shop_all:
    #     executor.submit(priceSearch,shop)
