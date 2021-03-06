from django.contrib import admin

from cepas.actions import export_as_excel

from .models import Credencial, Obrero, Ascenso


@admin.register(Credencial)
class CredencialAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion', 'orden']
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

class AscensoInline(admin.StackedInline):
	model = Ascenso
	extra = 1
	ordering = ('anio',)

@admin.register(Obrero)
class ObreroAdmin(admin.ModelAdmin):	
	list_display = ['id', 'obrero', 'CredencialObrero', 'iglesia', 'pastor', 'anio_nombramiento', 'AgnoUltimoAscenso', 'creadoFecha', 'creadoPor', 'modificado', 'modificadoPor']
	search_fields = ('obrero__nombres', 'obrero__apellidos')
	raw_id_fields = ('obrero',)
	list_filter = ( 'creadoPor', 'iglesia', 'pastor', 'anio_nombramiento')
	actions = (export_as_excel,)
	
	inlines = [AscensoInline]

	def save_model(self, request, obj, form, change):
		if obj.id == None:
			obj.creadoPor = request.user
		else:
			obj.modificadoPor = request.user

		obj.save()
