from yugioh_cardDB.management.commands.SettingDriver import settingDriver, returnSearchPage, executeSearch
from yugioh_cardDB.models import LinkMonster


def registrationLinkMarker():
    driver = settingDriver()
    for i in range(1, 10):
        if i == 5:
            continue
        driver.find_element_by_css_selector("label.linkbtn" + str(i)).click()
        executeSearch(driver)
        current_url = driver.current_url
        while True:
            tr_list = driver.find_elements_by_css_selector("tr.row")
            saveMarkerData(tr_list, i)
            page_num = driver.find_element_by_css_selector("div.page_num")
            page_num.find_elements_by_tag_name("a")[-1].click()
            if current_url == driver.current_url:
                break
            current_url = driver.current_url
        driver = returnSearchPage(driver)


def saveMarkerData(tr_list, i):
    for tr in tr_list:
        card_name = tr.find_element_by_tag_name("b").text
        link_monster = LinkMonster.objects.filter(card_name=card_name).first()
        if not link_monster.marker.filter(marker=i).exists():
            link_monster.marker.add(i)
        link_monster.save()
        print(card_name)
