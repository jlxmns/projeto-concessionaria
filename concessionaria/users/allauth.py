from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import Group
from django.urls import reverse


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return reverse('site_concessionaria:home')

    def get_signup_redirect_url(self, request):
        return reverse('site_concessionaria:home')

