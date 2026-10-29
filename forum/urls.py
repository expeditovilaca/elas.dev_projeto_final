from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_lista, name='forum_lista'),
    path('novo/', views.criar_postagem, name='criar_postagem'), # Nova rota
    path('<int:pk>/', views.forum_detalhe, name='forum_detalhe'),
]