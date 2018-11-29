from yugioh_cardDB.models import CardId, Pack, Rarity


def registrationCardId(soup, card):
    table = soup.select_one("div#pack_list > table")
    tr_list = table.find_all("tr", class_="row")
    for tr in tr_list:
        rarity_td = tr.find_all("td")[3]
        rarity = checkRarity(rarity_td)
        card_id_string = tr.find_all("td")[1].text
        if not card_id_string:
            continue
        if not CardId.objects.filter(card_id=card_id_string).exists():
            card_id = CardId(
                card_id=card_id_string,
                card_name=card,
            )
            card_id.save()
        else:
            card_id = CardId.objects.filter(card_id=card_id_string).first()
        card_id.rarity.add(rarity)
        card_id.save()
        registrationPack(tr)


def registrationPack(tr):
    pack_name = tr.find_all("td")[2].find("b").text
    pack = checkPack(pack_name, tr)
    pack.recording_card.add(CardId.objects.filter(card_id=tr.find_all("td")[1].text).first())
    pack.save()


def checkPack(pack_name, tr):
    if not Pack.objects.filter(pack_name=pack_name).exists():
        card_id = tr.find_all("td")[1].text
        pack_id = card_id[:card_id.index("-")]
        release_date = tr.find_all("td")[0].text
        pack = Pack(pack_name=pack_name,
                    pack_id=pack_id,
                    release_date=release_date)
        pack.save()
        return pack
    else:
        pack = Pack.objects.filter(pack_name=pack_name).first()
    return pack


def checkRarity(rarity_td):
    try:
        rarity_string = rarity_td.find("img").attrs['alt'].replace("仕様", "")
    except AttributeError:
        rarity_string = "ノーマル"
    if not Rarity.objects.filter(rarity=rarity_string).exists():
        rarity = Rarity(rarity=rarity_string)
        rarity.save()
        return rarity
    else:
        return Rarity.objects.filter(rarity=rarity_string).first()
