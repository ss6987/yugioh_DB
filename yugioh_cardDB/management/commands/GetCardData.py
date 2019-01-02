from django.core.management import BaseCommand
from yugioh_cardDB.management.commands.GetData.GetCardHTML import *
from yugioh_cardDB.management.commands.GetData.RegistrationLinkMarker import *
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import gc
from yugioh_cardDB.models.Card import Card

urllib3.disable_warnings(InsecureRequestWarning)


class Command(BaseCommand):
    def handle(self, *args, **options):
        Card.objects.all().delete()
        getCardHTML()
        print("カード詳細URL取得完了")
        gc.collect()
        registrationLinkMarker()
        print("リンクマーカー登録完了")
        print("ALLコンプリート")
