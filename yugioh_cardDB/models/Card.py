from django.db import models


class Card(models.Model):
    card_name = models.CharField('card_name', max_length=65535, primary_key=True)
    phonetic = models.CharField('phonetic', max_length=65535, default='', null=True, blank=True)
    english_name = models.CharField('english_name', max_length=65535, default='', null=True, blank=True)
    classification = models.ManyToManyField('CardClassification', related_name='card')
    card_effect = models.TextField('card_effect', blank=True, null=True)

    def __str__(self):
        return self.card_name

    def classification_string(self):
        strings = []
        for classification in self.classification.all():
            strings.append(str(classification))
        return "/".join(strings)


class CardClassification(models.Model):
    classification = models.CharField('classification', max_length=20, primary_key=True)

    def __str__(self):
        return self.classification
