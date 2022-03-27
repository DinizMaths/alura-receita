from django.shortcuts import get_object_or_404, render
from .models          import Receita

def index(request):
  receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

  dados = {
    'receitas': receitas
  }

  return render(request=request, template_name='index.html', context=dados)

def receita(request, receita_id):
  receita = get_object_or_404(Receita, pk=receita_id)

  receita_exibir = {
    'receita': receita
  }

  return render(request, template_name='receita.html', context=receita_exibir)

def buscar(request):
  lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

  if 'buscar' in request.GET:
    nome_a_buscar = request.GET['buscar']

    if buscar:
      lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

  dados = {
    'receitas': lista_receitas
  }

  return render(request, template_name='buscar.html', context=dados)