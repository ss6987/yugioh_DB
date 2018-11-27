import glob
from bs4 import BeautifulSoup


def openFile():
    files = glob.glob("yugioh_cardDB/texts/card_detail_html/*")
    for file in files:
        readCardDetail(open(file, "r", encoding="utf-8").read())


def readCardDetail(html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    print(h1.text)
