from lzma import FORMAT_ALONE
from django import forms
from .models import Pessoa
from .forms import PessoaForm

class PessoaForm(forms.ModelForm):
    class Meta:
        models = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativo']
        
class ListaCreateView (CreateView):
    modele = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'   #Aqui esta direcionando o usuario para pagina de Pessoas