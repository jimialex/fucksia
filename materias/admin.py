from django.contrib import admin
from .models import Materia, Modulo, Paralelo, Periodo, RecordAcademico

class MateriaAdmin(admin.ModelAdmin):
	list_display = ('sigla', 'nombre', 'modulo')
	list_filter = ('modulo',)
	filter_horizontal = ('pre_requisito','materias_inscritas')

class ParaleloAdmin(admin.ModelAdmin):
	list_display = ('id_materia', 'sigla_paralelo', 'nombre_docente')

class RecordAcademicoAdmin(admin.ModelAdmin):
	list_display = ('estudiante', 'materia', 'nota', 'gestion',)
	list_filter = ('estudiante',)

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Modulo)
admin.site.register(Paralelo, ParaleloAdmin)
admin.site.register(Periodo)
admin.site.register(RecordAcademico, RecordAcademicoAdmin)
