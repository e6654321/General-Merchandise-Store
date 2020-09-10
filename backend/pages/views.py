from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class RegCustomerPageView(TemplateView):
    template_name = 'regCustomer.html'

class RegProductPageView(TemplateView):
    template_name = 'regProduct.html'

class TableCustomerPageView(TemplateView):
    template_name = 'tableCustomer.html'

class TableProductPageView(TemplateView):
    template_name = 'tableProduct.html'

class ErrorPageView(TemplateView):
    template_name = '404.html'