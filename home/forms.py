from django.forms import ModelForm
from .models import *

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cnpj', 'inscricaoestadual']

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['ddd','telefone','tipo']
                  

class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade', 'status', 'tipo',
                  ]