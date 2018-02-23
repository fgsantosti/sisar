# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime, time
from datetime import date

# Create your models here.

class Professor(models.Model):
	nome = models.CharField(max_length=200)
	class Meta:
		verbose_name = 'Professore'

	def __str__(self):
		return self.nome

class Modalidade(models.Model):
	nome = models.CharField(max_length=200)
	def __str__(self):
		return self.nome

class Disciplina(models.Model):
	"""docstring for Disciplina"""
	nome = models.CharField(max_length=200)
	descricao = models.TextField()
	def __str__(self):
		return self.nome

class Curso(models.Model):
	"""docstring for Disciplina"""
	nome = models.CharField(max_length=200)
	descricao = models.TextField()
	def __str__(self):
		return self.nome

class Turma(models.Model):
	"""docstring for Disciplina"""
	nome = models.CharField(max_length=200)
	descricao = models.TextField()
	def __str__(self):
		return self.nome

class Antecipacao(models.Model):
	"""docstring for Antecipacao"""
	#professor = models.ForeignKey('auth.User', related_name='professor_antecipacao_set')
	professor = models.ForeignKey(Professor, models.CASCADE, related_name='professor_antecipacao_set')
	professor_substituido = models.ForeignKey(Professor, models.CASCADE, related_name='professor_substituido_antecipacao_set')
	modalidade = models.ForeignKey(Modalidade,models.CASCADE, verbose_name='Modalidade')
	servidor = models.ForeignKey('auth.User',models.CASCADE, related_name='servidor_antecipacao_set')
	conteudo = models.TextField()
	curso = models.ForeignKey(Curso, models.CASCADE,verbose_name='Curso')
	disciplina = models.ForeignKey(Disciplina, models.CASCADE,related_name='disciplina_antecipacao_set')
	disciplina_substituida = models.ForeignKey(Disciplina,models.CASCADE, related_name='disciplina_sustituida_antecipacao_set')
	turma = models.ForeignKey(Turma, models.CASCADE,verbose_name='Turma')
	quantidade_aulas = models.CharField(max_length=10)
	data = models.DateField()
	data_hora_inicio = models.TimeField(default=timezone.now)
	data_hora_fim = models.TimeField(default=timezone.now)

	def __str__(self):
		return self.professor.nome

	class Meta:
		verbose_name = 'Antecipaçõe'


class Reposicao(models.Model):
	"""docstring for Reposicao"""
	professor = models.ForeignKey(Professor, models.CASCADE,related_name='professor_reposicao_set')
	professor_substituido = models.ForeignKey(Professor, models.CASCADE,related_name='professor_substituido_reposicao_set')
	modalidade = models.ForeignKey(Modalidade, models.CASCADE,verbose_name='Modalidade')
	servidor = models.ForeignKey('auth.User', models.CASCADE,related_name='servidor_reposicao_set')
	conteudo = models.TextField()
	curso = models.ForeignKey(Curso, models.CASCADE,verbose_name='Curso')
	disciplina = models.ForeignKey(Disciplina, models.CASCADE,related_name='disciplina_reposicao_set')
	disciplina_substituida = models.ForeignKey(Disciplina, models.CASCADE,related_name='disciplina_sustituida_reposicao_set')
	turma = models.ForeignKey(Turma, models.CASCADE,verbose_name='Turma')
	quantidade_aulas = models.CharField(max_length=10)
	data = models.DateField()
	data_hora_inicio = models.TimeField(default=timezone.now)
	data_hora_fim = models.TimeField(default=timezone.now)
	
	def __str__(self):
		return self.professor.nome

	class Meta:
		verbose_name = 'Reposicõe'

#Falta.objects.create(professor='Apple', modalidade='', servidor='', curso='', disciplina='', turma='', quantidade_aulas='', data='', data_hora_inicio='',	data_hora_fim='', data_limite_para_reposicao=)
#Falta.objects.create(professor=1, modalidade=1, servidor=1, curso=1, disciplina=1, turma=1, quantidade_aulas=2, data='2018-02-03', data_hora_inicio='04:56:44',	data_hora_fim='04:56:44', data_limite_para_reposicao='2018-02-24')
class Falta(models.Model):
	"""docstring for Reposicao"""
	professor = models.ForeignKey(Professor, models.CASCADE,related_name='professor_falta_set')
	modalidade = models.ForeignKey(Modalidade, models.CASCADE,verbose_name='Modalidade')
	servidor = models.ForeignKey('auth.User', models.CASCADE,related_name='servidor_falta_set')
	curso = models.ForeignKey(Curso, models.CASCADE,verbose_name='Curso')
	disciplina = models.ForeignKey(Disciplina, models.CASCADE,related_name='disciplina_falta_set')
	turma = models.ForeignKey(Turma, models.CASCADE,verbose_name='Turma')
	quantidade_aulas = models.CharField(max_length=10)
	data = models.DateField()
	data_hora_inicio = models.TimeField(default=timezone.now)
	data_hora_fim = models.TimeField(default=timezone.now)
	data_limite_para_reposicao = models.DateField()


	def __str__(self):
		return  self.professor.nome
        #return 'char(%s)' % self.max_length

