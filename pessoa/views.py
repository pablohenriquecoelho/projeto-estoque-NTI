from django.shortcuts import render
from django.views.generic import ListView
from .models import pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):
    model = pessoa
    queryset = pessoa.objects.all().order_by('nome_completo') 

class PessoaCreateView(CreateView) :
    model = pessoa
    form_class = PessoaForm
    sucess_url = '/pessoas/'
