from django.db.models import Min, Max
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
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
        context['carros'] = Paginator(Carro.objects.all()[:9], 3)

        return context


class ListagemCarrosView(TemplateBaseView):
    template_name = "site_concessionaria/listagem-carros.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        carros = Carro.objects.all()[:20]
        carros_count = carros.count()

        valor_min_max = Carro.objects.aggregate(Min('valorBase'), Max('valorBase'))
        valor_min = valor_min_max['valorBase__min']
        valor_max = valor_min_max['valorBase__max']
        context['valor_min'] = valor_min
        context['valor_max'] = valor_max
        context['valor_media'] = (valor_min + valor_max) / 2
        filtros = [
            Filter(
                name="Marca",
                options=[Option(marca, "checkbox") for marca in Carro.objects.all().values_list('marca', flat=True).distinct()]
            ),
            Filter(
                name="Valor",
                options=[
                    Option("Valor", "slider")
                ]
            ),
            Filter(
                name="Ano",
                options=[Option(ano, "checkbox") for ano in Carro.objects.all().values_list('ano', flat=True).order_by('-ano').distinct()]
            )
        ]

        context['carros'] = carros
        context['carros_count'] = carros_count
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


def filtrar_carros(request):
    if request.htmx:
        carros = Carro.objects.all()

        marcas_selecionadas = []
        anos_selecionados = []
        for id, value in request.POST.items():

            if 'Marca-' in id:
                split = id.split('-')
                marca = split[1]
                marcas_selecionadas.append(marca)
            elif 'Ano-' in id:
                split = id.split('-')
                ano = split[1]
                anos_selecionados.append(ano)
        if marcas_selecionadas:
            carros = carros.filter(marca__in=marcas_selecionadas)

        if anos_selecionados:
            carros = carros.filter(ano__in=anos_selecionados)

        context = dict()
        context['carros'] = carros
        context['carros_count'] = carros.count()

        return render(request, 'site_concessionaria/componentes/carros-filtrados.html', context)
    return HttpResponse(status=400)

class AgendamentoView(TemplateBaseView):
    template_name = 'site_concessionaria/agendamento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
