from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from main.models import Home


class HomeView(TemplateView):
    model = Home
    template_name = 'layouts/base.html'
    


