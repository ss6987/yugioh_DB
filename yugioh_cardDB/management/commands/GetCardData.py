from django.core.management import BaseCommand
from yugioh_cardDB.management.commands.GetCardHTML import *
from yugioh_cardDB.management.commands.GetCardDetail import *
from yugioh_cardDB.management.commands.ReadCardDetail import *
from yugioh_cardDB.management.commands.RegistrationLinkMarker import *
from yugioh_cardDB.models import *
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


class Command(BaseCommand):
    def handle(self, *args, **options):
        Card.objects.all().delete()

        getCardHTML()
        print("カード詳細URL取得完了")
        getCardDetail()
        print("カード詳細取得完了")
        openFile()
        print("カード詳細登録完了")
        registrationLinkMarker()
        print("リンクマーカー登録完了")
        print("ALLコンプリート")
