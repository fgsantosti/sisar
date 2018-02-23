from .models import Professor, Modalidade, Disciplina, Curso, Turma, Antecipacao, Reposicao, Falta
from django import forms
from django.forms import ModelForm, Textarea, TimeField, TextInput

class ProfessorForm(forms.ModelForm): 

	class Meta:
		model = Professor
		fields = ['nome'] #todos os campos da tabela Professor
		labels = {
			'nome': ('Nome do Professor:'),
		}
		widgets = {
			'nome': TextInput(attrs={'size': 80, }),
		}

class ModalidadeForm(forms.ModelForm): 

	class Meta:
		model = Modalidade
		fields = '__all__' #todos os campos da tabela Modalidade

class DisciplinaForm(forms.ModelForm): 

	class Meta:
		model = Disciplina
		fields = '__all__' #todos os campos da tabela Disciplina

class CursoForm(forms.ModelForm): 

	class Meta:
		model = Curso
		fields = '__all__' #todos os campos da tabela Curso

class TurmaForm(forms.ModelForm): 

	class Meta:
		model = Turma
		fields = '__all__' #todos os campos da tabela Turma

class DateTimeInput(forms.DateTimeInput):
	input_type = 'datetime'

class TimeInput(forms.TimeInput):
	input_type = 'time'

class DateInput(TextInput):
     input_type = "date"

class DateField(forms.DateInput):
	input_type = 'date'

class AntecipacaoForm(forms.ModelForm): 

	class Meta:
		model = Antecipacao
		fields = '__all__'
		fields = ['professor', 'professor_substituido', 'servidor', 'modalidade', 
		 'curso','disciplina', 'disciplina_substituida', 'turma', 
		'quantidade_aulas', 'conteudo', 'data', 'data_hora_inicio', 'data_hora_fim']
		widgets = { 'data': DateInput(), 
		'data_hora_inicio': TimeInput(),
		 'data_hora_fim': TimeInput()  }


class ReposicaoForm(forms.ModelForm): 

	class Meta:
		model = Reposicao
		fields = '__all__'
		fields = ['professor', 'professor_substituido', 'servidor', 'modalidade', 
		'curso','disciplina', 'disciplina_substituida', 'turma', 
		'quantidade_aulas', 'conteudo', 'data', 'data_hora_inicio', 'data_hora_fim']
		widgets = { 'date': DateInput(), 
		'data_hora_inicio': TimeInput(), 
		'data_hora_fim': TimeInput()  }


class FaltaForm(forms.ModelForm): 

	class Meta:
		model = Falta
		fields = ['professor', 'servidor', 
		'modalidade', 'curso','disciplina', 
		'turma', 'quantidade_aulas', 'data', 
		'data_hora_inicio', 'data_hora_fim', 
		'data_limite_para_reposicao']


		widgets = {'data': DateInput(),
			'data_limite_para_reposicao':DateInput(),
			'data_hora_inicio': TimeInput(), 
			'data_hora_fim': TimeInput() 		}
		#data=forms.DateField(widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}), input_formats=('%m/%d/%Y', ))

		#widgets ={'data': DateInput(attrs={'format':'%Y-%m-%d'}),} 
'''

#'fecha_de_inicio': forms.DateInput(format='%d/%m/%Y')

#forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

class PostForm(forms.ModelForm): 

	class Meta:
		model = Post
		fields = '__all__' #todos os campos da tabela Post
		widgets = { 'published_date': DateInput(), 
					'created_date': DateInput() }

from django import forms
from core.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['author', 'title', 'text', 'created_date', 'published_date']
'''

