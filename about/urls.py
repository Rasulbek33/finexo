from django.urls import path
from about.views import AboutView

app_name = 'about'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),

]