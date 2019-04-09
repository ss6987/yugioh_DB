from django.views.generic import DetailView
from yugioh_cardDB.models import Pack


class PackDetailView(DetailView):
    model = Pack
    template_name = "yugioh_cardDB/page/pack_detail.html"
    queryset = Pack.objects.prefetch_related("recording_card").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards = []
        for card_id in context["pack"].get_recording_cards():
            strings = []
            for classification in card_id.card_name.classification.all():
                strings.append(str(classification))
            strings = "/".join(strings)

            if "リンク" in strings:
                card = card_id.card_name.monster.linkmonster
            elif "ペンデュラム" in strings:
                card = card_id.card_name.monster.pendulummonster
            elif not ("魔法" in strings or "罠" in strings):
                card = card_id.card_name.monster
            else:
                card = card_id.card_name
            cards.append(card)
        context["cards"] = cards
        return context
