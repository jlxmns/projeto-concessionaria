from django.urls import path
from . import views

app_name = 'site_concessionaria'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.HomeView.as_view(), name='search'),
    path('listagem-carros', views.ListagemCarrosView.as_view(), name='listagem-carros'),
]
