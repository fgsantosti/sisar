# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Antecipacao, Reposicao, Disciplina, Falta, Professor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound

from django.views import View

# Create your views here.
'''
def login(request):
	m = User.objects.get(username=request.POST['username'])
	if m.password == request.POST['password']:
		request.session['member_id'] = m.id
		return render(request, 'sisar/index.html')
	else:
		return HttpResponse("<h2>Your username and password didn't match.</h2>")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
		request.session['user_id'] = user.id
		return render(request, 'sisar/index.html')
    else:
		msg = "Problema com a password ou username."
		return render(request, 'sisar/login.html', {'msg':msg} )

def logout_view(request):
	logout(request)
	return render(request, 'sisar/login.html')

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sisar/index.html')
'''

def index(request):
	return render(request, 'sisar/index.html')

def sobre(request):
	return render(request, 'sisar/sobre.html')

def buscar_por_professor_disciplina(request):
	listar_disciplinas = Disciplina.objects.all()
	listar_professores = Professor.objects.all()

	return render(request, 'sisar/buscar_por_professor_disciplina.html',
		{'listar_disciplinas':listar_disciplinas,'listar_professores':listar_professores})

def listar_por_professor_disciplina(request):
	listar_antecipacao = Antecipacao.objects.filter(professor=request.POST['idprofessor'],
		disciplina=request.POST['iddisciplina'])
	listar_reposicao = Reposicao.objects.filter(professor=request.POST['idprofessor'],
		disciplina=request.POST['iddisciplina'])
	listar_faltas = Falta.objects.filter(professor=request.POST['idprofessor'],
		disciplina=request.POST['iddisciplina'])

	return render(request, 'sisar/listar_por_professor_disciplina.html',
		{'listar_antecipacao':listar_antecipacao, 'listar_reposicao':listar_reposicao,
		'listar_faltas':listar_faltas})

def buscar_por_professor(request):
	listar_professores = Professor.objects.all()

	return render(request, 'sisar/buscar_por_professor.html',
		{'listar_professores':listar_professores})


def listar_por_professor(request):
	listar_antecipacao = Antecipacao.objects.filter(professor=request.POST['idprofessor'])
	listar_reposicao = Reposicao.objects.filter(professor=request.POST['idprofessor'])
	listar_faltas = Falta.objects.filter(professor=request.POST['idprofessor'])

	quantidade_faltas_reposicao = 0
	for x in listar_reposicao:
		quantidade_faltas_reposicao = quantidade_faltas_reposicao + int(x.quantidade_aulas)

	quantidade_faltas_antecipacao = 0
	for x in listar_antecipacao:
		quantidade_faltas_antecipacao = quantidade_faltas_antecipacao + int(x.quantidade_aulas)
	
	quantidade_faltas_falta = 0
	for x in listar_faltas:
		quantidade_faltas_falta = quantidade_faltas_falta + int(x.quantidade_aulas)

	#quantidade_faltas_falta = len(listar_faltas)

	return render(request, 'sisar/listar_por_professor.html',
		{'listar_antecipacao':listar_antecipacao, 
		'listar_reposicao':listar_reposicao,
		'listar_faltas':listar_faltas, 
		'quantidade_faltas_antecipacao':quantidade_faltas_antecipacao,
		'quantidade_faltas_reposicao':quantidade_faltas_reposicao, 
		'quantidade_faltas_falta':quantidade_faltas_falta})


def buscar_por_nome_professor(request):
	return render(request, 'sisar/buscar_por_nome_professor.html')

def listar_por_nome_professor(request):
	#Entry.objects.filter(headline__contains='%')
	listar_professores = Professor.objects.filter(nome__contains=request.POST['nome'])
	listar_antecipacao = Antecipacao.objects.filter(professor__in=listar_professores)
	return render(request, 'sisar/listar_por_nome_professor.html',
		{'listar_professores':listar_professores,'listar_antecipacao':listar_antecipacao})

def buscar_por_data(request):
	#listar_professores = User.objects.all()
	return render(request, 'sisar/buscar_por_data.html')

def listar_por_data(request):
	#clientes = clientes.filter(data_cadastro__range=[dataini,datafim])
	listar_antecipacao = Antecipacao.objects.filter(data__range=[request.POST['dataini'],request.POST['datafim']])
	listar_reposicao = Reposicao.objects.filter(data__range=[request.POST['dataini'],request.POST['datafim']])
	listar_faltas = Falta.objects.filter(data__range=[request.POST['dataini'],request.POST['datafim']])

	return render(request, 'sisar/listar_por_data.html',
		{'listar_antecipacao':listar_antecipacao, 'listar_reposicao':listar_reposicao,
		'listar_faltas':listar_faltas})

def buscar_por_professor_data(request):
	listar_professores = Professor.objects.all()
	return render(request, 'sisar/buscar_por_professor_data.html',{'listar_professores':listar_professores})

def listar_por_professor_data(request):
	#clientes = clientes.filter(data_cadastro__range=[dataini,datafim])
	listar_antecipacao = Antecipacao.objects.filter(professor=request.POST['idprofessor'],data__range=[request.POST['dataini'],request.POST['datafim']])
	listar_reposicao = Reposicao.objects.filter(professor=request.POST['idprofessor'],data__range=[request.POST['dataini'],request.POST['datafim']])
	listar_faltas = Falta.objects.filter(professor=request.POST['idprofessor'],data__range=[request.POST['dataini'],request.POST['datafim']])

	return render(request, 'sisar/listar_por_professor_data.html',
		{'listar_antecipacao':listar_antecipacao, 'listar_reposicao':listar_reposicao,
		'listar_faltas':listar_faltas})

def buscar_por_professor_data_substituido(request):
	listar_professores = Professor.objects.all()
	return render(request, 'sisar/buscar_por_professor_data_substituido.html',{'listar_professores':listar_professores})

def listar_por_professor_data_substituido(request):
	#clientes = clientes.filter(data_cadastro__range=[dataini,datafim])
	listar_antecipacao = Antecipacao.objects.filter(professor_substituido=request.POST['idprofessor'],data__range=[request.POST['dataini'],request.POST['datafim']])
	listar_reposicao = Reposicao.objects.filter(professor_substituido=request.POST['idprofessor'],data__range=[request.POST['dataini'],request.POST['datafim']])
	listar_faltas = Falta.objects.filter(professor=request.POST['idprofessor'],data__range=[request.POST['dataini'],request.POST['datafim']])

	return render(request, 'sisar/listar_por_professor_data_substituido.html',
		{'listar_antecipacao':listar_antecipacao, 'listar_reposicao':listar_reposicao,
		'listar_faltas':listar_faltas})

def buscar_por_falta(request):
	listar_disciplinas = Disciplina.objects.all()
	listar_professores = Professor.objects.all()

	return render(request, 'sisar/buscar_por_falta.html',
		{'listar_disciplinas':listar_disciplinas,'listar_professores':listar_professores})

def listar_por_falta(request):
	listar_antecipacao = Antecipacao.objects.filter(professor=request.POST['idprofessor'],
		disciplina=request.POST['iddisciplina'])
	listar_reposicao = Reposicao.objects.filter(professor=request.POST['idprofessor'],
		disciplina=request.POST['iddisciplina'])
	listar_faltas = Falta.objects.filter(professor=request.POST['idprofessor'],
		disciplina=request.POST['iddisciplina'])

	return render(request, 'sisar/listar_por_falta.html',
		{'listar_antecipacao':listar_antecipacao, 'listar_reposicao':listar_reposicao,
		'listar_faltas':listar_faltas})
