from django.contrib import admin
from .models import OrderItem, Order
from unfold.admin import ModelAdmin

# Register your models here.


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass
