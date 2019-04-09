from django.contrib import admin
from .models import *


class PackAdmin(admin.ModelAdmin):
    readonly_fields = ["recording_card"]


class ShopURLAdmin(admin.ModelAdmin):
    readonly_fields = ["card"]


class PriceAdmin(admin.ModelAdmin):
    readonly_fields = ["shop_url"]


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
admin.site.register(SearchPage)
admin.site.register(ShopURL, ShopURLAdmin)
admin.site.register(PriceLog, PriceAdmin)
admin.site.register(Rarity)
