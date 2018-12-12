import glob
from bs4 import BeautifulSoup
from yugioh_cardDB.management.commands.RegistrationCardData import registrationCard
from yugioh_cardDB.management.commands.RegistrationCardId import registrationCardId
from tqdm import tqdm


def openFile():
    # file = open("yugioh_cardDB/texts/card_detail_html/4244.txt","r",encoding="utf-8")
    # text = file.read()
    # file.close()
    # readCardDetail(text)
    files = glob.glob("yugioh_cardDB/texts/card_detail_html/*")

    for file in tqdm(files,position=0):
        tmp_file = open(file, "r", encoding="utf-8")
        text = tmp_file.read()
        tmp_file.close()
        readCardDetail(text)
        del tmp_file
        del text


def readCardDetail(html):
    soup = BeautifulSoup(html, "html.parser")
    try:
        soup.select_one("div.forbidden_limited").extract()
    except AttributeError:
        pass
    card = registrationCard(soup)
    registrationCardId(soup, card)

