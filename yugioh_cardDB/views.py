from django.views.generic import TemplateView, FormView, ListView, DetailView
from yugioh_cardDB.forms import SearchForm
from yugioh_cardDB.models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import timedelta, date
from yugioh_cardDB.management.commands.ReplaceName import replaceName

# Create your views here.

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


class IndexView(TemplateView):
    template_name = "yugioh_cardDB/page/index.html"


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


class PackDetailView(DetailView):
    model = Pack
    template_name = "yugioh_cardDB/page/pack_detail.html"
    queryset = Pack.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards = []
        for card_id in context["pack"].get_recording_cards():
            cards.append(card_id.card_name.get_monster())
        context["cards"] = cards
        return context


class CardDetailView(DetailView):
    model = Card
    template_name = "yugioh_cardDB/page/card_detail.html"
    queryset = Card.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = context["card"]
        context["card"] = card.get_monster()
        context["price_data"] = card.get_price_data()
        context["classification"] = card.get_monster().get_type()
        return context


class SearchView(TemplateView):
    template_name = "yugioh_cardDB/page/card_search.html"


class SearchResultView(ListView):
    model = Card
    template_name = "yugioh_cardDB/page/search_result.html"
    queryset = Card.objects.all()
    paginate_by = 50

    def get_queryset(self):
        select = self.request.GET["name_or_all"]
        search_string = self.request.GET["search_text"]
        replace_search = replaceName(search_string)
        if 'name' in select:
            return Card.objects.filter(Q(card_name__icontains=search_string) | Q(phonetic__icontains=search_string) |
                                       Q(search_name__icontains=replace_search) | Q(search_phonetic__icontains=replace_search))
        elif "all":
            pendulum_monster = PendulumMonster.objects.filter(pendulum_effect__icontains=search_string).values_list(
                "card_name")

            card = Card.objects.filter(
                Q(card_name__icontains=search_string) |
                Q(phonetic__icontains=search_string) |
                Q(search_name__icontains=replace_search) |
                Q(search_phonetic__icontains=replace_search) |
                Q(english_name__icontains=search_string) |
                Q(card_effect__icontains=search_string) |
                Q(card_name__in=pendulum_monster)
            )
            return card
        else:
            return Card.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards = []
        for card in context["card_list"]:
            cards.append(card.get_monster())
        request = self.request.GET.copy()
        try:
            request.pop('page')
        except KeyError:
            pass

        context["page_list"] = self.create_page_list(context)
        context["card_list"] = cards
        context["query_string"] = request.urlencode()
        return context

    @staticmethod
    def create_page_list(context):
        page_range = context["page_obj"].paginator.page_range
        current_page = context["page_obj"].number
        if len(page_range) >= 10:
            if current_page - 5 >= 0 and current_page + 5 <= page_range.stop:
                return range(current_page - 4, current_page + 5)
            elif current_page - 5 < 0:
                return range(1, 10)
            else:
                return range(page_range.stop - 9, page_range.stop)
        else:
            return page_range
