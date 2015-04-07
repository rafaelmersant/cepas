from django.contrib import admin

from .models import Credencial, Obrero, Ascenso


@admin.register(Credencial)
class CredencialAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

@admin.register(Obrero)
class ObreroAdmin(admin.ModelAdmin):
	list_display = ['id', 'obrero', 'credencial', 'iglesia', 'pastor', 'anio_nombramiento']
	list_editable = ('credencial',)
	search_fields = ('obrero',)

@admin.register(Ascenso)
class AscensoAdmin(admin.ModelAdmin):
	list_display = ['id', 'obrero', 'rango_nuevo', 'anio',]
	list_editable = ('rango_nuevo', 'anio')
	search_fields = ('obrero',)