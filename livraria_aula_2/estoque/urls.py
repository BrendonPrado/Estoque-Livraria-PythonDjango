from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', include([
        path('', views.AutorSearchFormListView.as_view(), name='autor-list'),
        path('novo/', views.AutorCreateView.as_view(), name='autor-create'),
        path('<int:pk>/', views.AutorUpdateView.as_view(), name='autor-update'),
        path('remover/<int:pk>/', views.AutorDeleteView.as_view(), name='autor-delete'),
        path('autor.json',views.AutorJsonListView.as_view(),name='autor-json-list'),
        path('taken/',views.autor_nome_registrado,name='autor-taken')
    ])),
    path('livros/', include([
        path('', views.LivroSearchFormListView.as_view(), name='livro-list'),
        path('novo/', views.LivroCreateView.as_view(), name='livro-create'),
        path('<int:pk>/', views.LivroUpdateView.as_view(), name='livro-update'),
        path('remover/<int:pk>/', views.LivroDeleteView.as_view(), name='livro-delete'),
        path('livros.json',views.LivroJsonListView.as_view(),name='livro-json-list'),
        path('taken/',views.livro_nome_registrado,name='livro-taken'),
    ])),
    path('editoras/', include([
        path('', views.EditoraSearchFormListView.as_view(), name='editora-list'),
        path('novo/', views.EditoraCreateView.as_view(), name='editora-create'),
        path('<int:pk>/', views.EditoraUpdateView.as_view(), name='editora-update'),
        path('remover/<int:pk>/', views.EditoraDeleteView.as_view(), name='editora-delete'),
        path('editora.json',views.EditoraJsonListView.as_view(),name='editora-json-list'),
        path('taken/',views.editora_nome_registrado,name='editora-taken')
    ])),
     path('loja/', include([
        path('', views.LojaSearchFormListView.as_view(), name='loja-list'),
        path('novo/', views.LojaCreateView.as_view(), name='loja-create'),
        path('<int:pk>/', views.LojaUpdateView.as_view(), name='loja-update'),
        path('remover/<int:pk>/', views.LojaDeleteView.as_view(), name='loja-delete'),
        path('lojas.json',views.LojaJsonListView.as_view(),name='loja-json-list'),
        path('taken/',views.loja_nome_registrado,name='loja-taken')
    ])),
    ]
