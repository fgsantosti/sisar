"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from sisar import views

urlpatterns = [
    #falta
    path('buscar-por-falta', views.buscar_por_falta, name='buscar_por_falta'),
    path('listar_por_falta', views.listar_por_falta, name='listar_por_falta'),

    #antecipacao
    path('buscar-por-antecipacao', views.buscar_por_antecipacao, name='buscar_por_antecipacao'),
    path('listar_por_antecipacao', views.listar_por_antecipacao, name='listar_por_antecipacao'),

    #antecipacao
    path('buscar-por-reposicao', views.buscar_por_reposicao, name='buscar_por_reposicao'),
    path('listar_por_reposicao', views.listar_por_reposicao, name='listar_por_reposicao'),

    #antecipacao,reposicao,falta
    path('buscar-tudo', views.buscar_tudo, name='buscar_tudo'),
    path('listar_tudo', views.listar_tudo, name='listar_tudo'),

    #antecipacao,reposicao,falta
    path('buscar-faltas-professor', views.buscar_faltas_professor, name='buscar_faltas_professor_tudo'),
    path('listar-faltas-professor', views.listar_faltas_professor, name='listar_faltas_professor'),


    #links basicos
    path('',views.index,name='index'),
    path('contato',views.contato,name='contato'),
    path('sobre',views.sobre,name='sobre'),
]
