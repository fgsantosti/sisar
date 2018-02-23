from django.conf.urls import include, url
from . import views

#from .cadastrar import FaltaCreate, FaltaUpdate, FaltaDelete, FaltaListView
from .cadastrar import ProfessorCreate, ProfessorUpdate, ProfessorDelete, ProfessorListView
from .cadastrar import ModalidadeCreate, ModalidadeUpdate, ModalidadeDelete, ModalidadeListView
from .cadastrar import DisciplinaCreate, DisciplinaUpdate, DisciplinaDelete, DisciplinaListView
from .cadastrar import CursoCreate, CursoUpdate, CursoDelete, CursoListView
from .cadastrar import TurmaCreate, TurmaUpdate, TurmaDelete, TurmaListView
#from .cadastrar import AntecipacaoCreate, AntecipacaoUpdate, AntecipacaoDelete, AntecipacaoListView
from .cadastrar_faltas import falta_home, cadastrar_falta_professor, listar_faltas, atualizar_falta, deletar_falta
from .cadastrar_antecipacao import nova_antecipacao, listar_antecipacoes, cadastrar_antecipacao, atualizar_antecipacao, deletar_antecipacao
from .cadastrar_reposicao import nova_reposicao, listar_reposicoes, cadastrar_reposicao, atualizar_reposicao, deletar_reposicao

urlpatterns = [

	#rota de reposicao
	url(r'^nova_reposicao/$', nova_reposicao, name='nova_reposicao'),
	url(r'^cadastrar_reposicao/$', cadastrar_reposicao, name='cadastrar_reposicao'),
	url(r'^listar_reposicoes/$', listar_reposicoes, name='listar_reposicoes'),
	url(r'^atualizar_reposicao/(?P<id>\d+)/$', atualizar_reposicao, name='atualizar_reposicao'),
	url(r'^deletar_reposicao/(?P<id>\d+)/$', deletar_reposicao, name='deletar_reposicao'),

	#rota de antecipacao
	url(r'^nova_antecipacao/$', nova_antecipacao, name='nova_antecipacao'),
	url(r'^cadastrar_antecipacao/$', cadastrar_antecipacao, name='cadastrar_antecipacao'),
	url(r'^listar_antecipacoes/$', listar_antecipacoes, name='listar_antecipacoes'),
	url(r'^atualizar_antecipacao/(?P<id>\d+)/$', atualizar_antecipacao, name='atualizar_antecipacao'),
	url(r'^deletar_antecipacao/(?P<id>\d+)/$', deletar_antecipacao, name='deletar_antecipacao'),

	#rota de cadastro de falta
	url(r'^cadastrar-falta/$', falta_home, name='cadastrar_falta'),
	url(r'^cadastrar/$', cadastrar_falta_professor, name='cadastrar_falta_professor'),
	url(r'^listar_faltas/$', listar_faltas, name='listar_faltas'),
	url(r'^atualizar_falta/(?P<id>\d+)/$', atualizar_falta, name='atualizar_falta'),
	url(r'^deletar_falta/(?P<id>\d+)/$', deletar_falta, name='deletar_falta'),

	#rotas para professor   
	url(r'professor/add/$', ProfessorCreate.as_view(), name='professor_add'),
	url(r'professor/(?P<pk>[0-9]+)/$', ProfessorUpdate.as_view(), name='professor_update'),
	url(r'professor/(?P<pk>[0-9]+)/delete/$', ProfessorDelete.as_view(), name='professor_delete'),
	url(r'professor/list/$', ProfessorListView.as_view(), name='professor_list'),
	#rotas para modalidade   
	url(r'modalidade/add/$', ModalidadeCreate.as_view(), name='modalidade_add'),
	url(r'modalidade/(?P<pk>[0-9]+)/$', ModalidadeUpdate.as_view(), name='modalidade_update'),
	url(r'modalidade/(?P<pk>[0-9]+)/delete/$', ModalidadeDelete.as_view(), name='modalidade_delete'),
	url(r'modalidade/list/$', ModalidadeListView.as_view(), name='modalidade_list'),
	#rotas para disciplina   
	url(r'disciplina/add/$', DisciplinaCreate.as_view(), name='disciplina_add'),
	url(r'disciplina/(?P<pk>[0-9]+)/$', DisciplinaUpdate.as_view(), name='disciplina_update'),
	url(r'disciplina/(?P<pk>[0-9]+)/delete/$', DisciplinaDelete.as_view(), name='disciplina_delete'),
	url(r'disciplina/list/$', DisciplinaListView.as_view(), name='disciplina_list'),
	#rotas para curso   
	url(r'curso/add/$', CursoCreate.as_view(), name='curso_add'),
	url(r'curso/(?P<pk>[0-9]+)/$', CursoUpdate.as_view(), name='curso_update'),
	url(r'curso/(?P<pk>[0-9]+)/delete/$', CursoDelete.as_view(), name='curso_delete'),
	url(r'curso/list/$', CursoListView.as_view(), name='curso_list'),
	#rotas para turma   
	url(r'turma/add/$', TurmaCreate.as_view(), name='turma_add'),
	url(r'turma/(?P<pk>[0-9]+)/$', TurmaUpdate.as_view(), name='turma_update'),
	url(r'turma/(?P<pk>[0-9]+)/delete/$', TurmaDelete.as_view(), name='turma_delete'),
	url(r'turma/list/$', TurmaListView.as_view(), name='turma_list'),

	#rotas de buscas
	url(r'^$', views.index, name='index'),
	url(r'^sobre/$', views.sobre, name='sobre'),
	url(r'^contato/$', views.sobre, name='contato'),
	url(r'^buscar-por-professor-disciplina/$',
		views.buscar_por_professor_disciplina,
		name='buscar_por_professor_disciplina'),

	url(r'^listar-por-professor-disciplina/$',
		views.listar_por_professor_disciplina,
		name='listar_por_professor_disciplina'),

	url(r'^buscar-por-professor/$',
		views.buscar_por_professor,
		name='buscar_por_professor'),

	url(r'^listar-por-professor/$',
		views.listar_por_professor,
		name='listar_por_professor'),

	url(r'^buscar-por-professor-data/$',
		views.buscar_por_professor_data,
		name='buscar_por_professor_data'),

	url(r'^listar-por-professor-data/$',
		views.listar_por_professor_data,
		name='listar_por_professor_data'),

	url(r'^buscar-por-professor-data-substituido/$',
		views.buscar_por_professor_data_substituido,
		name='buscar_por_professor_data_substituido'),

	url(r'^listar-por-professor-data-substituido-substituido/$',
		views.listar_por_professor_data_substituido,
		name='listar_por_professor_data_substituido'),

	url(r'^buscar-por-data/$',
		views.buscar_por_data,
		name='buscar_por_data'),

	url(r'^listar-por-data/$',
		views.listar_por_data,
		name='listar_por_data'),

	url(r'^buscar-por-falta/$',
		views.buscar_por_falta,
		name='buscar_por_falta'),

	url(r'^listar-por-falta/$',
		views.listar_por_falta,
		name='listar_por_falta'),

	url(r'^buscar-por-nome-professor/$',
		views.buscar_por_nome_professor,
		name='buscar_por_nome_professor'),

	url(r'^listar-por-nome-professor/$',
		views.listar_por_nome_professor,
		name='listar_por_nome_professor'),

	url(r'^login/$',
		views.login,
		name='login'),

]

'''	#rotas para professor   
	url(r'falta/add/$', FaltaCreate.as_view(), name='falta_add'),
	url(r'falta/(?P<pk>[0-9]+)/$', FaltaUpdate.as_view(), name='falta_update'),
	url(r'falta/(?P<pk>[0-9]+)/delete/$', FaltaDelete.as_view(), name='falta_delete'),
	url(r'falta/list/$', FaltaListView.as_view(), name='falta_list'),

	#rotas para antecipacao   
	url(r'antecipacao/add/$', AntecipacaoCreate.as_view(), name='antecipacao_add'),
	url(r'antecipacao/(?P<pk>[0-9]+)/$', AntecipacaoUpdate.as_view(), name='antecipacao_update'),
	url(r'antecipacao/(?P<pk>[0-9]+)/delete/$', AntecipacaoDelete.as_view(), name='antecipacao_delete'),
	url(r'antecipacao/list/$', AntecipacaoListView.as_view(), name='antecipacao_list'),

'''
