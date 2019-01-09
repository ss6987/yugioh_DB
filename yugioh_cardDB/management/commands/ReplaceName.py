from jaconv import hira2kata, z2h, h2z
import re

trans_table = str.maketrans({
    "ガ": "カ", "ギ": "キ", "グ": "ク", "ゲ": "ケ", "ゴ": "コ",
    "ザ": "サ", "ジ": "シ", "ズ": "ス", "ゼ": "セ", "ゾ": "ソ",
    "ダ": "タ", "ヂ": "チ", "ヅ": "ツ", "デ": "テ", "ド": "ト",
    "バ": "ハ", "ビ": "ヒ", "ブ": "フ", "ベ": "ヘ", "ボ": "ホ",
    "パ": "ハ", "ピ": "ヒ", "プ": "フ", "ぺ": "ヘ", "ポ": "ホ"
})
trans_string_table = [
    ["ヴァ", "バ"],
    ["ヴィ", "ビ"],
    ["ヴ", "ブ"],
    ["ヴェ", "ベ"],
    ["ヴォ", "ボ"],
    ["Ⅰ", "I"],
    ["Ⅱ", "II"],
    ["Ⅲ", "III"],
    ["Ⅳ", "IV"],
    ["Ⅴ", "V"],
    ["Ⅵ", "VI"],
    ["Ⅶ", "VII"],
    ["Ⅷ", "VIII"],
    ["Ⅸ", "IX"],
    ["Ⅹ", "X"],
]
replace_string = "[^ぁ-んァ-ンa-zA-Z0-9一-龠０-９ΛγΩεαβδΖ]+"


def replaceName(string):
    string = hira2kata(z2h(string, digit=True, kana=False))
    for tmp_string in trans_string_table:
        string = string.replace(tmp_string[0], tmp_string[1])
    string = string.translate(trans_table)
    string = re.sub(replace_string, "", string)
    return string


def replaceSymbol(string):
    if "アルカナフォース" in string:
        return string[string.index("－") + 1:]
    string = re.sub("[－ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ]+", "", string)
    return string


def replaceh2z(string):
    return h2z(string, ascii=True, digit=True)


def replacez2h(string):
    return z2h(string,kana=False ,ascii=True, digit=True)
