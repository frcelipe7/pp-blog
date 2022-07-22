from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_register', views.login_register_view, name='login_register_view'),
    path('devocional/id=<int:id>', views.devocional, name='devocional'),
    path('adicionar', views.adicionar, name='adicionar'),
    path('search', views.search, name='search'),
    path('devocionais', views.devocionais, name='devocionais'),
]