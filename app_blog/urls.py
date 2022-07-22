from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('devocional/id=<int:id>', views.devocional, name='devocional'),
    path('adicionar', views.adicionar, name='adicionar'),
    path('search', views.search, name='search'),
    path('devocionais', views.devocionais, name='devocionais'),
]