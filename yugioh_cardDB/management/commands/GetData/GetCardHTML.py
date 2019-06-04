from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from .GetCardDetailURL import getCardDetailURL

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument('--disable-gpu')
options.add_argument('--lang=ja')
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=options)

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


def getURL():
    string = "https://www.db.yugioh-card.com/yugiohdb/card_search.action?"
    for name, value in fields.items():
        string += name + "=" + value + "&"
    return string


def getCardHTML():
    page = 1
    max_page = 2
    bar = None
    count = 0
    while max_page / 100 + 1 >= page:
        global driver
        driver.get(getURL())
        soup = BeautifulSoup(driver.page_source, "html.parser")
        if page == 1:
            page_num_text = soup.select_one("div.page_num_title").find("strong").text
            max_page_text = page_num_text[page_num_text.index("検索結果 ") + 5:page_num_text.index("件中")]
            max_page = int(max_page_text.replace(",", ""))
            bar = tqdm(total=max_page, position=0)
        flag = getCardDetailURL(soup, bar, driver)
        if not flag and count <= 10:
            driver = webdriver.Chrome(options=options)
            count += 0
            continue
        elif count >= 10:
            print("chromedriver_error")
            exit()
        page += 1
        fields["page"] = str(page)
        count = 0
    bar.close()
