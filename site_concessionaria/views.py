from django.templatetags.static import static
from comum.views import TemplateBaseView


import os

# Create your views here.

class HomeView(TemplateBaseView):
    template_name = "site_concessionaria/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        img1 = static('images/suzukivitara.jpg')
        img2 = static('images/toyotafortuner.jpg')
        img3 = static('images/toyotaprius.jpg')
        img4 = static('images/yaris3.png')
        context['imagens'] = [img1, img2, img3, img4]

        context['teste'] = "teste"

        return context


class CarSearch(TemplateBaseView):
    template_name = "site_concessionaria/carSearch.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        img1 = static('images/suzukivitara.jpg')
        img2 = static('images/toyotafortuner.jpg')
        img3 = static('images/toyotaprius.jpg')
        img4 = static('images/yaris3.png')
        context['imagens'] = [img1, img2, img3, img4]

        context['teste'] = "teste"

        return context



class MapView(TemplateBaseView):
    template_name = "site_concessionaria/mapSearch.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        img1 = static('images/suzukivitara.jpg')
        img2 = static('images/toyotafortuner.jpg')
        img3 = static('images/toyotaprius.jpg')
        img4 = static('images/yaris3.png')
        context['imagens'] = [img1, img2, img3, img4]

        context['teste'] = "teste"

        return context