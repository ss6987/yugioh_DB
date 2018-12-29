from yugioh_cardDB.models import *
import re
from .RegistrationCardId import registrationCardId

ITEM_BOX_RE = re.compile("^(item_box(_text)*)$")
LEVEL_OR_LINK_RE = re.compile("(レベル|リンク)")


def registrationCard(soup):
    names = readNames(soup)
    card_dict = {"card_name": names[0], "ruby": names[1], "english_name": names[2]}
    card = Card.objects.filter(card_name=card_dict["card_name"]).first()
    if card is not None:
        registrationCardId(soup, card)
        return
    table = soup.find("table", id="details")
    divs = table.find_all("div", class_=ITEM_BOX_RE)
    for div in divs:
        item_title = div.select_one(".item_box_title").extract().text.strip()
        brs = div.find_all("br")
        for br in brs:
            br.replace_with("\n")
        card_dict[item_title] = div.text.strip()
    if "効果" in card_dict:
        card = registrationMagicOrTrap(card_dict)
    else:
        if card_dict["攻撃力"] == '?':
            card_dict["攻撃力"] = -1
        if card_dict["守備力"] == '?':
            card_dict["守備力"] = -1
        if "ランク" in card_dict:
            card_dict["レベル"] = card_dict["ランク"]
        if "ペンデュラム" in card_dict["その他項目"]:
            monster = registrationPendulum(card_dict)
        elif "リンク" in card_dict["その他項目"]:
            monster = registrationLink(card_dict)
        else:
            monster = registrationMonster(card_dict)
        card = Card.objects.filter(card_name=monster.card_name).first()
    registrationCardId(soup, card)
    return


def registrationMagicOrTrap(card_dict):
    card = Card(
        card_name=card_dict["card_name"],
        phonetic=card_dict["ruby"],
        english_name=card_dict["english_name"],
        card_effect=card_dict["カードテキスト"]
    )
    card.save()
    card = registrationClassification(card, card_dict["効果"])
    card.save()
    return card


def registrationMonster(card_dict):
    monster = Monster(
        card_name=card_dict["card_name"],
        phonetic=card_dict["ruby"],
        english_name=card_dict["english_name"],
        level=card_dict["レベル"],
        attribute=checkAttribute(card_dict["属性"]),
        type=checkType(card_dict["種族"]),
        attack=card_dict["攻撃力"],
        defence=card_dict["守備力"],
        card_effect=card_dict["カードテキスト"]
    )
    monster.save()
    monster = registrationClassification(monster, card_dict["その他項目"])
    return monster


def registrationPendulum(card_dict):
    pendulum = PendulumMonster(
        card_name=card_dict["card_name"],
        phonetic=card_dict["ruby"],
        english_name=card_dict["english_name"],
        level=card_dict["レベル"],
        attribute=checkAttribute(card_dict["属性"]),
        type=checkType(card_dict["種族"]),
        attack=card_dict["攻撃力"],
        defence=card_dict["守備力"],
        card_effect=card_dict["カードテキスト"],
        scale=card_dict["ペンデュラムスケール"],
        pendulum_effect=card_dict["ペンデュラム効果"]
    )
    pendulum.save()
    pendulum = registrationClassification(pendulum, card_dict["その他項目"])
    return pendulum


def registrationLink(card_dict):
    link = LinkMonster(
        card_name=card_dict["card_name"],
        phonetic=card_dict["ruby"],
        english_name=card_dict["english_name"],
        level=card_dict["リンク"],
        attribute=checkAttribute(card_dict["属性"]),
        type=checkType(card_dict["種族"]),
        attack=card_dict["攻撃力"],
        defence=-2,
        card_effect=card_dict["カードテキスト"],
    )
    link.save()
    link = registrationClassification(link, card_dict["その他項目"])
    return link


def registrationClassification(card, classification):
    classification = classification.split("／")
    for tmp in checkClassification(classification):
        card.classification.add(tmp)
    card.save()
    return card


def checkClassification(classifications):
    return_classifications = []
    for classification in classifications:
        if not CardClassification.objects.filter(classification=classification).exists():
            tmp_classification = CardClassification(classification=classification)
            tmp_classification.save()
            return_classifications.append(tmp_classification)
        else:
            return_classifications.append(CardClassification.objects.filter(classification=classification)[0])
    return return_classifications


def checkAttribute(attribute):
    if not Attribute.objects.filter(attribute=attribute).exists():
        tmp_attribute = Attribute(attribute=attribute)
        tmp_attribute.save()
        return tmp_attribute
    else:
        return Attribute.objects.filter(attribute=attribute)[0]


def checkType(type):
    if not Type.objects.filter(type=type).exists():
        tmp_type = Type(type=type)
        tmp_type.save()
        return tmp_type
    else:
        return Type.objects.filter(type=type)[0]


def readNames(soup):
    h1 = soup.find("h1")
    name = h1.find("span", class_="ruby").next_sibling.strip()
    ruby = h1.find("span", class_="ruby").string
    try:
        english_name = h1.find("span", class_="").string
    except AttributeError:
        english_name = ""
    return name, ruby, english_name
