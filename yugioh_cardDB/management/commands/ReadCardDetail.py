import glob
from bs4 import BeautifulSoup
from yugioh_cardDB.management.commands.RegistrationCardData import registrationCard
from yugioh_cardDB.management.commands.RegistrationCardId import registrationCardId


def openFile():
    files = glob.glob("yugioh_cardDB/texts/card_detail_html/*")
    for file in files:
        readCardDetail(open(file, "r", encoding="utf-8").read())


def readCardDetail(html):
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.find("article")
    try:
        soup.select_one("div.forbidden_limited").extract()
    except AttributeError:
        pass
    card = registrationCard(soup)
    registrationCardId(soup,card)
