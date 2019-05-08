from .GetCardDetail import getCardDetail
from .RegistrationCardData import registrationCard
from ..SleepTime import setStart, sleep2sec


def getCardDetailURL(soup, bar,driver):
    tr_list = soup.select("tr.row")
    for tr in tr_list:
        setStart()
        td = tr.find_all("td")[1]
        url = td.select_one("input.link_value").attrs["value"]
        soup = getCardDetail(url,driver)
        registrationCard(soup)
        sleep2sec()
        bar.update(1)
