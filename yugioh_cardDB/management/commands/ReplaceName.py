from jaconv import hira2kata, z2h
import re

trans_table = str.maketrans({
    "ガ": "カ", "ギ": "キ", "グ": "ク", "ゲ": "ケ", "ゴ": "コ",
    "ザ": "サ", "ジ": "シ", "ズ": "ス", "ゼ": "セ", "ゾ": "ソ",
    "ダ": "タ", "ヂ": "チ", "ヅ": "ツ", "デ": "テ", "ド": "ト",
    "バ": "ハ", "ビ": "ヒ", "ブ": "フ", "ベ": "ヘ", "ボ": "ホ",
    "パ": "ハ", "ピ": "ヒ", "プ": "フ", "ぺ": "ヘ", "ポ": "ホ"
})
replace_string = "[^ぁ-んァ-ンa-zA-Z0-9一-龠０-９]+"


def replaceName(string):
    string = hira2kata(z2h(string, digit=True, kana=False))
    string = string.replace("ヴァ", "バ").replace("ヴィ", "ビ").replace("ヴ", "ブ").replace("ヴェ", "ベ").replace("ヴォ", "ボ")
    string = string.translate(trans_table)
    string = re.sub(replace_string, "", string)
    return string
