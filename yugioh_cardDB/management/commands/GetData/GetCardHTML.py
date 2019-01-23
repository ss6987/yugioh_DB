from .GetCardDetailURL import getCardDetailURL
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

fields = {
    "ope": "1",
    "sess": "1",
    "keyword": "",
    "stype": "1",
    "link_m": "2",
    "othercon": "2",
    "rp": "100",
    "page": "1",
    "mode": "2",
    "request_locale": "ja",
}


def getCardHTML():
    http = urllib3.PoolManager()
    page = 1
    max_page = 2
    bar = None
    while max_page / 100 + 1 >= page:
        request = http.request('GET', "https://www.db.yugioh-card.com/yugiohdb/card_search.action", fields=fields)
        soup = BeautifulSoup(request.data, "html.parser")
        if page == 1:
            page_num_text = soup.select_one("div.page_num_title").find("strong").text
            max_page_text = page_num_text[page_num_text.index("検索結果 ") + 5:page_num_text.index("件中")]
            max_page = int(max_page_text.replace(",", ""))
            bar = tqdm(total=max_page, position=0)
        getCardDetailURL(soup, bar)
        page += 1
        fields["page"] = str(page)
    bar.close()
