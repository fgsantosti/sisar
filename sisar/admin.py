# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Turma, Disciplina, Curso, Antecipacao, Reposicao, Falta, Professor, Modalidade

# Register your models here.
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Antecipacao)
admin.site.register(Reposicao)
admin.site.register(Falta)
admin.site.register(Professor)
admin.site.register(Modalidade)