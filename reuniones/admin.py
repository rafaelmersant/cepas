from django.contrib import admin

from .models import Tipo_Reunion, Reunion, Asistencia


@admin.register(Tipo_Reunion)
class TipoReunionAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion', 'observacion', ]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

@admin.register(Reunion)
class ReunionAdmin(admin.ModelAdmin):
	list_display = ['id', 'fecha', 'lugar', 'clase_reunion', 'tipo_reunion',]
	list_editable = ('lugar', 'clase_reunion',)
	search_fields = ('fecha',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ['id', 'obrero', 'reunion', 'motivo', 'excusa_descrp']
	list_editable = ('motivo',)
	search_fields = ('obrero',)