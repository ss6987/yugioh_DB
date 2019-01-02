from yugioh_cardDB.models.CardId import Rarity

raritys = Rarity.objects.all()


def getRarity(rarity_string):
    if "20thシク" == rarity_string:
        return raritys.filter(rarity="20thシークレットレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="KC").first()
    elif "KC+UR" == rarity_string:
        return raritys.filter(rarity="KCウルトラレア").first()
    elif "KC+R" == rarity_string:
        return raritys.filter(rarity="KCレア").first()
    elif "レリーフ" == rarity_string or "レリーフレア" == rarity_string or "アルティメトレア" == rarity_string or "アルティメット(レリーフ)" == rarity_string or "アルティメット" == rarity_string or "レリ" == rarity_string:
        return raritys.filter(rarity="アルティメットレア").first()
    elif "UR" == rarity_string or "ウルトラ" == rarity_string:
        return raritys.filter(rarity="ウルトラレア").first()
    elif "EXシク" == rarity_string or "EXシークレットレア" == rarity_string:
        return raritys.filter(rarity="エクストラシークレットレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="コレクターズレア").first()
    elif "ゴールドシークレット" == rarity_string:
        return raritys.filter(rarity="ゴールドシークレットレア").first()
    elif "GR" == rarity_string or "ゴールトレア" == rarity_string:
        return raritys.filter(rarity="ゴールドレア").first()
    elif "ウルトラシークレットレア" == rarity_string or "Uシク" == rarity_string or "シク" == rarity_string or "シークレット" == rarity_string:
        return raritys.filter(rarity="シークレットレア").first()
    elif "SR" == rarity_string or rarity_string == "スーパー":
        return raritys.filter(rarity="スーパーレア").first()
    elif "ノーマルレア" == rarity_string or "N" == rarity_string or "NR" == rarity_string:
        return raritys.filter(rarity="ノーマル").first()
    elif "ノーマルパラレル" == rarity_string or "Nパラ" == rarity_string or "パ" == rarity_string or "パラ" == rarity_string:
        return raritys.filter(rarity="パラレル").first()
    elif "ウルトラレアパラレル" == rarity_string or "URパラ" == rarity_string:
        return raritys.filter(rarity="パラレルウルトラレア").first()
    elif "エクストラシークレットレアパラレル" == rarity_string:
        return raritys.filter(rarity="パラレルエクストラシークレットレア").first()
    elif "シークレットレアパラレル" == rarity_string or "シクパラ" == rarity_string:
        return raritys.filter(rarity="パラレルシークレットレア").first()
    elif "スーパーレアパラレル" == rarity_string or "SRパラ" == rarity_string:
        return raritys.filter(rarity="パラレルスーパーレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="パラレルホログラフィックレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="パラレルレア").first()
    elif "ホロ" == rarity_string:
        return raritys.filter(rarity="ホログラフィックレア").first()
    elif "ミレニアムレア" == rarity_string or "スペシャルパラレル" == rarity_string:
        return raritys.filter(rarity="ミレニアム").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="ミレニアムウルトラレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="ミレニアムゴールドレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="ミレニアムシークレットレア").first()
    elif "///" == rarity_string:
        return raritys.filter(rarity="ミレニアムスーパーレア").first()
    elif "R" == rarity_string or "レ" == rarity_string:
        return raritys.filter(rarity="レア").first()
    return raritys.filter(rarity=rarity_string).first()
