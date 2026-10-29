# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('indicadores/', views.indicadores, name='indicadores'),
]