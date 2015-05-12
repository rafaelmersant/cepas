from django.contrib import admin

from .models import Credencial, Obrero, Ascenso


@admin.register(Credencial)
class CredencialAdmin(admin.ModelAdmin):
	list_display = ['id', 'descripcion',]
	list_editable = ('descripcion',)
	search_fields = ('descripcion',)

class AscensoInline(admin.StackedInline):
	model = Ascenso
	extra = 1

@admin.register(Obrero)
class ObreroAdmin(admin.ModelAdmin):
	list_display = ['id', 'obrero', 'credencial', 'iglesia', 'pastor', 'anio_nombramiento']
	list_editable = ('credencial',)
	search_fields = ('obrero',)
	raw_id_fields = ('obrero',)

	inlines = [AscensoInline]

	def save_model(self, request, obj, form, change):
		if obj.id == None:
			obj.creadoPor = request.user
		else:
			obj.modificadoPor = request.user

		obj.save()
