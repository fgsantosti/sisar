# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Antecipacao, Reposicao, Disciplina, Falta, Professor, Modalidade, Turma, Curso
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import FaltaForm

import datetime, time
from datetime import date


def falta_home(request):
	professores = Professor.objects.all()
	users = User.objects.all()
	modalidades = Modalidade.objects.all()
	cursos = Curso.objects.all()
	disciplinas = Disciplina.objects.all()
	turmas = Turma.objects.all()

	return render(request, 'sisar/cadastrar_falta_professor.html',
		{'professores':professores,'disciplinas':disciplinas,
		'modalidades':modalidades, 'turmas':turmas, 'users':users, 'cursos':cursos})

def data_limite(data):
	#recebendo a data escolhida
	data_cadastrada = datetime.datetime.strptime(data, "%Y-%m-%d").date()

	#transformando essa data em segundos
	data_em_segundos = time.mktime(data_cadastrada.timetuple())
	#data_em_segundos = time.mktime(datetime.datetime.strptime(data_cadastrada, "%Y-%m-%d").timetuple())
	#acrescentando o limite de dias para reposicao da aula
	#foi 1440x15=21600*60=1296000
	data_limite_reposicao_segundos = data_em_segundos + 1296000
	#transformando os segundos em data futura
	data_limite_reposicao = datetime.date.fromtimestamp(data_limite_reposicao_segundos)
	#criando um campo com a data futura
	#self.data_limite_para_reposicao = data_limite_reposicao

	data_limite_para_reposicao = data_limite_reposicao
	
	return data_limite_para_reposicao

def cadastrar_falta_professor(request):
	data_limite_para_reposicao = data_limite(request.POST['data'])

	professor = Professor.objects.get(id=request.POST['professor'])
	modalidade = Modalidade.objects.get(id=request.POST['modalidade'])
	disciplina = Disciplina.objects.get(id=request.POST['disciplina'])
	turma = Turma.objects.get(id=request.POST['turma'])
	servidor = User.objects.get(id=request.POST['servidor'])
	curso = Curso.objects.get(id=request.POST['curso'])
	
	Falta.objects.create(professor=professor, modalidade=modalidade, 
		servidor=servidor, curso=curso, disciplina=disciplina,
		turma=turma, quantidade_aulas=request.POST['quantidade_aulas'], 
		data=request.POST['data'], 
		data_hora_inicio=request.POST['data_hora_inicio'], 
		data_hora_fim=request.POST['data_hora_inicio'], 
		data_limite_para_reposicao=data_limite_para_reposicao)
	return redirect(listar_faltas)

def listar_faltas(request):
	faltas = Falta.objects.all()
	return render(request, 'sisar/listar_faltas.html',{'faltas':faltas})

def atualizar_falta(request,id):
	falta = Falta.objects.get(id=id)    
	form = FaltaForm(request.POST or None, instance=falta)
	if form.is_valid():
		falta.data_limite_para_reposicao = data_limite(request.POST['data'])
		form.save()
		return redirect(listar_faltas)

	return render(request, 'sisar/falta_form.html', {'form':form})

def deletar_falta(request,id):
	falta = Falta.objects.get(id=id)
	falta.delete()
	return redirect(listar_faltas)	

