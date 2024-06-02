from django.templatetags.static import static
from comum.views import TemplateBaseView


import os

# Create your views here.

class HomeView(TemplateBaseView):
    template_name = "site_concessionaria/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        img1 = {'link': static('images/suzukivitara.jpg'), 'desc': 'Suzuki Vitara'}
        img2 = {'link': static('images/toyotafortuner.jpg'), 'desc': 'Toyota Fortuner'}
        img3 = {'link': static('images/toyotaprius.jpg'), 'desc': 'Toyota Prius'}
        img4 = {'link': static('images/yaris3.png'), 'desc': 'Toyota Yaris'}

        context['imagens'] = [img1, img2, img3, img4]
        context['teste'] = "teste"
        # context['cards'] = queryset que contém os 3 carros mais recentes talvez?

        return context
