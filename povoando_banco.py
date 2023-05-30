import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from sisar.models import Modalidade
from sisar.models import Professor
from sisar.models import Curso
from sisar.models import Disciplina
from sisar.models import Turma

import csv
#ler o arquivo csv e salvar na tabela professor
def populate():
    with open('lprofessor.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Professor(nome=row['nome'], email=row['email'])
            p.save()

    with open('lmodalidade.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m = Modalidade(nome=row['nome'])
            m.save()

    with open('lcurso.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c = Curso(nome=row['nome'], modalidade=Modalidade.objects.get(nome=row['modalidade']))
            c.save()

    with open('ldisciplina.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            d = Disciplina(nome=row['nome'], curso=Curso.objects.get(nome=row['curso']))
            d.save()

    with open('lturma.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            t = Turma(nome=row['nome'], disciplina=Disciplina.objects.get(nome=row['disciplina']), professor=Professor.objects.get(nome=row['professor']))
            t.save()
    

populate()
print('Dados inseridos com sucesso!')

