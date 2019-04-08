from django.db import models
from .Card import Card

MARKER_CHOICES = [
    (1, '左下'),
    (2, '下'),
    (3, '右下'),
    (4, '左'),
    (5, '中央'),
    (6, '右'),
    (7, '左上'),
    (8, '上'),
    (9, '右上'),
]

SCALE_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
)


class Monster(Card):
    level = models.IntegerField('level', default=1)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE, related_name='monster')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='monster')
    attack = models.IntegerField('attack', default=0)
    defence = models.IntegerField('defence', default=0, null=True, blank=True)

    def __str__(self):
        return self.card_name

    def get_defence(self):
        if self.defence >= 0:
            return str(self.defence)
        elif self.defence == -1:
            return "?"
        else:
            return "---"


class PendulumMonster(Monster):
    scale = models.IntegerField('scale')
    pendulum_effect = models.TextField('pendulum_effect', blank=True, null=True)

    def __str__(self):
        return self.card_name


class LinkMonster(Monster):
    marker = models.ManyToManyField('LinkMarker', related_name='linkMonster')

    def __str__(self):
        return self.card_name

    def get_marker_string(self):
        strings = []
        for marker in self.marker.all():
            strings.append(str(marker))
        return "/".join(strings)


class Attribute(models.Model):
    attribute = models.CharField('attribute', max_length=10, primary_key=True)

    def __str__(self):
        return self.attribute.replace("属性", "")


class Type(models.Model):
    type = models.CharField('type', max_length=20, primary_key=True)

    def __str__(self):
        return self.type.replace("族", "")


class LinkMarker(models.Model):
    marker = models.IntegerField('marker', choices=MARKER_CHOICES, primary_key=True)

    def __str__(self):
        return MARKER_CHOICES[self.marker - 1][1]
