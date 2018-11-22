from django.db import models

CLASSIFICATION_CHOICES = (
    (1, "モンスター"),
    (2, "魔法"),
    (3, "罠")
)


# Create your models here.
class Card(models.Model):
    card_name = models.CharField('card_name', max_length=65535, primary_key=True)
    phonetic = models.CharField('phonetic',max_length=65535,default='')
    classification = models.IntegerField('classification', choices=CLASSIFICATION_CHOICES)
    card_effect = models.TextField('card_effect')
