from django.contrib import admin
from .models import *


class PackAdmin(admin.ModelAdmin):
    exclude = ['recording_card',]


admin.site.register(Card)
admin.site.register(Monster)
admin.site.register(PendulumMonster)
admin.site.register(LinkMonster)
admin.site.register(CardClassification)
admin.site.register(Attribute)
admin.site.register(Type)
admin.site.register(LinkMarker)
admin.site.register(CardId)
admin.site.register(Pack, PackAdmin)
admin.site.register(PackClassification)
admin.site.register(PackOfficialName)
admin.site.register(Shop)
admin.site.register(ShopURL)
admin.site.register(Price)
