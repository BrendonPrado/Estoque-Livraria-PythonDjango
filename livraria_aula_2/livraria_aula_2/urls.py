"""livraria_aula_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from estoque import views


urlpatterns = [
    path('estoque/', include('estoque.urls')),
    path('admin/', admin.site.urls),
    path('', views.logarUsuario.as_view(), name='home'),
    path('cadastro/',views.UsuarioCreateView.as_view(),name='usuario-create'),
    path('sair/',views.logout,name='logout')
]
