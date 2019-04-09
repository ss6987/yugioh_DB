from yugioh_cardDB.models.Shop import ShopURL, PriceLog
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


def registrationPrice(shop_url, price):
    price_data = PriceLog(
        shop_url=shop_url,
        price=price,
    )
    try:
        price_data.save()
        shop_url.now_price = price
        shop_url.save()
    except IntegrityError:
        return None
    return price_data
