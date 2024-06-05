from django.shortcuts import render
from site_concessionaria.models import Carro
from comum.views import TemplateBaseView

# Create your views here.


class ItemList(TemplateBaseView):
    template_name = "cart/item_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['items'] = Carro.objects.all()

        return context
