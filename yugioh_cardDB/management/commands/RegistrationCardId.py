from yugioh_cardDB.models import CardId, Pack


def registrationCardId(soup, card):
    table = soup.select_one("div#pack_list > table")
    tr_list = table.find_all("tr", class_="row")
    for tr in tr_list:
        card_id = CardId(
            card_id=tr.find_all("td")[1].text,
            card_name=card
        )
        card_id.save()
        registrationPack(tr)


def registrationPack(tr):
    pack_name = tr.find_all("td")[2].find("b").text
    pack = checkPack(pack_name, tr)
    print(pack_name)


def checkPack(pack_name, tr):
    if not Pack.objects.filter(pack_name=pack_name).exists():
        card_id = tr.find_all("td")[1].text
        pack_id = card_id[:card_id.index("-")]
        release_date = tr.find_all("td")[0].text
    else:
        pack = Pack.objects.filter(pack_name=pack_name)
    return pack
