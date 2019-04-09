from django.views.generic import TemplateView


class SearchView(TemplateView):
    template_name = "yugioh_cardDB/page/card_search.html"
