import urllib3
from bs4 import BeautifulSoup


def getCardDetail(url):
    http = urllib3.PoolManager()
    request = http.request('GET', "https://www.db.yugioh-card.com" + url + "&request_locale=ja")
    soup = BeautifulSoup(request.data, "html.parser")
    return soup
