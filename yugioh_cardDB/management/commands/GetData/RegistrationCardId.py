from yugioh_cardDB.models import CardId, Pack, Rarity, PackOfficialName
import sys

file = open("yugioh_cardDB/texts/card_ids/log.txt", "r", encoding="utf-8")
texts = file.readlines()
file.close()


def registrationCardId(soup, card):
    table = soup.select_one("div#pack_list > table")
    tr_list = table.find_all("tr", class_="row")
    for tr in tr_list:
        td_list = tr.find_all("td")
        rarity_td = td_list[3]
        rarity = checkRarity(rarity_td)
        card_id_string = td_list[1].text
        if card_id_string.strip() and CardId.objects.filter(card_id=card_id_string).exists():
            card_id = CardId.objects.filter(card_id=card_id_string).first()
        elif card_id_string.strip():
            card_id = CardId(
                card_id=card_id_string,
                card_name=card,
            )
            card_id.save()
        else:
            pack = PackOfficialName.objects.filter(official_name=td_list[2].find("b").text).first().db_pack
            flag = False
            for text in texts:
                if pack.pack_name + "," + card.card_name + "," in text \
                        and not CardId.objects.filter(card_id=text.replace("\n", "").split(",")[2]).exists():
                    card_id = CardId(
                        card_id=text.replace("\n", "").split(",")[2],
                        card_name=card
                    )
                    card_id.save()
                    flag = True
                    break
            if not flag:
                continue
        card_id.rarity.add(rarity)
        card_id.save()
        registrationPack(tr, card_id)


def registrationPack(tr, card_id):
    pack_name = tr.find_all("td")[2].find("b").text
    pack = checkPack(pack_name)
    pack.recording_card.add(card_id)
    pack.save()


def checkPack(pack_name):
    official_pack = PackOfficialName.objects.filter(official_name=pack_name).first()
    try:
        pack = official_pack.db_pack
    except AttributeError:
        print(pack_name)
        sys.exit()
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
