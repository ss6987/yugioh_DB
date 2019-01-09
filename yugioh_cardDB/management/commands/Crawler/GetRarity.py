from yugioh_cardDB.models.CardId import Rarity

raritys = Rarity.objects.all()


def getRarity(rarity_string):
    if rarity_string in ["20thシク", "20thシークレット", "20th シークレット"]:
        return raritys.filter(rarity="20thシークレットレア").first()
    elif rarity_string in ["KC レア"]:
        return raritys.filter(rarity="KC").first()
    elif rarity_string in ["KC+UR", "KCウルトラ"]:
        return raritys.filter(rarity="KCウルトラレア").first()
    elif rarity_string in ["KC+R"]:
        return raritys.filter(rarity="KCレア").first()
    elif rarity_string in ["レリーフ", "レリーフレア", "アルティメトレア", "アルティメット(レリーフ)", "アルティメット", "レリ", "Ultimate"]:
        return raritys.filter(rarity="アルティメットレア").first()
    elif rarity_string in ["UR", "ウルトラ", "ウルトラレアカード", "Ultra"]:
        return raritys.filter(rarity="ウルトラレア").first()
    elif rarity_string in ["EXシク", "EXシークレットレア", "エクストラシークレット", "Ex-Secret"]:
        return raritys.filter(rarity="エクストラシークレットレア").first()
    elif rarity_string in ["Collectors"]:
        return raritys.filter(rarity="コレクターズレア").first()
    elif rarity_string in ["ゴールドシークレット"]:
        return raritys.filter(rarity="ゴールドシークレットレア").first()
    elif rarity_string in ["GR", "ゴールトレア", "ゴールドレアカード", "ゴールド", "Gold"]:
        return raritys.filter(rarity="ゴールドレア").first()
    elif rarity_string in ["ウルトラシークレットレア", "Uシク", "シク", "シークレット", "Secret"]:
        return raritys.filter(rarity="シークレットレア").first()
    elif rarity_string in ["SR", "スーパー", "Super"]:
        return raritys.filter(rarity="スーパーレア").first()
    elif rarity_string in ["ノーマルレア", "N", "NR", "ノーレア", "ノーマルカード", "N-Rare"]:
        return raritys.filter(rarity="ノーマル").first()
    elif rarity_string in ["ノーマルパラレル", "Nパラ", "パ", "パラ", "ノーマルパラレルレア", "ノーパラ"]:
        return raritys.filter(rarity="パラレル").first()
    elif rarity_string in ["ウルトラレアパラレル", "URパラ", "ウルトラパラレル", "ウルトラパラレルレア"]:
        return raritys.filter(rarity="パラレルウルトラレア").first()
    elif rarity_string in ["エクストラシークレットレアパラレル", "エクストラシークレットパラレルレア"]:
        return raritys.filter(rarity="パラレルエクストラシークレットレア").first()
    elif rarity_string in ["シークレットレアパラレル", "シクパラ", "シークレットパラレル"]:
        return raritys.filter(rarity="パラレルシークレットレア").first()
    elif rarity_string in ["スーパーレアパラレル", "SRパラ", "スーパーパラレル", "スーパーパラレルレア"]:
        return raritys.filter(rarity="パラレルスーパーレア").first()
    elif rarity_string in []:
        return raritys.filter(rarity="パラレルホログラフィックレア").first()
    elif rarity_string in []:
        return raritys.filter(rarity="パラレルレア").first()
    elif rarity_string in ["ホロ", "ホログラフック", "ホログラフックレア", "ホログラフィック", "Holographic"]:
        return raritys.filter(rarity="ホログラフィックレア").first()
    elif rarity_string in ["ミレニアムレア", "スペシャルパラレル", "Millennium"]:
        return raritys.filter(rarity="ミレニアム").first()
    elif rarity_string in ["ミレニアムウルトラ"]:
        return raritys.filter(rarity="ミレニアムウルトラレア").first()
    elif rarity_string in []:
        return raritys.filter(rarity="ミレニアムゴールドレア").first()
    elif rarity_string in ["ミレニムシークレット"]:
        return raritys.filter(rarity="ミレニアムシークレットレア").first()
    elif rarity_string in ["ミレニアムスーパー"]:
        return raritys.filter(rarity="ミレニアムスーパーレア").first()
    elif rarity_string in ["R", "レ", "レアカード"]:
        return raritys.filter(rarity="レア").first()
    return raritys.filter(rarity=rarity_string).first()
