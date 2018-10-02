from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView, CreateView,
    UpdateView, ListView,TemplateView
)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse,HttpResponse,HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormMixin,ModelFormMixin
from django.db.models import Avg

from estoque.models import Autor, Livro, Editora, Loja,Usuario
from estoque.forms import AutorSearchForm,EditoraSearchForm,LivroSearchForm,LojaSearchForm

class SearchFormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        self.form = self.get_form(self.get_form_class())
        self.object_list = self.form.get_queryset()
        return self.render_to_response(self.get_context_data(object_list=self.object_list, form=self.form))

    def get_form_kwargs(self):
        return {'initial': self.get_initial(), 'data': self.request.GET}


class JsonListMixin(object):
    json_fields = []

    def get(self,request,*args,**kwargs):
        self.object_list = self.get_queryset().values_list(*self.json_fields)
        json_dict ={
            'header':self.json_fields,
            'object_list':list(self.object_list)
        }
        return JsonResponse(json_dict)

class PageInfoMixin(object):
    page_info = None

    def get_page_info(self):
        if self.model:
            return self.model._meta.verbose_name
        return None

    def get_context_data(self,**kwargs):
        if self.page_info is None:
            kwargs['page_info'] = self.get_page_info()
            return super().get_context_data(**kwargs)
 
def index(request):
    if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
    livro_mais_barato = Livro.objects.order_by('-preco').last()
    livro_mais_caro = Livro.objects.order_by('-preco').first()
    livro_preco_medio = Livro.objects.filter().aggregate(Avg('preco')) or 0
    qtd_autores = Autor.objects.count()
    qtd_editoras = Editora.objects.count()
    qtd_livros = Livro.objects.count()
    qtd_lojas = Loja.objects.count()
    return render(request, 'estoque/index.html', {
        'livro_mais_barato': livro_mais_barato,
        'livro_mais_caro': livro_mais_caro,
        'livro_preco_medio': livro_preco_medio.get('preco__avg', 0),
        'qtd_autores': qtd_autores,
        'qtd_editoras': qtd_editoras,
        'qtd_livros': qtd_livros,
        'qtd_lojas': qtd_lojas,
    })

class AutorCreateView(CreateView):
    model = Autor
    fields = '__all__'
    success_url = reverse_lazy('autor-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

    
class AutorListView(PageInfoMixin,ListView):
    model = Autor
    fields = '__all__'

    def get(self,request,*args,**kwargs):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            self.object = None
            return super().get(request,*args,**kwargs)

class AutorUpdateView(UpdateView):
    fields = '__all__'
    model = Autor
    success_url = reverse_lazy('autor-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class AutorSearchFormListView(PageInfoMixin,SearchFormListView):
    form_class = AutorSearchForm
    model = Autor

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)


class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor-list')
    template_name = 'estoque/confirm_delete.html'

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class AutorJsonListView(JsonListMixin,AutorListView):
    json_fields = [
        'nome',
       'idade'
    ]

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)



class LivroCreateView(PageInfoMixin, CreateView):
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('livro-list')  

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)
    
class LivroListView(ListView):
    model = Livro
    fields = '__all__'

    def get(self,request,*args,**kwargs):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            self.object = None
            return super().get(request,*args,**kwargs)

class LivroUpdateView(UpdateView):
    fields = '__all__'
    model = Livro
    success_url = reverse_lazy('livro-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class LivroSearchFormListView(PageInfoMixin,SearchFormListView):
    form_class = LivroSearchForm
    model = Livro

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)


class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('livro-list')
    template_name = 'estoque/confirm_delete.html'

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class LivroJsonListView(JsonListMixin,LivroListView):
    json_fields = [
        'nome',
        'preco',
        'avaliacao',
        'editora__nome',
        'autores__nome',
    ]

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class EditoraListView(ModelFormMixin,ListView):
    model = Editora
    fields = '__all__'

    def get(self,request,*args,**kwargs):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            self.object = None
            return super().get(request,*args,**kwargs)

class EditoraCreateView(CreateView):
    fields = '__all__'
    model = Editora
    success_url = reverse_lazy('editora-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class EditoraSearchFormListView(PageInfoMixin,SearchFormListView):
    form_class = EditoraSearchForm
    model = Editora

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class EditoraUpdateView(UpdateView):
    fields = '__all__'
    model = Editora
    success_url = reverse_lazy('editora-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class EditoraDeleteView(DeleteView):
    model = Editora
    success_url = reverse_lazy('editora-list')
    template_name = 'estoque/confirm_delete.html'

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)


class EditoraJsonListView(JsonListMixin,EditoraListView):
    json_fields = [
        'nome',
        'avaliacao',
    ]

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class LojaListView(ModelFormMixin,ListView):
    model = Loja
    fields = '__all__'

    def get(self,request,*args,**kwargs):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            self.object = None
            return super().get(request,*args,**kwargs)


class LojaCreateView(CreateView):
    fields = '__all__'
    model = Loja
    success_url = reverse_lazy('loja-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class LojaSearchFormListView(PageInfoMixin,SearchFormListView):
    form_class = LojaSearchForm
    model = Loja

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class LojaUpdateView(UpdateView):
    fields = '__all__'
    model = Loja
    success_url = reverse_lazy('loja-list')

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)

class LojaDeleteView(DeleteView):
    model = Loja
    success_url = reverse_lazy('loja-list')
    template_name = 'estoque/confirm_delete.html'

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)


class LojaJsonListView(JsonListMixin,LojaListView):
    json_fields = [
        'nome',
        'quantidade_de_clientes'
    ]

    def get(self,request):
        if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
        else:
            return super().get(request)



def autor_nome_registrado(request):
    if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
    else:
            return super().get(request)

    nome = request.GET.get('nome', None)
    data = {
        'is_taken': Autor.objects.filter(nome__iexact=nome).exists(),
        'message': 'Válido'
    }
    if data['is_taken']:
        data['message'] = 'O Autor já está cadastrado'
    return JsonResponse(data)

def livro_nome_registrado(request):
    if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
    else:
            return super().get(request)
    nome = request.GET.get('nome',None)
    data ={
        'is_taken':Livro.objects.filter(nome__iexact=nome).exists()
    }
    if(data['is_taken']):
        data['message'] = 'O Livro ja esta cadastrado'
    return JsonResponse(data)

def editora_nome_registrado(request):
    if(len(request.session.keys())==0):
            return HttpResponseRedirect('/')
    else:
            return super().get(request)
    nome = request.GET.get('nome',None)
    data ={
        'is_taken':Editora.objects.filter(nome__iexact=nome).exists()
    }
    if(data['is_taken']):
        data['message'] = 'A Editora ja esta cadastrada'
    return JsonResponse(data)

def loja_nome_registrado(request):
    nome = request.GET.get('nome',None)
    data ={
        'is_taken':Loja.objects.filter(nome__iexact=nome).exists()
    }
    if(data['is_taken']):
        data['message'] = 'A loja ja esta cadastrada'
    return JsonResponse(data)

class logarUsuario(CreateView):
    fields = '__all__'
    model = Usuario
    template_name = 'estoque/home.html'
    failed_url = 'estoque/home.html'

    def post(self,request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = Usuario.objects.filter(email__iexact=email)
        if len(user)>0:
            senha_certa = user[0].senha
            if(senha_certa==senha):
                request.session[email] = senha
                return HttpResponseRedirect('/estoque/')
            else:
                return HttpResponseRedirect(request.path_info)
        else:
                return HttpResponseRedirect(request.path_info)

class UsuarioCreateView(CreateView):  
    fields = '__all__'
    model = Usuario
    success_url = reverse_lazy('home')

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')

    
        

