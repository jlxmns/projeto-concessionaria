from django.shortcuts import render
from django.contrib import admin
from django.views.generic import TemplateView
from unfold.settings import get_config
from typing import Any, Callable, Optional, Union

# Create your views here.
class TemplateBaseView(TemplateView):
   settings_name = "UNFOLD"
   template_name = 'admin/base_site.html'
   def get_context_data(self, **kwargs):
      retorno = super().get_context_data(**kwargs)
      retorno['pagina'] = 'view_base_default.html'
      retorno['available_apps'] = admin.site.get_app_list(self.request)
      retorno['site_header'] = 'Portal de Sistemas da JFPB'

      ## DEPENDÊNCIAS UNFOLD TEMPLATE
      retorno['is_nav_sidebar_enabled'] = True
      retorno['sidebar_navigation'] = True
      retorno['sidebar_show_search'] = True
      retorno['colors'] = get_config(self.settings_name)["COLORS"]
      retorno['styles'] = [self._get_value(style, self.request) for style in get_config(self.settings_name)["STYLES"]]
      retorno['scripts'] = [self._get_value(script, self.request) for script in get_config(self.settings_name)["SCRIPTS"]]
      retorno['logo'] = self._get_value(get_config(self.settings_name)["SIDEBAR"].get("logo"), self.request)
      retorno['icon'] = self._get_value(get_config(self.settings_name)["SITE_ICON"], self.request)
      retorno['has_permission'] = self.request.user.is_authenticated

      return retorno

   def _get_value(
           self, instance: Union[str, Callable, None], *args: Any
   ) -> Optional[str]:
      if instance is None:
         return None

      if isinstance(instance, str):
         return instance

      return instance(*args)
