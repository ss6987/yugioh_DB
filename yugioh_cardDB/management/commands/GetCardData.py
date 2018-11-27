from django.core.management import BaseCommand
from yugioh_cardDB.management.commands.GetCardDetail import *
from yugioh_cardDB.management.commands.ReadCardDetail import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        # getCardHTML()
        # getCardDetail()
        openFile()
