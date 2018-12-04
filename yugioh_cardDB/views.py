from django.views.generic import TemplateView, FormView, ListView
from yugioh_cardDB.forms import SearchForm
from yugioh_cardDB.models import *


# Create your views here.

class IndexView(TemplateView):
    template_name = "yugioh_cardDB/page/index.html"


class PackListView(ListView):
    model = PackClassification
    context_object_name = "pack_classification"
    template_name = "yugioh_cardDB/page/pack_list.html"


class PackDetailView(ListView):
    model = Pack
    context_object_name = "pack"
    template_name = "yugioh_cardDB/page/pack_detail.html"
    queryset = Pack.objects.all()

    def get_queryset(self):
        results = self.model.objects.all()
        results = results.filter(pack_name=self.kwargs["pack_name"]).first()
        return results

