from django.views.generic import DetailView
from yugioh_cardDB.models import Pack


class PackDetailView(DetailView):
    model = Pack
    template_name = "yugioh_cardDB/page/pack_detail.html"
    queryset = Pack.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pack = context["pack"]
        recording_cards = pack.recording_card.select_related("card_name").prefetch_related("card_name__classification",
                                                                                           "card_name__monster",
                                                                                           "card_name__monster__classification",
                                                                                           "card_name__monster__linkmonster",
                                                                                           "card_name__monster__linkmonster__classification",
                                                                                           "card_name__monster__pendulummonster",
                                                                                           "card_name__monster__pendulummonster__classification").all()
        cards = []
        for card in recording_cards:
            cards.append(card.card_name.get_monster())
        context["cards"] = cards
        return context
