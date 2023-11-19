from django.shortcuts import render
from about.models import About
from django.views.generic import ListView

app_name = 'about'

class AboutView(ListView):
    model = About
    template_name = 'about.html'
