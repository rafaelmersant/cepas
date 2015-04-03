from django.contrib import admin

from .models import Zona

class ZonaAdmin(admin.ModelAdmin):
	list_display = ['id','Descripcion','Provincia',]
	list_editable = ('Descripcion','Provincia')
	search_fields = ('Descripcion',)

admin.site.register(Zona,ZonaAdmin)