from django.db import models


class Card(models.Model):
    card_name = models.CharField('card_name', max_length=65535, unique=True)
    phonetic = models.CharField('phonetic', max_length=65535, default='', null=True, blank=True)
    english_name = models.CharField('english_name', max_length=65535, default='', null=True, blank=True)
    classification = models.ManyToManyField('CardClassification', related_name='card')
    card_effect = models.TextField('card_effect', blank=True, null=True)
    search_name = models.CharField('search_name', max_length=65535)
    search_phonetic = models.CharField('search_phonetic', max_length=65535, default='', null=True, blank=True)

    def __str__(self):
        return self.card_name

    def classification_string(self):
        strings = []
        for classification in self.classification.all():
            strings.append(str(classification))
        return "/".join(strings)

    def get_monster(self):
        classification_string = self.classification_string()
        if "リンク" in classification_string:
            return self.monster.linkmonster
        elif "ペンデュラム" in classification_string:
            return self.monster.pendulummonster
        elif not ("魔法" in classification_string or "罠" in classification_string):
            return self.monster
        return self

    def get_type(self):
        classification = self.classification_string()
        if "魔法" in classification:
            return "Magic"
        elif "罠" in classification:
            return "Trap"
        elif "リンク" in classification:
            return "Link"
        elif "ペンデュラム" in classification:
            return "Pendulum"
        elif "儀式" in classification:
            return "Ritual"
        elif "融合" in classification:
            return "Fusion"
        elif "シンクロ" in classification:
            return "Synchro"
        elif "エクシーズ" in classification:
            return "XYZ"
        elif "効果" in classification:
            return "Effect"
        elif "通常" in classification:
            return "Normal"
        return str(type(self))

    def get_effect(self):
        return self.card_effect.replace("\n", "<br/>")

    def get_price_data(self):
        price_data = []
        rarity_list = self.card_id.all().order_by('rarity__order_rank').values('rarity').distinct()
        for rarity in rarity_list:
            shop_list = self.shop_url.filter(rarity=rarity['rarity'])
            if not shop_list:
                continue
            last_date = shop_list.order_by('-price__registration_date').first().price.last().registration_date
            price_list = []
            for shop in shop_list:
                tmp_price = shop.price.filter(registration_date=last_date).exclude(price=None).first()
                if tmp_price is not None:
                    price_list.append(tmp_price)
            if not price_list:
                continue
            price_list = sorted(price_list, key=lambda p: p.price)
            rarity['price_list'] = price_list
            price_data.append(rarity)
        return price_data


class CardClassification(models.Model):
    classification = models.CharField('classification', max_length=20, primary_key=True)

    def __str__(self):
        return self.classification
