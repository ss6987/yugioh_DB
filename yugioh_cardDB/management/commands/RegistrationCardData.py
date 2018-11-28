from yugioh_cardDB.models import *


def registrationCard(soup):
    names = readNames(soup)
    table = soup.find("table", id="details")
    titles = table.select(".item_box_title")
    for title in titles:
        title.extract()
    divs = table.find_all("div", class_="item_box")
    text = table.find("div", class_="item_box_text")
    try:
        text.find("br").replace_with("\n")
    except AttributeError:
        pass
    if len(divs) == 1:
        card = registrationMagicOrTrap(names, divs, text)
    else:
        monster = registrationMonster(names, divs, text)
        card = Card.objects.filter(card_name=monster.card_name)[0]
    return card


def registrationMagicOrTrap(names, divs, text):
    card_name = names[0]
    phonetic = names[1]
    english_name = names[2]
    classification = divs[0].text.strip()
    card_effect = text.text.strip()
    card = Card(
        card_name=card_name,
        phonetic=phonetic,
        english_name=english_name,
        card_effect=card_effect
    )
    card.save()
    for tmp in checkClassification([classification]):
        card.classification.add(tmp)
    card.save()
    return card


def registrationMonster(names, divs, text):
    classification = divs[3].text.strip()
    if "ペンデュラム" in classification:
        registrationPendulum(names, divs)
        return
    if "リンク" in classification:
        registrationLink(names, divs)
        return
    card_name = names[0]
    phonetic = names[1]
    english_name = names[2]
    attribute = checkAttribute(divs[0].text.strip())
    level = divs[1].text.strip()
    type = checkType(divs[2].text.strip())
    classification = divs[3].text.strip()
    attack = divs[4].text.strip()
    if attack == '?':
        attack = -1
    defence = divs[5].text.strip()
    if defence == '?':
        defence = -1
    effect = text.text.strip()
    monster = Monster(
        card_name=card_name,
        phonetic=phonetic,
        english_name=english_name,
        level=level,
        attribute=attribute,
        type=type,
        attack=attack,
        defence=defence,
        card_effect=effect
    )
    monster.save()
    classification = classification.split("／")
    for tmp in checkClassification(classification):
        monster.classification.add(tmp)
    monster.save()
    return monster


def registrationPendulum(names, divs):
    print("OK")


def registrationLink(names, divs):
    print("OK")


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
