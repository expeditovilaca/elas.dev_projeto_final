# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def pesquisa(request):
    return render(request, 'core/pesquisa.html')

def indicadores(request):
    return render(request, 'core/indicadores.html')