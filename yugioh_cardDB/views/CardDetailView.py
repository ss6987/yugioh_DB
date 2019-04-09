from django.views.generic import DetailView
from yugioh_cardDB.models import Card


class CardDetailView(DetailView):
    model = Card
    template_name = "yugioh_cardDB/page/card_detail.html"
    queryset = Card.objects.prefetch_related().all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = context["card"]
        price_date = []
        shop_urls = card.shop_url.all()
        last_price = shop_urls.order_by("-price__registration_date").first().price.last()
        print(last_price)
        # for shop_url in shop_urls:
        #     now_price = shop_url.price.filter(registration_date=last_price.registration_date).exclude(price=None).last()
        #     if now_price:
        #         price_date.append(now_price)
        # context["price_date"] = price_date
        return context
