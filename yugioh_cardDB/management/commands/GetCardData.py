from django.core.management import BaseCommand
from .GetData.GetCardHTML import getCardHTML


class Command(BaseCommand):
    def handle(self, *args, **options):
        getCardHTML()
