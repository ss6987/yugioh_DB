from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "yugioh_cardDB/page/index.html"
