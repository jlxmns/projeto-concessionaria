from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

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


@admin.register(Carro)
class CarroAdmin(ModelAdmin):
    list_display = ['modelo', 'ano', 'marca', 'valorBase', 'ativo']
    search_fields = ['modelo', 'ano', 'marca']
    list_filter = ['marca', 'ativo']

@admin.register(Anexo)
class AnexoAdmin(ModelAdmin):
    list_display = ['nome', 'get_carro', 'get_arquivo']
    search_fields = ['nome', 'carro__modelo']
    list_filter = ['carro']

    @admin.display(description="Carro")
    def get_carro(self, obj):
        print(obj)
        carro_id = obj.carro.id
        url = reverse('admin:site_concessionaria_carro_change', args=[carro_id])

        return format_html(f"<a href='{url}'>Ver Carro</a>")

    @admin.display(description="Arquivo")
    def get_arquivo(self, obj):
        url = (
                f"<a class='flex-auto items-center justify-center' href='{obj.arquivo.url}'>"
                f"<span class='material-symbols-outlined md-18 pt-0.5 mr-3 w-4.5'>search</span>"
                "</a>"
        )

        return format_html(url)

@admin.register(Recurso)
class RecursoAdmin(ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']

@admin.register(Loja)
class LojaAdmin(ModelAdmin):
    list_display = ['nome', 'telefone', 'endereco']
    search_fields = ['nome', 'telefone']
    list_filter = ['endereco']

@admin.register(Agendamentos)
class AgendamentosAdmin(ModelAdmin):
    list_display = ['cliente', 'loja', 'dataHoraAgendamento']
    search_fields = ['cliente__user__username', 'loja__nome']
    list_filter = ['loja']