from django.db import models


class SearchPage(models.Model):
    page_name = models.CharField('page_name', max_length=255, primary_key=True)
    search_url = models.URLField('search_url')

    def __str__(self):
        return self.page_name


class ShopURL(models.Model):
    card_url = models.URLField('card_url', primary_key=True)
    card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='price')
    search_page = models.ForeignKey('SearchPage', on_delete=models.CASCADE, related_name='URL', default="")
    rarity = models.ForeignKey('Rarity', on_delete=models.SET_NULL, related_name='price', null=True)

    def __str__(self):
        return str(self.card_url)


class Price(models.Model):
    shop_url = models.ForeignKey('ShopURL', on_delete=models.CASCADE, related_name='price')
    shop_name = models.CharField('shop_name', max_length=255, default="")
    price = models.IntegerField('price')
    registration_date = models.DateField('registration_date')

    def __str__(self):
        return str(self.shop_url) + ',' + str(self.price)
