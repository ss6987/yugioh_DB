from .GetCardDetail import getCardDetail
from .RegistrationCardData import registrationCard
import time


def getCardDetailURL(soup, bar):
    tr_list = soup.select("tr.row")
    for tr in tr_list:
        start = time.time()
        td = tr.find_all("td")[1]
        url = td.select_one("input.link_value").attrs["value"]
        soup = getCardDetail(url)
        registrationCard(soup)
        sleep_time = 2 - (time.time() - start)
        if sleep_time > 0:
            time.sleep(sleep_time)
        # bar.update(1)
