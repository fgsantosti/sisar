from django.contrib import admin
from .models import Reposicao, Curso, Disciplina, Falta, Modalidade, Professor, Turma, Antecipacao

admin.site.register(Modalidade)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Professor)

class Faltas(admin.ModelAdmin):
    list_display = ('nome_professor','data',)
    #list_display_links = ('view_name_categoria',)
    #search_fields = ('nome',)
    list_filter = ('professor','curso','disciplina', )
    list_per_page = 20
    
    @admin.display(ordering='nome_professor')
    def nome_professor(self, obj):
        return obj.professor.nome
    
admin.site.register(Falta, Faltas)

class Antecipacoes(admin.ModelAdmin):
    list_display = ('nome_professor','nome_professor_sustituido', 'data',)
    #list_display_links = ('view_name_categoria',)
    #search_fields = ('nome',)
    list_filter = ('professor','curso','disciplina', )
    list_per_page = 20
    
    @admin.display(ordering='nome_professor')
    def nome_professor(self, obj):
        return obj.professor.nome
    
    @admin.display(ordering='nome_professor_sustituido')
    def nome_professor_sustituido(self, obj):
        return obj.professor_substituido.nome

admin.site.register(Antecipacao, Antecipacoes)

class Reposicoes(admin.ModelAdmin):
    list_display = ('nome_professor','nome_professor_sustituido', 'data',)
    #list_display_links = ('view_name_categoria',)
    #search_fields = ('nome',)
    list_filter = ('professor','curso','disciplina', )
    list_per_page = 20
    
    @admin.display(ordering='nome_professor')
    def nome_professor(self, obj):
        return obj.professor.nome
    
    @admin.display(ordering='nome_professor_sustituido')
    def nome_professor_sustituido(self, obj):
        return obj.professor_substituido.nome

admin.site.register(Reposicao, Reposicoes)

