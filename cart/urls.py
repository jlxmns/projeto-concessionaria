from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.ItemList.as_view(), name="item-list"),
]