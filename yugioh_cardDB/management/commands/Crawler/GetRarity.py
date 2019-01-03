from yugioh_cardDB.models.CardId import Rarity

raritys = Rarity.objects.all()


def getRarity(rarity_string):
    if ["20thシク", "20thシークレット"] in rarity_string:
        return raritys.filter(rarity="20thシークレットレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="KC").first()
    elif ["KC+UR", "KCウルトラ"] in rarity_string:
        return raritys.filter(rarity="KCウルトラレア").first()
    elif ["KC+R"] in rarity_string:
        return raritys.filter(rarity="KCレア").first()
    elif ["レリーフ", "レリーフレア", "アルティメトレア", "アルティメット(レリーフ)", "アルティメット", "レリ"] in rarity_string:
        return raritys.filter(rarity="アルティメットレア").first()
    elif ["UR", "ウルトラ", "ウルトラレアカード"] in rarity_string:
        return raritys.filter(rarity="ウルトラレア").first()
    elif ["EXシク", "EXシークレットレア","エクストラシークレット"] in rarity_string:
        return raritys.filter(rarity="エクストラシークレットレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="コレクターズレア").first()
    elif ["ゴールドシークレット"] in rarity_string:
        return raritys.filter(rarity="ゴールドシークレットレア").first()
    elif ["GR", "ゴールトレア", "ゴールドレアカード"] in rarity_string:
        return raritys.filter(rarity="ゴールドレア").first()
    elif ["ウルトラシークレットレア", "Uシク", "シク", "シークレット"] in rarity_string:
        return raritys.filter(rarity="シークレットレア").first()
    elif ["SR", "スーパー"] in rarity_string:
        return raritys.filter(rarity="スーパーレア").first()
    elif ["ノーマルレア", "N", "NR"] in rarity_string:
        return raritys.filter(rarity="ノーマル").first()
    elif ["ノーマルパラレル", "Nパラ", "パ", "パラ", "ノーマルパラレルレア", "ノーパラ"] in rarity_string:
        return raritys.filter(rarity="パラレル").first()
    elif ["ウルトラレアパラレル", "URパラ", "ウルトラパラレル"] in rarity_string:
        return raritys.filter(rarity="パラレルウルトラレア").first()
    elif ["エクストラシークレットレアパラレル"] in rarity_string:
        return raritys.filter(rarity="パラレルエクストラシークレットレア").first()
    elif ["シークレットレアパラレル", "シクパラ","シークレットパラレル"] in rarity_string:
        return raritys.filter(rarity="パラレルシークレットレア").first()
    elif ["スーパーレアパラレル", "SRパラ"] in rarity_string:
        return raritys.filter(rarity="パラレルスーパーレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="パラレルホログラフィックレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="パラレルレア").first()
    elif ["ホロ","ホログラフック"] in rarity_string:
        return raritys.filter(rarity="ホログラフィックレア").first()
    elif ["ミレニアムレア", "スペシャルパラレル"] in rarity_string:
        return raritys.filter(rarity="ミレニアム").first()
    elif ["ミレニアムウルトラ"] in rarity_string:
        return raritys.filter(rarity="ミレニアムウルトラレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="ミレニアムゴールドレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="ミレニアムシークレットレア").first()
    elif ["ミレニアムスーパー"] in rarity_string:
        return raritys.filter(rarity="ミレニアムスーパーレア").first()
    elif ["R", "レ"] in rarity_string:
        return raritys.filter(rarity="レア").first()
    return raritys.filter(rarity=rarity_string).first()
