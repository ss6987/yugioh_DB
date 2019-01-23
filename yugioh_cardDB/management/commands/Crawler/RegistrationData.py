from yugioh_cardDB.models.Shop import ShopURL, Price
from django.db.utils import IntegrityError


def registrationShopURL(card, shop, card_url, rarity):
    shop_url = ShopURL(
        card_url=card_url,
        card=card,
        search_page=shop,
        rarity=rarity
    )
    try:
        shop_url.save()
    except IntegrityError:
        return ShopURL.objects.filter(card_url=card_url).first()
    return shop_url


def registrationPrice(shop_url, shop_name, price):
    price_data = Price(
        shop_url=shop_url,
        shop_name=shop_name,
        price=price,
    )
    try:
        price_data.save()
    except IntegrityError:
        return None
    return price_data
