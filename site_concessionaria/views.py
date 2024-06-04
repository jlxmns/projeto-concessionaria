from django.templatetags.static import static
from comum.views import TemplateBaseView

import os

from site_concessionaria.models import Carro


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


class ListagemCarrosView(TemplateBaseView):
    template_name = "site_concessionaria/listagem-carros.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filtros = [
            Filter(
                name="Veículos",
                options=[
                    Option("Carros", "checkbox"),
                    Option("Elétricos", "checkbox"),
                    Option("SUV", "checkbox"),
                    Option("Minivan", "checkbox"),
                ]),
            Filter(
                name="Valor",
                options=[
                    Option("Valor", "slider")
                ]
            ),
            Filter(
                name="Ano",
                options=[
                    Option("2022", type="checkbox"),
                    Option("2023", type="checkbox"),
                    Option("2024", type="checkbox"),
                    Option("2025", type="checkbox"),
                ]
            )
        ]

        context['carros'] = Carro.objects.all()[:20]
        context['filtros'] = filtros

        return context


class Filter:
    def __init__(self, name, options):
        self.name = name
        self.options = options


class Option:
    def __init__(self, display_name, type):
        self.display_name = display_name
        self.type = type.lower()

    def is_checkbox(self):
        return self.type == 'checkbox'

    def is_slider(self):
        return self.type == 'slider'


class CarSearch(TemplateBaseView):
    template_name = "site_concessionaria/car_detail.html"

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

class CarDetail(TemplateBaseView):
    template_name = "site_concessionaria/car_detail.html"

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       carro = kwargs.get("car_id")
       carro = Carro.objects.filter(id=carro).first()
       context["car"] = carro
       return context