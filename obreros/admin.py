from django.contrib import admin

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
	list_display = ['id', 'obrero', 'CredencialObrero', 'iglesia', 'pastor', 'anio_nombramiento', 'AgnoUltimoAscenso']
	search_fields = ('obrero__nombres', 'obrero__apellidos')
	raw_id_fields = ('obrero',)
	list_filter = ( 'credencial', 'iglesia', 'pastor', 'anio_nombramiento')

	inlines = [AscensoInline]

	def save_model(self, request, obj, form, change):
		if obj.id == None:
			obj.creadoPor = request.user
		else:
			obj.modificadoPor = request.user

		obj.save()
