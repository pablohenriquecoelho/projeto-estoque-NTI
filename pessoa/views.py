from django.shortcuts import render
from django.views.generic import ListView
from .models import pessoa

class ListaPessoaView(ListView):
    model = pessoa
    queryset = pessoa.objects.all().order_by('nome_completo') 

