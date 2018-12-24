from django.core.management import BaseCommand
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("OK")
