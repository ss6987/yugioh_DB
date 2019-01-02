from yugioh_cardDB.models.Card import Card
from .SearchCard import searchCard
from .UpdatePrice import updatePrice
from tqdm import tqdm
import datetime

cards = Card.objects.all().order_by("-card_name")
today = datetime.date.today()


def priceSearch(shop):
    for card in tqdm(cards):
        if card.shop_url.filter(search_page=shop).exists():
            shop_urls = card.shop_url.filter(search_page=shop).all()
            for shop_url in shop_urls:
                if shop_url.price.first().registration_date != today:
                    updatePrice(shop_url)
        else:
            searchCard(card, shop)
