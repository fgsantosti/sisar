from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
import datetime

email_coordenacao = 'cd.cacor@ifpi.edu.br'

# Create your models here.
class Modalidade(models.Model):
	nome = models.CharField(max_length=200)
	def __str__(self):
		return self.nome 

class Curso(models.Model):
	"""docstring for Disciplina"""
	nome = models.CharField(max_length=200)
	descricao = models.TextField()

	def __str__(self):
		return self.nome

class Professor(models.Model):
	nome = models.CharField(max_length=200)
	matricula = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)
	
	class Meta:
		verbose_name = 'Professore'

	def __str__(self):
		return self.nome

class Disciplina(models.Model):
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

class Falta(models.Model):
	"""docstring for Reposicao"""
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
	modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE,verbose_name='Modalidade')
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name='Curso')
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
	turma = models.ForeignKey(Turma, on_delete=models.CASCADE,verbose_name='Turma')
	quantidade_aulas = models.CharField(max_length=10)
	data = models.DateField()
	data_hora_inicio = models.TimeField(default=timezone.now)
	data_hora_fim = models.TimeField(default=timezone.now)
	data_limite_para_reposicao = models.DateField()

	def __str__(self):
		return self.professor.nome
	datetime.date.today()


	def save(self, *args, **kwargs):
		data = datetime.date.today()
		ano = data.year
		mes = data.month
		dia = data.day
		html_content = f'<p>Esse é um e-mail do SisAR campus CACOR</p> <p>Olá professor {self.professor.nome},</p><p>Foram adicionadas {self.quantidade_aulas} ausência(s) no dia {dia}/{mes}/{ano}</p><p>No {self.curso}</p><p>Na turma {self.turma}</p><p>Na disciplina {self.disciplina}</p><br> <br> <p>Atenciosamente, </p> <br> <p> Coordenação de Disciplina </p>'
		
		send_mail(f'SisAR: Notificação professor {self.professor.nome}', 
		'Esse é um email do SisAr campus CACOR', 
		email_coordenacao,
		[self.professor.email], html_message=html_content)
		
		super().save(*args, **kwargs)  # Call the "real" save() method.

class Antecipacao(models.Model):
	"""docstring for Antecipacao"""
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE,related_name='professor_antecipacao_set')
	professor_substituido = models.ForeignKey(Professor, on_delete=models.CASCADE)
	modalidade = models.ForeignKey(Modalidade,on_delete=models.CASCADE)
	conteudo = models.TextField()
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,related_name='disciplina_antecipacao_set')
	disciplina_substituida = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
	turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
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
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE,related_name='professor_reposicao_set')
	professor_substituido = models.ForeignKey(Professor, on_delete=models.CASCADE)
	modalidade = models.ForeignKey(Modalidade,on_delete=models.CASCADE)
	conteudo = models.TextField()
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,related_name='disciplina_reposicao_set')
	disciplina_substituida = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
	turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
	quantidade_aulas = models.CharField(max_length=10)
	data = models.DateField()
	data_hora_inicio = models.TimeField(default=timezone.now)
	data_hora_fim = models.TimeField(default=timezone.now)
	
	def __str__(self):
		return self.professor.nome

	class Meta:
		verbose_name = 'Reposicõe'
