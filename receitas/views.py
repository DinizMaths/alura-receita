from django.shortcuts import render

import receitas

def index(request):
  return render(request, 'index.html')

def receita(request):
  return render(request, 'receita.html')
