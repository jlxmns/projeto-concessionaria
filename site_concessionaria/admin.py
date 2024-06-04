from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from unfold.admin import ModelAdmin

from site_concessionaria.models import *

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua', 'numero', 'cidade', 'estado', 'cep']
    search_fields = ['rua', 'numero', 'cidade', 'estado', 'cep']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefone']
    search_fields = ['user__username', 'telefone']

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'ano', 'marca', 'valorBase', 'ativo']
    search_fields = ['modelo', 'ano', 'marca']
    list_filter = ['marca', 'ativo']

@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'carro', 'arquivo']
    search_fields = ['nome', 'carro__modelo']
    list_filter = ['carro']

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'endereco']
    search_fields = ['nome', 'telefone']
    list_filter = ['endereco']

@admin.register(Agendamentos)
class AgendamentosAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'loja', 'dataHoraAgendamento']
    search_fields = ['cliente__user__username', 'loja__nome']
    list_filter = ['loja']

@admin.register(Simulacao)
class SimulacaoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'nome', 'precoFinal']
    search_fields = ['cliente__user__first_name' + 'cliente__user__last_name', 'nome']
    list_filter = ['cliente']

@admin.register(CarroRecurso)
class CarroRecursoAdmin(admin.ModelAdmin):
    list_display = ['simulacao', 'carro', 'recurso']
    search_fields = ['carro' + 'simulacao', 'recurso']
    list_filter = ['carro', 'recurso']


