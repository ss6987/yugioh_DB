from django.views.generic import ListView
from django.db.models import Q
from yugioh_cardDB.models.Card import Card
from yugioh_cardDB.models.Monster import PendulumMonster
from yugioh_cardDB.management.commands.ReplaceName import replaceName


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
            card = Card.objects \
                .prefetch_related("classification",
                                  "monster",
                                  "monster__classification",
                                  "monster__pendulummonster",
                                  "monster__pendulummonster__classification",
                                  "monster__linkmonster",
                                  "monster__linkmonster__classification") \
                .filter(Q(card_name__icontains=search_string) |
                        Q(phonetic__icontains=search_string) |
                        Q(search_name__icontains=replace_search) |
                        Q(search_phonetic__icontains=replace_search))
            return card
        elif "all":
            pendulum_monster = PendulumMonster.objects.filter(pendulum_effect__icontains=search_string).values_list("card_name")
            card = Card.objects \
                .prefetch_related("classification",
                                  "monster",
                                  "monster__classification",
                                  "monster__pendulummonster",
                                  "monster__pendulummonster__classification",
                                  "monster__linkmonster",
                                  "monster__linkmonster__classification") \
                .filter(
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
            card = Card.objects.prefetch_related("classification",
                                                 "monster",
                                                 "monster__classification",
                                                 "monster__pendulummonster",
                                                 "monster__pendulummonster__classification",
                                                 "monster__linkmonster",
                                                 "monster__linkmonster__classification").all()
            return card

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
