from django.db import models


class CardId(models.Model):
    card_id = models.CharField('card_id', max_length=20, primary_key=True)
    card_name = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='card_id')

    def __str__(self):
        return self.card_id + ',' + self.card_name
