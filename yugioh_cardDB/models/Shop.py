from django.db import models


class Shop(models.Model):
    shop_name = models.CharField('shop_name', max_length=255)

    def __str__(self):
        return self.shop_name


class ShopURL(models.Model):
    card_url = models.URLField('card_url')
    card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='price')
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name='URL')

    def __str__(self):
        return str(self.card_url)


class Price(models.Model):
    shop_url = models.ForeignKey('ShopURL', on_delete=models.CASCADE, related_name='price')
    price = models.IntegerField('price')
    registration_date = models.DateField('registration_date')

    def __str__(self):
        return str(self.shop_url) + ',' + str(self.price)
