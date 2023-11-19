from django.urls import path
from main.views import HomeView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
