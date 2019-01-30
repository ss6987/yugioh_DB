from .PriceSearch import *
from yugioh_cardDB.models.Shop import SearchPage, ShopURL
import concurrent.futures


def crawlerStarter():
    # ShopURL.objects.all().delete()
    shop_all = SearchPage.objects.all()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    file = open("log.txt","w",encoding="utf-8")
    file.write("START\n")
    # priceSearch(shop_all.filter(page_name="俺のターン").first(),0)
    
    results = [
        executor.submit(priceSearch, shop_all.filter(page_name="宝島").first(), 0),
        executor.submit(priceSearch, shop_all.filter(page_name="若院").first(), 1),
        executor.submit(priceSearch, shop_all.filter(page_name="駿河屋").first(), 2),
        executor.submit(priceSearch, shop_all.filter(page_name="遊道場").first(), 3),
        executor.submit(priceSearch, shop_all.filter(page_name="俺のターン").first(), 4)
    ]
    for future in concurrent.futures.as_completed(results):
        file.write("exception:" + str(future.exception()) + "\n")
    file.write("END")
    file.close()
    # for number, shop in enumerate(shop_all):
    #     executor.submit(priceSearch, shop, number)
