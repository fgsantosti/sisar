from django.shortcuts import render
from .models import Reposicao, Antecipacao, Disciplina, Falta, Professor, Curso, Modalidade, Turma
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum

def index(request):
    return render(request, 'sisar/index.html')

def contato(request):
    return render(request, 'sisar/contato.html')

def sobre(request):
    return render(request, 'sisar/sobre.html')

def buscar_por_falta(request):
    listar_modalidade = Modalidade.objects.all()
    listar_curso = Curso.objects.all()
    listar_professores = Professor.objects.all()
    listar_turma = Turma.objects.all()
    listar_disciplinas = Disciplina.objects.all() 

    return render(request, 'sisar/buscar_por_falta.html',
		{'listar_disciplinas':listar_disciplinas,
        'listar_professores':listar_professores,
        'listar_curso':listar_curso,
        'listar_modalidade':listar_modalidade,
        'listar_turma':listar_turma,
        })

def listar_por_falta(request):
    queryset_base = Falta.objects.all()

    if idmodalidade := request.POST.get("idmodalidade", None):
        queryset_base = queryset_base.filter(modalidade=idmodalidade)
  
    if idcurso := request.POST.get("idcurso", None):
        queryset_base = queryset_base.filter(curso=idcurso)

    if iddisciplina := request.POST.get("iddisciplina", None):
        queryset_base = queryset_base.filter(disciplina=iddisciplina)

    if idprofessor := request.POST.get("idprofessor", None):
        queryset_base = queryset_base.filter(professor=idprofessor)
    
    if idturma := request.POST.get("idturma", None):
        queryset_base = queryset_base.filter(turma=idturma)

    queryset_base = queryset_base.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])

    return render(request, 'sisar/listar_por_falta.html',
		{'listar_faltas':queryset_base})

def buscar_por_antecipacao(request):
    listar_modalidade = Modalidade.objects.all()
    listar_curso = Curso.objects.all()
    listar_professores = Professor.objects.all()
    listar_turma = Turma.objects.all()
    listar_disciplinas = Disciplina.objects.all() 

    return render(request, 'sisar/buscar_por_antecipacao.html',
		{'listar_disciplinas':listar_disciplinas,
        'listar_professores':listar_professores,
        'listar_curso':listar_curso,
        'listar_modalidade':listar_modalidade,
        'listar_turma':listar_turma,
        })

def listar_por_antecipacao(request):
    queryset_base = Antecipacao.objects.all()

    if idmodalidade := request.POST.get("idmodalidade", None):
        queryset_base = queryset_base.filter(modalidade=idmodalidade)
  
    if idcurso := request.POST.get("idcurso", None):
        queryset_base = queryset_base.filter(curso=idcurso)

    if iddisciplina := request.POST.get("iddisciplina", None):
        queryset_base = queryset_base.filter(disciplina=iddisciplina)

    if idprofessor := request.POST.get("idprofessor", None):
        queryset_base = queryset_base.filter(professor=idprofessor)
    
    if idturma := request.POST.get("idturma", None):
        queryset_base = queryset_base.filter(turma=idturma)

    queryset_base = queryset_base.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])

    return render(request, 'sisar/listar_por_antecipacao.html',
		{'listar_antecipacao':queryset_base})

def buscar_por_reposicao(request):
    listar_modalidade = Modalidade.objects.all()
    listar_curso = Curso.objects.all()
    listar_professores = Professor.objects.all()
    listar_turma = Turma.objects.all()
    listar_disciplinas = Disciplina.objects.all() 

    return render(request, 'sisar/buscar_por_reposicao.html',
		{'listar_disciplinas':listar_disciplinas,
        'listar_professores':listar_professores,
        'listar_curso':listar_curso,
        'listar_modalidade':listar_modalidade,
        'listar_turma':listar_turma,
        })

def listar_por_reposicao(request):
    queryset_base = Reposicao.objects.all()

    if idmodalidade := request.POST.get("idmodalidade", None):
        queryset_base = queryset_base.filter(modalidade=idmodalidade)
  
    if idcurso := request.POST.get("idcurso", None):
        queryset_base = queryset_base.filter(curso=idcurso)

    if iddisciplina := request.POST.get("iddisciplina", None):
        queryset_base = queryset_base.filter(disciplina=iddisciplina)

    if idprofessor := request.POST.get("idprofessor", None):
        queryset_base = queryset_base.filter(professor=idprofessor)
    
    if idturma := request.POST.get("idturma", None):
        queryset_base = queryset_base.filter(turma=idturma)

    queryset_base = queryset_base.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])

    return render(request, 'sisar/listar_por_reposicao.html',
		{'listar_reposicao':queryset_base})

def buscar_tudo(request):
    listar_modalidade = Modalidade.objects.all()
    listar_curso = Curso.objects.all()
    listar_professores = Professor.objects.all()
    listar_turma = Turma.objects.all()
    listar_disciplinas = Disciplina.objects.all() 

    return render(request, 'sisar/buscar_tudo.html',
		{'listar_disciplinas':listar_disciplinas,
        'listar_professores':listar_professores,
        'listar_curso':listar_curso,
        'listar_modalidade':listar_modalidade,
        'listar_turma':listar_turma,})

def listar_tudo(request):
    queryset_base1 = Antecipacao.objects.all()
    queryset_base2 = Reposicao.objects.all()
    queryset_base3 = Falta.objects.all()
    queryset_base4 = Falta.objects.all()

    if idmodalidade := request.POST.get("idmodalidade", None):
        queryset_base1 = queryset_base1.filter(modalidade=idmodalidade)
        queryset_base2 = queryset_base2.filter(modalidade=idmodalidade)
        queryset_base3 = queryset_base3.filter(modalidade=idmodalidade)
        queryset_base4 = queryset_base4.filter(modalidade=idmodalidade)

  
    if idcurso := request.POST.get("idcurso", None):
        queryset_base1 = queryset_base1.filter(curso=idcurso)
        queryset_base2 = queryset_base2.filter(curso=idcurso)
        queryset_base3 = queryset_base3.filter(curso=idcurso)
        queryset_base4 = queryset_base4.filter(curso=idcurso)

    if iddisciplina := request.POST.get("iddisciplina", None):
        queryset_base1 = queryset_base1.filter(disciplina=iddisciplina)
        queryset_base2 = queryset_base2.filter(disciplina=iddisciplina)
        queryset_base3 = queryset_base3.filter(disciplina=iddisciplina)
        queryset_base4 = queryset_base4.filter(disciplina=iddisciplina)

    if idprofessor := request.POST.get("idprofessor", None):
        queryset_base1 = queryset_base1.filter(professor=idprofessor)
        queryset_base2 = queryset_base2.filter(professor=idprofessor)
        queryset_base3 = queryset_base3.filter(professor=idprofessor)
        queryset_base4 = queryset_base4.filter(professor=idprofessor)
    
    if idturma := request.POST.get("idturma", None):
        queryset_base1 = queryset_base1.filter(turma=idturma)
        queryset_base2 = queryset_base2.filter(turma=idturma)
        queryset_base3 = queryset_base3.filter(turma=idturma)   
        queryset_base4 = queryset_base4.filter(turma=idturma) 

    queryset_base1 = queryset_base1.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])
    queryset_base2 = queryset_base2.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])
    
    queryset_base3 = queryset_base4.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])
    
    queryset_base4 = queryset_base4.values(
        'professor__nome').annotate(total=Sum(
            'quantidade_aulas')).filter(
                data__range=[request.POST['dataini'],
                request.POST['datafim']])


    return render(request, 'sisar/listar_tudo.html',
		{'listar_antecipacao':queryset_base1,
        'listar_reposicao':queryset_base2,
        'listar_faltas':queryset_base3,
        'listar_faltas_professor':queryset_base4,})


def buscar_faltas_professor(request):
    listar_modalidade = Modalidade.objects.all()
    listar_curso = Curso.objects.all()
    listar_professores = Professor.objects.all()
    listar_turma = Turma.objects.all()
    listar_disciplinas = Disciplina.objects.all() 

    return render(request, 'sisar/buscar_faltas_professor.html',
		{'listar_disciplinas':listar_disciplinas,
        'listar_professores':listar_professores,
        'listar_curso':listar_curso,
        'listar_modalidade':listar_modalidade,
        'listar_turma':listar_turma,
        })

def listar_faltas_professor(request):
    queryset_base = Falta.objects.all()

    if idmodalidade := request.POST.get("idmodalidade", None):
        queryset_base = queryset_base.filter(modalidade=idmodalidade)
  
    if idcurso := request.POST.get("idcurso", None):
        queryset_base = queryset_base.filter(curso=idcurso)

    if iddisciplina := request.POST.get("iddisciplina", None):
        queryset_base = queryset_base.filter(disciplina=iddisciplina)

    if idprofessor := request.POST.get("idprofessor", None):
        queryset_base = queryset_base.filter(professor=idprofessor)

    if idturma := request.POST.get("idturma", None):
        queryset_base = queryset_base.filter(turma=idturma)     

    '''queryset_base = queryset_base.filter(
        data__range=[request.POST['dataini'],
        request.POST['datafim']])'''

    #some a quantidade de faltas por professor
    
    queryset_base = queryset_base.values('professor__nome').annotate(total=Sum('quantidade_aulas'))


    return render(request, 'sisar/listar_faltas_professor.html',
		{'listar_faltas':queryset_base})


