from yugioh_cardDB.models import LinkMonster
import urllib3
from bs4 import BeautifulSoup
from time import sleep
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


def registrationLinkMarker():
    http = urllib3.PoolManager()
    loop_range = list(range(1, 10))
    loop_range.remove(5)
    for i in tqdm(loop_range,position=0):
        fields["linkbtn" + str(i)] = str(i)
        page = 1
        max_page = 2
        while max_page >= page:
            request = http.request('GET', 'https://www.db.yugioh-card.com/yugiohdb/card_search.action',
                                   fields=fields)
            soup = BeautifulSoup(request.data, "html.parser")
            saveMarkerData(soup, i)
            del fields["linkbtn" + str(i)]
            if page == 1:
                page_num_text = soup.select_one("div.page_num_title").find("strong").text
                max_page_text = page_num_text[page_num_text.index("検索結果 ") + 5:page_num_text.index("件中")]
                max_page = int(int(max_page_text.replace(",", "")) / 100) + 1
            else:
                sleep(1)
            page += 1
            fields["page"] = str(page)
        fields["page"] = "1"


# def registrationLinkMarker():
#     driver = settingDriver()
#     for i in range(1, 10):
#         if i == 5:
#             continue
#         driver.find_element_by_css_selector("label.linkbtn" + str(i)).click()
#         executeSearch(driver)
#         current_url = driver.current_url
#         while True:
#             tr_list = driver.find_elements_by_css_selector("tr.row")
#             saveMarkerData(tr_list, i)
#             page_num = driver.find_element_by_css_selector("div.page_num")
#             page_num.find_elements_by_tag_name("a")[-1].click()
#             if current_url == driver.current_url:
#                 break
#             current_url = driver.current_url
#         driver = returnSearchPage(driver)


def saveMarkerData(soup, i):
    for tr in soup.select("tr.row"):
        card_name = tr.find("b").string.strip()
        link_monster = LinkMonster.objects.filter(card_name=card_name).first()
        if not link_monster.marker.filter(marker=i).exists():
            link_monster.marker.add(i)
            link_monster.save()

    # for tr in tr_list:
    #     card_name = tr.find_element_by_tag_name("b").text
    #     link_monster = LinkMonster.objects.filter(card_name=card_name).first()
    #     if not link_monster.marker.filter(marker=i).exists():
    #         link_monster.marker.add(i)
    #
