from django.contrib import admin

from .models import Ascenso

class AscensoAdmin(admin.ModelAdmin):
	list_display = ['id','anio','obrero','rango_nuevo',]
	list_editable = ('anio','obrero','rango_nuevo',)
	search_fields = ('anio','obrero','rango_nuevo')

admin.site.register(Ascenso,AscensoAdmin)