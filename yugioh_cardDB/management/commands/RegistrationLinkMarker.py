from yugioh_cardDB.management.commands.SettingDriver import settingDriver, returnSearchPage, executeSearch
from yugioh_cardDB.models import LinkMonster


def registrationLinkMarker():
    driver = settingDriver()
    for i in range(1, 10):
        if i == 5:
            continue
        driver.find_element_by_css_selector("label.linkbtn" + str(i)).click()
        executeSearch(driver)
        tr_list = driver.find_elements_by_css_selector("tr.row")
        for tr in tr_list:
            card_name = tr.find_element_by_tag_name("b").text
            link_monster = LinkMonster.objects.filter(card_name=card_name).first()
            link_monster.marker.add(i)
            link_monster.save()
            print(card_name)
        driver = returnSearchPage(driver)
