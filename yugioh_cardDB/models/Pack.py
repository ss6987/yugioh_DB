from django.db import models


class PackClassification(models.Model):
    pack_classification = models.CharField('pack_classification', max_length=255, primary_key=True)
    packs = models.ManyToManyField("Pack", related_name='pack_classification')

    def __str__(self):
        return self.pack_classification


class Pack(models.Model):
    pack_name = models.CharField('pack_name', max_length=255, primary_key=True)
    pack_id = models.CharField('pack_id', max_length=10)
    release_date = models.DateField('release_date', null=True, blank=True)
    recording_card = models.ManyToManyField('CardId', related_name='pack')

    def __str__(self):
        return self.pack_name
