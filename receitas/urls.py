from django.urls import path
from .           import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:receita_id>', view=views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]
