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

    def __str__(self):
        return str(self.card_url)

    class Meta:
        unique_together = (("card_url", "card", "search_page", "rarity"))


class Price(models.Model):
    shop_url = models.ForeignKey('ShopURL', on_delete=models.CASCADE, related_name='price')
    shop_name = models.CharField('shop_name', max_length=255, default="")
    price = models.IntegerField('price',null=True)
    registration_date = models.DateField('registration_date', default=timezone.now())

    def __str__(self):
        return str(self.shop_url) + ',' + str(self.price)

    class Meta:
        unique_together = (("shop_url", "shop_name", "registration_date"))
