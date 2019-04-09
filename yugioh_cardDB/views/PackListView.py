from django.views.generic import ListView
from yugioh_cardDB.models.Pack import PackClassification


PACK_CLASSIFICATIONS = [
    "第10期",
    "第9期",
    "第8期",
    "第7期",
    "第6期",
    "第5期",
    "第4期",
    "第3期",
    "第2期",
    "第1期",
    "デュエルターミナル",
    "ストラクチャーデッキ",
    "デュエリストパック",
    "BOOSTER",
    "再販カード",
    "特別パック",
    "V JUMP EDITION",
    "LIMITED EDITION",
    "PREMIUM PACK",
    "スターターデッキ",
    "ザ・ヴァリュアブル・ブック",
    "雑誌",
    "コミック",
    "書籍・DVD",
    "ゲーム・攻略本",
    "トーナメントパック",
    "イベント",
    "その他",
]


class PackListView(ListView):
    model = PackClassification
    context_object_name = "pack_classification"
    template_name = "yugioh_cardDB/page/pack_list.html"

    def get_queryset(self):
        pack_classification = PackClassification.objects.all()
        result = []
        for text in PACK_CLASSIFICATIONS:
            result.append(pack_classification.filter(pack_classification=text).first())
        return result
