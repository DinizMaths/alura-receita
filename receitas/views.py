from django.shortcuts import get_object_or_404, render
from .models          import Receita

def index(request):
  receitas = Receita.objects.all()

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
