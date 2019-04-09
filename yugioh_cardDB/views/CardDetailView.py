from django.views.generic import DetailView
from yugioh_cardDB.models import Card


class CardDetailView(DetailView):
    model = Card
    template_name = "yugioh_cardDB/page/card_detail.html"
    queryset = Card.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = context["card"]
        price_data = []
        shop_urls = card.shop_url.select_related("rarity","search_page").all().order_by("rarity__order_rank")
        raritys = shop_urls.values_list("rarity",flat=True)
        for rarity in raritys:
            price_dict = {
                "rarity":rarity,
                "shop_urls":shop_urls.filter(rarity__rarity=rarity)
            }
            price_data.append(price_dict)
        context["price_data"] = price_data
        return context
