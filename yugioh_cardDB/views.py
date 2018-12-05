from django.views.generic import TemplateView, FormView, ListView, DetailView
from yugioh_cardDB.forms import SearchForm
from yugioh_cardDB.models import *


# Create your views here.

class IndexView(TemplateView):
    template_name = "yugioh_cardDB/page/index.html"


class PackListView(ListView):
    model = PackClassification
    context_object_name = "pack_classification"
    template_name = "yugioh_cardDB/page/pack_list.html"


class PackDetailView(DetailView):
    model = Pack
    template_name = "yugioh_cardDB/page/pack_detail.html"
    queryset = Pack.objects.all()


class CardDetailView(DetailView):
    model = Card
    template_name = "yugioh_cardDB/page/card_detail.html"
    queryset = Card.objects.all()


class SearchView(FormView):
    form_class = SearchForm
    template_name = "yugioh_cardDB/page/card_search.html"
    success_url = "yugioh_cardDB/result"
