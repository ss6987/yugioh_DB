from yugioh_cardDB.models.Card import Card
from yugioh_cardDB.models.Shop import ShopURL
from .SearchCard import searchCard

cards = Card.objects.all().order_by("-card_name")


def priceSearch(shop):
    for card in cards:
        if ShopURL.objects.filter(card=card, search_page=shop).exists():
            print("OK")
        else:
            searchCard(card, shop)
