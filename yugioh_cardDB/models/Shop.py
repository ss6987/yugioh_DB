from django.db import models
from django.utils import timezone


class SearchPage(models.Model):
    page_name = models.CharField('page_name', max_length=255, primary_key=True)
    search_url = models.URLField('search_url')

    def __str__(self):
        return self.page_name


class ShopURL(models.Model):
    card_url = models.URLField('card_url')
    card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='shop_url')
    search_page = models.ForeignKey('SearchPage', on_delete=models.CASCADE, related_name='shop_url', default="")
    rarity = models.ForeignKey('Rarity', on_delete=models.CASCADE, related_name='shop_url', default="")
    now_price = models.IntegerField('now_price', default=0, null=True)

    def __str__(self):
        return str(self.card_url)

    class Meta:
        unique_together = (("card_url", "card", "search_page", "rarity"))


class PriceLog(models.Model):
    shop_url = models.ForeignKey('ShopURL', on_delete=models.CASCADE, related_name='price')
    registration_date = models.DateField('registration_date', default=timezone.now)
    price = models.IntegerField('price', null=True)

    def __str__(self):
        return str(self.registration_date)

    class Meta:
        unique_together = (("shop_url", "registration_date"))
