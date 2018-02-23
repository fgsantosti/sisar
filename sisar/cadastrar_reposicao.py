# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Antecipacao, Reposicao, Disciplina, Falta, Professor, Modalidade, Turma, Curso
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ReposicaoForm

import datetime, time
from datetime import date

def listar_reposicoes(request):
	reposicoes = Reposicao.objects.all()
	return render(request, 'sisar/reposicao_list.html',{'reposicoes':reposicoes})

def nova_reposicao(request):
	professores = Professor.objects.all()
	users = User.objects.all()
	modalidades = Modalidade.objects.all()
	cursos = Curso.objects.all()
	disciplinas = Disciplina.objects.all()
	turmas = Turma.objects.all()

	return render(request, 'sisar/cadastrar_reposicao.html',
		{'professores':professores,'disciplinas':disciplinas,
		'modalidades':modalidades, 'turmas':turmas, 'users':users, 'cursos':cursos})

def cadastrar_reposicao(request):
	professor = Professor.objects.get(id=request.POST['professor'])
	professor_substituido = Professor.objects.get(id=request.POST['professor_substituido'])
	modalidade = Modalidade.objects.get(id=request.POST['modalidade'])
	disciplina = Disciplina.objects.get(id=request.POST['disciplina'])
	disciplina_substituida = Disciplina.objects.get(id=request.POST['disciplina_substituida'])
	turma = Turma.objects.get(id=request.POST['turma'])
	servidor = User.objects.get(id=request.POST['servidor'])
	curso = Curso.objects.get(id=request.POST['curso'])
	
	Reposicao.objects.create(professor=professor, professor_substituido=professor_substituido,
		modalidade=modalidade, servidor=servidor, curso=curso, 
		disciplina=disciplina, disciplina_substituida=disciplina_substituida,
		turma=turma, quantidade_aulas=request.POST['quantidade_aulas'], 
		conteudo=request.POST['conteudo'], data=request.POST['data'], 
		data_hora_inicio=request.POST['data_hora_inicio'], 
		data_hora_fim=request.POST['data_hora_fim'])
	return redirect(listar_reposicoes)

def atualizar_reposicao(request, id):
	reposicao = Reposicao.objects.get(id=id)    
	form = ReposicaoForm(request.POST or None, instance=reposicao)
	if form.is_valid():
		form.save()
		return redirect(listar_reposicoes)

	return render(request, 'sisar/reposicao_form.html', {'form':form})


def deletar_reposicao(request, id):
	antecipacao = Reposicao.objects.get(id=id)
	antecipacao.delete()
	return redirect(listar_reposicoes)	
