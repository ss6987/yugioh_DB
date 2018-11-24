from django.db import models


# Create your models here.
class Card(models.Model):
    card_name = models.CharField('card_name', max_length=65535, primary_key=True)
    phonetic = models.CharField('phonetic', max_length=65535, default='', null=True, blank=True)
    classification = models.ManyToManyField('CardClassification', related_name='card')
    card_effect = models.TextField('card_effect', blank=True, null=True)

    def __str__(self):
        return self.card_name


class Monster(Card):
    level = models.IntegerField('level', default=1)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE, related_name='monster')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='monster')
    attack = models.IntegerField('attack', default=0)
    defence = models.IntegerField('defence', default=0,null=True,blank=True)

    def __str__(self):
        return self.card_name


class CardClassification(models.Model):
    classification = models.CharField('classification', max_length=20, primary_key=True)

    def __str__(self):
        return self.classification


class Attribute(models.Model):
    attribute = models.CharField('attribute', max_length=10, primary_key=True)

    def __str__(self):
        return self.attribute


class Type(models.Model):
    type = models.CharField('type', max_length=20, primary_key=True)

    def __str__(self):
        return self.type
