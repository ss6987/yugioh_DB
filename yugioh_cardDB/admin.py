from django.contrib import admin
from .models import *


class PackAdmin(admin.ModelAdmin):
    readonly_fields = ["recording_card"]
    list_display = ["pack_name", "pack_id", "release_date", "pack_classification", "pack_season"]
    list_filter = ["pack_classification", "pack_season"]
    search_fields = ["pack_name", "pack_id"]


class ShopURLAdmin(admin.ModelAdmin):
    readonly_fields = ["card"]


class PriceAdmin(admin.ModelAdmin):
    readonly_fields = ["shop_url"]


class PackClassificationAdmin(admin.ModelAdmin):
    ordering = ('-order_rank',)
    list_display = ["pack_classification", "order_rank", "regex"]


class PackSeasonAdmin(admin.ModelAdmin):
    ordering = ('-order_rank',)
    list_display = ["season_name", "start_date", "order_rank"]


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
admin.site.register(PackClassification, PackClassificationAdmin)
admin.site.register(PackSeason, PackSeasonAdmin)
admin.site.register(SearchPage)
admin.site.register(ShopURL, ShopURLAdmin)
admin.site.register(PriceLog, PriceAdmin)
admin.site.register(Rarity)
