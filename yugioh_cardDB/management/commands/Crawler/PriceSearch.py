from yugioh_cardDB.models.Card import Card
from yugioh_cardDB.models.Shop import ShopURL
from .SearchCard import searchCard
from .UpdatePrice import updatePrice
from tqdm import tqdm
import datetime

cards = Card.objects.all().filter().order_by("card_name")
today = datetime.date.today()


def priceSearch(shop, number):
    for card in tqdm(cards, position=number, desc="loop" + str(number)):
        if card.shop_url.filter(search_page=shop).count() != card.card_id.values("rarity").count():
            searchCard(card, shop)
        shop_urls = card.shop_url.filter(search_page=shop).all()
        for shop_url in shop_urls:
            if shop_url.price.first() is None:
                updatePrice(shop_url)
            elif shop_url.price.first().registration_date != today:
                updatePrice(shop_url)
