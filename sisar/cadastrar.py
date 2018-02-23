# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Antecipacao, Reposicao, Disciplina, Falta, Professor, Modalidade, Curso,Turma
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from .forms import ProfessorForm, FaltaForm, ModalidadeForm, DisciplinaForm, CursoForm, TurmaForm
from django.views.generic.list import ListView

import datetime, time
from datetime import date

#CRUD PROFESSOR
class ProfessorListView(ListView):
	model = Professor
	def get_queryset(self, **kwargs):
		return Professor.objects.all()

class ProfessorCreate(CreateView):
	model = Professor
	form_class = ProfessorForm
	success_url = reverse_lazy('professor_list')
	success_message = "Professor adicionado com sucesso."

class ProfessorUpdate(UpdateView):
	model = Professor
	form_class = ProfessorForm
	success_url = reverse_lazy('professor_list')
	success_message = "Professor adicionado com sucesso."

class ProfessorDelete(DeleteView):
	model = Professor
	success_url = reverse_lazy('professor_list')

#CRUD MODALIDADE
class ModalidadeListView(ListView):
	model = Modalidade
	def get_queryset(self, **kwargs):
		return Modalidade.objects.all()

class ModalidadeCreate(CreateView):
	model = Modalidade
	form_class = ModalidadeForm
	success_url = reverse_lazy('modalidade_list')
	success_message = "Modalidade adicionado com sucesso."

class ModalidadeUpdate(UpdateView):
	model = Modalidade
	form_class = ModalidadeForm
	success_url = reverse_lazy('modalidade_list')
	success_message = "Modalidade adicionado com sucesso."

class ModalidadeDelete(DeleteView):
	model = Modalidade
	success_url = reverse_lazy('modalidade_list')

#CRUD DISCIPLINA
class DisciplinaListView(ListView):
	model = Disciplina
	def get_queryset(self, **kwargs):
		return Disciplina.objects.all()

class DisciplinaCreate(CreateView):
	model = Disciplina
	form_class = DisciplinaForm
	success_url = reverse_lazy('disciplina_list')
	success_message = "Disciplina adicionado com sucesso."

class DisciplinaUpdate(UpdateView):
	model = Disciplina
	form_class = DisciplinaForm
	success_url = reverse_lazy('disciplina_list')
	success_message = "Disciplina adicionado com sucesso."

class DisciplinaDelete(DeleteView):
	model = Disciplina
	success_url = reverse_lazy('disciplina_list')


#CRUD CURSO
class CursoListView(ListView):
	model = Curso
	def get_queryset(self, **kwargs):
		return Curso.objects.all()

class CursoCreate(CreateView):
	model = Curso
	form_class = CursoForm
	success_url = reverse_lazy('curso_list')
	success_message = "Curso adicionado com sucesso."

class CursoUpdate(UpdateView):
	model = Curso
	form_class = DisciplinaForm
	success_url = reverse_lazy('curso_list')
	success_message = "Curso adicionado com sucesso."

class CursoDelete(DeleteView):
	model = Curso
	success_url = reverse_lazy('curso_list')

#CRUD TURMA
class TurmaListView(ListView):
	model = Turma
	def get_queryset(self, **kwargs):
		return Turma.objects.all()

class TurmaCreate(CreateView):
	model = Turma
	form_class = TurmaForm
	success_url = reverse_lazy('turma_list')
	success_message = "Turma adicionado com sucesso."

class TurmaUpdate(UpdateView):
	model = Turma
	form_class = TurmaForm
	success_url = reverse_lazy('turma_list')
	success_message = "Turma adicionado com sucesso."

class TurmaDelete(DeleteView):
	model = Turma
	success_url = reverse_lazy('turma_list')

#CRUD ANTECIPACAO
class AntecipacaoListView(ListView):
	model = Antecipacao
	def get_queryset(self, **kwargs):
		return Antecipacao.objects.all()

'''class AntecipacaoCreate(CreateView):
	model = Antecipacao
	form_class = AntecipacaoForm
	success_url = reverse_lazy('antecipacao_list')
	success_message = "Antecipacao adicionado com sucesso."

class AntecipacaoUpdate(UpdateView):
	model = Antecipacao
	form_class = AntecipacaoForm
	success_url = reverse_lazy('antecipacao_list')
	success_message = "Antecipacao adicionado com sucesso."

class AntecipacaoDelete(DeleteView):
	model = Antecipacao
	success_url = reverse_lazy('antecipacao_list')
'''
