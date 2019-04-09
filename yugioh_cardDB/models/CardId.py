from django.db import models


class CardId(models.Model):
    card_id = models.CharField('card_id', max_length=20, unique=True)
    card_name = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='card_id')
    rarity = models.ManyToManyField('Rarity', related_name='card_id')

    def __str__(self):
        return self.card_id + ',' + self.card_name.card_name


class Rarity(models.Model):
    rarity = models.CharField('rarity', max_length=255, primary_key=True)
    order_rank = models.IntegerField('order_rank',unique=False, default=0)

    def __str__(self):
        return self.rarity
