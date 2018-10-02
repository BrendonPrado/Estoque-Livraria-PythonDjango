from django import forms
from django.db.models import Avg, Q
from estoque.models import Autor,Livro, Editora, Loja



class LivroSearchForm(forms.Form):
    nome = forms.CharField(required=False)

    def get_queryset(self):
        q = Q()
        if self.is_valid():
            if self.cleaned_data.get('nome'):
                q = q & Q(nome__icontains=self.cleaned_data['nome'])
        return Livro.objects.filter(q)




class AutorSearchForm(forms.Form):
    nome = forms.CharField(required=False)

    def get_queryset(self):
        q = Q()
        if self.is_valid():
            if self.cleaned_data.get('nome'):
                q = q & Q(nome__icontains=self.cleaned_data['nome'])
        return Autor.objects.filter(q)

class EditoraSearchForm(forms.Form):
    nome = forms.CharField(required=False)

    def get_queryset(self):
        q = Q()
        if self.is_valid():
            if self.cleaned_data.get('nome'):
                q = q & Q(nome__icontains=self.cleaned_data['nome'])
        return Editora.objects.filter(q)

class LojaSearchForm(forms.Form):
    nome = forms.CharField(required=False)

    def get_queryset(self):
        q = Q()
        if self.is_valid():
            if self.cleaned_data.get('nome'):
                q = q & Q(nome__icontains=self.cleaned_data['nome'])
        return Loja.objects.filter(q)