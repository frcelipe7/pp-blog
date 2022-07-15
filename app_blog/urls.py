from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devocional/id=<int:id>', views.devocional, name='devocional'),
]