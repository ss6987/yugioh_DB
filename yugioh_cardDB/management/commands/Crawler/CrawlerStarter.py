from .PriceSearch import *
from yugioh_cardDB.models.Shop import SearchPage, ShopURL
import concurrent.futures


def crawlerStarter():
    # ShopURL.objects.all().delete()
    shop_all = SearchPage.objects.all()
    priceSearch(shop_all.filter(page_name="宝島").first(),0)
    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    # executor.submit(priceSearch, shop_all.filter(page_name="宝島").first(), 0)
    # executor.submit(priceSearch, shop_all.filter(page_name="若院").first(), 0)
    # executor.submit(priceSearch, shop_all.filter(page_name="駿河屋").first(), 0)
    # executor.submit(priceSearch, shop_all.filter(page_name="遊道場").first(), 0)
    # for number, shop in enumerate(shop_all):
    #     executor.submit(priceSearch, shop, number)
