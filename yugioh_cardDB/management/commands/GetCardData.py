from django.core.management import BaseCommand
from yugioh_cardDB.management.commands.GetCardHTML import *
from yugioh_cardDB.management.commands.GetCardDetail import *
from yugioh_cardDB.management.commands.ReadCardDetail import *
from yugioh_cardDB.management.commands.RegistrationLinkMarker import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        getCardHTML()
        getCardDetail()
        openFile()
        registrationLinkMarker()
