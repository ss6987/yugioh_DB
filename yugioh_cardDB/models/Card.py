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

    def get_monster(self):
        from yugioh_cardDB.models import Monster, PendulumMonster, LinkMonster
        classification_string = self.classification_string()
        if "リンク" in classification_string:
            return LinkMonster.objects.filter(card_name=self.card_name).first()
        elif "ペンデュラム" in classification_string:
            return PendulumMonster.objects.filter(card_name=self.card_name).first()
        elif not ("魔法" in classification_string or "罠" in classification_string):
            return Monster.objects.filter(card_name=self.card_name).first()
        return None


class CardClassification(models.Model):
    classification = models.CharField('classification', max_length=20, primary_key=True)

    def __str__(self):
        return self.classification


