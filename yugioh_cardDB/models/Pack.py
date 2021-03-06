from django.db import models


class Pack(models.Model):
    pack_name = models.CharField('pack_name', max_length=255, unique=True)
    pack_id = models.CharField('pack_id', max_length=10)
    release_date = models.DateField('release_date', null=True, blank=True)
    recording_card = models.ManyToManyField('CardId', related_name='pack')
    pack_classification = models.ForeignKey('PackClassification', on_delete=models.SET_NULL, related_name='packs',
                                            blank=True, null=True)

    def __str__(self):
        return self.pack_name

    def get_recording_cards(self):
        return self.recording_card.order_by("card_id").prefetch_related("card_name")


class PackClassification(models.Model):
    pack_classification = models.CharField('pack_classification', max_length=255, primary_key=True)
    order_rank = models.IntegerField("order_rank",default=0,unique=True)

    def __str__(self):
        return self.pack_classification

    def get_packs(self):
        return self.packs.all()


class PackOfficialName(models.Model):
    official_name = models.CharField('db_pack_name', max_length=255, primary_key=True)
    official_id = models.CharField('db_pack_id', max_length=10, default="", blank=True, null=True)
    db_pack = models.ForeignKey('Pack', on_delete=models.SET_NULL, related_name='official_name', null=True)

    def __str__(self):
        return self.official_name
