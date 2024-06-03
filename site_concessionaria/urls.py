from django.urls import path
from . import views

app_name = 'site_concessionaria'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.CarSearch.as_view(), name='car_search'),
    path('map', views.MapView.as_view(), name='map_view'),
]
