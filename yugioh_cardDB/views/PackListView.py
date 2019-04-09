from django.views.generic import ListView
from yugioh_cardDB.models.Pack import PackClassification, Pack
from django.db.models import Prefetch


class PackListView(ListView):
    model = PackClassification
    context_object_name = "pack_classification"
    template_name = "yugioh_cardDB/page/pack_list.html"
    queryset = PackClassification.objects.all().prefetch_related(
        Prefetch("packs", queryset=Pack.objects.all().order_by("-release_date"))).order_by("order_rank")
