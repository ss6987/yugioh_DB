from yugioh_cardDB.models import CardId, Pack, Rarity, PackSeason, PackClassification
import re

file = open("yugioh_cardDB/texts/card_ids/special_id_list.txt", "r", encoding="utf-8")
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
            card_id = CardId.objects.get(card_id=card_id_string)
        elif card_id_string.strip():
            card_id = CardId(
                card_id=card_id_string,
                card_name=card,
            )
            card_id.save()
        else:
            pack_name = td_list[2].find("b").text.strip()
            flag = False
            for text in texts:
                if pack_name + "," + card.card_name + "," in text \
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
    td_list = tr.find_all("td")
    release_date = td_list[0].text
    pack_id = card_id.card_id[:card_id.card_id.index("-")]
    pack_name = td_list[2].find("b").text
    if "2パックセット 特典カード" in pack_name or "ベンダー版" in pack_name:
        return
    ban_text = r"付録カード|同梱カード"
    pack_name = re.sub(ban_text, "", pack_name).strip()
    if Pack.objects.filter(pack_name=pack_name).exists():
        pack = Pack.objects.get(pack_name=pack_name)
    else:
        pack_classification = checkPackClassification(pack_name)
        if pack_classification.pack_classification == "未設定":
            pack_classification = checkRegularPack(pack_name)

        pack = Pack(
            pack_name=pack_name,
            pack_id=pack_id,
            release_date=release_date,
            pack_season=PackSeason.objects.all().first(),
            pack_classification=pack_classification
        )
        pack.save()
    pack.recording_card.add(card_id)
    pack.save()


def checkPackClassification(pack_name):
    for pack_classification in PackClassification.objects.all():
        if not pack_classification.regex:
            continue
        match = re.match(pack_classification.regex, pack_name)
        if match:
            return pack_classification
    return PackClassification.objects.get(pack_classification="未設定")


def checkRegularPack(pack_name):
    file = open("yugioh_cardDB/management/commands/GetData/regular_pack_list.txt", encoding="utf-8")
    text = file.read()
    file.close()
    if pack_name + "\n" in text:
        return PackClassification.objects.get(pack_classification="レギュラーパック")
    return PackClassification.objects.get(pack_classification="未設定")


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
